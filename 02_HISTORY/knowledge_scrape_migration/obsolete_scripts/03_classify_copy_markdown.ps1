param(
    [string]$KnowledgeRoot = (Split-Path -Parent $PSScriptRoot),
    [string]$InventoryCsv = '',
    [string]$UrlIndexCsv = '',
    [string[]]$SourceFolders = @(
        'C:\KICAD_SCRAPE\markdown_10k_clean',
        'C:\KICAD_SCRAPE\markdown_url2_clean'
    ),
    [switch]$Force
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($InventoryCsv)) {
    $InventoryCsv = Join-Path $KnowledgeRoot '_raw_inventory\source_file_inventory.csv'
}
if ([string]::IsNullOrWhiteSpace($UrlIndexCsv)) {
    $UrlIndexCsv = Join-Path $KnowledgeRoot 'URL_INDEX.csv'
}

function Ensure-Directory {
    param([Parameter(Mandatory = $true)][string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) {
        New-Item -ItemType Directory -Force -Path $Path | Out-Null
    }
}

function Get-SafeText {
    param([Parameter(Mandatory = $true)][string]$Path)
    return [System.IO.File]::ReadAllText($Path, [System.Text.Encoding]::UTF8)
}

function ConvertTo-Bool {
    param([AllowNull()]$Value)
    if ($null -eq $Value) { return $false }
    $text = $Value.ToString().Trim().ToLowerInvariant()
    return $text -in @('true', '1', 'yes', 'y')
}

function ConvertTo-NullableInt {
    param([AllowNull()]$Value)
    if ($null -eq $Value) { return $null }
    $text = $Value.ToString().Trim()
    if ([string]::IsNullOrWhiteSpace($text)) { return $null }
    $parsed = 0
    if ([int]::TryParse($text, [ref]$parsed)) { return $parsed }
    return $null
}

function ConvertTo-NullableLong {
    param([AllowNull()]$Value)
    if ($null -eq $Value) { return $null }
    $text = $Value.ToString().Trim()
    if ([string]::IsNullOrWhiteSpace($text)) { return $null }
    $parsed = [int64]0
    if ([int64]::TryParse($text, [ref]$parsed)) { return $parsed }
    return $null
}

function Normalize-Url {
    param([AllowNull()][string]$Url)

    if ([string]::IsNullOrWhiteSpace($Url)) {
        return $null
    }

    $candidate = $Url.Trim()
    $uri = $null
    if (-not [System.Uri]::TryCreate($candidate, [System.UriKind]::Absolute, [ref]$uri)) {
        return $candidate
    }

    $scheme = if ([string]::IsNullOrWhiteSpace($uri.Scheme)) { 'https' } else { $uri.Scheme.ToLowerInvariant() }
    $uriHost = $uri.Host.ToLowerInvariant()
    if ([string]::IsNullOrWhiteSpace($uriHost)) {
        return $candidate
    }

    $path = if ([string]::IsNullOrWhiteSpace($uri.AbsolutePath)) { '/' } else { $uri.AbsolutePath }
    $path = [regex]::Replace($path, '/+', '/')
    if ($path.Length -gt 1 -and $path.EndsWith('/')) {
        $path = $path.TrimEnd('/')
    }

    $dropParams = @(
        'utm_source',
        'utm_medium',
        'utm_campaign',
        'utm_term',
        'utm_content',
        'fbclid',
        'gclid',
        'mc_cid',
        'mc_eid'
    )

    $queryPairs = New-Object System.Collections.Generic.List[string]
    if (-not [string]::IsNullOrWhiteSpace($uri.Query)) {
        foreach ($pair in $uri.Query.TrimStart('?').Split('&', [System.StringSplitOptions]::RemoveEmptyEntries)) {
            $parts = $pair.Split('=', 2)
            $key = [System.Uri]::UnescapeDataString($parts[0]).Trim()
            if ([string]::IsNullOrWhiteSpace($key)) {
                continue
            }
            $keyLower = $key.ToLowerInvariant()
            if ($dropParams -contains $keyLower) {
                continue
            }
            $value = if ($parts.Count -gt 1) { [System.Uri]::UnescapeDataString($parts[1]) } else { '' }
            if ([string]::IsNullOrEmpty($value)) {
                $queryPairs.Add($keyLower)
            }
            else {
                $queryPairs.Add(('{0}={1}' -f $keyLower, [System.Uri]::EscapeDataString($value)))
            }
        }
    }

    $fragment = $uri.Fragment.TrimStart('#')
    $preserveFragment = $false
    if (-not [string]::IsNullOrWhiteSpace($fragment)) {
        $fragmentLower = $fragment.ToLowerInvariant()
        if (
            $fragmentLower -notin @('top', 'content', 'main', 'home', 'overview') -and
            ($fragmentLower -match '[a-z]' -or $fragmentLower -match '^[a-z0-9_-]{6,}$')
        ) {
            $preserveFragment = $true
        }
    }

    $builder = New-Object System.Text.StringBuilder
    [void]$builder.Append($scheme)
    [void]$builder.Append('://')
    [void]$builder.Append($uriHost)
    [void]$builder.Append($path)
    if ($queryPairs.Count -gt 0) {
        [void]$builder.Append('?')
        [void]$builder.Append((($queryPairs | Sort-Object) -join '&'))
    }
    if ($preserveFragment) {
        [void]$builder.Append('#')
        [void]$builder.Append($fragment)
    }

    return $builder.ToString()
}

function Get-FrontmatterValue {
    param(
        [AllowNull()][string]$Text,
        [Parameter(Mandatory = $true)][string]$Key
    )

    if ([string]::IsNullOrEmpty($Text)) {
        return $null
    }

    $trimmed = $Text.TrimStart([char]0xFEFF)
    $frontmatterMatch = [regex]::Match($trimmed, '^(?s)---\r?\n(.*?)\r?\n---\r?\n')
    if (-not $frontmatterMatch.Success) {
        return $null
    }

    $pattern = '(?m)^{0}:\s*(.+?)\s*$' -f [regex]::Escape($Key)
    $match = [regex]::Match($frontmatterMatch.Groups[1].Value, $pattern)
    if (-not $match.Success) {
        return $null
    }

    $value = $match.Groups[1].Value.Trim()
    if (($value.StartsWith('"') -and $value.EndsWith('"')) -or ($value.StartsWith("'") -and $value.EndsWith("'"))) {
        $value = $value.Substring(1, $value.Length - 2)
    }
    return $value
}

function Get-SourceUrlFromMarkdown {
    param([AllowNull()][string]$Text)
    return Get-FrontmatterValue -Text $Text -Key 'source_url'
}

function Get-MarkdownBodyText {
    param([AllowNull()][string]$Text)

    if ([string]::IsNullOrEmpty($Text)) {
        return $Text
    }

    $trimmed = $Text.TrimStart([char]0xFEFF)
    $frontmatterMatch = [regex]::Match($trimmed, '^(?s)---\r?\n(.*?)\r?\n---\r?\n')
    if ($frontmatterMatch.Success) {
        return $trimmed.Substring($frontmatterMatch.Length)
    }

    return $trimmed
}

function Get-FirstHeading {
    param([AllowNull()][string]$Text)

    if ([string]::IsNullOrEmpty($Text)) {
        return $null
    }

    $headingMatch = [regex]::Match($Text, '(?m)^\s*#\s+(.+?)\s*$')
    if ($headingMatch.Success) {
        return $headingMatch.Groups[1].Value.Trim()
    }
    return $null
}

function Clean-Title {
    param([AllowNull()][string]$Title)

    if ([string]::IsNullOrWhiteSpace($Title)) {
        return $null
    }

    $clean = $Title
    $clean = [regex]::Replace($clean, '\[([^\]]+)\]\([^)]+\)', '$1')
    $clean = [regex]::Replace($clean, '<[^>]+>', ' ')
    $clean = [regex]::Replace($clean, '[^\u0000-\u007F]+', ' ')
    $clean = [regex]::Replace($clean, '\s+', ' ').Trim()
    if ([string]::IsNullOrWhiteSpace($clean)) {
        return $null
    }
    return $clean
}

function ConvertTo-YamlScalar {
    param([AllowNull()]$Value)

    if ($null -eq $Value) {
        return "''"
    }

    $text = $Value.ToString()
    $text = $text -replace "'", "''"
    return ("'{0}'" -f $text)
}

function Join-Distinct {
    param([AllowNull()][System.Collections.IEnumerable]$Values)

    if ($null -eq $Values) {
        return $null
    }

    $items = New-Object System.Collections.Generic.List[string]
    foreach ($value in $Values) {
        if ($null -eq $value) { continue }
        $text = $value.ToString().Trim()
        if ([string]::IsNullOrWhiteSpace($text)) { continue }
        if (-not $items.Contains($text)) {
            $items.Add($text)
        }
    }

    if ($items.Count -eq 0) {
        return $null
    }

    return ($items -join '; ')
}

function Get-RelativePath {
    param(
        [Parameter(Mandatory = $true)][string]$BasePath,
        [Parameter(Mandatory = $true)][string]$TargetPath
    )

    $separator = [string][System.IO.Path]::DirectorySeparatorChar
    $baseFull = [System.IO.Path]::GetFullPath($BasePath)
    if (-not $baseFull.EndsWith($separator)) {
        $baseFull = $baseFull + $separator
    }
    $targetFull = [System.IO.Path]::GetFullPath($TargetPath)

    $baseUri = New-Object System.Uri($baseFull)
    $targetUri = New-Object System.Uri($targetFull)
    $relativeUri = $baseUri.MakeRelativeUri($targetUri)
    return [System.Uri]::UnescapeDataString($relativeUri.ToString()).Replace('/', [System.IO.Path]::DirectorySeparatorChar)
}

function Test-MatchesAny {
    param(
        [AllowNull()][string]$Text,
        [Parameter(Mandatory = $true)][string[]]$Patterns
    )

    if ([string]::IsNullOrWhiteSpace($Text)) {
        return $false
    }

    foreach ($pattern in $Patterns) {
        if ($Text -match $pattern) {
            return $true
        }
    }
    return $false
}

function Get-CategoryFromSignals {
    param(
        [Parameter(Mandatory = $true)]$UrlRow,
        [Parameter(Mandatory = $true)]$InventoryRow,
        [Parameter(Mandatory = $true)][string]$UrlSignal,
        [Parameter(Mandatory = $true)][string]$TopicSignal,
        [Parameter(Mandatory = $true)][string]$BodyExcerpt
    )

    $sizeBytes = ConvertTo-NullableLong $InventoryRow.size_bytes
    $quality = if ($null -eq $UrlRow.content_quality) { '' } else { $UrlRow.content_quality.ToString().ToLowerInvariant() }
    $scrapedStatus = if ($null -eq $UrlRow.scraped_status) { '' } else { $UrlRow.scraped_status.ToString().ToLowerInvariant() }
    $truthLevel = if ($null -eq $UrlRow.source_of_truth_level) { '' } else { $UrlRow.source_of_truth_level.ToString().ToLowerInvariant() }
    $rejectionReason = if ($null -eq $InventoryRow.rejection_reason_guess) { '' } else { $InventoryRow.rejection_reason_guess.ToString().ToLowerInvariant() }
    $containsRawHtml = ConvertTo-Bool $InventoryRow.contains_raw_html
    $rawHtmlTagCount = ConvertTo-NullableInt $InventoryRow.raw_html_tag_count

    if ($null -eq $sizeBytes) { $sizeBytes = [int64]0 }
    if ($null -eq $rawHtmlTagCount) { $rawHtmlTagCount = 0 }

    if ($sizeBytes -lt 500) { return '91_rejected_low_value' }
    if ($scrapedStatus -eq 'rejected') { return '91_rejected_low_value' }
    if ($quality -eq 'junk') { return '91_rejected_low_value' }
    if (-not [string]::IsNullOrWhiteSpace($rejectionReason)) { return '91_rejected_low_value' }
    if (Test-MatchesAny -Text $UrlSignal -Patterns @('captcha', 'blocked')) { return '91_rejected_low_value' }
    if ($truthLevel -eq '8_low_value_index_or_search' -and $containsRawHtml -and $rawHtmlTagCount -ge 30 -and ($quality -in @('low', 'unknown'))) {
        return '91_rejected_low_value'
    }
    if (Test-MatchesAny -Text $BodyExcerpt -Patterns @('home help search login register', 'page not found', 'did not exist on "master"', "did not exist on 'master'")) {
        return '91_rejected_low_value'
    }

    if (Test-MatchesAny -Text $UrlSignal -Patterns @('youtube\.com', 'youtu\.be', 'robertferanec', 'altiumacademy', 'eevblog-videos', "phil'?s\s+lab", 'philslab')) { return '15_video_reference_index' }
    if (Test-MatchesAny -Text $UrlSignal -Patterns @('eevblog', 'electronics\.stackexchange', 'forum\.kicad', 'reddit', 'esp32\.com')) { return '12_forums_peer_review' }
    if (Test-MatchesAny -Text $UrlSignal -Patterns @('snapeda', 'ultralibrarian', 'mouser', 'digikey', 'lcsc', 'octopart', 'nexar', 'easyeda', 'samacsys', 'pcblibraries', 'bourns', 'hirose', 'samesky')) { return '13_vendor_parts_cad_models' }
    if (Test-MatchesAny -Text $TopicSignal -Patterns @('doxygen-python', 'kicad-python', 'pcbnew python', '\bswig\b', 'ipc-api', 'apis-and-binding')) { return '02_kicad_python_api' }
    if (Test-MatchesAny -Text $TopicSignal -Patterns @('\bsexpr\b', 'file-formats', 'schematic format', 'footprint format', 'pcb format')) { return '03_kicad_file_formats' }
    if (Test-MatchesAny -Text $TopicSignal -Patterns @('kicad-symbols', 'kicad-footprints', 'kicad-packages3d', 'kicad-library-utils', 'klc\.kicad\.org', 'package_', 'connector_', 'resistor_smd', 'mcu_st', 'mcu_microchip', 'mcu_espressif', 'rf_module', 'device\.kicad_sym', 'interface_usb\.kicad_sym')) { return '04_kicad_libraries_symbols_footprints' }
    if (Test-MatchesAny -Text $TopicSignal -Patterns @('espressif', 'esp32', 'esp-idf', 'esp-hardware-design-guidelines', 'esp32s3', 'esp32-c3', 'esp32-c6', 'esp32-s3-wroom')) { return '05_esp32_espressif' }
    if (Test-MatchesAny -Text $TopicSignal -Patterns @('docs\.kicad\.org/9\.0', 'docs\.kicad\.org', 'kicad\.org', 'eeschema', 'pcbnew', 'gerbview', 'kicad-cli', '\bcli\b', 'pcb_calculator')) { return '01_kicad_core' }
    if (Test-MatchesAny -Text $TopicSignal -Patterns @('calculator', '\bipc\b', 'saturn', 'trace-width', 'microstrip', 'impedance', 'pasternack', 'omnicalculator')) { return '11_calculators_ipc_reference' }
    if (Test-MatchesAny -Text $TopicSignal -Patterns @('usb-c', 'type-c', '\busb\b', 'differential', '\btpd\b', '\besd\b', '\becmf\b', 'high-speed', 'connector usb')) { return '07_usb_c_high_speed_esd' }
    if (Test-MatchesAny -Text $TopicSignal -Patterns @('buck', 'switching', 'regulator', 'dc-dc', 'lm2596', '\btps\b', 'monolithicpower', 'richtek', 'power-supply', 'inductor', 'converter')) { return '08_power_buck_regulators' }
    if (Test-MatchesAny -Text $TopicSignal -Patterns @('pcb-layout', 'grounding', 'ground-plane', '\bemi\b', '\bemc\b', 'signal-integrity', '\brf\b', 'antenna', 'decoupling', '\bvia\b', 'crosstalk')) { return '09_pcb_layout_grounding_emi_si' }
    if (Test-MatchesAny -Text $TopicSignal -Patterns @('jlcpcb', 'pcbway', 'oshpark', 'eurocircuits', '4pcb', 'sunstone', 'protoexpress', 'fabrication', 'assembly', 'gerber', 'stackup', 'soldermask', 'silkscreen', 'annular', 'via-in-pad', 'panel')) { return '10_dfm_fabrication_assembly' }
    if (Test-MatchesAny -Text $TopicSignal -Patterns @('stm32', 'microchip', '\bpic\b', 'atmega', 'attiny', 'arduino', 'raspberrypi', 'rp2040', 'rp2350', 'nordic', 'silabs', 'renesas', 'infineon', '\bwch\b', 'gd32', 'bouffalo')) { return '06_microcontrollers' }

    $detectedCategory = if ($null -eq $UrlRow.detected_category) { '' } else { $UrlRow.detected_category.ToString() }
    if ($detectedCategory -in @(
            '01_kicad_core',
            '02_kicad_python_api',
            '03_kicad_file_formats',
            '04_kicad_libraries_symbols_footprints',
            '05_esp32_espressif',
            '06_microcontrollers',
            '07_usb_c_high_speed_esd',
            '08_power_buck_regulators',
            '09_pcb_layout_grounding_emi_si',
            '10_dfm_fabrication_assembly',
            '11_calculators_ipc_reference',
            '12_forums_peer_review',
            '13_vendor_parts_cad_models',
            '15_video_reference_index',
            '90_unsorted_review',
            '91_rejected_low_value'
        )) {
        return $detectedCategory
    }

    return '90_unsorted_review'
}

function Get-DestinationFileName {
    param(
        [Parameter(Mandatory = $true)][string]$UrlIndexId,
        [Parameter(Mandatory = $true)][string]$SourceFileName
    )

    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($SourceFileName)
    $safeBase = [regex]::Replace($baseName, '[^A-Za-z0-9._-]+', '_')
    $safeBase = $safeBase.Trim('_')
    if ([string]::IsNullOrWhiteSpace($safeBase)) {
        $safeBase = 'source_markdown'
    }
    if ($safeBase.Length -gt 110) {
        $safeBase = $safeBase.Substring(0, 110)
    }
    return ('{0}--{1}.md' -f $UrlIndexId, $safeBase)
}

function Set-PropertyValue {
    param(
        [Parameter(Mandatory = $true)]$Object,
        [Parameter(Mandatory = $true)][string]$Name,
        [AllowNull()]$Value
    )

    if ($null -eq $Object.PSObject.Properties[$Name]) {
        Add-Member -InputObject $Object -MemberType NoteProperty -Name $Name -Value $Value
    }
    else {
        $Object.$Name = $Value
    }
}

Ensure-Directory -Path $KnowledgeRoot
$logsDir = Join-Path $KnowledgeRoot '_logs'
Ensure-Directory -Path $logsDir

if (-not (Test-Path -LiteralPath $InventoryCsv)) {
    throw ('Inventory CSV not found: {0}' -f $InventoryCsv)
}
if (-not (Test-Path -LiteralPath $UrlIndexCsv)) {
    throw ('URL_INDEX CSV not found: {0}' -f $UrlIndexCsv)
}

$importedAt = (Get-Date).ToString('s')
$logPath = Join-Path $logsDir 'classify_copy_log.csv'

$inventoryRows = @(Import-Csv -LiteralPath $InventoryCsv)
$urlRows = @(Import-Csv -LiteralPath $UrlIndexCsv)

$inventoryByPath = @{}
foreach ($row in $inventoryRows) {
    if (-not [string]::IsNullOrWhiteSpace($row.source_file_path)) {
        $inventoryByPath[$row.source_file_path] = $row
    }
}

$urlByNormalized = @{}
$urlBySourcePath = @{}
$urlBySourceFileName = @{}

foreach ($row in $urlRows) {
    Set-PropertyValue -Object $row -Name 'current_knowledge_file' -Value ''

    if (-not [string]::IsNullOrWhiteSpace($row.normalized_url)) {
        $urlByNormalized[$row.normalized_url] = $row
    }
    if (-not [string]::IsNullOrWhiteSpace($row.source_scraped_file)) {
        $urlBySourcePath[$row.source_scraped_file] = $row
        $fileName = [System.IO.Path]::GetFileName($row.source_scraped_file)
        if (-not $urlBySourceFileName.ContainsKey($fileName)) {
            $urlBySourceFileName[$fileName] = New-Object System.Collections.Generic.List[object]
        }
        $urlBySourceFileName[$fileName].Add($row)
    }
}

$processedFiles = New-Object System.Collections.Generic.List[object]
foreach ($sourceFolder in $SourceFolders) {
    if (-not (Test-Path -LiteralPath $sourceFolder)) {
        continue
    }
    foreach ($file in Get-ChildItem -LiteralPath $sourceFolder -File -Filter '*.md') {
        $processedFiles.Add($file)
    }
}

$processedFiles = @($processedFiles | Sort-Object FullName)

$logRows = New-Object System.Collections.Generic.List[object]
$matchedCount = 0
$unmatchedCount = 0
$copiedCount = 0
$alreadyPresentCount = 0
$rejectedCount = 0
$unsortedCount = 0
$matchByFilenameInferenceCount = 0
$skippedNonCanonicalCount = 0
$categoryCountMap = @{}

foreach ($file in $processedFiles) {
    $text = Get-SafeText -Path $file.FullName
    $sourceUrl = Get-SourceUrlFromMarkdown -Text $text
    $normalizedUrl = Normalize-Url -Url $sourceUrl
    $body = Get-MarkdownBodyText -Text $text

    $frontmatterTitle = Get-FrontmatterValue -Text $text -Key 'title'
    $headingTitle = Get-FirstHeading -Text $body
    $title = Clean-Title -Title $frontmatterTitle
    if ([string]::IsNullOrWhiteSpace($title)) {
        $title = Clean-Title -Title $headingTitle
    }
    if ([string]::IsNullOrWhiteSpace($title)) {
        $title = Clean-Title -Title $file.BaseName
    }

    $inventoryRow = $null
    if ($inventoryByPath.ContainsKey($file.FullName)) {
        $inventoryRow = $inventoryByPath[$file.FullName]
    }
    else {
        $inventoryRow = [pscustomobject]@{
            source_file_path = $file.FullName
            source_file_name = $file.Name
            source_folder = Split-Path -Leaf $file.DirectoryName
            size_bytes = $file.Length
            last_write_time = $file.LastWriteTime.ToString('s')
            likely_domain = $null
            likely_category_guess = $null
            quality_guess = 'unknown'
            rejection_reason_guess = $null
            contains_raw_html = $false
            raw_html_tag_count = 0
        }
    }

    $matchedUrlRow = $null
    $matchMethod = $null
    $wasInferredByFilename = $false

    if (-not [string]::IsNullOrWhiteSpace($normalizedUrl) -and $urlByNormalized.ContainsKey($normalizedUrl)) {
        $matchedUrlRow = $urlByNormalized[$normalizedUrl]
        $matchMethod = 'source_url'
    }
    elseif ($urlBySourcePath.ContainsKey($file.FullName)) {
        $matchedUrlRow = $urlBySourcePath[$file.FullName]
        $matchMethod = 'source_scraped_file'
    }
    elseif ($urlBySourceFileName.ContainsKey($file.Name) -and $urlBySourceFileName[$file.Name].Count -eq 1) {
        $matchedUrlRow = $urlBySourceFileName[$file.Name][0]
        $matchMethod = 'source_filename'
        $wasInferredByFilename = $true
        $matchByFilenameInferenceCount += 1
    }

    if ($null -eq $matchedUrlRow) {
        $unmatchedCount += 1
        $logRows.Add([pscustomobject][ordered]@{
                source_file_path = $file.FullName
                source_file_name = $file.Name
                source_folder = Split-Path -Leaf $file.DirectoryName
                source_url = $sourceUrl
                normalized_url = $normalizedUrl
                url_index_id = $null
                match_method = $null
                category = $null
                destination_file = $null
                action = 'skipped_unmatched_url_index'
                reason = 'no_url_index_match'
            })
        continue
    }

    $matchedCount += 1

    if (-not [string]::IsNullOrWhiteSpace($matchedUrlRow.source_scraped_file) -and $matchedUrlRow.source_scraped_file -ne $file.FullName) {
        $skippedNonCanonicalCount += 1
        $logRows.Add([pscustomobject][ordered]@{
                source_file_path = $file.FullName
                source_file_name = $file.Name
                source_folder = Split-Path -Leaf $file.DirectoryName
                source_url = $sourceUrl
                normalized_url = $normalizedUrl
                url_index_id = $matchedUrlRow.id
                match_method = $matchMethod
                category = $null
                destination_file = $null
                action = 'skipped_noncanonical_duplicate'
                reason = ('canonical_source_scraped_file={0}' -f $matchedUrlRow.source_scraped_file)
            })
        continue
    }

    $sourceDomain = if (-not [string]::IsNullOrWhiteSpace($matchedUrlRow.source_domain)) { $matchedUrlRow.source_domain } else { $inventoryRow.likely_domain }

    $urlSignal = ('{0} {1} {2} {3} {4} {5}' -f $matchedUrlRow.original_url, $matchedUrlRow.normalized_url, $matchedUrlRow.source_domain, $file.Name, $title, $matchedUrlRow.detected_category).ToLowerInvariant()
    $bodyExcerpt = $body
    if ($bodyExcerpt.Length -gt 12000) {
        $bodyExcerpt = $bodyExcerpt.Substring(0, 12000)
    }
    $bodyExcerpt = $bodyExcerpt.ToLowerInvariant()
    $topicSignal = ('{0} {1} {2} {3} {4}' -f $urlSignal, $bodyExcerpt, $matchedUrlRow.source_of_truth_level, $matchedUrlRow.trust_label, $inventoryRow.likely_category_guess).ToLowerInvariant()

    $knowledgeCategory = Get-CategoryFromSignals -UrlRow $matchedUrlRow -InventoryRow $inventoryRow -UrlSignal $urlSignal -TopicSignal $topicSignal -BodyExcerpt $bodyExcerpt

    if (-not $categoryCountMap.ContainsKey($knowledgeCategory)) {
        $categoryCountMap[$knowledgeCategory] = 0
    }
    $categoryCountMap[$knowledgeCategory] += 1

    if ($knowledgeCategory -eq '91_rejected_low_value') {
        $rejectedCount += 1
    }
    elseif ($knowledgeCategory -eq '90_unsorted_review') {
        $unsortedCount += 1
    }

    $destinationDir = Join-Path $KnowledgeRoot $knowledgeCategory
    Ensure-Directory -Path $destinationDir

    $destinationFileName = Get-DestinationFileName -UrlIndexId $matchedUrlRow.id -SourceFileName $file.Name
    $destinationPath = Join-Path $destinationDir $destinationFileName
    $relativeDestination = Get-RelativePath -BasePath $KnowledgeRoot -TargetPath $destinationPath

    $contentQuality = if (-not [string]::IsNullOrWhiteSpace($matchedUrlRow.content_quality)) { $matchedUrlRow.content_quality } else { $inventoryRow.quality_guess }
    $futureRescrapeCandidate = 'false'
    if ((ConvertTo-Bool $matchedUrlRow.needs_future_rescrape) -or ($matchedUrlRow.scraped_status -in @('failed', 'needs_rescrape', 'not_found_in_outputs'))) {
        $futureRescrapeCandidate = 'true'
    }

    $notesParts = New-Object System.Collections.Generic.List[string]
    $notesParts.Add(('match_method={0}' -f $matchMethod))
    if ($wasInferredByFilename) {
        $notesParts.Add('url_match_inferred_by_filename')
    }
    if (-not [string]::IsNullOrWhiteSpace($inventoryRow.rejection_reason_guess)) {
        $notesParts.Add(('source_rejection_guess={0}' -f $inventoryRow.rejection_reason_guess))
    }
    $rawHtmlTagCount = ConvertTo-NullableInt $inventoryRow.raw_html_tag_count
    if ($null -ne $rawHtmlTagCount -and $rawHtmlTagCount -gt 0) {
        $notesParts.Add(('raw_html_tags={0}' -f $rawHtmlTagCount))
    }
    if (-not [string]::IsNullOrWhiteSpace($matchedUrlRow.duplicate_group_id)) {
        $notesParts.Add(('duplicate_group_id={0}' -f $matchedUrlRow.duplicate_group_id))
    }
    if (-not [string]::IsNullOrWhiteSpace($matchedUrlRow.scraped_status) -and $matchedUrlRow.scraped_status -ne 'success') {
        $notesParts.Add(('scraped_status={0}' -f $matchedUrlRow.scraped_status))
    }
    $notes = Join-Distinct -Values $notesParts

    $frontmatterLines = New-Object System.Collections.Generic.List[string]
    $frontmatterLines.Add('---')
    $frontmatterLines.Add(('title: {0}' -f (ConvertTo-YamlScalar $title)))
    $frontmatterLines.Add(('source_url: {0}' -f (ConvertTo-YamlScalar $matchedUrlRow.original_url)))
    $frontmatterLines.Add(('normalized_url: {0}' -f (ConvertTo-YamlScalar $matchedUrlRow.normalized_url)))
    $frontmatterLines.Add(('url_index_id: {0}' -f (ConvertTo-YamlScalar $matchedUrlRow.id)))
    $frontmatterLines.Add(('source_domain: {0}' -f (ConvertTo-YamlScalar $sourceDomain)))
    $frontmatterLines.Add(('source_file: {0}' -f (ConvertTo-YamlScalar $file.FullName)))
    $frontmatterLines.Add(('source_folder: {0}' -f (ConvertTo-YamlScalar (Split-Path -Leaf $file.DirectoryName))))
    $frontmatterLines.Add(('knowledge_category: {0}' -f (ConvertTo-YamlScalar $knowledgeCategory)))
    $frontmatterLines.Add(('source_of_truth_level: {0}' -f (ConvertTo-YamlScalar $matchedUrlRow.source_of_truth_level)))
    $frontmatterLines.Add(('trust_label: {0}' -f (ConvertTo-YamlScalar $matchedUrlRow.trust_label)))
    $frontmatterLines.Add(('imported_at: {0}' -f (ConvertTo-YamlScalar $importedAt)))
    $frontmatterLines.Add(('content_quality: {0}' -f (ConvertTo-YamlScalar $contentQuality)))
    $frontmatterLines.Add(('future_rescrape_candidate: {0}' -f $futureRescrapeCandidate.ToLowerInvariant()))
    $frontmatterLines.Add(('notes: {0}' -f (ConvertTo-YamlScalar $notes)))
    $frontmatterLines.Add('---')
    $frontmatterLines.Add('')

    $bodyWithoutLeadingBlank = $body.TrimStart("`r", "`n")
    $outputText = (($frontmatterLines -join "`r`n") + $bodyWithoutLeadingBlank)

    $action = 'copied'
    $reason = 'copied_to_category'
    if (Test-Path -LiteralPath $destinationPath) {
        if ($Force) {
            $action = 'overwritten'
            $reason = 'force_overwrite'
        }
        else {
            $action = 'already_present'
            $reason = 'destination_exists'
            $alreadyPresentCount += 1
        }
    }

    if ($action -in @('copied', 'overwritten')) {
        Set-Content -LiteralPath $destinationPath -Value $outputText -Encoding UTF8
        $copiedCount += 1
    }

    $matchedUrlRow.current_knowledge_file = $relativeDestination

    $logRows.Add([pscustomobject][ordered]@{
            source_file_path = $file.FullName
            source_file_name = $file.Name
            source_folder = Split-Path -Leaf $file.DirectoryName
            source_url = $matchedUrlRow.original_url
            normalized_url = $matchedUrlRow.normalized_url
            url_index_id = $matchedUrlRow.id
            match_method = $matchMethod
            category = $knowledgeCategory
            destination_file = $relativeDestination
            action = $action
            reason = $reason
        })
}

$logRows | Export-Csv -LiteralPath $logPath -NoTypeInformation -Encoding UTF8

$urlRows | Export-Csv -LiteralPath $UrlIndexCsv -NoTypeInformation -Encoding UTF8
$urlIndexJsonPath = Join-Path $KnowledgeRoot 'URL_INDEX.json'
$urlRows | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $urlIndexJsonPath -Encoding UTF8

$linkedUrlCount = @($urlRows | Where-Object { -not [string]::IsNullOrWhiteSpace($_.current_knowledge_file) }).Count
$unlinkedUrlCount = $urlRows.Count - $linkedUrlCount

$knowledgeCategoryRows = @(
    Get-ChildItem -LiteralPath $KnowledgeRoot -Directory |
    Where-Object { $_.Name -match '^(00|01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|90|91|99)_' } |
    Sort-Object Name |
    ForEach-Object {
        $mdCount = @(Get-ChildItem -LiteralPath $_.FullName -File -Filter '*.md' | Where-Object { $_.Name -ne '.gitkeep' }).Count
        [pscustomobject][ordered]@{
            category = $_.Name
            markdown_files = $mdCount
        }
    }
)

$statusSummaryLines = @(
    $urlRows |
    Group-Object scraped_status |
    Sort-Object Name |
    ForEach-Object {
        '- `{0}`: `{1}`' -f $_.Name, $_.Count
    }
)

$topDomains = @(
    $urlRows |
    Group-Object source_domain |
    Sort-Object Count -Descending |
    Select-Object -First 15 |
    ForEach-Object {
        $domainName = if ([string]::IsNullOrWhiteSpace($_.Name)) { '(unknown)' } else { $_.Name }
        '- `{0}`: `{1}`' -f $domainName, $_.Count
    }
)

$topLinkedCategories = @(
    $knowledgeCategoryRows |
    Where-Object { $_.markdown_files -gt 0 } |
    Sort-Object -Property @{ Expression = { $_.markdown_files }; Descending = $true }, @{ Expression = { $_.category }; Descending = $false } |
    Select-Object -First 20
)

$urlIndexMarkdownLines = New-Object System.Collections.Generic.List[string]
$urlIndexMarkdownLines.Add('# URL_INDEX')
$urlIndexMarkdownLines.Add('')
$urlIndexMarkdownLines.Add(('Generated at: `{0}`' -f $importedAt))
$urlIndexMarkdownLines.Add('')
$urlIndexMarkdownLines.Add('## Summary')
$urlIndexMarkdownLines.Add('')
$urlIndexMarkdownLines.Add(('- Total URLs known: `{0}`' -f $urlRows.Count))
$urlIndexMarkdownLines.Add(('- URLs linked to copied knowledge files: `{0}`' -f $linkedUrlCount))
$urlIndexMarkdownLines.Add(('- URLs still without a knowledge file: `{0}`' -f $unlinkedUrlCount))
$urlIndexMarkdownLines.Add(('- Markdown files copied this run: `{0}`' -f $copiedCount))
$urlIndexMarkdownLines.Add(('- Markdown files already present and relinked: `{0}`' -f $alreadyPresentCount))
$urlIndexMarkdownLines.Add('')
$urlIndexMarkdownLines.Add('## URL Status Summary')
$urlIndexMarkdownLines.Add('')
foreach ($line in $statusSummaryLines) {
    $urlIndexMarkdownLines.Add($line)
}
$urlIndexMarkdownLines.Add('')
$urlIndexMarkdownLines.Add('## Top Domains')
$urlIndexMarkdownLines.Add('')
foreach ($line in $topDomains) {
    $urlIndexMarkdownLines.Add($line)
}
$urlIndexMarkdownLines.Add('')
$urlIndexMarkdownLines.Add('## Knowledge Category Counts')
$urlIndexMarkdownLines.Add('')
$urlIndexMarkdownLines.Add('| Category | Markdown Files |')
$urlIndexMarkdownLines.Add('| --- | ---: |')
foreach ($row in $topLinkedCategories) {
    $urlIndexMarkdownLines.Add(('| {0} | {1} |' -f $row.category, $row.markdown_files))
}
$urlIndexMarkdownLines.Add('')
$urlIndexMarkdownLines.Add('## Notes')
$urlIndexMarkdownLines.Add('')
$urlIndexMarkdownLines.Add('1. `current_knowledge_file` is populated only for copied or already-present Markdown imports.')
$urlIndexMarkdownLines.Add('2. PDF rows remain unlinked here until PDF extraction/import is implemented.')
$urlIndexMarkdownLines.Add('3. Non-canonical duplicate source files remain in the raw scrape folders and are recorded in `_logs/classify_copy_log.csv`.')

$urlIndexMarkdownPath = Join-Path $KnowledgeRoot 'URL_INDEX.md'
$urlIndexMarkdownLines | Set-Content -LiteralPath $urlIndexMarkdownPath -Encoding UTF8

$indexLines = New-Object System.Collections.Generic.List[string]
$indexLines.Add('# knowledge_scrape Index')
$indexLines.Add('')
$indexLines.Add(('Generated at: `{0}`' -f $importedAt))
$indexLines.Add('')
$indexLines.Add('- `SOURCE_AUDIT.md`: scrape input inventory summary.')
$indexLines.Add('- `URL_INDEX.csv/json/md`: canonical URL registry with `current_knowledge_file` links.')
$indexLines.Add('- `RESCRAPE_QUEUE.csv`: follow-up scrape targets from the registry builder.')
$indexLines.Add('- `_logs/classify_copy_log.csv`: copy/classification actions for each source Markdown file.')
$indexLines.Add('- `_raw_inventory/`: raw file inventory and QA reports.')
$indexLines.Add('- `_source_registry/`: source URL list registry, domain summary, and success/error indexes.')
$indexLines.Add('')
$indexLines.Add('## Category Counts')
$indexLines.Add('')
$indexLines.Add('| Category | Markdown Files |')
$indexLines.Add('| --- | ---: |')
foreach ($row in $knowledgeCategoryRows) {
    $indexLines.Add(('| {0} | {1} |' -f $row.category, $row.markdown_files))
}

$indexPath = Join-Path $KnowledgeRoot 'INDEX.md'
$indexLines | Set-Content -LiteralPath $indexPath -Encoding UTF8

$manifest = [ordered]@{
    name = 'knowledge_scrape'
    status = 'markdown_classification_and_copy_completed'
    created_for = 'scrape audit and URL/source inventory'
    content_copy_status = 'markdown_completed'
    pdf_extraction_status = 'not_started'
    primary_builders = @(
        '_scripts/01_build_raw_inventory.ps1',
        '_scripts/02_build_url_registry.ps1',
        '_scripts/03_classify_copy_markdown.ps1'
    )
    generated_at = $importedAt
    scan_roots = $SourceFolders
    inventory_csv = $InventoryCsv
    url_index_csv = $UrlIndexCsv
    copied_count = $copiedCount
    already_present_count = $alreadyPresentCount
    rejected_count = $rejectedCount
    unsorted_count = $unsortedCount
    url_index_matched_count = $matchedCount
    url_index_unmatched_count = $unmatchedCount
    filename_inference_match_count = $matchByFilenameInferenceCount
    noncanonical_duplicate_skipped_count = $skippedNonCanonicalCount
    linked_url_count = $linkedUrlCount
    unlinked_url_count = $unlinkedUrlCount
    category_counts = [ordered]@{}
}

foreach ($row in $knowledgeCategoryRows) {
    $manifest.category_counts[$row.category] = $row.markdown_files
}

$manifestPath = Join-Path $KnowledgeRoot 'MANIFEST.json'
$manifest | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $manifestPath -Encoding UTF8

[pscustomobject][ordered]@{
    processed_markdown_files = $processedFiles.Count
    copied_count = $copiedCount
    already_present_count = $alreadyPresentCount
    rejected_count = $rejectedCount
    unsorted_count = $unsortedCount
    url_index_matched_count = $matchedCount
    url_index_unmatched_count = $unmatchedCount
    filename_inference_match_count = $matchByFilenameInferenceCount
    noncanonical_duplicate_skipped_count = $skippedNonCanonicalCount
    linked_url_count = $linkedUrlCount
    unlinked_url_count = $unlinkedUrlCount
} | Format-List
