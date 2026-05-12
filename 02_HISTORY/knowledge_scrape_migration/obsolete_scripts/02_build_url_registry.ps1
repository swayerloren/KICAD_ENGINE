param(
    [string]$KnowledgeRoot = (Split-Path -Parent $PSScriptRoot),
    [string]$InventoryCsv = '',
    [string]$UrlSourceCsv = '',
    [string[]]$DoneLogPaths = @(
        'C:\KICAD_SCRAPE\markdown_10k_clean\_done_urls.txt',
        'C:\KICAD_SCRAPE\markdown_url2_clean\_done_urls.txt'
    ),
    [string[]]$ErrorLogPaths = @(
        'C:\KICAD_SCRAPE\markdown_10k_clean\_errors.txt',
        'C:\KICAD_SCRAPE\markdown_url2_clean\_errors.txt'
    )
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($InventoryCsv)) {
    $InventoryCsv = Join-Path $KnowledgeRoot '_raw_inventory\source_file_inventory.csv'
}
if ([string]::IsNullOrWhiteSpace($UrlSourceCsv)) {
    $UrlSourceCsv = Join-Path $KnowledgeRoot '_source_registry\url_source_lists.csv'
}

function Ensure-Directory {
    param([Parameter(Mandatory = $true)][string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) {
        New-Item -ItemType Directory -Force -Path $Path | Out-Null
    }
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
    if ([int]::TryParse($text, [ref]$parsed)) {
        return $parsed
    }
    return $null
}

function ConvertTo-NullableLong {
    param([AllowNull()]$Value)
    if ($null -eq $Value) { return $null }
    $text = $Value.ToString().Trim()
    if ([string]::IsNullOrWhiteSpace($text)) { return $null }
    $parsed = [int64]0
    if ([int64]::TryParse($text, [ref]$parsed)) {
        return $parsed
    }
    return $null
}

function ConvertTo-NullableDateTime {
    param([AllowNull()]$Value)
    if ($null -eq $Value) { return $null }
    $text = $Value.ToString().Trim()
    if ([string]::IsNullOrWhiteSpace($text)) { return $null }
    $parsed = [datetime]::MinValue
    if ([datetime]::TryParse($text, [ref]$parsed)) {
        return $parsed
    }
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

function Get-FirstUrlFromText {
    param([AllowNull()][string]$Text)

    if ([string]::IsNullOrWhiteSpace($Text)) {
        return $null
    }

    $match = [regex]::Match($Text, 'https?://\S+')
    if ($match.Success) {
        return $match.Value.Trim()
    }

    return $null
}

function Get-UrlDomain {
    param(
        [AllowNull()][string]$Url,
        [AllowNull()][string]$FallbackDomain
    )

    if (-not [string]::IsNullOrWhiteSpace($Url)) {
        $uri = $null
        if ([System.Uri]::TryCreate($Url, [System.UriKind]::Absolute, [ref]$uri) -and -not [string]::IsNullOrWhiteSpace($uri.Host)) {
            return $uri.Host.ToLowerInvariant()
        }
    }

    if (-not [string]::IsNullOrWhiteSpace($FallbackDomain)) {
        return $FallbackDomain.ToLowerInvariant()
    }

    return $null
}

function Get-SourceFileType {
    param([Parameter(Mandatory = $true)]$Row)

    $name = if ($null -eq $Row.source_file_name) { '' } else { $Row.source_file_name.ToString() }
    if (ConvertTo-Bool $Row.is_markdown) {
        return 'markdown'
    }
    if (ConvertTo-Bool $Row.is_pdf) {
        if ($name.ToLowerInvariant().EndsWith('.pdf.pdf')) {
            return 'pdf_pdf'
        }
        return 'pdf'
    }
    if ((ConvertTo-Bool $Row.is_error_log) -or (ConvertTo-Bool $Row.is_done_log)) {
        return 'log'
    }
    return 'unknown'
}

function Get-DetectedCategory {
    param(
        [AllowNull()][string]$Url,
        [AllowNull()][string]$FallbackCategory,
        [AllowNull()][string]$SourceFileType
    )

    if (-not [string]::IsNullOrWhiteSpace($FallbackCategory)) {
        return $FallbackCategory
    }

    $signal = ''
    if (-not [string]::IsNullOrWhiteSpace($Url)) {
        $signal = $Url.ToLowerInvariant()
    }

    if ($SourceFileType -in @('pdf', 'pdf_pdf')) { return '14_datasheets_pdf_markdown' }
    if ($signal -match 'forum\.kicad\.info|eevblog\.com|stackexchange\.com|reddit\.com|esp32\.com') { return '12_forums_peer_review' }
    if ($signal -match 'youtube\.com|youtu\.be') { return '15_video_reference_index' }
    if ($signal -match 'snapeda|ultralibrarian|componentsearchengine|mouser|digikey|lcsc') { return '13_vendor_parts_cad_models' }
    if ($signal -match 'kicad-python|doxygen-python|pcbnew|apis-and-binding') { return '02_kicad_python_api' }
    if ($signal -match 'file-formats|sexpr') { return '03_kicad_file_formats' }
    if ($signal -match 'docs\.kicad\.org|dev-docs\.kicad\.org|kicad-cli|eeschema|pcbnew|gitlab\.com/kicad') { return '01_kicad_core' }
    if ($signal -match 'footprint|symbol|3d|library|libraries|klc\.kicad\.org') { return '04_kicad_libraries_symbols_footprints' }
    if ($signal -match 'espressif|esp32|esp-idf|esp-iot|esptool') { return '05_esp32_espressif' }
    if ($signal -match 'stm32|microchip|avr|sam|nordic|arduino|raspberrypi|rp2040|rp2350|wch|silabs|sony|nxp|infineon|renesas|onsemi|rohm') { return '06_microcontrollers' }
    if ($signal -match 'usb|type-c|high-speed|superspeed|esd') { return '07_usb_c_high_speed_esd' }
    if ($signal -match 'buck|regulator|converter|power-supply|switching-regulator|vrm') { return '08_power_buck_regulators' }
    if ($signal -match 'ground|emi|emc|signal integrity|differential pair|stackup|pcb layout|layout guidelines|trace width') { return '09_pcb_layout_grounding_emi_si' }
    if ($signal -match 'jlcpcb|oshpark|4pcb|pcbway|eurocircuits|protoexpress|sunstone|assembly|dfm|fabrication') { return '10_dfm_fabrication_assembly' }
    if ($signal -match 'calculator|microstrip|ipc') { return '11_calculators_ipc_reference' }

    return '90_unsorted_review'
}

function Get-SourceOfTruthLevel {
    param(
        [AllowNull()][string]$OriginalUrl,
        [AllowNull()][string]$SourceDomain,
        [AllowNull()][string]$DetectedCategory,
        [AllowNull()][string]$SourceFileType
    )

    $domain = if ($null -eq $SourceDomain) { '' } else { $SourceDomain.ToLowerInvariant() }
    $url = if ($null -eq $OriginalUrl) { '' } else { $OriginalUrl.ToLowerInvariant() }

    if ($domain -match 'youtube\.com|youtu\.be') {
        return '7_video_index'
    }

    if ($url -match 'search|/tag/|/tags/|questions/tagged|/category/|/categories/' -or $DetectedCategory -eq '91_rejected_low_value') {
        return '8_low_value_index_or_search'
    }

    if ($domain -match '(^|\.)(espressif\.com|ti\.com|microchip\.com|silabs\.com|raspberrypi\.com|st\.com|nxp\.com|nexperia\.com|infineon\.com|renesas\.com|onsemi\.com|rohm\.com|we-online\.com)$') {
        if ($url -match 'appnote|application-note|hardware-design-guidelines|design-guide|user-guide|migration|implementation|reference-design|errata') {
            return '2_official_manufacturer_app_note'
        }
        if ($SourceFileType -in @('pdf', 'pdf_pdf') -or $url -match '\.pdf($|\?)|datasheet|reference-manual|technical-reference-manual') {
            return '1_official_manufacturer_datasheet'
        }
    }

    if ($domain -match '(^|\.)(docs\.kicad\.org|dev-docs\.kicad\.org|kicad\.org)$' -or $url -match 'gitlab\.com/kicad') {
        return '3_official_kicad_docs'
    }

    if ($domain -match '(^|\.)(jlcpcb\.com|pcbway\.com|oshpark\.com|eurocircuits\.com|4pcb\.com|sunstone\.com|protoexpress\.com)$') {
        return '4_fabricator_docs'
    }

    if ($domain -match '(^|\.)(eevblog\.com|electronics\.stackexchange\.com|forum\.kicad\.info|esp32\.com)$') {
        return '5_engineering_forum_peer_review'
    }

    if ($domain -match '(^|\.)(hackaday\.com|sparkfun\.com|adafruit\.com)$' -or $url -match 'resources\.altium|resources\.cadence|autodesk|monolithicpower') {
        return '6_blog_tutorial'
    }

    return '8_low_value_index_or_search'
}

function Get-TrustLabel {
    param([Parameter(Mandatory = $true)][string]$SourceOfTruthLevel)

    switch ($SourceOfTruthLevel) {
        '1_official_manufacturer_datasheet' { return 'primary_official' }
        '2_official_manufacturer_app_note' { return 'official_reference' }
        '3_official_kicad_docs' { return 'official_docs' }
        '4_fabricator_docs' { return 'official_fabricator' }
        '5_engineering_forum_peer_review' { return 'peer_review' }
        '6_blog_tutorial' { return 'tutorial' }
        '7_video_index' { return 'video_index' }
        default { return 'low_value' }
    }
}

function Get-QualityRank {
    param([AllowNull()][string]$Quality)
    switch ($Quality) {
        'high' { return 4 }
        'medium' { return 3 }
        'low' { return 2 }
        'junk' { return 1 }
        default { return 0 }
    }
}

function Get-SourceTypeRank {
    param([AllowNull()][string]$SourceFileType)
    switch ($SourceFileType) {
        'markdown' { return 4 }
        'pdf' { return 3 }
        'pdf_pdf' { return 2 }
        'log' { return 1 }
        default { return 0 }
    }
}

function Get-InventorySelectionScore {
    param([Parameter(Mandatory = $true)]$Row)

    $quality = if ($null -eq $Row.quality_guess) { $null } else { $Row.quality_guess.ToString() }
    $sourceType = if ($null -eq $Row.source_file_type) { $null } else { $Row.source_file_type.ToString() }
    $sizeBytes = ConvertTo-NullableLong $Row.size_bytes
    if ($null -eq $sizeBytes) {
        $sizeBytes = [int64]0
    }
    $score = (Get-QualityRank -Quality $quality) * 100000
    $score += (Get-SourceTypeRank -SourceFileType $sourceType) * 10000

    if (-not (ConvertTo-Bool $Row.contains_raw_html)) {
        $score += 7000
    }
    if ([string]::IsNullOrWhiteSpace($Row.rejection_reason_guess)) {
        $score += 5000
    }
    if (-not [string]::IsNullOrWhiteSpace($Row.detected_source_url)) {
        $score += 1000
    }

    $score += [Math]::Min($sizeBytes, [int64]500000)
    return $score
}

function Get-BestInventoryRow {
    param([Parameter(Mandatory = $true)][System.Collections.IEnumerable]$Rows)

    $rowArray = @($Rows)
    $bestRow = $null
    $bestScore = [int64]::MinValue
    $bestDate = [datetime]::MinValue

    foreach ($row in $rowArray) {
        $score = Get-InventorySelectionScore -Row $row
        $rowDate = ConvertTo-NullableDateTime $row.last_write_time
        if ($null -eq $rowDate) {
            $rowDate = [datetime]::MinValue
        }

        if ($null -eq $bestRow -or $score -gt $bestScore -or ($score -eq $bestScore -and $rowDate -gt $bestDate)) {
            $bestRow = $row
            $bestScore = $score
            $bestDate = $rowDate
        }
    }

    return $bestRow
}

function Get-LocalPdfFileNameCandidatesFromUrl {
    param([AllowNull()][string]$Url)

    $candidates = New-Object System.Collections.Generic.List[string]
    if ([string]::IsNullOrWhiteSpace($Url)) {
        return $candidates
    }

    $uri = $null
    if (-not [System.Uri]::TryCreate($Url.Trim(), [System.UriKind]::Absolute, [ref]$uri)) {
        return $candidates
    }

    $path = [System.Uri]::UnescapeDataString($uri.AbsolutePath)
    if ([string]::IsNullOrWhiteSpace($path)) {
        return $candidates
    }
    $path = $path.Trim('/')
    if (-not ($path -match '(?i)\.pdf$')) {
        return $candidates
    }

    $hosts = New-Object System.Collections.Generic.List[string]
    $uriHost = $uri.Host.ToLowerInvariant()
    $hosts.Add($uriHost)
    if ($uriHost.StartsWith('www.')) {
        $hosts.Add($uriHost.Substring(4))
    }

    foreach ($hostCandidate in ($hosts | Select-Object -Unique)) {
        $stem = '{0}-{1}' -f $hostCandidate, ($path -replace '/', '-')
        $candidates.Add(('{0}.pdf' -f $stem))
    }

    return ($candidates | Select-Object -Unique)
}

function Join-Distinct {
    param([AllowNull()][System.Collections.IEnumerable]$Values)

    if ($null -eq $Values) {
        return $null
    }

    $items = @()
    foreach ($value in $Values) {
        if ($null -eq $value) { continue }
        $text = $value.ToString().Trim()
        if ([string]::IsNullOrWhiteSpace($text)) { continue }
        $items += $text
    }

    if ($items.Count -eq 0) {
        return $null
    }

    return (($items | Select-Object -Unique) -join '; ')
}

function Get-ErrorClassification {
    param(
        [AllowNull()][string]$HttpError,
        [AllowNull()][string]$ErrorMessage
    )

    $message = if ($null -eq $ErrorMessage) { '' } else { $ErrorMessage.ToLowerInvariant() }
    $http = if ($null -eq $HttpError) { '' } else { $HttpError.ToString() }

    if ($http -eq '403' -or $message -match 'forbidden') { return 'http_403' }
    if ($http -eq '404' -or $message -match 'not found') { return 'http_404' }
    if ($message -match 'timed out|timeout') { return 'timeout' }
    if ($message -match 'connection was closed|connection closed|underlying connection was closed') { return 'connection_closed' }
    if ($message -match 'could not be resolved|name could not be resolved|dns') { return 'dns_failure' }
    return 'generic_failure'
}

function Get-RescrapeMethod {
    param(
        [AllowNull()][string]$Reason,
        [AllowNull()][string]$HttpError,
        [AllowNull()][string]$SourceOfTruthLevel
    )

    $reasonText = if ($null -eq $Reason) { '' } else { $Reason.ToLowerInvariant() }
    $http = if ($null -eq $HttpError) { '' } else { $HttpError.ToString() }

    if ($reasonText -match 'search|tag|index|low_value|invalid_source_path') {
        return 'skip_low_value'
    }
    if ($http -eq '404' -or $reasonText -match 'http_404|replace_dead_url|dns_failure|invalid_source_path') {
        return 'replace_dead_url'
    }
    if ($http -eq '403' -or $reasonText -match 'captcha|forbidden|raw_html_noise|connection_closed') {
        return 'browser_playwright'
    }
    if ($reasonText -match 'low_quality|manual|html_saved_as_pdf') {
        return 'manual_review'
    }
    return 'powershell_retry'
}

function Get-RescrapePriority {
    param(
        [AllowNull()][string]$SourceOfTruthLevel,
        [AllowNull()][string]$ScrapedStatus
    )

    if ($SourceOfTruthLevel -in @('1_official_manufacturer_datasheet', '2_official_manufacturer_app_note', '3_official_kicad_docs')) {
        return 'high'
    }
    if ($SourceOfTruthLevel -in @('4_fabricator_docs', '5_engineering_forum_peer_review', '6_blog_tutorial')) {
        if ($ScrapedStatus -eq 'failed') {
            return 'medium'
        }
        return 'medium'
    }
    return 'low'
}

function Parse-DoneLog {
    param([Parameter(Mandatory = $true)][string]$Path)

    $results = New-Object System.Collections.Generic.List[object]
    if (-not (Test-Path -LiteralPath $Path)) {
        return $results
    }

    $logInfo = Get-Item -LiteralPath $Path
    $lineNumber = 0
    foreach ($line in [System.IO.File]::ReadLines($Path)) {
        $lineNumber += 1
        $trimmed = $line.Trim()
        if ([string]::IsNullOrWhiteSpace($trimmed)) {
            continue
        }

        $normalized = Normalize-Url -Url $trimmed
        $results.Add([pscustomobject]@{
                original_url = $trimmed
                normalized_url = $normalized
                log_file = $Path
                source_folder = Split-Path -Leaf (Split-Path -Parent $Path)
                line_number = $lineNumber
                last_scraped_at = $logInfo.LastWriteTime.ToString('s')
            })
    }

    return $results
}

function Parse-ErrorLog {
    param([Parameter(Mandatory = $true)][string]$Path)

    $results = New-Object System.Collections.Generic.List[object]
    if (-not (Test-Path -LiteralPath $Path)) {
        return $results
    }

    $logInfo = Get-Item -LiteralPath $Path
    $pendingUrl = $null
    $pendingLine = $null
    $lineNumber = 0

    foreach ($line in [System.IO.File]::ReadLines($Path)) {
        $lineNumber += 1
        $trimmed = $line.Trim()
        if ($trimmed -match '^FAILED:\s*(.+?)\s*$') {
            $pendingUrl = $Matches[1].Trim()
            $pendingLine = $lineNumber
            continue
        }
        if ($trimmed -match '^ERROR:\s*(.+?)\s*$' -and -not [string]::IsNullOrWhiteSpace($pendingUrl)) {
            $message = $Matches[1].Trim()
            $httpError = $null
            if ($message -match '\((\d{3})\)') {
                $httpError = $Matches[1]
            }

            $results.Add([pscustomobject]@{
                    original_url = $pendingUrl
                    normalized_url = (Normalize-Url -Url $pendingUrl)
                    log_file = $Path
                    source_folder = Split-Path -Leaf (Split-Path -Parent $Path)
                    line_number = $pendingLine
                    http_error_if_known = $httpError
                    error_message_if_known = $message
                    last_scraped_at = $logInfo.LastWriteTime.ToString('s')
                })

            $pendingUrl = $null
            $pendingLine = $null
        }
    }

    if (-not [string]::IsNullOrWhiteSpace($pendingUrl)) {
        $results.Add([pscustomobject]@{
                original_url = $pendingUrl
                normalized_url = (Normalize-Url -Url $pendingUrl)
                log_file = $Path
                source_folder = Split-Path -Leaf (Split-Path -Parent $Path)
                line_number = $pendingLine
                http_error_if_known = $null
                error_message_if_known = $null
                last_scraped_at = $logInfo.LastWriteTime.ToString('s')
            })
    }

    return $results
}

function New-UrlRecord {
    param([Parameter(Mandatory = $true)][string]$NormalizedUrl)

    return @{
        normalized_url = $NormalizedUrl
        original_urls = (New-Object System.Collections.Generic.List[string])
        source_list_files = (New-Object System.Collections.Generic.List[string])
        source_list_rows = (New-Object System.Collections.Generic.List[string])
        inventory_rows = (New-Object System.Collections.Generic.List[object])
        done_entries = (New-Object System.Collections.Generic.List[object])
        error_entries = (New-Object System.Collections.Generic.List[object])
        notes = (New-Object System.Collections.Generic.List[string])
    }
}

Ensure-Directory -Path $KnowledgeRoot
$sourceRegistryDir = Join-Path $KnowledgeRoot '_source_registry'
Ensure-Directory -Path $sourceRegistryDir

if (-not (Test-Path -LiteralPath $InventoryCsv)) {
    throw ('Inventory CSV not found: {0}' -f $InventoryCsv)
}
if (-not (Test-Path -LiteralPath $UrlSourceCsv)) {
    throw ('URL source list CSV not found: {0}' -f $UrlSourceCsv)
}

$inventoryRowsRaw = @(Import-Csv -LiteralPath $InventoryCsv)
$urlSourceRowsRaw = @(Import-Csv -LiteralPath $UrlSourceCsv)
$urlSourceRows = New-Object System.Collections.Generic.List[object]

foreach ($rawSourceRow in $urlSourceRowsRaw) {
    $candidateUrl = $null
    if (-not [string]::IsNullOrWhiteSpace($rawSourceRow.extracted_url) -and $rawSourceRow.extracted_url -match '^https?://') {
        $candidateUrl = $rawSourceRow.extracted_url.Trim()
    }
    else {
        $candidateUrl = Get-FirstUrlFromText -Text $rawSourceRow.raw_line
    }

    if ([string]::IsNullOrWhiteSpace($candidateUrl)) {
        continue
    }

    $normalizedUrl = Normalize-Url -Url $candidateUrl
    if ([string]::IsNullOrWhiteSpace($normalizedUrl)) {
        continue
    }

    $urlSourceRows.Add([pscustomobject]@{
            list_file = $rawSourceRow.list_file
            line_number = $rawSourceRow.line_number
            raw_line = $rawSourceRow.raw_line
            source_tag = $rawSourceRow.source_tag
            extracted_url = $candidateUrl
            normalized_url = $normalizedUrl
            url_domain = (Get-UrlDomain -Url $normalizedUrl -FallbackDomain $null)
        })
}

$doneEntries = New-Object System.Collections.Generic.List[object]
foreach ($donePath in $DoneLogPaths) {
    foreach ($entry in (Parse-DoneLog -Path $donePath)) {
        $doneEntries.Add($entry)
    }
}

$errorEntries = New-Object System.Collections.Generic.List[object]
foreach ($errorPath in $ErrorLogPaths) {
    foreach ($entry in (Parse-ErrorLog -Path $errorPath)) {
        $errorEntries.Add($entry)
    }
}

$candidateUrlsForPdfMatching = New-Object System.Collections.Generic.List[string]
foreach ($urlRow in $urlSourceRows) {
    if (-not [string]::IsNullOrWhiteSpace($urlRow.extracted_url)) {
        $candidateUrlsForPdfMatching.Add($urlRow.extracted_url)
    }
}
foreach ($entry in $doneEntries) {
    if (-not [string]::IsNullOrWhiteSpace($entry.original_url)) {
        $candidateUrlsForPdfMatching.Add($entry.original_url)
    }
}
foreach ($entry in $errorEntries) {
    if (-not [string]::IsNullOrWhiteSpace($entry.original_url)) {
        $candidateUrlsForPdfMatching.Add($entry.original_url)
    }
}
foreach ($row in $inventoryRowsRaw) {
    if (-not [string]::IsNullOrWhiteSpace($row.detected_source_url)) {
        $candidateUrlsForPdfMatching.Add($row.detected_source_url)
    }
}

$pdfUrlCandidateMap = @{}
foreach ($candidateUrl in ($candidateUrlsForPdfMatching | Select-Object -Unique)) {
    foreach ($fileNameCandidate in (Get-LocalPdfFileNameCandidatesFromUrl -Url $candidateUrl)) {
        if (-not $pdfUrlCandidateMap.ContainsKey($fileNameCandidate)) {
            $pdfUrlCandidateMap[$fileNameCandidate] = New-Object System.Collections.Generic.List[string]
        }
        $pdfUrlCandidateMap[$fileNameCandidate].Add($candidateUrl)
    }
}

$duplicateGroups = @{}
$groupIndex = 0
$inventoryDuplicateGroups =
    $inventoryRowsRaw |
    Where-Object {
        -not [string]::IsNullOrWhiteSpace($_.duplicate_hash) -and
        -not (ConvertTo-Bool $_.is_error_log) -and
        -not (ConvertTo-Bool $_.is_done_log)
    } |
    Group-Object duplicate_hash |
    Where-Object { $_.Count -gt 1 } |
    Sort-Object -Property @{ Expression = { $_.Count }; Descending = $true }, Name

foreach ($group in $inventoryDuplicateGroups) {
    $groupIndex += 1
    $duplicateGroups[$group.Name] = ('dup_{0:d4}' -f $groupIndex)
}

$inventoryRows = New-Object System.Collections.Generic.List[object]
foreach ($rawRow in $inventoryRowsRaw) {
    $normalizedDetectedSourceUrl = Normalize-Url -Url $rawRow.detected_source_url
    $row = [pscustomobject]@{
        source_file_path = $rawRow.source_file_path
        source_file_name = $rawRow.source_file_name
        source_folder = $rawRow.source_folder
        extension = $rawRow.extension
        size_bytes = (ConvertTo-NullableLong $rawRow.size_bytes)
        last_write_time = $rawRow.last_write_time
        detected_source_url = $rawRow.detected_source_url
        normalized_source_url = $normalizedDetectedSourceUrl
        source_url_present = (ConvertTo-Bool $rawRow.source_url_present)
        is_pdf = (ConvertTo-Bool $rawRow.is_pdf)
        is_markdown = (ConvertTo-Bool $rawRow.is_markdown)
        is_error_log = (ConvertTo-Bool $rawRow.is_error_log)
        is_done_log = (ConvertTo-Bool $rawRow.is_done_log)
        contains_raw_html = (ConvertTo-Bool $rawRow.contains_raw_html)
        raw_html_tag_count = (ConvertTo-NullableInt $rawRow.raw_html_tag_count)
        line_count = (ConvertTo-NullableInt $rawRow.line_count)
        first_heading = $rawRow.first_heading
        likely_domain = $rawRow.likely_domain
        likely_category_guess = $rawRow.likely_category_guess
        quality_guess = $rawRow.quality_guess
        rejection_reason_guess = $rawRow.rejection_reason_guess
        duplicate_hash = $rawRow.duplicate_hash
        source_file_type = $null
        duplicate_group_id = $null
        resolved_original_url = $null
        resolved_normalized_url = $null
        url_resolution_note = $null
    }

    $row.source_file_type = Get-SourceFileType -Row $row
    if (-not [string]::IsNullOrWhiteSpace($row.duplicate_hash) -and $duplicateGroups.ContainsKey($row.duplicate_hash)) {
        $row.duplicate_group_id = $duplicateGroups[$row.duplicate_hash]
    }

    if (-not [string]::IsNullOrWhiteSpace($row.normalized_source_url)) {
        $row.resolved_original_url = $row.detected_source_url
        $row.resolved_normalized_url = $row.normalized_source_url
    }
    elseif ($row.source_file_type -eq 'pdf_pdf' -or $row.source_file_type -eq 'pdf') {
        $fileName = if ($null -eq $row.source_file_name) { '' } else { $row.source_file_name.ToString() }
        if ($pdfUrlCandidateMap.ContainsKey($fileName)) {
            $matchedUrl = ($pdfUrlCandidateMap[$fileName] | Select-Object -First 1)
            $row.resolved_original_url = $matchedUrl
            $row.resolved_normalized_url = Normalize-Url -Url $matchedUrl
            if ($pdfUrlCandidateMap[$fileName].Count -gt 1) {
                $row.url_resolution_note = 'pdf_url_inferred_from_filename_ambiguous'
            }
            else {
                $row.url_resolution_note = 'pdf_url_inferred_from_filename'
            }
        }
    }

    $inventoryRows.Add($row)
}

$urlRegistry = @{}
foreach ($sourceRow in $urlSourceRows) {
    $normalizedUrl = $sourceRow.normalized_url
    if ([string]::IsNullOrWhiteSpace($normalizedUrl)) {
        continue
    }

    if (-not $urlRegistry.ContainsKey($normalizedUrl)) {
        $urlRegistry[$normalizedUrl] = New-UrlRecord -NormalizedUrl $normalizedUrl
    }
    $record = $urlRegistry[$normalizedUrl]
    if (-not [string]::IsNullOrWhiteSpace($sourceRow.extracted_url)) {
        $record.original_urls.Add($sourceRow.extracted_url)
    }
    if (-not [string]::IsNullOrWhiteSpace($sourceRow.list_file)) {
        $record.source_list_files.Add($sourceRow.list_file)
    }
    if (-not [string]::IsNullOrWhiteSpace($sourceRow.line_number)) {
        $record.source_list_rows.Add(('{0}:{1}' -f $sourceRow.list_file, $sourceRow.line_number))
    }
}

foreach ($row in $inventoryRows) {
    if ([string]::IsNullOrWhiteSpace($row.resolved_normalized_url)) {
        continue
    }

    if (-not $urlRegistry.ContainsKey($row.resolved_normalized_url)) {
        $urlRegistry[$row.resolved_normalized_url] = New-UrlRecord -NormalizedUrl $row.resolved_normalized_url
    }
    $record = $urlRegistry[$row.resolved_normalized_url]
    if (-not [string]::IsNullOrWhiteSpace($row.resolved_original_url)) {
        $record.original_urls.Add($row.resolved_original_url)
    }
    if (-not [string]::IsNullOrWhiteSpace($row.url_resolution_note)) {
        $record.notes.Add($row.url_resolution_note)
    }
    $record.inventory_rows.Add($row)
}

foreach ($entry in $doneEntries) {
    if ([string]::IsNullOrWhiteSpace($entry.normalized_url)) {
        continue
    }

    if (-not $urlRegistry.ContainsKey($entry.normalized_url)) {
        $urlRegistry[$entry.normalized_url] = New-UrlRecord -NormalizedUrl $entry.normalized_url
    }
    $record = $urlRegistry[$entry.normalized_url]
    $record.original_urls.Add($entry.original_url)
    $record.done_entries.Add($entry)
}

foreach ($entry in $errorEntries) {
    if ([string]::IsNullOrWhiteSpace($entry.normalized_url)) {
        continue
    }

    if (-not $urlRegistry.ContainsKey($entry.normalized_url)) {
        $urlRegistry[$entry.normalized_url] = New-UrlRecord -NormalizedUrl $entry.normalized_url
    }
    $record = $urlRegistry[$entry.normalized_url]
    $record.original_urls.Add($entry.original_url)
    $record.error_entries.Add($entry)
}

$importedAt = (Get-Date).ToString('s')
$urlIndexRows = New-Object System.Collections.Generic.List[object]
$rescrapeQueueRows = New-Object System.Collections.Generic.List[object]

foreach ($normalizedUrl in ($urlRegistry.Keys | Sort-Object)) {
    $record = $urlRegistry[$normalizedUrl]
    $bestInventoryRow = $null
    if ($record.inventory_rows.Count -gt 0) {
        $bestInventoryRow = Get-BestInventoryRow -Rows ($record.inventory_rows.ToArray())
    }

    $originalUrl = $null
    if ($record.original_urls.Count -gt 0) {
        $originalUrl = $record.original_urls[0]
    }
    elseif ($bestInventoryRow -and -not [string]::IsNullOrWhiteSpace($bestInventoryRow.resolved_original_url)) {
        $originalUrl = $bestInventoryRow.resolved_original_url
    }
    else {
        $originalUrl = $normalizedUrl
    }

    $sourceDomain = $null
    if ($bestInventoryRow) {
        $sourceDomain = Get-UrlDomain -Url $normalizedUrl -FallbackDomain $bestInventoryRow.likely_domain
    }
    else {
        $sourceDomain = Get-UrlDomain -Url $normalizedUrl -FallbackDomain $null
    }

    $detectedCategory = if ($bestInventoryRow) {
        Get-DetectedCategory -Url $originalUrl -FallbackCategory $bestInventoryRow.likely_category_guess -SourceFileType $bestInventoryRow.source_file_type
    }
    else {
        Get-DetectedCategory -Url $originalUrl -FallbackCategory $null -SourceFileType 'unknown'
    }

    $sourceFileTypeForTruth = 'unknown'
    if ($bestInventoryRow) {
        $sourceFileTypeForTruth = $bestInventoryRow.source_file_type
    }
    $sourceOfTruthLevel = Get-SourceOfTruthLevel -OriginalUrl $originalUrl -SourceDomain $sourceDomain -DetectedCategory $detectedCategory -SourceFileType $sourceFileTypeForTruth
    if ($sourceOfTruthLevel -eq '4_fabricator_docs') {
        if ($originalUrl -match 'calculator') {
            $detectedCategory = '11_calculators_ipc_reference'
        }
        else {
            $detectedCategory = '10_dfm_fabrication_assembly'
        }
    }
    elseif ($sourceOfTruthLevel -eq '7_video_index') {
        $detectedCategory = '15_video_reference_index'
    }
    elseif ($sourceOfTruthLevel -eq '1_official_manufacturer_datasheet' -and $sourceFileTypeForTruth -in @('pdf', 'pdf_pdf')) {
        $detectedCategory = '14_datasheets_pdf_markdown'
    }
    $trustLabel = Get-TrustLabel -SourceOfTruthLevel $sourceOfTruthLevel

    $httpErrorIfKnown = $null
    $errorMessageIfKnown = $null
    $lastScrapedAt = $null
    if ($record.error_entries.Count -gt 0) {
        $latestError = $record.error_entries |
            Sort-Object -Property @{ Expression = { ConvertTo-NullableDateTime $_.last_scraped_at }; Descending = $true }, @{ Expression = { $_.line_number }; Descending = $true } |
            Select-Object -First 1
        $httpErrorIfKnown = $latestError.http_error_if_known
        $errorMessageIfKnown = $latestError.error_message_if_known
        $lastScrapedAt = $latestError.last_scraped_at
    }
    if ($bestInventoryRow -and -not [string]::IsNullOrWhiteSpace($bestInventoryRow.last_write_time)) {
        $lastScrapedAt = $bestInventoryRow.last_write_time
    }
    elseif ($record.done_entries.Count -gt 0 -and -not $lastScrapedAt) {
        $latestDone = $record.done_entries |
            Sort-Object -Property @{ Expression = { ConvertTo-NullableDateTime $_.last_scraped_at }; Descending = $true }, @{ Expression = { $_.line_number }; Descending = $true } |
            Select-Object -First 1
        $lastScrapedAt = $latestDone.last_scraped_at
    }

    $contentQuality = if ($bestInventoryRow -and -not [string]::IsNullOrWhiteSpace($bestInventoryRow.quality_guess)) {
        $bestInventoryRow.quality_guess
    }
    else {
        'unknown'
    }

    $scrapedStatus = 'unknown'
    $needsFutureRescrape = 'false'
    $rescrapeReason = $null

    if ($bestInventoryRow) {
        $sizeBytes = ConvertTo-NullableLong $bestInventoryRow.size_bytes
        $rawHtmlTagCount = ConvertTo-NullableInt $bestInventoryRow.raw_html_tag_count
        $rejectionReason = if ($null -eq $bestInventoryRow.rejection_reason_guess) { '' } else { $bestInventoryRow.rejection_reason_guess.ToString() }
        $containsRawHtml = ConvertTo-Bool $bestInventoryRow.contains_raw_html
        $tooSmall = $false
        if ($bestInventoryRow.source_file_type -eq 'markdown' -and $sizeBytes -lt 1200) {
            $tooSmall = $true
        }
        elseif ($bestInventoryRow.source_file_type -in @('pdf', 'pdf_pdf') -and $sizeBytes -lt 4096) {
            $tooSmall = $true
        }

        if ($rejectionReason -in @('search_or_tag_index', 'repo_or_forum_index_page', 'forum_index_or_shell_page', 'invalid_archive_date_path')) {
            $scrapedStatus = 'rejected'
            $contentQuality = 'junk'
            $rescrapeReason = $rejectionReason
        }
        elseif ($rejectionReason -in @('404_or_missing_page', 'invalid_gitlab_tree_path')) {
            $scrapedStatus = 'rejected'
            if ($contentQuality -eq 'unknown') {
                $contentQuality = 'junk'
            }
            $rescrapeReason = if ($rejectionReason -eq '404_or_missing_page') { 'http_404' } else { 'invalid_source_path' }
        }
        elseif ($rejectionReason -eq 'captcha_page') {
            $scrapedStatus = 'needs_rescrape'
            $contentQuality = 'junk'
            $needsFutureRescrape = 'true'
            $rescrapeReason = 'captcha_page'
        }
        elseif ($bestInventoryRow.source_file_type -in @('pdf', 'pdf_pdf') -and $containsRawHtml) {
            $scrapedStatus = 'needs_rescrape'
            $contentQuality = 'low'
            $needsFutureRescrape = 'true'
            $rescrapeReason = 'html_saved_as_pdf'
        }
        elseif ($tooSmall) {
            $scrapedStatus = 'needs_rescrape'
            if ($contentQuality -eq 'unknown') {
                $contentQuality = 'low'
            }
            $needsFutureRescrape = 'true'
            $rescrapeReason = 'output_too_small'
        }
        elseif ($containsRawHtml -and $rawHtmlTagCount -ge 40) {
            $scrapedStatus = 'needs_rescrape'
            if ($contentQuality -in @('high', 'medium')) {
                $contentQuality = 'low'
            }
            elseif ($contentQuality -eq 'unknown') {
                $contentQuality = 'low'
            }
            $needsFutureRescrape = 'true'
            $rescrapeReason = 'raw_html_noise'
        }
        elseif ($contentQuality -eq 'low' -and $sourceOfTruthLevel -ne '8_low_value_index_or_search') {
            $scrapedStatus = 'needs_rescrape'
            $needsFutureRescrape = 'true'
            $rescrapeReason = 'low_quality_but_useful'
        }
        else {
            $scrapedStatus = 'success'
            $needsFutureRescrape = 'false'
        }
    }
    elseif ($record.error_entries.Count -gt 0) {
        $scrapedStatus = 'failed'
        $needsFutureRescrape = 'true'
        $rescrapeReason = Get-ErrorClassification -HttpError $httpErrorIfKnown -ErrorMessage $errorMessageIfKnown
        if ($contentQuality -eq 'unknown') {
            $contentQuality = 'unknown'
        }
    }
    elseif ($record.done_entries.Count -gt 0 -or $record.source_list_files.Count -gt 0) {
        $scrapedStatus = 'not_found_in_outputs'
        $needsFutureRescrape = 'true'
        $rescrapeReason = 'missing_output_file'
    }

    $sourceScrapedFile = if ($bestInventoryRow) { $bestInventoryRow.source_file_path } else { $null }
    $sourceFileType = if ($bestInventoryRow) { $bestInventoryRow.source_file_type } else { 'unknown' }
    $duplicateGroupId = if ($bestInventoryRow) { $bestInventoryRow.duplicate_group_id } else { $null }
    $currentKnowledgeFile = $null

    if ($bestInventoryRow) {
        $record.notes.Add('matched_source_files={0}' -f $record.inventory_rows.Count)
        if ($record.inventory_rows.Count -gt 1) {
            $record.notes.Add('multiple_scraped_files_for_same_url')
        }
        if ($record.error_entries.Count -gt 0) {
            $record.notes.Add('historical_error_present')
        }
        $record.notes.Add('not_imported_into_category_tree_yet')
    }
    elseif ($record.done_entries.Count -gt 0) {
        $record.notes.Add('done_log_present_without_output_file')
    }

    $urlIndexRows.Add([pscustomobject][ordered]@{
            id = $null
            original_url = $originalUrl
            normalized_url = $normalizedUrl
            source_domain = $sourceDomain
            source_list_file = (Join-Distinct -Values $record.source_list_files)
            source_list_row = (Join-Distinct -Values $record.source_list_rows)
            scraped_status = $scrapedStatus
            http_error_if_known = $httpErrorIfKnown
            error_message_if_known = $errorMessageIfKnown
            source_scraped_file = $sourceScrapedFile
            current_knowledge_file = $currentKnowledgeFile
            source_file_type = $sourceFileType
            detected_category = $detectedCategory
            source_of_truth_level = $sourceOfTruthLevel
            trust_label = $trustLabel
            content_quality = $contentQuality
            needs_future_rescrape = $needsFutureRescrape
            rescrape_reason = $rescrapeReason
            imported_at = $importedAt
            last_scraped_at = $lastScrapedAt
            duplicate_group_id = $duplicateGroupId
            notes = (Join-Distinct -Values $record.notes)
        })
}

$orderedUrlRows = @(
    $urlIndexRows |
    Sort-Object -Property normalized_url |
    ForEach-Object -Begin { $counter = 0 } -Process {
        $counter += 1
        $_.id = ('url_{0:d6}' -f $counter)
        $_
    }
)

foreach ($row in $orderedUrlRows) {
    $includeInQueue = $false
    if ($row.scraped_status -in @('failed', 'not_found_in_outputs', 'needs_rescrape')) {
        $includeInQueue = $true
    }
    elseif ($row.scraped_status -eq 'rejected' -and -not [string]::IsNullOrWhiteSpace($row.rescrape_reason)) {
        $includeInQueue = $true
    }

    if (-not $includeInQueue) {
        continue
    }

    $reason = if (-not [string]::IsNullOrWhiteSpace($row.rescrape_reason)) {
        $row.rescrape_reason
    }
    elseif ($row.scraped_status -eq 'failed') {
        'failed'
    }
    else {
        'manual_review'
    }

    $method = Get-RescrapeMethod -Reason $reason -HttpError $row.http_error_if_known -SourceOfTruthLevel $row.source_of_truth_level
    $priority = Get-RescrapePriority -SourceOfTruthLevel $row.source_of_truth_level -ScrapedStatus $row.scraped_status

    $rescrapeQueueRows.Add([pscustomobject][ordered]@{
            url = $row.original_url
            reason = $reason
            recommended_method = $method
            priority = $priority
            category_guess = $row.detected_category
            source_domain = $row.source_domain
        })
}

$domainSummaryRows = @(
    $orderedUrlRows |
    Group-Object source_domain |
    Sort-Object Count -Descending |
    ForEach-Object {
        $domainName = $_.Name
        $groupRows = @($_.Group)
        [pscustomobject][ordered]@{
            source_domain = if ([string]::IsNullOrWhiteSpace($domainName)) { '(unknown)' } else { $domainName }
            total_urls = $groupRows.Count
            success_count = @($groupRows | Where-Object { $_.scraped_status -eq 'success' }).Count
            failed_count = @($groupRows | Where-Object { $_.scraped_status -eq 'failed' }).Count
            not_found_in_outputs_count = @($groupRows | Where-Object { $_.scraped_status -eq 'not_found_in_outputs' }).Count
            rejected_count = @($groupRows | Where-Object { $_.scraped_status -eq 'rejected' }).Count
            needs_rescrape_count = @($groupRows | Where-Object { $_.scraped_status -eq 'needs_rescrape' }).Count
            unknown_count = @($groupRows | Where-Object { $_.scraped_status -eq 'unknown' }).Count
            high_quality_count = @($groupRows | Where-Object { $_.content_quality -eq 'high' }).Count
            medium_quality_count = @($groupRows | Where-Object { $_.content_quality -eq 'medium' }).Count
            low_quality_count = @($groupRows | Where-Object { $_.content_quality -eq 'low' }).Count
            junk_quality_count = @($groupRows | Where-Object { $_.content_quality -eq 'junk' }).Count
            unknown_quality_count = @($groupRows | Where-Object { $_.content_quality -eq 'unknown' }).Count
            queue_count = @($rescrapeQueueRows | Where-Object { $_.source_domain -eq $domainName }).Count
        }
    }
)

$errorUrlIndexRows = @(
    $orderedUrlRows |
    Where-Object {
        $_.scraped_status -eq 'failed' -or
        -not [string]::IsNullOrWhiteSpace($_.http_error_if_known) -or
        -not [string]::IsNullOrWhiteSpace($_.error_message_if_known)
    } |
    Sort-Object normalized_url
)

$successUrlIndexRows = @(
    $orderedUrlRows |
    Where-Object { $_.scraped_status -eq 'success' } |
    Sort-Object normalized_url
)

$totalUrlsKnown = $orderedUrlRows.Count
$totalSuccessful = @($orderedUrlRows | Where-Object { $_.scraped_status -eq 'success' }).Count
$totalFailed = @($orderedUrlRows | Where-Object { $_.scraped_status -eq 'failed' }).Count
$totalNotMatched = @($orderedUrlRows | Where-Object { $_.scraped_status -eq 'not_found_in_outputs' }).Count
$totalNeedsRescrape = @($orderedUrlRows | Where-Object { $_.scraped_status -eq 'needs_rescrape' }).Count
$totalRejected = @($orderedUrlRows | Where-Object { $_.scraped_status -eq 'rejected' }).Count

$qualitySummary = [ordered]@{
    high = @($orderedUrlRows | Where-Object { $_.content_quality -eq 'high' }).Count
    medium = @($orderedUrlRows | Where-Object { $_.content_quality -eq 'medium' }).Count
    low = @($orderedUrlRows | Where-Object { $_.content_quality -eq 'low' }).Count
    junk = @($orderedUrlRows | Where-Object { $_.content_quality -eq 'junk' }).Count
    unknown = @($orderedUrlRows | Where-Object { $_.content_quality -eq 'unknown' }).Count
}

$topDomains = @($domainSummaryRows | Select-Object -First 15)
$methodSummary = @(
    $rescrapeQueueRows |
    Group-Object recommended_method |
    Sort-Object Count -Descending |
    ForEach-Object {
        '- `{0}`: {1}' -f $_.Name, $_.Count
    }
)

$markdownLines = New-Object System.Collections.Generic.List[string]
$markdownLines.Add('# URL_INDEX')
$markdownLines.Add('')
$markdownLines.Add(('Generated at: `{0}`' -f $importedAt))
$markdownLines.Add('')
$markdownLines.Add('## Summary')
$markdownLines.Add('')
$markdownLines.Add(('- Total URLs known: `{0}`' -f $totalUrlsKnown))
$markdownLines.Add(('- Total successful: `{0}`' -f $totalSuccessful))
$markdownLines.Add(('- Total failed: `{0}`' -f $totalFailed))
$markdownLines.Add(('- Total not matched to files: `{0}`' -f $totalNotMatched))
$markdownLines.Add(('- Total needs rescrape: `{0}`' -f $totalNeedsRescrape))
$markdownLines.Add(('- Total rejected: `{0}`' -f $totalRejected))
$markdownLines.Add(('- Rescrape queue rows: `{0}`' -f $rescrapeQueueRows.Count))
$markdownLines.Add('')
$markdownLines.Add('## Top Domains')
$markdownLines.Add('')
$markdownLines.Add('| Domain | Total | Success | Failed | Missing | Rescrape | Rejected |')
$markdownLines.Add('| --- | ---: | ---: | ---: | ---: | ---: | ---: |')
foreach ($row in $topDomains) {
    $markdownLines.Add(('| {0} | {1} | {2} | {3} | {4} | {5} | {6} |' -f $row.source_domain, $row.total_urls, $row.success_count, $row.failed_count, $row.not_found_in_outputs_count, $row.needs_rescrape_count, $row.rejected_count))
}
$markdownLines.Add('')
$markdownLines.Add('## Scrape Quality Summary')
$markdownLines.Add('')
$markdownLines.Add(('- `high`: `{0}`' -f $qualitySummary.high))
$markdownLines.Add(('- `medium`: `{0}`' -f $qualitySummary.medium))
$markdownLines.Add(('- `low`: `{0}`' -f $qualitySummary.low))
$markdownLines.Add(('- `junk`: `{0}`' -f $qualitySummary.junk))
$markdownLines.Add(('- `unknown`: `{0}`' -f $qualitySummary.unknown))
$markdownLines.Add('')
$markdownLines.Add('## Future Scrape Instructions')
$markdownLines.Add('')
$markdownLines.Add('1. Retry `failed` and `not_found_in_outputs` URLs first, prioritizing official manufacturer PDFs and KiCad docs.')
$markdownLines.Add('2. Use `browser_playwright` for CAPTCHA, 403, and raw-HTML shell pages that look useful but were scraped poorly.')
$markdownLines.Add('3. Replace dead 404 and invalid-source-path URLs instead of reusing the same target unchanged.')
$markdownLines.Add('4. Keep `rejected` search, tag, and generic index pages out of the main knowledge base unless a human explicitly wants them retained.')
$markdownLines.Add('5. Do not populate `current_knowledge_file` until content is actually moved into category folders.')
$markdownLines.Add('')
$markdownLines.Add('### Rescrape Method Summary')
$markdownLines.Add('')
if ($methodSummary.Count -eq 0) {
    $markdownLines.Add('- No rescrape items generated.')
}
else {
    foreach ($line in $methodSummary) {
        $markdownLines.Add($line)
    }
}

$urlIndexCsvPath = Join-Path $KnowledgeRoot 'URL_INDEX.csv'
$urlIndexJsonPath = Join-Path $KnowledgeRoot 'URL_INDEX.json'
$urlIndexMarkdownPath = Join-Path $KnowledgeRoot 'URL_INDEX.md'
$rescrapeQueueCsvPath = Join-Path $KnowledgeRoot 'RESCRAPE_QUEUE.csv'
$domainSummaryCsvPath = Join-Path $sourceRegistryDir 'domain_summary.csv'
$errorUrlIndexCsvPath = Join-Path $sourceRegistryDir 'error_url_index.csv'
$successUrlIndexCsvPath = Join-Path $sourceRegistryDir 'success_url_index.csv'

$orderedUrlRows | Export-Csv -LiteralPath $urlIndexCsvPath -NoTypeInformation -Encoding UTF8
$orderedUrlRows | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $urlIndexJsonPath -Encoding UTF8
$markdownLines | Set-Content -LiteralPath $urlIndexMarkdownPath -Encoding UTF8
$rescrapeQueueRows | Export-Csv -LiteralPath $rescrapeQueueCsvPath -NoTypeInformation -Encoding UTF8
$domainSummaryRows | Export-Csv -LiteralPath $domainSummaryCsvPath -NoTypeInformation -Encoding UTF8
$errorUrlIndexRows | Export-Csv -LiteralPath $errorUrlIndexCsvPath -NoTypeInformation -Encoding UTF8
$successUrlIndexRows | Export-Csv -LiteralPath $successUrlIndexCsvPath -NoTypeInformation -Encoding UTF8

[pscustomobject][ordered]@{
    total_urls_known = $totalUrlsKnown
    total_successful = $totalSuccessful
    total_failed = $totalFailed
    total_not_found_in_outputs = $totalNotMatched
    total_needs_rescrape = $totalNeedsRescrape
    total_rejected = $totalRejected
    rescrape_queue_rows = $rescrapeQueueRows.Count
    success_url_index_rows = $successUrlIndexRows.Count
    error_url_index_rows = $errorUrlIndexRows.Count
    done_log_rows = $doneEntries.Count
    error_log_rows = $errorEntries.Count
} | Format-List
