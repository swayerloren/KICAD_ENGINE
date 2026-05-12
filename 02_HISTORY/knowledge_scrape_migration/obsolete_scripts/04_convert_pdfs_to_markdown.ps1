param(
    [string]$KnowledgeRoot = (Split-Path -Parent $PSScriptRoot),
    [string]$UrlIndexCsv = '',
    [string]$InventoryCsv = '',
    [switch]$Force
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($UrlIndexCsv)) {
    $UrlIndexCsv = Join-Path $KnowledgeRoot 'URL_INDEX.csv'
}
if ([string]::IsNullOrWhiteSpace($InventoryCsv)) {
    $InventoryCsv = Join-Path $KnowledgeRoot '_raw_inventory\source_file_inventory.csv'
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

function ConvertTo-YamlScalar {
    param([AllowNull()]$Value)

    if ($null -eq $Value) {
        return "''"
    }

    $text = $Value.ToString()
    $text = $text -replace "'", "''"
    return ("'{0}'" -f $text)
}

function Get-SafeStem {
    param(
        [Parameter(Mandatory = $true)][string]$Prefix,
        [Parameter(Mandatory = $true)][string]$SourceFileName
    )

    $safeBase = [regex]::Replace($SourceFileName, '[^A-Za-z0-9._-]+', '_')
    $safeBase = $safeBase.Trim('_')
    if ([string]::IsNullOrWhiteSpace($safeBase)) {
        $safeBase = 'source_pdf'
    }
    if ($safeBase.Length -gt 120) {
        $safeBase = $safeBase.Substring(0, 120)
    }
    return ('{0}--{1}' -f $Prefix, $safeBase)
}

function Get-PdfPathLeaf {
    param([AllowNull()][string]$Url)

    if ([string]::IsNullOrWhiteSpace($Url)) {
        return $null
    }

    $uri = $null
    if (-not [System.Uri]::TryCreate($Url, [System.UriKind]::Absolute, [ref]$uri)) {
        return $null
    }

    $leaf = [System.IO.Path]::GetFileName($uri.AbsolutePath)
    if ([string]::IsNullOrWhiteSpace($leaf)) {
        return $null
    }
    return $leaf.ToLowerInvariant()
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

function Test-RealPdfHeader {
    param([Parameter(Mandatory = $true)][string]$Path)

    $bytes = [System.IO.File]::ReadAllBytes($Path)
    if ($bytes.Length -lt 5) {
        return $false
    }
    $head = [System.Text.Encoding]::ASCII.GetString($bytes, 0, [Math]::Min(8, $bytes.Length))
    return $head.StartsWith('%PDF-')
}

function Get-FirstMeaningfulLine {
    param([AllowNull()][string]$Text)

    if ([string]::IsNullOrWhiteSpace($Text)) {
        return $null
    }

    foreach ($line in ($Text -split "\r?\n")) {
        $trimmed = $line.Trim()
        if ([string]::IsNullOrWhiteSpace($trimmed)) { continue }
        if ($trimmed -match '^\[PAGE\s+\d+\]$') { continue }
        if ($trimmed -match '^[-=_]{3,}$') { continue }
        return $trimmed
    }

    return $null
}

function Get-PdfCategoryGuess {
    param(
        [AllowNull()]$UrlRow,
        [AllowNull()]$InventoryRow,
        [AllowNull()][string]$ExtractedText,
        [AllowNull()][string]$DetectedTitle
    )

    $originalUrl = if ($null -eq $UrlRow) { '' } else { ($UrlRow.original_url | Out-String).Trim() }
    $sourceDomain = if ($null -eq $UrlRow) { '' } else { ($UrlRow.source_domain | Out-String).Trim() }
    $sourceTruth = if ($null -eq $UrlRow) { '' } else { ($UrlRow.source_of_truth_level | Out-String).Trim() }
    $fileName = if ($null -eq $InventoryRow) { '' } else { ($InventoryRow.source_file_name | Out-String).Trim() }
    $likelyDomain = if ($null -eq $InventoryRow) { '' } else { ($InventoryRow.likely_domain | Out-String).Trim() }

    $signal = ('{0} {1} {2} {3} {4} {5}' -f $originalUrl, $sourceDomain, $sourceTruth, $fileName, $likelyDomain, $DetectedTitle).ToLowerInvariant()
    if (-not [string]::IsNullOrWhiteSpace($ExtractedText)) {
        $excerpt = $ExtractedText
        if ($excerpt.Length -gt 6000) {
            $excerpt = $excerpt.Substring(0, 6000)
        }
        $signal = '{0} {1}' -f $signal, $excerpt.ToLowerInvariant()
    }

    if ($signal -match 'espressif|esp32|esp-idf|esp32-s3|esp32-c3|esp32-c6|esp32-s2') {
        return '05_esp32_espressif'
    }
    if ($signal -match 'ti\.com') {
        if ($signal -match 'lit/an/slva|buck|regulator|dc-dc|power|converter|inductor|supply|charger|pmic|voltage') {
            return '08_power_buck_regulators'
        }
        if ($signal -match 'lit/an/scaa|lit/an/slla|usb|type-c|high-speed|superspeed|esd|signal integrity|interface|differential') {
            return '07_usb_c_high_speed_esd'
        }
        return '07_usb_c_high_speed_esd'
    }
    if ($signal -match 'microchip|silabs|raspberrypi|rp2040|rp2350|stm32|st\.com|nordic|renesas|infineon|wch|gd32|bouffalo') {
        return '06_microcontrollers'
    }
    if ($signal -match 'rohm|monolithicpower|mps|richtek|onsemi') {
        if ($signal -match 'power|regulator|buck|converter|supply|inductor') {
            return '08_power_buck_regulators'
        }
    }
    if ($signal -match 'we-online|wurth') {
        if ($signal -match 'esd|usb|type-c|high-speed|connector') {
            return '07_usb_c_high_speed_esd'
        }
        return '09_pcb_layout_grounding_emi_si'
    }
    if ($signal -match 'nexperia') {
        if ($signal -match 'esd|usb|type-c|high-speed|ecmf|tpd') {
            return '07_usb_c_high_speed_esd'
        }
        if ($signal -match 'emi|emc|filter|noise|ground') {
            return '09_pcb_layout_grounding_emi_si'
        }
        return '06_microcontrollers'
    }
    if ($signal -match 'usb|type-c|high-speed|superspeed|esd|connector usb') {
        return '07_usb_c_high_speed_esd'
    }
    if ($signal -match 'buck|regulator|dc-dc|power|converter|inductor|charger|pmic') {
        return '08_power_buck_regulators'
    }
    if ($signal -match 'emi|emc|signal integrity|antenna|rf|crosstalk|grounding|ground plane') {
        return '09_pcb_layout_grounding_emi_si'
    }
    return '06_microcontrollers'
}

function Get-SourceOfTruthLevel {
    param(
        [AllowNull()][string]$OriginalUrl,
        [AllowNull()][string]$SourceDomain
    )

    $domain = if ($null -eq $SourceDomain) { '' } else { $SourceDomain.ToLowerInvariant() }
    $url = if ($null -eq $OriginalUrl) { '' } else { $OriginalUrl.ToLowerInvariant() }

    if ($domain -match '(^|\.)(espressif\.com|ti\.com|microchip\.com|silabs\.com|raspberrypi\.com|st\.com|nxp\.com|nexperia\.com|infineon\.com|renesas\.com|onsemi\.com|rohm\.com|we-online\.com)$') {
        if ($url -match 'lit/an/|/appnotes/|appnote|application-note|hardware-design-guidelines|hardware_design_guidelines|design-guide|user-guide|migration|implementation|reference-design|errata|an\d{3,}') {
            return '2_official_manufacturer_app_note'
        }
        if ($url -match 'datasheet|reference-manual|technical-reference-manual|lit/ds/') {
            return '1_official_manufacturer_datasheet'
        }
        return '1_official_manufacturer_datasheet'
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

function Infer-UrlFromPdfFileName {
    param([Parameter(Mandatory = $true)][string]$SourceFileName)

    $name = $SourceFileName.Trim()

    if ($name -match '^documentation\.espressif\.com-(.+\.pdf)\.pdf$') {
        return ('https://documentation.espressif.com/{0}' -f $Matches[1])
    }
    if ($name -match '^fscdn\.rohm\.com-en-products-databook-applinote-ic-power-(.+\.pdf)\.pdf$') {
        return ('https://fscdn.rohm.com/en/products/databook/applinote/ic/power/{0}' -f $Matches[1])
    }
    if ($name -match '^onsemi\.com-pub-Collateral-(.+\.PDF)\.pdf$') {
        return ('https://www.onsemi.com/pub/Collateral/{0}' -f $Matches[1])
    }
    if ($name -match '^silabs\.com-documents-public-application-notes-(.+\.pdf)\.pdf$') {
        return ('https://www.silabs.com/documents/public/application-notes/{0}' -f $Matches[1])
    }
    if ($name -match '^ti\.com-lit-an-([A-Za-z0-9]+)-([A-Za-z0-9]+\.pdf)\.pdf$') {
        return ('https://www.ti.com/lit/an/{0}/{1}' -f $Matches[1], $Matches[2])
    }
    if ($name -match '^ti\.com-lit-ds-symlink-([A-Za-z0-9]+\.pdf)\.pdf$') {
        return ('https://www.ti.com/lit/ds/symlink/{0}' -f $Matches[1])
    }
    if ($name -match '^we-online\.com-components-media-(.+\.pdf)\.pdf$') {
        $leaf = $Matches[1] -replace '-20', '%20'
        return ('https://www.we-online.com/components/media/{0}' -f $leaf)
    }

    return $null
}

function Invoke-PdfTextExtraction {
    param(
        [Parameter(Mandatory = $true)][string]$SourcePdfPath,
        [Parameter(Mandatory = $true)][string]$BodyTextPath,
        [AllowNull()][string]$PdftotextPath,
        [bool]$HasPython,
        [bool]$HasPypdf,
        [bool]$HasPymupdf
    )

    if (-not [string]::IsNullOrWhiteSpace($PdftotextPath)) {
        try {
            & $PdftotextPath -layout -nopgbrk $SourcePdfPath $BodyTextPath | Out-Null
            if (Test-Path -LiteralPath $BodyTextPath) {
                $text = [System.IO.File]::ReadAllText($BodyTextPath, [System.Text.Encoding]::UTF8)
                if (-not [string]::IsNullOrWhiteSpace($text)) {
                    return [pscustomobject]@{
                        status = 'success'
                        tool = 'pdftotext'
                        error = $null
                        page_count = $null
                        char_count = $text.Length
                        detected_title = $null
                    }
                }
            }
        }
        catch {
        }
    }

    if ($HasPython -and ($HasPypdf -or $HasPymupdf)) {
        $pythonScript = @'
import json
import os
import sys

source_pdf = sys.argv[1]
body_text_path = sys.argv[2]
has_pypdf = sys.argv[3].lower() == "true"
has_pymupdf = sys.argv[4].lower() == "true"

tool_order = []
if has_pypdf:
    tool_order.append("pypdf")
if has_pymupdf:
    tool_order.append("pymupdf")

result = {
    "status": "failed",
    "tool": None,
    "error": "no_tool_available",
    "page_count": None,
    "char_count": 0,
    "detected_title": None,
}

def write_text(text):
    with open(body_text_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)

for tool in tool_order:
    try:
        if tool == "pypdf":
            from pypdf import PdfReader
            reader = PdfReader(source_pdf)
            text_parts = []
            for index, page in enumerate(reader.pages, start=1):
                text_parts.append(f"[PAGE {index}]")
                text_parts.append(page.extract_text() or "")
                text_parts.append("")
            extracted_text = "\n".join(text_parts).strip()
            metadata_title = None
            try:
                metadata_title = getattr(reader.metadata, "title", None)
            except Exception:
                metadata_title = None
            if not extracted_text.strip():
                raise RuntimeError("empty_text")
            write_text(extracted_text)
            result = {
                "status": "success",
                "tool": "pypdf",
                "error": None,
                "page_count": len(reader.pages),
                "char_count": len(extracted_text),
                "detected_title": metadata_title,
            }
            break
        if tool == "pymupdf":
            import pymupdf
            doc = pymupdf.open(source_pdf)
            text_parts = []
            for index, page in enumerate(doc, start=1):
                text_parts.append(f"[PAGE {index}]")
                text_parts.append(page.get_text("text") or "")
                text_parts.append("")
            extracted_text = "\n".join(text_parts).strip()
            metadata_title = None
            try:
                metadata_title = doc.metadata.get("title")
            except Exception:
                metadata_title = None
            if not extracted_text.strip():
                raise RuntimeError("empty_text")
            write_text(extracted_text)
            result = {
                "status": "success",
                "tool": "pymupdf",
                "error": None,
                "page_count": doc.page_count,
                "char_count": len(extracted_text),
                "detected_title": metadata_title,
            }
            break
    except Exception as exc:
        result = {
            "status": "failed",
            "tool": tool,
            "error": f"{tool}: {exc}",
            "page_count": None,
            "char_count": 0,
            "detected_title": None,
        }

print(json.dumps(result))
'@

        $jsonResult = $pythonScript | python - $SourcePdfPath $BodyTextPath $HasPypdf.ToString().ToLowerInvariant() $HasPymupdf.ToString().ToLowerInvariant()
        if (-not [string]::IsNullOrWhiteSpace($jsonResult)) {
            return ($jsonResult | ConvertFrom-Json)
        }
    }

    return [pscustomobject]@{
        status = 'failed'
        tool = $null
        error = 'no_extraction_tool_available'
        page_count = $null
        char_count = 0
        detected_title = $null
    }
}

Ensure-Directory -Path $KnowledgeRoot

$pdfRoot = Join-Path $KnowledgeRoot '14_datasheets_pdf_markdown'
$originalPdfDir = Join-Path $pdfRoot 'original_pdf'
$extractedMarkdownDir = Join-Path $pdfRoot 'extracted_markdown'
$extractionLogsDir = Join-Path $pdfRoot 'extraction_logs'
Ensure-Directory -Path $pdfRoot
Ensure-Directory -Path $originalPdfDir
Ensure-Directory -Path $extractedMarkdownDir
Ensure-Directory -Path $extractionLogsDir

if (-not (Test-Path -LiteralPath $UrlIndexCsv)) {
    throw ('URL_INDEX CSV not found: {0}' -f $UrlIndexCsv)
}
if (-not (Test-Path -LiteralPath $InventoryCsv)) {
    throw ('Inventory CSV not found: {0}' -f $InventoryCsv)
}

$pdftotextCommand = Get-Command 'pdftotext' -ErrorAction SilentlyContinue
$pdftotextPath = if ($null -ne $pdftotextCommand) { $pdftotextCommand.Source } else { $null }
$pythonCommand = Get-Command 'python' -ErrorAction SilentlyContinue
$hasPython = $null -ne $pythonCommand
$hasPypdf = $false
$hasPymupdf = $false
if ($hasPython) {
    & python -c "import pypdf" 2>$null
    if ($LASTEXITCODE -eq 0) { $hasPypdf = $true }
    & python -c "import pymupdf" 2>$null
    if ($LASTEXITCODE -eq 0) { $hasPymupdf = $true }
}

$warningText = 'PDF extraction may lose diagrams, tables, pinouts, layout drawings, package drawings, and figures. Original PDF remains source of truth.'
$generatedAt = (Get-Date).ToString('s')

$urlRows = @(Import-Csv -LiteralPath $UrlIndexCsv)
$inventoryRows = @(Import-Csv -LiteralPath $InventoryCsv)
$nextUrlNumericId = 0
foreach ($row in $urlRows) {
    if ($row.id -match '^url_(\d+)$') {
        $numericId = [int]$Matches[1]
        if ($numericId -gt $nextUrlNumericId) {
            $nextUrlNumericId = $numericId
        }
    }
}

foreach ($row in $urlRows) {
    Set-PropertyValue -Object $row -Name 'original_pdf_path' -Value ''
    Set-PropertyValue -Object $row -Name 'extracted_markdown_path' -Value ''
    Set-PropertyValue -Object $row -Name 'extraction_status' -Value ''
    Set-PropertyValue -Object $row -Name 'extraction_tool' -Value ''
    Set-PropertyValue -Object $row -Name 'extraction_warning' -Value ''
}

$urlBySourcePath = @{}
$urlByGeneratedCandidate = @{}
$urlByPdfLeaf = @{}

foreach ($row in $urlRows) {
    if ($row.source_file_type -notin @('pdf', 'pdf_pdf')) {
        continue
    }

    if (-not [string]::IsNullOrWhiteSpace($row.source_scraped_file)) {
        $urlBySourcePath[$row.source_scraped_file] = $row
    }

    foreach ($candidate in (Get-LocalPdfFileNameCandidatesFromUrl -Url $row.original_url)) {
        if (-not $urlByGeneratedCandidate.ContainsKey($candidate)) {
            $urlByGeneratedCandidate[$candidate] = New-Object System.Collections.Generic.List[object]
        }
        $urlByGeneratedCandidate[$candidate].Add($row)
    }

    $pdfLeaf = Get-PdfPathLeaf -Url $row.original_url
    if (-not [string]::IsNullOrWhiteSpace($pdfLeaf)) {
        if (-not $urlByPdfLeaf.ContainsKey($pdfLeaf)) {
            $urlByPdfLeaf[$pdfLeaf] = New-Object System.Collections.Generic.List[object]
        }
        $urlByPdfLeaf[$pdfLeaf].Add($row)
    }
}

$pdfInventoryRows = @(
    $inventoryRows |
    Where-Object { ConvertTo-Bool $_.is_pdf } |
    Sort-Object source_file_path
)

$pdfIndexRows = New-Object System.Collections.Generic.List[object]
$extractionLogRows = New-Object System.Collections.Generic.List[object]
$aggregatesByUrlId = @{}

$pdfCountFound = $pdfInventoryRows.Count
$pdfsCopied = 0
$pdfsExtracted = 0
$extractionFailures = 0
$urlIndexMatched = 0
$urlIndexUnmatched = 0
$unmatchedSequence = 0
$availableExtractionTools = New-Object System.Collections.Generic.List[string]
if (-not [string]::IsNullOrWhiteSpace($pdftotextPath)) {
    $availableExtractionTools.Add('pdftotext')
}
if ($hasPypdf) {
    $availableExtractionTools.Add('pypdf')
}
if ($hasPymupdf) {
    $availableExtractionTools.Add('pymupdf')
}

foreach ($inventoryRow in $pdfInventoryRows) {
    $sourceFilePath = $inventoryRow.source_file_path
    $sourceFileName = $inventoryRow.source_file_name
    $matchedUrlRow = $null
    $matchMethod = $null

    if ($urlBySourcePath.ContainsKey($sourceFilePath)) {
        $matchedUrlRow = $urlBySourcePath[$sourceFilePath]
        $matchMethod = 'source_scraped_file'
    }
    elseif ($urlByGeneratedCandidate.ContainsKey($sourceFileName) -and $urlByGeneratedCandidate[$sourceFileName].Count -eq 1) {
        $matchedUrlRow = $urlByGeneratedCandidate[$sourceFileName][0]
        $matchMethod = 'generated_candidate_filename'
    }
    else {
        $pdfLeafFromSource = $sourceFileName.ToLowerInvariant()
        $leafMatch = [regex]::Match($pdfLeafFromSource, '([a-z0-9._-]+\.pdf)(?:\.pdf)?$')
        if ($leafMatch.Success) {
            $pdfLeaf = $leafMatch.Groups[1].Value.ToLowerInvariant()
            if ($urlByPdfLeaf.ContainsKey($pdfLeaf) -and $urlByPdfLeaf[$pdfLeaf].Count -eq 1) {
                $matchedUrlRow = $urlByPdfLeaf[$pdfLeaf][0]
                $matchMethod = 'pdf_leaf'
            }
        }
    }

    $urlId = $null
    $originalUrl = $null
    $normalizedUrl = $null
    $sourceDomain = if (-not [string]::IsNullOrWhiteSpace($inventoryRow.likely_domain)) { $inventoryRow.likely_domain } else { '' }
    $sourceOfTruthLevel = ''
    $trustLabel = ''
    if ($null -ne $matchedUrlRow) {
        $urlIndexMatched += 1
        $urlId = $matchedUrlRow.id
        $originalUrl = $matchedUrlRow.original_url
        $normalizedUrl = $matchedUrlRow.normalized_url
        if (-not [string]::IsNullOrWhiteSpace($matchedUrlRow.source_domain)) {
            $sourceDomain = $matchedUrlRow.source_domain
        }
        $sourceOfTruthLevel = Get-SourceOfTruthLevel -OriginalUrl $originalUrl -SourceDomain $sourceDomain
        $trustLabel = Get-TrustLabel -SourceOfTruthLevel $sourceOfTruthLevel
        $matchedUrlRow.source_of_truth_level = $sourceOfTruthLevel
        $matchedUrlRow.trust_label = $trustLabel

        if (-not $aggregatesByUrlId.ContainsKey($urlId)) {
            $aggregatesByUrlId[$urlId] = @{
                original_pdf_path = (New-Object System.Collections.Generic.List[string])
                extracted_markdown_path = (New-Object System.Collections.Generic.List[string])
                current_knowledge_file = (New-Object System.Collections.Generic.List[string])
                extraction_status = (New-Object System.Collections.Generic.List[string])
                extraction_tool = (New-Object System.Collections.Generic.List[string])
            }
        }
    }
    else {
        $inferredUrl = Infer-UrlFromPdfFileName -SourceFileName $sourceFileName
        if (-not [string]::IsNullOrWhiteSpace($inferredUrl)) {
            $nextUrlNumericId += 1
            $urlId = ('url_{0:d6}' -f $nextUrlNumericId)
            $originalUrl = $inferredUrl
            $normalizedUrl = Normalize-Url -Url $originalUrl
            $uri = [System.Uri]$normalizedUrl
            $sourceDomain = $uri.Host.ToLowerInvariant()
            $sourceOfTruthLevel = Get-SourceOfTruthLevel -OriginalUrl $originalUrl -SourceDomain $sourceDomain
            $trustLabel = Get-TrustLabel -SourceOfTruthLevel $sourceOfTruthLevel

            $matchedUrlRow = [pscustomobject][ordered]@{
                id = $urlId
                original_url = $originalUrl
                normalized_url = $normalizedUrl
                source_domain = $sourceDomain
                source_list_file = ''
                source_list_row = ''
                scraped_status = 'success'
                http_error_if_known = ''
                error_message_if_known = ''
                source_scraped_file = $sourceFilePath
                current_knowledge_file = ''
                source_file_type = $(if ($sourceFileName.ToLowerInvariant().EndsWith('.pdf.pdf')) { 'pdf_pdf' } else { 'pdf' })
                detected_category = '14_datasheets_pdf_markdown'
                source_of_truth_level = $sourceOfTruthLevel
                trust_label = $trustLabel
                content_quality = $(if (-not [string]::IsNullOrWhiteSpace($inventoryRow.quality_guess)) { $inventoryRow.quality_guess } else { 'unknown' })
                needs_future_rescrape = 'false'
                rescrape_reason = ''
                imported_at = $generatedAt
                last_scraped_at = $inventoryRow.last_write_time
                duplicate_group_id = ''
                notes = 'url_inferred_from_pdf_filename'
                original_pdf_path = ''
                extracted_markdown_path = ''
                extraction_status = ''
                extraction_tool = ''
                extraction_warning = ''
            }

            $urlRows += $matchedUrlRow
            $urlBySourcePath[$sourceFilePath] = $matchedUrlRow
            foreach ($candidate in (Get-LocalPdfFileNameCandidatesFromUrl -Url $originalUrl)) {
                if (-not $urlByGeneratedCandidate.ContainsKey($candidate)) {
                    $urlByGeneratedCandidate[$candidate] = New-Object System.Collections.Generic.List[object]
                }
                $urlByGeneratedCandidate[$candidate].Add($matchedUrlRow)
            }
            $pdfLeaf = Get-PdfPathLeaf -Url $originalUrl
            if (-not [string]::IsNullOrWhiteSpace($pdfLeaf)) {
                if (-not $urlByPdfLeaf.ContainsKey($pdfLeaf)) {
                    $urlByPdfLeaf[$pdfLeaf] = New-Object System.Collections.Generic.List[object]
                }
                $urlByPdfLeaf[$pdfLeaf].Add($matchedUrlRow)
            }

            $urlIndexMatched += 1
            $matchMethod = 'inferred_from_pdf_filename'
            if (-not $aggregatesByUrlId.ContainsKey($urlId)) {
                $aggregatesByUrlId[$urlId] = @{
                    original_pdf_path = (New-Object System.Collections.Generic.List[string])
                    extracted_markdown_path = (New-Object System.Collections.Generic.List[string])
                    current_knowledge_file = (New-Object System.Collections.Generic.List[string])
                    extraction_status = (New-Object System.Collections.Generic.List[string])
                    extraction_tool = (New-Object System.Collections.Generic.List[string])
                }
            }
        }
        else {
            $urlIndexUnmatched += 1
            $unmatchedSequence += 1
            $urlId = ('unmatched_pdf_{0:d3}' -f $unmatchedSequence)
            $originalUrl = ''
            $normalizedUrl = ''
            $sourceOfTruthLevel = '8_low_value_index_or_search'
            $trustLabel = 'low_value'
        }
    }

    $safeStem = Get-SafeStem -Prefix $urlId -SourceFileName $sourceFileName
    $copiedOriginalPath = Join-Path $originalPdfDir $safeStem
    if (-not $copiedOriginalPath.ToLowerInvariant().EndsWith('.pdf') -and -not $copiedOriginalPath.ToLowerInvariant().EndsWith('.pdf.pdf')) {
        $copiedOriginalPath = '{0}.pdf' -f $copiedOriginalPath
    }
    $legacyCopiedOriginalPath = '{0}.pdf' -f $copiedOriginalPath
    if ((-not (Test-Path -LiteralPath $copiedOriginalPath)) -and (Test-Path -LiteralPath $legacyCopiedOriginalPath)) {
        Move-Item -LiteralPath $legacyCopiedOriginalPath -Destination $copiedOriginalPath -Force
    }
    if (-not (Test-Path -LiteralPath $copiedOriginalPath) -or $Force) {
        Copy-Item -LiteralPath $sourceFilePath -Destination $copiedOriginalPath -Force
    }
    $pdfsCopied += 1

    $isRealPdf = Test-RealPdfHeader -Path $sourceFilePath
    $bodyTextPath = Join-Path $extractionLogsDir ('{0}.body.txt' -f $safeStem)
    if (Test-Path -LiteralPath $bodyTextPath) {
        Remove-Item -LiteralPath $bodyTextPath -Force
    }

    $extractionResult = $null
    if ($isRealPdf) {
        $extractionResult = Invoke-PdfTextExtraction -SourcePdfPath $sourceFilePath -BodyTextPath $bodyTextPath -PdftotextPath $pdftotextPath -HasPython:$hasPython -HasPypdf:$hasPypdf -HasPymupdf:$hasPymupdf
    }
    else {
        $extractionResult = [pscustomobject]@{
            status = 'failed'
            tool = $null
            error = 'invalid_pdf_header'
            page_count = $null
            char_count = 0
            detected_title = $null
        }
    }

    $extractedText = $null
    if ($extractionResult.status -eq 'success' -and (Test-Path -LiteralPath $bodyTextPath)) {
        $extractedText = [System.IO.File]::ReadAllText($bodyTextPath, [System.Text.Encoding]::UTF8)
    }

    $detectedTitle = $null
    if (-not [string]::IsNullOrWhiteSpace($extractionResult.detected_title)) {
        $detectedTitle = $extractionResult.detected_title
    }
    if ([string]::IsNullOrWhiteSpace($detectedTitle)) {
        $detectedTitle = Get-FirstMeaningfulLine -Text $extractedText
    }
    if ([string]::IsNullOrWhiteSpace($detectedTitle) -and -not [string]::IsNullOrWhiteSpace($originalUrl)) {
        $detectedTitle = [System.IO.Path]::GetFileNameWithoutExtension((Get-PdfPathLeaf -Url $originalUrl))
    }
    if ([string]::IsNullOrWhiteSpace($detectedTitle)) {
        $detectedTitle = [System.IO.Path]::GetFileNameWithoutExtension($sourceFileName)
    }
    $detectedTitle = $detectedTitle.Trim()

    $categoryGuess = Get-PdfCategoryGuess -UrlRow $matchedUrlRow -InventoryRow $inventoryRow -ExtractedText $extractedText -DetectedTitle $detectedTitle
    $extractedMarkdownPath = $null
    $categoryCopyPath = $null
    $extractionStatus = 'extraction_failed'
    $extractionTool = $extractionResult.tool
    $failureReason = $null

    if ($extractionResult.status -eq 'success' -and -not [string]::IsNullOrWhiteSpace($extractedText)) {
        $canonicalMarkdownPath = Join-Path $extractedMarkdownDir ('{0}.md' -f $safeStem)
        $categoryDir = Join-Path $KnowledgeRoot $categoryGuess
        Ensure-Directory -Path $categoryDir
        $categoryCopyPath = Join-Path $categoryDir ('{0}.md' -f $safeStem)
        $relativeOriginalPdfPath = Get-RelativePath -BasePath $KnowledgeRoot -TargetPath $copiedOriginalPath
        $relativeCanonicalMarkdownPath = Get-RelativePath -BasePath $KnowledgeRoot -TargetPath $canonicalMarkdownPath
        $relativeCategoryCopyPath = Get-RelativePath -BasePath $KnowledgeRoot -TargetPath $categoryCopyPath

        $frontmatterLines = New-Object System.Collections.Generic.List[string]
        $frontmatterLines.Add('---')
        $frontmatterLines.Add(('title: {0}' -f (ConvertTo-YamlScalar $detectedTitle)))
        $frontmatterLines.Add(('source_url: {0}' -f (ConvertTo-YamlScalar $originalUrl)))
        $frontmatterLines.Add(('normalized_url: {0}' -f (ConvertTo-YamlScalar $normalizedUrl)))
        $frontmatterLines.Add(('url_index_id: {0}' -f (ConvertTo-YamlScalar $urlId)))
        $frontmatterLines.Add(('source_pdf: {0}' -f (ConvertTo-YamlScalar $sourceFilePath)))
        $frontmatterLines.Add(('original_pdf_path: {0}' -f (ConvertTo-YamlScalar $relativeOriginalPdfPath)))
        $frontmatterLines.Add(('extracted_markdown_path: {0}' -f (ConvertTo-YamlScalar $relativeCanonicalMarkdownPath)))
        $frontmatterLines.Add(('extraction_tool: {0}' -f (ConvertTo-YamlScalar $extractionTool)))
        $frontmatterLines.Add(('extracted_at: {0}' -f (ConvertTo-YamlScalar $generatedAt)))
        $frontmatterLines.Add(('source_domain: {0}' -f (ConvertTo-YamlScalar $sourceDomain)))
        $frontmatterLines.Add(('source_of_truth_level: {0}' -f (ConvertTo-YamlScalar $sourceOfTruthLevel)))
        $frontmatterLines.Add(('trust_label: {0}' -f (ConvertTo-YamlScalar $trustLabel)))
        $frontmatterLines.Add(('category_guess: {0}' -f (ConvertTo-YamlScalar $categoryGuess)))
        $frontmatterLines.Add(('warning: {0}' -f (ConvertTo-YamlScalar $warningText)))
        $frontmatterLines.Add('---')
        $frontmatterLines.Add('')
        $frontmatterLines.Add('# ' + $detectedTitle)
        $frontmatterLines.Add('')
        $frontmatterLines.Add('> PDF extraction warning: diagrams, tables, pinouts, package drawings, layout figures, and formatting may be incomplete. Use the original PDF as source of truth.')
        $frontmatterLines.Add('')
        $frontmatterLines.Add($extractedText.Trim())
        $markdownText = ($frontmatterLines -join "`r`n")

        if (-not (Test-Path -LiteralPath $canonicalMarkdownPath) -or $Force) {
            Set-Content -LiteralPath $canonicalMarkdownPath -Value $markdownText -Encoding UTF8
        }
        if (-not (Test-Path -LiteralPath $categoryCopyPath) -or $Force) {
            Set-Content -LiteralPath $categoryCopyPath -Value $markdownText -Encoding UTF8
        }

        $extractedMarkdownPath = $relativeCanonicalMarkdownPath
        $categoryCopyPath = $relativeCategoryCopyPath
        $extractionStatus = 'success'
        $pdfsExtracted += 1
    }
    else {
        $failureReason = $extractionResult.error
        $extractionFailures += 1
    }

    $relativeCopiedOriginalPath = Get-RelativePath -BasePath $KnowledgeRoot -TargetPath $copiedOriginalPath

    $perFileLogPath = Join-Path $extractionLogsDir ('{0}.log.txt' -f $safeStem)
    $perFileLogLines = @(
        ('generated_at={0}' -f $generatedAt),
        ('source_file_path={0}' -f $sourceFilePath),
        ('url_index_id={0}' -f $urlId),
        ('match_method={0}' -f $matchMethod),
        ('is_real_pdf={0}' -f $isRealPdf),
        ('original_pdf_path={0}' -f $relativeCopiedOriginalPath),
        ('extracted_markdown_path={0}' -f $extractedMarkdownPath),
        ('category_copy_path={0}' -f $categoryCopyPath),
        ('category_guess={0}' -f $categoryGuess),
        ('extraction_status={0}' -f $extractionStatus),
        ('extraction_tool={0}' -f $extractionTool),
        ('page_count={0}' -f $extractionResult.page_count),
        ('char_count={0}' -f $extractionResult.char_count),
        ('error={0}' -f $failureReason),
        ('warning={0}' -f $warningText)
    )
    Set-Content -LiteralPath $perFileLogPath -Value ($perFileLogLines -join "`r`n") -Encoding UTF8

    $pdfIndexRows.Add([pscustomobject][ordered]@{
            url_index_id = $urlId
            original_url = $originalUrl
            normalized_url = $normalizedUrl
            source_domain = $sourceDomain
            source_file_path = $sourceFilePath
            source_file_name = $sourceFileName
            original_pdf_path = $relativeCopiedOriginalPath
            extracted_markdown_path = $extractedMarkdownPath
            current_knowledge_file = $categoryCopyPath
            category_guess = $categoryGuess
            extraction_status = $extractionStatus
            extraction_tool = $extractionTool
            page_count = $extractionResult.page_count
            extracted_char_count = $extractionResult.char_count
            match_method = $matchMethod
            warning = $warningText
            notes = $failureReason
        })

    $extractionLogRows.Add([pscustomobject][ordered]@{
            generated_at = $generatedAt
            source_file_path = $sourceFilePath
            source_file_name = $sourceFileName
            url_index_id = $urlId
            original_url = $originalUrl
            match_method = $matchMethod
            is_real_pdf = $isRealPdf
            extraction_status = $extractionStatus
            extraction_tool = $extractionTool
            page_count = $extractionResult.page_count
            extracted_char_count = $extractionResult.char_count
            original_pdf_path = $relativeCopiedOriginalPath
            extracted_markdown_path = $extractedMarkdownPath
            current_knowledge_file = $categoryCopyPath
            error = $failureReason
        })

    if ($null -ne $matchedUrlRow) {
        $aggregate = $aggregatesByUrlId[$urlId]
        $aggregate.original_pdf_path.Add($relativeCopiedOriginalPath)
        if (-not [string]::IsNullOrWhiteSpace($extractedMarkdownPath)) {
            $aggregate.extracted_markdown_path.Add($extractedMarkdownPath)
        }
        if (-not [string]::IsNullOrWhiteSpace($categoryCopyPath)) {
            $aggregate.current_knowledge_file.Add($categoryCopyPath)
        }
        $aggregate.extraction_status.Add($extractionStatus)
        if (-not [string]::IsNullOrWhiteSpace($extractionTool)) {
            $aggregate.extraction_tool.Add($extractionTool)
        }
        $matchedUrlRow.extraction_warning = $warningText
        if ($matchedUrlRow.detected_category -eq '14_datasheets_pdf_markdown' -or [string]::IsNullOrWhiteSpace($matchedUrlRow.current_knowledge_file)) {
            $matchedUrlRow.detected_category = $categoryGuess
        }
    }
}

foreach ($row in $urlRows) {
    if ($row.source_file_type -notin @('pdf', 'pdf_pdf')) {
        continue
    }

    if ($aggregatesByUrlId.ContainsKey($row.id)) {
        $aggregate = $aggregatesByUrlId[$row.id]
        $row.original_pdf_path = Join-Distinct -Values $aggregate.original_pdf_path
        $row.extracted_markdown_path = Join-Distinct -Values $aggregate.extracted_markdown_path
        $row.current_knowledge_file = Join-Distinct -Values $aggregate.current_knowledge_file
        $row.extraction_tool = Join-Distinct -Values $aggregate.extraction_tool
        $statuses = @($aggregate.extraction_status | Select-Object -Unique)
        if ($statuses.Count -eq 1) {
            $row.extraction_status = $statuses[0]
        }
        elseif ($statuses.Count -gt 1) {
            if ($statuses -contains 'success') {
                $row.extraction_status = 'partial_success'
            }
            else {
                $row.extraction_status = Join-Distinct -Values $statuses
            }
        }
        $row.extraction_warning = $warningText
    }
    elseif ([string]::IsNullOrWhiteSpace($row.extraction_status)) {
        $row.extraction_status = 'not_processed'
        $row.extraction_warning = $warningText
    }
}

$pdfIndexCsvPath = Join-Path $pdfRoot 'PDF_INDEX.csv'
$pdfIndexMarkdownPath = Join-Path $pdfRoot 'PDF_INDEX.md'
$extractionLogCsvPath = Join-Path $extractionLogsDir 'pdf_extraction_log.csv'

$pdfIndexRows | Export-Csv -LiteralPath $pdfIndexCsvPath -NoTypeInformation -Encoding UTF8
$extractionLogRows | Export-Csv -LiteralPath $extractionLogCsvPath -NoTypeInformation -Encoding UTF8

$categorySummary = @(
    $pdfIndexRows |
    Group-Object category_guess |
    Sort-Object Count -Descending |
    ForEach-Object { '- `{0}`: `{1}`' -f $_.Name, $_.Count }
)
$statusSummary = @(
    $pdfIndexRows |
    Group-Object extraction_status |
    Sort-Object Count -Descending |
    ForEach-Object { '- `{0}`: `{1}`' -f $_.Name, $_.Count }
)
$toolSummary = @(
    $pdfIndexRows |
    Group-Object extraction_tool |
    Sort-Object Count -Descending |
    ForEach-Object { '- `{0}`: `{1}`' -f $(if ([string]::IsNullOrWhiteSpace($_.Name)) { '(none)' } else { $_.Name }), $_.Count }
)

$pdfIndexMarkdownLines = New-Object System.Collections.Generic.List[string]
$pdfIndexMarkdownLines.Add('# PDF_INDEX')
$pdfIndexMarkdownLines.Add('')
$pdfIndexMarkdownLines.Add(('Generated at: `{0}`' -f $generatedAt))
$pdfIndexMarkdownLines.Add('')
$pdfIndexMarkdownLines.Add('## Summary')
$pdfIndexMarkdownLines.Add('')
$pdfIndexMarkdownLines.Add(('- PDF count found: `{0}`' -f $pdfCountFound))
$pdfIndexMarkdownLines.Add(('- PDFs copied: `{0}`' -f $pdfsCopied))
$pdfIndexMarkdownLines.Add(('- PDFs extracted: `{0}`' -f $pdfsExtracted))
$pdfIndexMarkdownLines.Add(('- Extraction failures: `{0}`' -f $extractionFailures))
$pdfIndexMarkdownLines.Add(('- URL_INDEX matched: `{0}`' -f $urlIndexMatched))
$pdfIndexMarkdownLines.Add(('- URL_INDEX unmatched: `{0}`' -f $urlIndexUnmatched))
$pdfIndexMarkdownLines.Add('')
$pdfIndexMarkdownLines.Add('## Extraction Status')
$pdfIndexMarkdownLines.Add('')
foreach ($line in $statusSummary) {
    $pdfIndexMarkdownLines.Add($line)
}
$pdfIndexMarkdownLines.Add('')
$pdfIndexMarkdownLines.Add('## Extraction Tools')
$pdfIndexMarkdownLines.Add('')
foreach ($line in $toolSummary) {
    $pdfIndexMarkdownLines.Add($line)
}
$pdfIndexMarkdownLines.Add('')
$pdfIndexMarkdownLines.Add('## Category Summary')
$pdfIndexMarkdownLines.Add('')
foreach ($line in $categorySummary) {
    $pdfIndexMarkdownLines.Add($line)
}
$pdfIndexMarkdownLines.Add('')
$pdfIndexMarkdownLines.Add('## Warning')
$pdfIndexMarkdownLines.Add('')
$pdfIndexMarkdownLines.Add('- Original PDF remains source of truth. Extracted Markdown may omit diagrams, tables, pinouts, package drawings, layout figures, and formatting.')
$pdfIndexMarkdownLines | Set-Content -LiteralPath $pdfIndexMarkdownPath -Encoding UTF8

$urlRows | Export-Csv -LiteralPath $UrlIndexCsv -NoTypeInformation -Encoding UTF8
$urlIndexJsonPath = Join-Path $KnowledgeRoot 'URL_INDEX.json'
$urlRows | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $urlIndexJsonPath -Encoding UTF8

$linkedUrlCount = @($urlRows | Where-Object { -not [string]::IsNullOrWhiteSpace($_.current_knowledge_file) }).Count
$pdfLinkedUrlCount = @($urlRows | Where-Object { $_.source_file_type -in @('pdf', 'pdf_pdf') -and -not [string]::IsNullOrWhiteSpace($_.current_knowledge_file) }).Count
$pdfStatusSummary = @(
    $urlRows |
    Where-Object { $_.source_file_type -in @('pdf', 'pdf_pdf') } |
    Group-Object extraction_status |
    Sort-Object Count -Descending |
    ForEach-Object { '- `{0}`: `{1}`' -f $_.Name, $_.Count }
)

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

$urlStatusSummaryLines = @(
    $urlRows |
    Group-Object scraped_status |
    Sort-Object Name |
    ForEach-Object { '- `{0}`: `{1}`' -f $_.Name, $_.Count }
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
$urlIndexMarkdownLines.Add(('Generated at: `{0}`' -f $generatedAt))
$urlIndexMarkdownLines.Add('')
$urlIndexMarkdownLines.Add('## Summary')
$urlIndexMarkdownLines.Add('')
$urlIndexMarkdownLines.Add(('- Total URLs known: `{0}`' -f $urlRows.Count))
$urlIndexMarkdownLines.Add(('- URLs linked to knowledge files: `{0}`' -f $linkedUrlCount))
$urlIndexMarkdownLines.Add(('- PDF URL rows linked to extracted Markdown: `{0}`' -f $pdfLinkedUrlCount))
$urlIndexMarkdownLines.Add(('- PDF count found: `{0}`' -f $pdfCountFound))
$urlIndexMarkdownLines.Add(('- PDFs extracted: `{0}`' -f $pdfsExtracted))
$urlIndexMarkdownLines.Add(('- PDF extraction failures: `{0}`' -f $extractionFailures))
$urlIndexMarkdownLines.Add('')
$urlIndexMarkdownLines.Add('## URL Status Summary')
$urlIndexMarkdownLines.Add('')
foreach ($line in $urlStatusSummaryLines) {
    $urlIndexMarkdownLines.Add($line)
}
$urlIndexMarkdownLines.Add('')
$urlIndexMarkdownLines.Add('## PDF Extraction Summary')
$urlIndexMarkdownLines.Add('')
foreach ($line in $pdfStatusSummary) {
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
$urlIndexMarkdownLines.Add('1. PDF extraction is text-only. Original PDFs remain source of truth.')
$urlIndexMarkdownLines.Add('2. `original_pdf_path`, `extracted_markdown_path`, `extraction_status`, `extraction_tool`, and `extraction_warning` are populated on PDF-backed URL rows.')
$urlIndexMarkdownLines.Add('3. Multiple copied/extracted files may be joined with `; ` when more than one scraped PDF maps to the same URL row.')

$urlIndexMarkdownPath = Join-Path $KnowledgeRoot 'URL_INDEX.md'
$urlIndexMarkdownLines | Set-Content -LiteralPath $urlIndexMarkdownPath -Encoding UTF8

$indexLines = New-Object System.Collections.Generic.List[string]
$indexLines.Add('# knowledge_scrape Index')
$indexLines.Add('')
$indexLines.Add(('Generated at: `{0}`' -f $generatedAt))
$indexLines.Add('')
$indexLines.Add('- `SOURCE_AUDIT.md`: scrape input inventory summary.')
$indexLines.Add('- `URL_INDEX.csv/json/md`: canonical URL registry with Markdown and PDF link fields.')
$indexLines.Add('- `RESCRAPE_QUEUE.csv`: follow-up scrape targets from the registry builder.')
$indexLines.Add('- `_logs/classify_copy_log.csv`: Markdown copy/classification actions.')
$indexLines.Add('- `14_datasheets_pdf_markdown/PDF_INDEX.csv/md`: PDF extraction inventory and summary.')
$indexLines.Add('- `14_datasheets_pdf_markdown/original_pdf/`: copied source PDFs.')
$indexLines.Add('- `14_datasheets_pdf_markdown/extracted_markdown/`: canonical extracted Markdown for PDFs.')
$indexLines.Add('- `14_datasheets_pdf_markdown/extraction_logs/pdf_extraction_log.csv`: PDF extraction run log.')
$indexLines.Add('')
$indexLines.Add('## Category Counts')
$indexLines.Add('')
$indexLines.Add('| Category | Markdown Files |')
$indexLines.Add('| --- | ---: |')
foreach ($row in $knowledgeCategoryRows) {
    $indexLines.Add(('| {0} | {1} |' -f $row.category, $row.markdown_files))
}
$indexLines.Add('')
$indexLines.Add('## PDF Summary')
$indexLines.Add('')
$indexLines.Add(('- PDF count found: `{0}`' -f $pdfCountFound))
$indexLines.Add(('- PDFs copied: `{0}`' -f $pdfsCopied))
$indexLines.Add(('- PDFs extracted: `{0}`' -f $pdfsExtracted))
$indexLines.Add(('- Extraction failures: `{0}`' -f $extractionFailures))

$indexPath = Join-Path $KnowledgeRoot 'INDEX.md'
$indexLines | Set-Content -LiteralPath $indexPath -Encoding UTF8

$manifest = [ordered]@{
    name = 'knowledge_scrape'
    status = 'markdown_and_pdf_import_completed'
    created_for = 'scrape audit and URL/source inventory'
    content_copy_status = 'markdown_completed'
    pdf_extraction_status = 'completed'
    primary_builders = @(
        '_scripts/01_build_raw_inventory.ps1',
        '_scripts/02_build_url_registry.ps1',
        '_scripts/03_classify_copy_markdown.ps1',
        '_scripts/04_convert_pdfs_to_markdown.ps1'
    )
    generated_at = $generatedAt
    inventory_csv = $InventoryCsv
    url_index_csv = $UrlIndexCsv
    pdf_count_found = $pdfCountFound
    pdfs_copied = $pdfsCopied
    pdfs_extracted = $pdfsExtracted
    extraction_failures = $extractionFailures
    url_index_pdf_matched = $urlIndexMatched
    url_index_pdf_unmatched = $urlIndexUnmatched
    pdf_extraction_tool_priority = @($availableExtractionTools)
    linked_url_count = $linkedUrlCount
    category_counts = [ordered]@{}
}

foreach ($row in $knowledgeCategoryRows) {
    $manifest.category_counts[$row.category] = $row.markdown_files
}

$manifestPath = Join-Path $KnowledgeRoot 'MANIFEST.json'
$manifest | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $manifestPath -Encoding UTF8

[pscustomobject][ordered]@{
    pdf_count_found = $pdfCountFound
    pdfs_copied = $pdfsCopied
    pdfs_extracted = $pdfsExtracted
    extraction_failures = $extractionFailures
    url_index_matched = $urlIndexMatched
    url_index_unmatched = $urlIndexUnmatched
    extraction_tools_available = (Join-Distinct -Values $availableExtractionTools)
} | Format-List
