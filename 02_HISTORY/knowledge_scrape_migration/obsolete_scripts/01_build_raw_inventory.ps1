param(
    [string]$KnowledgeRoot = (Split-Path -Parent $PSScriptRoot),
    [string[]]$ScanFolders = @(
        'C:\KICAD_SCRAPE\markdown_10k_clean',
        'C:\KICAD_SCRAPE\markdown_url2_clean'
    ),
    [string[]]$UrlListFiles = @(
        'C:\KICAD_SCRAPE\urls.txt',
        'C:\KICAD_SCRAPE\url2.txt'
    )
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

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

function Get-Bytes {
    param([Parameter(Mandatory = $true)][string]$Path)
    return [System.IO.File]::ReadAllBytes($Path)
}

function Get-Sha256HexFromText {
    param([AllowNull()][string]$Text)
    if ($null -eq $Text) {
        return $null
    }
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        $bytes = [System.Text.Encoding]::UTF8.GetBytes($Text)
        $hashBytes = $sha.ComputeHash($bytes)
        return ([System.BitConverter]::ToString($hashBytes)).Replace('-', '').ToLowerInvariant()
    }
    finally {
        $sha.Dispose()
    }
}

function Normalize-Url {
    param([AllowNull()][string]$Url)

    if ([string]::IsNullOrWhiteSpace($Url)) {
        return $null
    }

    $candidate = $Url.Trim()
    $uri = $null
    if (-not [System.Uri]::TryCreate($candidate, [System.UriKind]::Absolute, [ref]$uri)) {
        return $candidate.ToLowerInvariant()
    }

    $scheme = if ([string]::IsNullOrWhiteSpace($uri.Scheme)) { 'https' } else { $uri.Scheme.ToLowerInvariant() }
    if ([string]::IsNullOrWhiteSpace($uri.Host)) {
        return $candidate.ToLowerInvariant()
    }
    $uriHost = $uri.Host.ToLowerInvariant()
    if ($uriHost.StartsWith('www.')) {
        $uriHost = $uriHost.Substring(4)
    }

    $path = if ([string]::IsNullOrWhiteSpace($uri.AbsolutePath)) { '/' } else { $uri.AbsolutePath }
    $path = [regex]::Replace($path, '/+', '/')
    if ($path.Length -gt 1 -and $path.EndsWith('/')) {
        $path = $path.TrimEnd('/')
    }

    $dropParams = @('fbclid', 'gclid', 'mc_cid', 'mc_eid', 'ref', 'source')
    $queryPairs = New-Object System.Collections.Generic.List[string]
    if (-not [string]::IsNullOrWhiteSpace($uri.Query)) {
        foreach ($pair in $uri.Query.TrimStart('?').Split('&', [System.StringSplitOptions]::RemoveEmptyEntries)) {
            $parts = $pair.Split('=', 2)
            $key = [System.Uri]::UnescapeDataString($parts[0]).ToLowerInvariant()
            if ($key.StartsWith('utm_') -or $dropParams -contains $key) {
                continue
            }
            $value = if ($parts.Count -gt 1) { [System.Uri]::UnescapeDataString($parts[1]) } else { '' }
            if ([string]::IsNullOrEmpty($value)) {
                $queryPairs.Add($key)
            }
            else {
                $queryPairs.Add(('{0}={1}' -f $key, [System.Uri]::EscapeDataString($value)))
            }
        }
    }

    $query = ($queryPairs | Sort-Object) -join '&'
    $base = '{0}://{1}{2}' -f $scheme, $uriHost, $path
    if ([string]::IsNullOrEmpty($query)) {
        return $base
    }
    return '{0}?{1}' -f $base, $query
}

function Get-SourceUrlFromMarkdown {
    param([AllowNull()][string]$Text)

    if ([string]::IsNullOrEmpty($Text)) {
        return $null
    }

    $trimmed = $Text.TrimStart([char]0xFEFF)
    $frontmatterMatch = [regex]::Match($trimmed, '^(?s)---\r?\n(.*?)\r?\n---\r?\n')
    if (-not $frontmatterMatch.Success) {
        return $null
    }

    $sourceMatch = [regex]::Match($frontmatterMatch.Groups[1].Value, '(?m)^source_url:\s*(.+?)\s*$')
    if (-not $sourceMatch.Success) {
        return $null
    }

    $value = $sourceMatch.Groups[1].Value.Trim()
    if (($value.StartsWith('"') -and $value.EndsWith('"')) -or ($value.StartsWith("'") -and $value.EndsWith("'"))) {
        $value = $value.Substring(1, $value.Length - 2)
    }

    return $value
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

function Get-RawHtmlTagCount {
    param([AllowNull()][string]$Text)

    if ([string]::IsNullOrEmpty($Text)) {
        return 0
    }

    $pattern = '(?i)<!DOCTYPE html|</?(html|head|body|div|span|table|thead|tbody|tr|td|th|script|style|iframe|section|article|main|nav|img|svg|path|meta|link|colgroup|col)\b'
    $count = ([regex]::Matches($Text, $pattern)).Count
    $count += ([regex]::Matches($Text, 'data:image/')).Count
    return $count
}

function Get-LikelyDomain {
    param(
        [AllowNull()][string]$DetectedSourceUrl,
        [Parameter(Mandatory = $true)][string]$FileName
    )

    if (-not [string]::IsNullOrWhiteSpace($DetectedSourceUrl)) {
        $uri = $null
        if ([System.Uri]::TryCreate($DetectedSourceUrl, [System.UriKind]::Absolute, [ref]$uri) -and -not [string]::IsNullOrWhiteSpace($uri.Host)) {
            $uriHost = $uri.Host.ToLowerInvariant()
            if ($uriHost.StartsWith('www.')) {
                $uriHost = $uriHost.Substring(4)
            }
            return $uriHost
        }
    }

    if ($FileName -match '^([A-Za-z0-9._-]+?)-') {
        return $Matches[1].ToLowerInvariant()
    }

    return $null
}

function Get-LikelyCategoryGuess {
    param(
        [AllowNull()][string]$DetectedSourceUrl,
        [Parameter(Mandatory = $true)][string]$FileName,
        [AllowNull()][string]$Text,
        [bool]$IsPdf
    )

    $safeText = if ($null -eq $Text) { '' } else { $Text }
    $signal = '{0} {1} {2}' -f $DetectedSourceUrl, $FileName.ToLowerInvariant(), $safeText.ToLowerInvariant()

    if ($IsPdf) { return '14_datasheets_pdf_markdown' }
    if ($signal -match 'forum\.kicad\.info|eevblog\.com|stackexchange\.com|reddit\.com') { return '12_forums_peer_review' }
    if ($signal -match 'youtube\.com|youtu\.be') { return '15_video_reference_index' }
    if ($signal -match 'snapeda|ultralibrarian|componentsearchengine|mouser|digikey|lcsc') { return '13_vendor_parts_cad_models' }
    if ($signal -match 'docs\.kicad\.org/.+doxygen|docs\.kicad\.org/.+python|pcbnew|ipc-api|kicad-python|apis-and-binding') { return '02_kicad_python_api' }
    if ($signal -match 'dev-docs\.kicad\.org/.+file-formats|sexpr|file-formats') { return '03_kicad_file_formats' }
    if ($signal -match 'docs\.kicad\.org|dev-docs\.kicad\.org|kicad-cli|eeschema|pcbnew') { return '01_kicad_core' }
    if ($signal -match 'footprint|symbol|3d|library|libraries|klc\.kicad\.org') { return '04_kicad_libraries_symbols_footprints' }
    if ($signal -match 'espressif|esp32|esp-idf|esp-iot|esptool') { return '05_esp32_espressif' }
    if ($signal -match 'stm32|microchip|avr|sam|nordic|arduino|raspberrypi|rp2040|rp2350|wch|silabs|sony|nxp') { return '06_microcontrollers' }
    if ($signal -match 'usb|type-c|high-speed|esd|superspeed') { return '07_usb_c_high_speed_esd' }
    if ($signal -match 'buck|regulator|converter|power-supply|switching-regulator|vrm') { return '08_power_buck_regulators' }
    if ($signal -match 'ground|emi|emc|signal integrity|differential pair|stackup|pcb layout|layout guidelines|trace width') { return '09_pcb_layout_grounding_emi_si' }
    if ($signal -match 'jlcpcb|oshpark|4pcb|pcbway|eurocircuits|protoexpress|assembly|dfm|fabrication') { return '10_dfm_fabrication_assembly' }
    if ($signal -match 'calculator|microstrip|ipc') { return '11_calculators_ipc_reference' }

    return '90_unsorted_review'
}

function Get-RejectionReasonGuess {
    param(
        [AllowNull()][string]$DetectedSourceUrl,
        [Parameter(Mandatory = $true)][string]$FileName,
        [AllowNull()][string]$Text,
        [bool]$IsErrorLog,
        [bool]$IsDoneLog
    )

    if ($IsErrorLog) { return 'error_log' }
    if ($IsDoneLog) { return 'done_log' }

    $safeText = if ($null -eq $Text) { '' } else { $Text }
    $signal = '{0} {1} {2}' -f $DetectedSourceUrl, $FileName.ToLowerInvariant(), $safeText.ToLowerInvariant()

    if ($signal -match 'captcha') { return 'captcha_page' }
    if ($signal -match '404 page|page not found|\(404\) not found') { return '404_or_missing_page' }
    if ($signal -match 'did not exist on "master"|did not exist on ''master''') { return 'invalid_gitlab_tree_path' }
    if ($signal -match 'questions/tagged|/search|search\.md|tagged/|/tag/|/tags/') { return 'search_or_tag_index' }
    if ($signal -match 'forum index|login with username|activation email|home help search login register') { return 'forum_index_or_shell_page' }
    if ($signal -match 'issues(\?|$)|/issues$|/tree/master|/blob/main|topic-list-container') { return 'repo_or_forum_index_page' }
    if ($signal -match '/20\d{2}/\d{2}/3[2-9]/') { return 'invalid_archive_date_path' }

    return $null
}

function Get-QualityGuess {
    param(
        [bool]$IsPdf,
        [bool]$SourceUrlPresent,
        [bool]$ContainsRawHtml,
        [AllowNull()][string]$LikelyDomain,
        [AllowNull()][string]$FirstHeading,
        [AllowNull()][string]$RejectionReasonGuess
    )

    if (-not [string]::IsNullOrWhiteSpace($RejectionReasonGuess)) {
        if ($RejectionReasonGuess -in @('error_log', 'done_log')) {
            return 'low'
        }
        return 'junk'
    }

    if ($IsPdf) {
        if ($LikelyDomain -match 'ti\.com|microchip\.com|espressif\.com|nexperia\.com|datasheets\.raspberrypi\.com|silabs\.com|rohm\.com|onsemi\.com') {
            return 'high'
        }
        return 'medium'
    }

    if (-not $SourceUrlPresent) {
        return 'low'
    }

    if ($LikelyDomain -match 'docs\.kicad\.org|dev-docs\.kicad\.org|docs\.espressif\.com|ti\.com|microchip\.com|espressif\.com') {
        if ($ContainsRawHtml) { return 'medium' }
        return 'high'
    }

    if ($LikelyDomain -match 'forum\.kicad\.info|eevblog\.com|stackexchange\.com|reddit\.com') {
        if ($FirstHeading) { return 'medium' }
        return 'low'
    }

    if ($ContainsRawHtml) {
        return 'low'
    }

    if ($FirstHeading) {
        return 'medium'
    }

    return 'unknown'
}

function Get-NormalizedTextForDuplicateHash {
    param([AllowNull()][string]$Text)

    if ([string]::IsNullOrEmpty($Text)) {
        return $null
    }

    $normalized = $Text.ToLowerInvariant()
    $normalized = [regex]::Replace($normalized, 'data:image/[^\s)]+', ' ')
    $normalized = [regex]::Replace($normalized, 'https?://\S+', ' ')
    $normalized = [regex]::Replace($normalized, '\[[^\]]+\]\([^)]+\)', ' ')
    $normalized = [regex]::Replace($normalized, '<[^>]+>', ' ')
    $normalized = [regex]::Replace($normalized, '[^a-z0-9]+', ' ')
    $normalized = [regex]::Replace($normalized, '\s+', ' ').Trim()
    return $normalized
}

Ensure-Directory -Path $KnowledgeRoot
$rawInventoryDir = Join-Path $KnowledgeRoot '_raw_inventory'
$sourceRegistryDir = Join-Path $KnowledgeRoot '_source_registry'
$logsDir = Join-Path $KnowledgeRoot '_logs'
Ensure-Directory -Path $rawInventoryDir
Ensure-Directory -Path $sourceRegistryDir
Ensure-Directory -Path $logsDir

$inventoryRows = New-Object System.Collections.Generic.List[object]
$urlSourceRows = New-Object System.Collections.Generic.List[object]
$duplicateSeedRows = New-Object System.Collections.Generic.List[object]
$inventoryByNormalizedSourceUrl = @{}

foreach ($listPath in $UrlListFiles) {
    if (-not (Test-Path -LiteralPath $listPath)) {
        continue
    }

    $lineNumber = 0
    foreach ($line in [System.IO.File]::ReadLines($listPath)) {
        $lineNumber += 1
        $trimmed = $line.Trim()
        if ([string]::IsNullOrWhiteSpace($trimmed)) {
            continue
        }

        $sourceTag = $null
        $extractedUrl = $trimmed
        if ($trimmed.Contains("`t")) {
            $parts = $trimmed.Split("`t")
            if ($parts.Count -ge 2) {
                $sourceTag = $parts[0].Trim()
                $extractedUrl = $parts[$parts.Count - 1].Trim()
            }
        }

        $normalizedUrl = Normalize-Url -Url $extractedUrl
        $urlDomain = $null
        if ($normalizedUrl) {
            try {
                $urlDomain = ([System.Uri]$normalizedUrl).Host.ToLowerInvariant()
            }
            catch {
                $urlDomain = $null
            }
        }

        $urlSourceRows.Add([pscustomobject]@{
                list_file = [System.IO.Path]::GetFileName($listPath)
                line_number = $lineNumber
                raw_line = $trimmed
                source_tag = $sourceTag
                extracted_url = $extractedUrl
                normalized_url = $normalizedUrl
                url_domain = $urlDomain
            })
    }
}

foreach ($scanFolder in $ScanFolders) {
    if (-not (Test-Path -LiteralPath $scanFolder)) {
        Write-Warning ('Scan folder missing: {0}' -f $scanFolder)
        continue
    }

    $folderName = Split-Path -Leaf $scanFolder
    foreach ($item in Get-ChildItem -LiteralPath $scanFolder -File) {
        $extension = $item.Extension.ToLowerInvariant()
        $isMarkdown = $extension -eq '.md'
        $isPdf = $extension -eq '.pdf'
        $isErrorLog = $item.Name -ieq '_errors.txt'
        $isDoneLog = $item.Name -ieq '_done_urls.txt'

        $textContent = $null
        $lineCount = 0
        $firstHeading = $null
        $detectedSourceUrl = $null
        $rawHtmlTagCount = 0
        $containsRawHtml = $false
        $duplicateHash = $null
        $textForDuplicateHash = $null

        if ($isMarkdown -or $extension -eq '.txt') {
            $textContent = Get-SafeText -Path $item.FullName
            $lineCount = ([regex]::Matches($textContent, "\r?\n")).Count + 1
            $firstHeading = Get-FirstHeading -Text $textContent
            if ($isMarkdown) {
                $detectedSourceUrl = Get-SourceUrlFromMarkdown -Text $textContent
                $textForDuplicateHash = Get-MarkdownBodyText -Text $textContent
            }
            else {
                $textForDuplicateHash = $textContent
            }
            $rawHtmlTagCount = Get-RawHtmlTagCount -Text $textContent
            $containsRawHtml = $rawHtmlTagCount -gt 0
            $duplicateHash = Get-Sha256HexFromText -Text (Get-NormalizedTextForDuplicateHash -Text $textForDuplicateHash)
        }
        elseif ($isPdf) {
            $bytes = Get-Bytes -Path $item.FullName
            $headLength = [Math]::Min(4096, $bytes.Length)
            $headText = [System.Text.Encoding]::ASCII.GetString($bytes, 0, $headLength)
            $rawHtmlTagCount = Get-RawHtmlTagCount -Text $headText
            $containsRawHtml = $rawHtmlTagCount -gt 0
            $duplicateHash = (Get-FileHash -LiteralPath $item.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
        }

        $sourceUrlPresent = -not [string]::IsNullOrWhiteSpace($detectedSourceUrl)
        $likelyDomain = Get-LikelyDomain -DetectedSourceUrl $detectedSourceUrl -FileName $item.Name
        $likelyCategoryGuess = if ($isErrorLog -or $isDoneLog) {
            '99_source_logs'
        }
        else {
            Get-LikelyCategoryGuess -DetectedSourceUrl $detectedSourceUrl -FileName $item.Name -Text $textContent -IsPdf:$isPdf
        }
        $rejectionReasonGuess = Get-RejectionReasonGuess -DetectedSourceUrl $detectedSourceUrl -FileName $item.Name -Text $textContent -IsErrorLog:$isErrorLog -IsDoneLog:$isDoneLog
        $qualityGuess = Get-QualityGuess -IsPdf:$isPdf -SourceUrlPresent:$sourceUrlPresent -ContainsRawHtml:$containsRawHtml -LikelyDomain $likelyDomain -FirstHeading $firstHeading -RejectionReasonGuess $rejectionReasonGuess
        $normalizedSourceUrl = Normalize-Url -Url $detectedSourceUrl

        if ($normalizedSourceUrl) {
            if (-not $inventoryByNormalizedSourceUrl.ContainsKey($normalizedSourceUrl)) {
                $inventoryByNormalizedSourceUrl[$normalizedSourceUrl] = 0
            }
            $inventoryByNormalizedSourceUrl[$normalizedSourceUrl] += 1
        }

        $row = [pscustomobject]@{
            source_file_path = $item.FullName
            source_file_name = $item.Name
            source_folder = $folderName
            extension = $extension
            size_bytes = $item.Length
            last_write_time = $item.LastWriteTime.ToString('s')
            detected_source_url = $detectedSourceUrl
            normalized_source_url = $normalizedSourceUrl
            source_url_present = $sourceUrlPresent
            is_pdf = $isPdf
            is_markdown = $isMarkdown
            is_error_log = $isErrorLog
            is_done_log = $isDoneLog
            contains_raw_html = $containsRawHtml
            raw_html_tag_count = $rawHtmlTagCount
            line_count = $lineCount
            first_heading = $firstHeading
            likely_domain = $likelyDomain
            likely_category_guess = $likelyCategoryGuess
            quality_guess = $qualityGuess
            rejection_reason_guess = $rejectionReasonGuess
            duplicate_hash = $duplicateHash
        }

        $inventoryRows.Add($row)
        if ($duplicateHash) {
            $duplicateSeedRows.Add($row)
        }
    }
}

$inventoryCsvPath = Join-Path $rawInventoryDir 'source_file_inventory.csv'
$inventoryJsonPath = Join-Path $rawInventoryDir 'source_file_inventory.json'
$urlListCsvPath = Join-Path $sourceRegistryDir 'url_source_lists.csv'
$urlListJsonPath = Join-Path $sourceRegistryDir 'url_source_lists.json'
$missingSourceCsvPath = Join-Path $rawInventoryDir 'files_missing_source_url.csv'
$rawHtmlCsvPath = Join-Path $rawInventoryDir 'raw_html_noise_report.csv'
$duplicateCsvPath = Join-Path $rawInventoryDir 'duplicate_candidates.csv'
$sourceAuditPath = Join-Path $KnowledgeRoot 'SOURCE_AUDIT.md'

$inventoryRows |
    Sort-Object source_folder, source_file_name |
    Export-Csv -LiteralPath $inventoryCsvPath -NoTypeInformation -Encoding UTF8
$inventoryRows |
    Sort-Object source_folder, source_file_name |
    ConvertTo-Json -Depth 6 |
    Set-Content -LiteralPath $inventoryJsonPath -Encoding UTF8

$urlSourceRowsWithMatches = foreach ($row in $urlSourceRows) {
    [pscustomobject]@{
        list_file = $row.list_file
        line_number = $row.line_number
        raw_line = $row.raw_line
        source_tag = $row.source_tag
        extracted_url = $row.extracted_url
        normalized_url = $row.normalized_url
        url_domain = $row.url_domain
        matched_source_file_count = if ($row.normalized_url -and $inventoryByNormalizedSourceUrl.ContainsKey($row.normalized_url)) { $inventoryByNormalizedSourceUrl[$row.normalized_url] } else { 0 }
    }
}

$urlSourceRowsWithMatches |
    Sort-Object list_file, line_number |
    Export-Csv -LiteralPath $urlListCsvPath -NoTypeInformation -Encoding UTF8
$urlSourceRowsWithMatches |
    Sort-Object list_file, line_number |
    ConvertTo-Json -Depth 6 |
    Set-Content -LiteralPath $urlListJsonPath -Encoding UTF8

$missingSourceRows = $inventoryRows | Where-Object { $_.is_markdown -and -not $_.source_url_present }
$missingSourceRows |
    Sort-Object source_folder, source_file_name |
    Export-Csv -LiteralPath $missingSourceCsvPath -NoTypeInformation -Encoding UTF8

$rawHtmlRows = $inventoryRows | Where-Object { $_.contains_raw_html }
$rawHtmlRows |
    Sort-Object source_folder, @{ Expression = 'raw_html_tag_count'; Descending = $true }, source_file_name |
    Export-Csv -LiteralPath $rawHtmlCsvPath -NoTypeInformation -Encoding UTF8

$duplicateGroups = $duplicateSeedRows |
    Group-Object duplicate_hash |
    Where-Object { $_.Count -gt 1 }

$duplicateRows = New-Object System.Collections.Generic.List[object]
$groupIndex = 0
foreach ($group in ($duplicateGroups | Sort-Object @{ Expression = 'Count'; Descending = $true }, Name)) {
    $groupIndex += 1
    $groupId = 'dup_{0:d4}' -f $groupIndex
    foreach ($entry in $group.Group) {
        $duplicateRows.Add([pscustomobject]@{
                duplicate_group_id = $groupId
                duplicate_hash = $group.Name
                duplicate_count = $group.Count
                source_file_path = $entry.source_file_path
                source_file_name = $entry.source_file_name
                source_folder = $entry.source_folder
                detected_source_url = $entry.detected_source_url
                likely_domain = $entry.likely_domain
                likely_category_guess = $entry.likely_category_guess
                quality_guess = $entry.quality_guess
                rejection_reason_guess = $entry.rejection_reason_guess
            })
    }
}

$duplicateRows |
    Sort-Object @{ Expression = 'duplicate_count'; Descending = $true }, duplicate_group_id, source_file_name |
    Export-Csv -LiteralPath $duplicateCsvPath -NoTypeInformation -Encoding UTF8

$markdownCounts = $inventoryRows | Where-Object { $_.is_markdown } | Group-Object source_folder | Sort-Object Name
$pdfCounts = $inventoryRows | Where-Object { $_.is_pdf } | Group-Object source_folder | Sort-Object Name
$obviousRejectedRows = $inventoryRows | Where-Object {
    -not [string]::IsNullOrWhiteSpace($_.rejection_reason_guess) -and
    $_.rejection_reason_guess -notin @('error_log', 'done_log')
}
$missingSourceCount = ($missingSourceRows | Measure-Object).Count
$rawHtmlCount = ($rawHtmlRows | Measure-Object).Count
$duplicateGroupCount = ($duplicateGroups | Measure-Object).Count
$duplicateFileCount = $duplicateRows.Count
$obviousRejectedCount = ($obviousRejectedRows | Measure-Object).Count

$summaryLines = New-Object System.Collections.Generic.List[string]
$summaryLines.Add('# SOURCE_AUDIT')
$summaryLines.Add('')
$summaryLines.Add(('Generated at: `{0}`' -f (Get-Date).ToString('yyyy-MM-dd HH:mm:ss')))
$summaryLines.Add('')
$summaryLines.Add('## Markdown Count By Source Folder')
foreach ($group in $markdownCounts) {
    $summaryLines.Add(('- `{0}`: `{1}`' -f $group.Name, $group.Count))
}
$summaryLines.Add('')
$summaryLines.Add('## PDF Count By Source Folder')
foreach ($group in $pdfCounts) {
    $summaryLines.Add(('- `{0}`: `{1}`' -f $group.Name, $group.Count))
}
$summaryLines.Add('')
$summaryLines.Add('## Inventory Summary')
$summaryLines.Add(('- files missing `source_url`: `{0}`' -f $missingSourceCount))
$summaryLines.Add(('- raw HTML noisy files: `{0}`' -f $rawHtmlCount))
$summaryLines.Add(('- duplicate candidate groups: `{0}`' -f $duplicateGroupCount))
$summaryLines.Add(('- duplicate candidate files: `{0}`' -f $duplicateFileCount))
$summaryLines.Add(('- obvious rejected files: `{0}`' -f $obviousRejectedCount))
$summaryLines.Add('')
$summaryLines.Add('## URL Source List Counts')
foreach ($listFile in ($urlSourceRowsWithMatches | Group-Object list_file | Sort-Object Name)) {
    $summaryLines.Add(('- `{0}` rows: `{1}`' -f $listFile.Name, $listFile.Count))
}
$summaryLines.Add('')
$summaryLines.Add('## Top Rejection Reasons')
foreach ($reasonGroup in ($obviousRejectedRows | Group-Object rejection_reason_guess | Sort-Object @{ Expression = 'Count'; Descending = $true }, Name | Select-Object -First 10)) {
    $summaryLines.Add(('- `{0}`: `{1}`' -f $reasonGroup.Name, $reasonGroup.Count))
}
$summaryLines.Add('')
$summaryLines.Add('## Generated Files')
$summaryLines.Add('- `_raw_inventory/source_file_inventory.csv`')
$summaryLines.Add('- `_raw_inventory/source_file_inventory.json`')
$summaryLines.Add('- `_raw_inventory/files_missing_source_url.csv`')
$summaryLines.Add('- `_raw_inventory/raw_html_noise_report.csv`')
$summaryLines.Add('- `_raw_inventory/duplicate_candidates.csv`')
$summaryLines.Add('- `_source_registry/url_source_lists.csv`')
$summaryLines.Add('- `_source_registry/url_source_lists.json`')

$summaryLines | Set-Content -LiteralPath $sourceAuditPath -Encoding UTF8

$scriptSummary = [pscustomobject]@{
    knowledge_root = $KnowledgeRoot
    markdown_counts_by_folder = @($markdownCounts | ForEach-Object { [pscustomobject]@{ source_folder = $_.Name; count = $_.Count } })
    pdf_counts_by_folder = @($pdfCounts | ForEach-Object { [pscustomobject]@{ source_folder = $_.Name; count = $_.Count } })
    missing_source_url_count = $missingSourceCount
    raw_html_noisy_file_count = $rawHtmlCount
    duplicate_candidate_group_count = $duplicateGroupCount
    duplicate_candidate_file_count = $duplicateFileCount
    obvious_rejected_file_count = $obviousRejectedCount
    url_source_list_counts = @($urlSourceRowsWithMatches | Group-Object list_file | ForEach-Object { [pscustomobject]@{ list_file = $_.Name; count = $_.Count } })
    generated_files = @(
        $inventoryCsvPath,
        $inventoryJsonPath,
        $urlListCsvPath,
        $urlListJsonPath,
        $missingSourceCsvPath,
        $rawHtmlCsvPath,
        $duplicateCsvPath,
        $sourceAuditPath
    )
}

$scriptSummary | ConvertTo-Json -Depth 6
