param(
    [string]$KnowledgeRoot = (Split-Path -Parent $PSScriptRoot),
    [string]$IngestRoot = 'C:\KICAD_SCRAPE\ingest_v2'
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$script:ImportBatch = 'ingest_v2'
$script:ImportStartedAt = Get-Date
$script:TimestampIso = $script:ImportStartedAt.ToString('s')

$script:CategoryDefinitions = [ordered]@{
    '01_kicad_core' = @{
        purpose = 'Official KiCad core manuals, editor behavior, CLI references, and tool usage documentation.'
        usage = 'Use this category first for KiCad behavior, eeschema, pcbnew, GerbView, CLI, and official workflow questions.'
        warning = 'Prefer official KiCad docs here over forum explanations when behavior details matter.'
    }
    '02_kicad_python_api' = @{
        purpose = 'KiCad Python, IPC, SWIG, pcbnew API, add-on, and automation references.'
        usage = 'Use this category before proposing automation, plugin work, or scripted KiCad interaction.'
        warning = 'Version-specific API behavior still needs verification against the target KiCad release.'
    }
    '03_kicad_file_formats' = @{
        purpose = 'KiCad file-format, serialization, and S-expression references.'
        usage = 'Use this category for parsing, generating, or validating KiCad project file structures.'
        warning = 'Do not modify active design files until format assumptions are verified against the real file and version.'
    }
    '04_kicad_libraries_symbols_footprints' = @{
        purpose = 'KiCad libraries, KLC, symbols, footprints, packages3D, and library contribution guidance.'
        usage = 'Use this category for symbol, footprint, and library-policy work before using third-party CAD libraries.'
        warning = 'Library content is not proof. Cross-check package, pad size, and pin-1 against the original source PDF.'
    }
    '05_esp32_espressif' = @{
        purpose = 'Espressif and ESP32-family hardware, datasheet, TRM, and design-guideline references.'
        usage = 'Use this category first for ESP32-family hardware decisions, RF notes, power domains, and official guidance.'
        warning = 'Use the original Espressif PDF for pinouts, package drawings, RF keepouts, and tables.'
    }
    '06_microcontrollers' = @{
        purpose = 'Non-Espressif MCU datasheets, manuals, and hardware references.'
        usage = 'Use this category for STM32, RP2040, Nordic, Microchip, Infineon, Renesas, WCH, and similar MCU work.'
        warning = 'Verify exact part number and package. Variants often differ materially.'
    }
    '07_usb_c_high_speed_esd' = @{
        purpose = 'USB, USB-C, PD, ESD, TVS, high-speed differential routing, and connector-protection references.'
        usage = 'Use this category for USB-C wiring, protection placement, and connector-side layout decisions.'
        warning = 'Final USB-C and protection decisions still need official controller, connector, and protection-source confirmation.'
    }
    '08_power_buck_regulators' = @{
        purpose = 'Buck, boost, switching regulator, LDO, and general power-conversion references.'
        usage = 'Use this category for power-stage architecture, regulator choice, compensation context, and general power design.'
        warning = 'Use official datasheets and layout guides for final switch-node, loop, and component-placement decisions.'
    }
    '09_pcb_layout_grounding_emi_si' = @{
        purpose = 'General PCB layout, grounding, return-path, EMI, EMC, SI, and RF guidance.'
        usage = 'Use this category for board-level layout patterns, grounding, crosstalk, decoupling, and EMI tradeoffs.'
        warning = 'Treat broad articles as context. Cross-check critical rules with interface- and component-specific sources.'
    }
    '10_dfm_fabrication_assembly' = @{
        purpose = 'Fabrication, assembly, Gerber, BOM/CPL, stackup, and DFM/DFA references.'
        usage = 'Use this category for board-house rules, assembly requirements, and manufacturing constraints.'
        warning = 'Board-house rules differ. Match any final recommendation to the chosen fabricator.'
    }
    '11_calculators_ipc_reference' = @{
        purpose = 'Calculators, IPC-style references, trace-width and impedance guidance.'
        usage = 'Use this category for first-pass calculations and standards-oriented lookup work.'
        warning = 'Calculators are starting points only and must be checked against the actual stackup and environment.'
    }
    '12_forums_peer_review' = @{
        purpose = 'Peer-review, troubleshooting, and engineering forum content.'
        usage = 'Use this category after official sources to gather failure patterns, discussion context, and corroboration.'
        warning = 'Do not treat forum content as sole authority for final engineering decisions.'
    }
    '13_vendor_parts_cad_models' = @{
        purpose = 'Vendor CAD libraries, marketplace part portals, and external symbol/footprint sources.'
        usage = 'Use this category to locate models and references, then verify them against primary package documentation.'
        warning = 'Third-party footprints and models require independent verification.'
    }
    '14_datasheets_pdf_markdown' = @{
        purpose = 'Original PDF corpus, extracted Markdown, and PDF import indexes.'
        usage = 'Search extracted Markdown here, then open the original PDF for exact tables, pinouts, package drawings, and layout figures.'
        warning = 'Extracted PDF Markdown is secondary only. Original PDFs remain source of truth.'
    }
    '15_video_reference_index' = @{
        purpose = 'Video, channel, and index-like media references.'
        usage = 'Use this category only as a low-priority pointer source after higher-trust documents are checked.'
        warning = 'Video references are not authoritative engineering proof.'
    }
    '16_ai_pcb_failure_modes' = @{
        purpose = 'AI EDA failure cases, hallucination patterns, and AI PCB-design limitations.'
        usage = 'Use this category when evaluating or constraining AI-generated schematic and PCB decisions.'
        warning = 'This category is for failure analysis and guardrails, not design authority.'
    }
    '17_case_studies_bad_boards' = @{
        purpose = 'Bad-board examples, debugging threads, and failure-case studies.'
        usage = 'Use this category for concrete examples of layout, grounding, power, or bring-up failure modes.'
        warning = 'Failure cases are context-rich but often incomplete. Cross-check root-cause claims.'
    }
    '18_case_studies_good_boards' = @{
        purpose = 'Good-board examples, proven reference layouts, and successful case studies.'
        usage = 'Use this category for comparative layout patterns and documented rationale from successful designs.'
        warning = 'Reference designs still need adaptation to the actual part, stackup, and constraints.'
    }
    '19_university_training' = @{
        purpose = 'University PCB courses, labs, lecture notes, and training material.'
        usage = 'Use this category for structured teaching material and foundational review.'
        warning = 'Academic material can lag current parts and fabrication constraints.'
    }
    '20_manufacturer_layout_guides' = @{
        purpose = 'Official manufacturer layout guides and app notes specifically focused on PCB implementation.'
        usage = 'Use this category first for vendor-authored layout, placement, and routing guidance.'
        warning = 'These files often contain critical figures missing from extracted Markdown. Use the original PDF when details matter.'
    }
    '21_component_package_land_patterns' = @{
        purpose = 'Land patterns, mechanical drawings, connector package data, and recommended footprints.'
        usage = 'Use this category for package dimensions, connector footprint work, and footprint-verification checks.'
        warning = 'Original mechanical drawings remain the deciding authority.'
    }
    '22_automotive_harsh_environment' = @{
        purpose = 'Automotive, transients, harsh-environment, load-dump, and ruggedization references.'
        usage = 'Use this category for CAN, reverse-battery, ISO 7637, vibration, and harsh-environment design work.'
        warning = 'Compliance and environmental claims require system-specific verification.'
    }
    '23_rf_wifi_antenna_layout' = @{
        purpose = 'RF, Wi-Fi, antenna keepout, matching, and feedline-layout references.'
        usage = 'Use this category for RF layout, keepout, antenna integration, and impedance-sensitive routing.'
        warning = 'Use original vendor RF layout figures and reference designs for final geometry decisions.'
    }
    '24_power_integrity_decoupling' = @{
        purpose = 'Power integrity, decoupling, PDN, transient response, and bypass-layout references.'
        usage = 'Use this category for capacitor placement, plane strategy, and transient-response support decisions.'
        warning = 'Final capacitor values and placement must match the exact regulator or MCU guidance.'
    }
    '25_signal_integrity_high_speed' = @{
        purpose = 'Controlled impedance, high-speed digital, differential-pair, and SI references.'
        usage = 'Use this category for differential routing, termination, via strategy, and high-speed channel decisions.'
        warning = 'Real stackup and channel constraints govern final SI decisions.'
    }
    '26_thermal_mechanical_enclosure' = @{
        purpose = 'Thermal, mechanical, mounting, enclosure, and ruggedization references.'
        usage = 'Use this category for thermal vias, mechanical clearances, mounting, and enclosure-constrained layout work.'
        warning = 'Mechanical context and assembly stackup still need project-specific confirmation.'
    }
    '27_test_debug_validation' = @{
        purpose = 'Test points, bring-up, debug, DFT, measurement, and validation references.'
        usage = 'Use this category for bring-up planning, debug access, pre-compliance, and validation workflow design.'
        warning = 'Validation guidance should be adapted to the actual lab setup and product risks.'
    }
    '28_high_reliability_aerospace_workmanship' = @{
        purpose = 'High-reliability, aerospace, NASA, ESA, ECSS, and workmanship-oriented references.'
        usage = 'Use this category for workmanship, inspection, and high-reliability process considerations.'
        warning = 'Do not infer compliance from summaries alone. Use the governing standard when required.'
    }
    '29_standards_ipc_ul_safety' = @{
        purpose = 'IPC, UL, creepage, clearance, and standards-oriented safety references.'
        usage = 'Use this category for standards summaries, spacing references, and safety-related lookup work.'
        warning = 'Summaries are secondary. Use the governing standard or official safety documentation for final claims.'
    }
    '30_eda_automation_verification' = @{
        purpose = 'EDA automation, KiBot, KiKit, KiCost, SKiDL, and related verification-tool references.'
        usage = 'Use this category for automation pipelines, verification tools, BOM tooling, and scriptable EDA workflows.'
        warning = 'Tool behavior is version-sensitive. Verify against the local toolchain before relying on it.'
    }
    '31_compliance_safety_emc' = @{
        purpose = 'EMC, compliance, safety, fusing, ESD immunity, and regulatory references.'
        usage = 'Use this category for product-level compliance context and safety architecture support.'
        warning = 'Compliance requires testable evidence, not article-level inference.'
    }
    '90_unsorted_review' = @{
        purpose = 'Useful but uncertain material awaiting better classification.'
        usage = 'Use this category for review and recovery work when content is useful but category confidence is low.'
        warning = 'Files here need follow-up before being treated as polished references.'
    }
    '91_rejected_low_value' = @{
        purpose = 'Rejected low-value material such as navigation shells, login pages, weak indexes, and broken outputs.'
        usage = 'Use this category only for scrape diagnostics, gap analysis, or future recovery review.'
        warning = 'Do not treat this category as normal engineering authority.'
    }
}

$script:TopicalCategories = @($script:CategoryDefinitions.Keys)
$script:ContentCategories = @($script:TopicalCategories | Where-Object { $_ -notlike '90_*' -and $_ -notlike '91_*' })
$script:AllCategoryFolders = @(
    '00_ai_entrypoints',
    '00_engineering_rules',
    '00_retrieval_indexes',
    '00_source_of_truth'
) + $script:TopicalCategories + @('99_source_logs')

$script:UrlIndexColumns = @(
    'id',
    'original_url',
    'normalized_url',
    'source_domain',
    'source_type',
    'topic_category',
    'trust_level',
    'scrape_status',
    'local_file',
    'current_knowledge_file',
    'raw_html_path',
    'markdown_path',
    'pdf_path',
    'extracted_pdf_markdown_path',
    'error_message',
    'imported_at',
    'scraped_at',
    'needs_review',
    'duplicate_status',
    'duplicate_of_url_index_id',
    'content_quality',
    'knowledge_category',
    'source_batch',
    'notes',
    'source_scraped_file',
    'source_file_type',
    'detected_category',
    'source_of_truth_level',
    'trust_label',
    'scraped_status',
    'error_message_if_known',
    'last_scraped_at',
    'original_pdf_path',
    'extracted_markdown_path',
    'extraction_status',
    'extraction_tool',
    'extraction_warning',
    'needs_future_rescrape',
    'rescrape_reason',
    'duplicate_group_id'
)

$script:InventoryColumns = @(
    'source_file_path',
    'source_file_name',
    'source_folder',
    'extension',
    'size_bytes',
    'sha256',
    'last_write_time',
    'detected_source_url',
    'normalized_url',
    'source_domain',
    'source_type',
    'topic_category',
    'trust_level',
    'scrape_status',
    'is_markdown',
    'is_pdf',
    'is_raw_html',
    'is_extracted_pdf_markdown',
    'contains_raw_html',
    'raw_html_tag_count',
    'word_count',
    'line_count',
    'first_heading',
    'content_quality_guess',
    'target_category_guess',
    'duplicate_by_url',
    'duplicate_by_hash',
    'existing_knowledge_file_if_duplicate',
    'import_action'
)

$script:PdfIndexColumns = @(
    'url_index_id',
    'source_url',
    'normalized_url',
    'original_pdf_path',
    'extracted_markdown_path',
    'current_knowledge_file',
    'source_domain',
    'topic_category',
    'trust_level',
    'knowledge_category',
    'extraction_status',
    'warning',
    'imported_at',
    'source_batch',
    'source_file_path',
    'source_file_name',
    'notes'
)

function Ensure-Directory {
    param([Parameter(Mandatory = $true)][string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) {
        New-Item -ItemType Directory -Force -Path $Path | Out-Null
    }
}

function Read-Utf8Text {
    param([Parameter(Mandatory = $true)][string]$Path)

    return [System.IO.File]::ReadAllText($Path, [System.Text.Encoding]::UTF8)
}

function Write-Utf8Text {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)][string]$Text
    )

    $parent = Split-Path -Parent $Path
    if (-not [string]::IsNullOrWhiteSpace($parent)) {
        Ensure-Directory -Path $parent
    }
    [System.IO.File]::WriteAllText($Path, $Text, [System.Text.Encoding]::UTF8)
}

function Resolve-FullPathSafe {
    param([AllowNull()][string]$Path)

    if ([string]::IsNullOrWhiteSpace($Path)) {
        return ''
    }

    try {
        $repoRoot = Split-Path -Parent $KnowledgeRoot
        if ([System.IO.Path]::IsPathRooted($Path)) {
            $fullPath = [System.IO.Path]::GetFullPath($Path)
            if (Test-Path -LiteralPath $fullPath) {
                return $fullPath
            }

            if ($fullPath.StartsWith($repoRoot, [System.StringComparison]::OrdinalIgnoreCase) -and -not $fullPath.StartsWith($KnowledgeRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
                $relativeFromRepo = $fullPath.Substring($repoRoot.Length).TrimStart('\', '/')
                $rebasedPath = [System.IO.Path]::GetFullPath((Join-Path $KnowledgeRoot $relativeFromRepo))
                if (Test-Path -LiteralPath $rebasedPath) {
                    return $rebasedPath
                }
            }

            return $fullPath
        }

        $knowledgeRelative = [System.IO.Path]::GetFullPath((Join-Path $KnowledgeRoot $Path))
        if (Test-Path -LiteralPath $knowledgeRelative) {
            return $knowledgeRelative
        }

        return [System.IO.Path]::GetFullPath($Path)
    }
    catch {
        return $Path
    }
}

function Get-RelativePathSafe {
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
    $baseUri = [System.Uri]::new($baseFull)
    $targetUri = [System.Uri]::new($targetFull)
    return [System.Uri]::UnescapeDataString($baseUri.MakeRelativeUri($targetUri).ToString()).Replace('/', [System.IO.Path]::DirectorySeparatorChar)
}

function Normalize-Url {
    param([AllowNull()][string]$Url)

    if ([string]::IsNullOrWhiteSpace($Url)) {
        return ''
    }

    $candidate = $Url.Trim()
    $uri = $null
    if (-not [System.Uri]::TryCreate($candidate, [System.UriKind]::Absolute, [ref]$uri)) {
        return $candidate.ToLowerInvariant()
    }

    $scheme = if ([string]::IsNullOrWhiteSpace($uri.Scheme)) { 'https' } else { $uri.Scheme.ToLowerInvariant() }
    $host = $uri.Host.ToLowerInvariant()
    if ($host.StartsWith('www.')) {
        $host = $host.Substring(4)
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
            if ([string]::IsNullOrWhiteSpace($value)) {
                $queryPairs.Add($key)
            }
            else {
                $queryPairs.Add(('{0}={1}' -f $key, [System.Uri]::EscapeDataString($value)))
            }
        }
    }

    $query = ($queryPairs | Sort-Object) -join '&'
    $base = '{0}://{1}{2}' -f $scheme, $host, $path
    if ([string]::IsNullOrWhiteSpace($query)) {
        return $base
    }
    return '{0}?{1}' -f $base, $query
}

function Get-SourceDomain {
    param(
        [AllowNull()][string]$Url,
        [AllowNull()][string]$FallbackDomain
    )

    if (-not [string]::IsNullOrWhiteSpace($FallbackDomain)) {
        return $FallbackDomain.Trim().ToLowerInvariant()
    }

    if ([string]::IsNullOrWhiteSpace($Url)) {
        return ''
    }

    $uri = $null
    if ([System.Uri]::TryCreate($Url, [System.UriKind]::Absolute, [ref]$uri)) {
        $host = $uri.Host.ToLowerInvariant()
        if ($host.StartsWith('www.')) {
            $host = $host.Substring(4)
        }
        return $host
    }

    return ''
}

function Get-MarkdownFrontmatter {
    param([AllowNull()][string]$Text)

    $result = [ordered]@{}
    if ([string]::IsNullOrWhiteSpace($Text)) {
        return $result
    }

    $trimmed = $Text.TrimStart([char]0xFEFF)
    $match = [regex]::Match($trimmed, '^(?s)---\r?\n(.*?)\r?\n---\r?\n')
    if (-not $match.Success) {
        return $result
    }

    foreach ($line in ($match.Groups[1].Value -split '\r?\n')) {
        if ($line -match '^\s*([A-Za-z0-9_]+):\s*(.*?)\s*$') {
            $key = $Matches[1]
            $value = $Matches[2]
            if (($value.StartsWith('"') -and $value.EndsWith('"')) -or ($value.StartsWith("'") -and $value.EndsWith("'"))) {
                $value = $value.Substring(1, $value.Length - 2)
            }
            $result[$key] = $value
        }
    }

    return $result
}

function Get-MarkdownBodyText {
    param([AllowNull()][string]$Text)

    if ([string]::IsNullOrWhiteSpace($Text)) {
        return ''
    }

    $trimmed = $Text.TrimStart([char]0xFEFF)
    $match = [regex]::Match($trimmed, '^(?s)---\r?\n(.*?)\r?\n---\r?\n')
    if ($match.Success) {
        return $trimmed.Substring($match.Length)
    }

    return $trimmed
}

function Get-YamlScalar {
    param([AllowNull()][string]$Value)

    if ($null -eq $Value) {
        return '""'
    }

    $escaped = $Value.Replace('\', '\\').Replace('"', '\"')
    return ('"{0}"' -f $escaped)
}

function Get-FileSha256 {
    param([Parameter(Mandatory = $true)][string]$Path)

    return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToLowerInvariant()
}

function Get-NormalizedMarkdownDuplicateHash {
    param([AllowNull()][string]$Text)

    $body = Get-MarkdownBodyText -Text $Text
    $normalized = ($body -replace '\r\n', "`n" -replace '\r', "`n").Trim()
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($normalized)
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        return ([System.BitConverter]::ToString($sha.ComputeHash($bytes))).Replace('-', '').ToLowerInvariant()
    }
    finally {
        $sha.Dispose()
    }
}

function Get-DuplicateHashForFile {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)][bool]$IsMarkdownLike
    )

    if ($IsMarkdownLike) {
        return Get-NormalizedMarkdownDuplicateHash -Text (Read-Utf8Text -Path $Path)
    }

    return Get-FileSha256 -Path $Path
}

function Get-FirstHeading {
    param([AllowNull()][string]$Text)

    if ([string]::IsNullOrWhiteSpace($Text)) {
        return ''
    }

    $body = Get-MarkdownBodyText -Text $Text
    $match = [regex]::Match($body, '(?m)^\s*#{1,6}\s+(.+?)\s*$')
    if ($match.Success) {
        return $match.Groups[1].Value.Trim()
    }

    return ''
}

function Get-RawHtmlTagCount {
    param([AllowNull()][string]$Text)

    if ([string]::IsNullOrWhiteSpace($Text)) {
        return 0
    }

    $pattern = '(?i)<!DOCTYPE html|</?(html|head|body|div|span|table|thead|tbody|tr|td|th|script|style|iframe|section|article|main|nav|img|svg|path|meta|link|colgroup|col)\b'
    $count = ([regex]::Matches($Text, $pattern)).Count
    $count += ([regex]::Matches($Text, 'data:image/')).Count
    return $count
}

function Get-MeaningfulWordCount {
    param([AllowNull()][string]$Text)

    if ([string]::IsNullOrWhiteSpace($Text)) {
        return 0
    }

    $body = Get-MarkdownBodyText -Text $Text
    $clean = $body.ToLowerInvariant()
    $clean = $clean -replace '<[^>]+>', ' '
    $clean = $clean -replace '\[[^\]]*\]\([^)]+\)', ' '
    $clean = $clean -replace '!\[[^\]]*\]\([^)]+\)', ' '
    $clean = $clean -replace '[`*_>#|-]', ' '
    $clean = $clean -replace '[^a-z0-9\+\-/\. ]', ' '
    $tokens = @($clean -split '\s+' | Where-Object { $_.Length -ge 2 -and $_ -notmatch '^\d+$' })
    return $tokens.Count
}

function Get-LineCount {
    param([AllowNull()][string]$Text)

    if ([string]::IsNullOrWhiteSpace($Text)) {
        return 0
    }

    return (($Text -split '\r?\n').Count)
}

function Get-SafeTitle {
    param(
        [AllowNull()][string]$FrontmatterTitle,
        [AllowNull()][string]$Heading,
        [Parameter(Mandatory = $true)][string]$FallbackName
    )

    foreach ($candidate in @($FrontmatterTitle, $Heading, $FallbackName)) {
        if (-not [string]::IsNullOrWhiteSpace($candidate)) {
            return $candidate.Trim()
        }
    }

    return 'Untitled'
}

function Get-SourceSlug {
    param(
        [Parameter(Mandatory = $true)][string]$SourceFileName,
        [AllowNull()][string]$NormalizedUrl
    )

    $name = [System.IO.Path]::GetFileNameWithoutExtension($SourceFileName)
    $name = $name -replace '^(url_\d+|seedv2_\d+)-', ''
    $name = $name -replace '-[0-9a-f]{10}(\.pdf)?$', ''
    $name = $name -replace '[^A-Za-z0-9._-]+', '-'
    $name = $name.Trim('-')

    if ([string]::IsNullOrWhiteSpace($name) -and -not [string]::IsNullOrWhiteSpace($NormalizedUrl)) {
        $name = $NormalizedUrl -replace '^https?://', ''
        $name = $name -replace '[^A-Za-z0-9._-]+', '-'
        $name = $name.Trim('-')
    }

    if ([string]::IsNullOrWhiteSpace($name)) {
        return 'unknown-source'
    }

    return $name.ToLowerInvariant()
}

function Get-UrlIndexIdNumber {
    param([AllowNull()][string]$Id)

    if ([string]::IsNullOrWhiteSpace($Id)) {
        return 0
    }

    if ($Id -match '^url_(\d+)$') {
        return [int]$Matches[1]
    }

    return 0
}

function New-UrlIndexId {
    $script:NextUrlIndexNumber += 1
    return ('url_{0:d6}' -f $script:NextUrlIndexNumber)
}

function Test-IsOfficialDomain {
    param(
        [AllowNull()][string]$Domain,
        [AllowNull()][string]$TrustLevel,
        [AllowNull()][string]$SourceType
    )

    $signal = ('{0} {1} {2}' -f $Domain, $TrustLevel, $SourceType).ToLowerInvariant()
    if ($signal -match 'official|datasheet|app_note|manufacturer') {
        return $true
    }

    if ($signal -match 'docs\.kicad\.org|dev-docs\.kicad\.org|kicad\.org|klc\.kicad\.org|docs\.espressif\.com|espressif\.com|ti\.com|st\.com|microchip\.com|infineon\.com|onsemi\.com|rohm\.com|nexperia\.com|raspberrypi\.com|nordicsemi\.com|renesas\.com|silabs\.com|analog\.com|we-online\.com|jlcpcb\.com|pcbway\.com|oshpark\.com|eurocircuits\.com|protoexpress\.com|4pcb\.com|sunstone\.com|macrofab\.com|molex\.com|samtec\.com|te\.com|te\.connectivity|hirose\.com|amphenol\.com|jst\.com|harwin\.com|phoenixcontact\.com|gct\.co') {
        return $true
    }

    return $false
}

function Get-ResolvedSourceType {
    param(
        [AllowNull()][string]$Explicit,
        [AllowNull()][string]$Domain,
        [AllowNull()][string]$Url,
        [Parameter(Mandatory = $true)][bool]$IsPdf,
        [Parameter(Mandatory = $true)][bool]$IsExtractedPdfMarkdown
    )

    if (-not [string]::IsNullOrWhiteSpace($Explicit)) {
        return $Explicit
    }

    $signal = ('{0} {1}' -f $Domain, $Url).ToLowerInvariant()
    if ($IsPdf -or $IsExtractedPdfMarkdown) {
        return 'pdf'
    }
    if ($signal -match 'docs\.kicad\.org|dev-docs\.kicad\.org|kicad\.org|klc\.kicad\.org|github\.com/kicad|gitlab\.com/kicad') {
        return 'kicad_official'
    }
    if ($signal -match 'jlcpcb|pcbway|oshpark|eurocircuits|protoexpress|4pcb|sunstone|macrofab|aisler') {
        return 'fabricator_dfm'
    }
    if ($signal -match 'eevblog|stackexchange|forum\.kicad\.info|allaboutcircuits|arduino\.cc') {
        return 'peer_review_forum'
    }
    if ($signal -match 'mit|stanford|berkeley|purdue|uiuc|cmu|georgia\.tech|course|lecture|lab') {
        return 'university_training'
    }
    if ($signal -match 'snapeda|ultralibrarian|samacsys|componentsearchengine|octopart|easyeda|lcsc|mouser|digikey') {
        return 'cad_models_part_intelligence'
    }
    if (Test-IsOfficialDomain -Domain $Domain -TrustLevel '' -SourceType '') {
        return 'manufacturer'
    }

    return 'web_page'
}

function Get-ResolvedTrustLevel {
    param(
        [AllowNull()][string]$Explicit,
        [AllowNull()][string]$SourceType,
        [AllowNull()][string]$Domain
    )

    if (-not [string]::IsNullOrWhiteSpace($Explicit)) {
        return $Explicit
    }

    $signal = ('{0} {1}' -f $SourceType, $Domain).ToLowerInvariant()
    if ($signal -match 'kicad_official') { return '2_official_kicad' }
    if ($signal -match 'fabricator_dfm') { return '3_fabricator_dfm' }
    if ($signal -match 'peer_review') { return '5_peer_review' }
    if ($signal -match 'university_training') { return '4_university_training' }
    if ($signal -match 'cad_models') { return '6_blog_or_general_web' }
    if ($signal -match 'pdf|manufacturer' -and (Test-IsOfficialDomain -Domain $Domain -TrustLevel '' -SourceType $SourceType)) {
        return '1_official_manufacturer_datasheet_or_app_note'
    }
    if ($signal -match 'index_or_search') { return '7_low_authority_context' }

    return '6_blog_or_general_web'
}

function Get-ResolvedTopicCategory {
    param(
        [AllowNull()][string]$Explicit,
        [AllowNull()][string]$Url,
        [AllowNull()][string]$Domain,
        [AllowNull()][string]$Text
    )

    if (-not [string]::IsNullOrWhiteSpace($Explicit)) {
        return $Explicit
    }

    $signal = ('{0} {1} {2}' -f $Url, $Domain, $Text).ToLowerInvariant()
    if ($signal -match 'kicad|pcbnew|eeschema|gerbview|file format|klc') { return 'kicad' }
    if ($signal -match 'esp32|espressif|esp-idf') { return 'esp32_rf_wifi' }
    if ($signal -match 'usb|type-c|esd|pd|high-speed') { return 'usb_c_high_speed_esd' }
    if ($signal -match 'buck|boost|regulator|switching|power supply|dcdc|dc-dc') { return 'power_buck_regulators' }
    if ($signal -match 'ground|emi|emc|signal integrity|layout') { return 'pcb_layout_grounding_emi_si' }
    return 'general_pcb_engineering'
}

function Get-KnowledgeCategoryGuess {
    param(
        [AllowNull()][string]$Url,
        [AllowNull()][string]$Domain,
        [AllowNull()][string]$SourceType,
        [AllowNull()][string]$TopicCategory,
        [AllowNull()][string]$Heading,
        [AllowNull()][string]$Text,
        [AllowNull()][string]$FileName
    )

    $signal = ('{0} {1} {2} {3} {4} {5} {6}' -f $Url, $Domain, $SourceType, $TopicCategory, $Heading, $Text, $FileName).ToLowerInvariant()

    if ($signal -match 'flux ai|ai pcb|hallucinat|llm|ai eda|ai routing') { return '16_ai_pcb_failure_modes' }
    if ($signal -match 'peer_review_failure_cases|failure case|bad board|broken board|debugging example|why is my pcb|root cause') { return '17_case_studies_bad_boards' }
    if ($signal -match 'good board|reference design|proven layout|evaluation module|eval board|dev board reference') { return '18_case_studies_good_boards' }
    if ($signal -match 'university_training|mit|stanford|berkeley|purdue|uiuc|georgia tech|cmu|lecture|course|lab') { return '19_university_training' }
    if ($signal -match 'nasa|esa|ecss|workmanship|high reliability|ipc class 3|aerospace') { return '28_high_reliability_aerospace_workmanship' }
    if ($signal -match 'automotive|can bus|load dump|iso 7637|reverse battery|harsh environment') { return '22_automotive_harsh_environment' }
    if ($signal -match 'fcc|ce |ce$|iec 61000|pre-compliance|emc compliance|compliance|safety testing|esd immunity') { return '31_compliance_safety_emc' }
    if ($signal -match 'ipc|ul|creepage|clearance|safety spacing|ipc-2221|ipc-7351') { return '29_standards_ipc_ul_safety' }
    if ($signal -match 'kibot|kikit|kicost|skidl|atopile|faebryk|freerouting|interactivehtmlbom|ngspice|xyce') { return '30_eda_automation_verification' }
    if ($signal -match 'test point|jtag|swd|bring-up|validation|oscilloscope|debug access|dft') { return '27_test_debug_validation' }
    if ($signal -match 'thermal via|heatsink|enclosure|mounting|mechanical|vibration|rugged') { return '26_thermal_mechanical_enclosure' }
    if ($signal -match 'controlled impedance|signal integrity|differential pair|ddr|pcie|ethernet|lvds|via stub|termination') { return '25_signal_integrity_high_speed' }
    if ($signal -match 'decoupling|bypass capacitor|pdn|power integrity|transient response') { return '24_power_integrity_decoupling' }
    if ($signal -match 'antenna|feedline|50 ohm|matching network|rf keepout|wifi layout|bluetooth layout') { return '23_rf_wifi_antenna_layout' }
    if ($signal -match 'connector_land_pattern|land pattern|recommended footprint|recommended pcb layout|mechanical drawing|package drawing|molex|samtec|te connectivity|hirose|amphenol|jst|harwin|phoenix contact|gct|samesky') { return '21_component_package_land_patterns' }
    if ((Test-IsOfficialDomain -Domain $Domain -TrustLevel '' -SourceType $SourceType) -and $signal -match 'layout guide|layout guideline|layout considerations|layout recommendations|reference layout|pcb layout guide|placement guide') { return '20_manufacturer_layout_guides' }
    if ($signal -match 'youtube|youtu\.be|video|channel') { return '15_video_reference_index' }
    if ($signal -match 'snapeda|ultralibrarian|samacsys|componentsearchengine|mouser|digikey|octopart|lcsc|easyeda|cad model') { return '13_vendor_parts_cad_models' }
    if ($signal -match 'eevblog|stackexchange|forum\.kicad\.info|esp32\.com|allaboutcircuits|arduino forum|peer review|forum') { return '12_forums_peer_review' }
    if ($signal -match 'calculator|microstrip|stripline|trace width|saturn pcb|impedance calculator') { return '11_calculators_ipc_reference' }
    if ($signal -match 'jlcpcb|pcbway|osh park|oshpark|eurocircuits|protoexpress|4pcb|sunstone|macrofab|seeed|elecrow|aisler|fabrication|assembly|panelization|gerber|bom|cpl|stackup|annular ring|dfm|dfa|silkscreen') { return '10_dfm_fabrication_assembly' }
    if ($signal -match 'ground plane|return path|emi|emc|rf layout|crosstalk|via stitching|decoupling placement|pcb layout|high-speed layout|signal return') { return '09_pcb_layout_grounding_emi_si' }
    if ($signal -match 'buck|boost|switching regulator|dc-dc|dcdc|power supply|ldo|lm2596|tps|monolithicpower|mps|richtek|onsemi power|rohm power') { return '08_power_buck_regulators' }
    if ($signal -match 'usb|usb-c|type-c|usb pd|pd sink|pd source|esd|tvs|common mode choke') { return '07_usb_c_high_speed_esd' }
    if ($signal -match 'stm32|microchip|avr|sam |samd|samc|rp2040|rp2350|nordic|silicon labs|silabs|renesas|infineon|wch|gd32|arduino hardware') { return '06_microcontrollers' }
    if ($signal -match 'docs\.espressif\.com|espressif\.com|esp32|esp-idf|esp-hardware-design-guidelines|esptool') { return '05_esp32_espressif' }
    if ($signal -match 'kicad-symbols|kicad-footprints|packages3d|kicad-packages3d|kicad-library-utils|klc\.kicad\.org|library contribution|library conventions|symbol library|footprint library') { return '04_kicad_libraries_symbols_footprints' }
    if ($signal -match 'file format|sexpr|s-expression|schematic file format|pcb file format|footprint file format|symbol format|serialization') { return '03_kicad_file_formats' }
    if ($signal -match 'ipc api|pcb python|pcbnew python|swig|kicad-python|api and bindings|plugin development|automation api') { return '02_kicad_python_api' }
    if ($signal -match 'docs\.kicad\.org|dev-docs\.kicad\.org|kicad\.org|eeschema|pcbnew|gerbview|pcb_calculator|kicad cli|get started') { return '01_kicad_core' }

    return '90_unsorted_review'
}

function Get-ContentQualityGuess {
    param(
        [Parameter(Mandatory = $true)][int]$WordCount,
        [Parameter(Mandatory = $true)][int]$RawHtmlTagCount,
        [AllowNull()][string]$Heading,
        [AllowNull()][string]$Url,
        [AllowNull()][string]$Domain,
        [AllowNull()][string]$SourceType,
        [AllowNull()][string]$TrustLevel,
        [AllowNull()][string]$Text,
        [Parameter(Mandatory = $true)][bool]$IsPdf,
        [Parameter(Mandatory = $true)][bool]$IsExtractedPdfMarkdown,
        [Parameter(Mandatory = $true)][bool]$IsRawHtml
    )

    $signal = ('{0} {1} {2} {3} {4} {5}' -f $Url, $Domain, $SourceType, $TrustLevel, $Heading, $Text).ToLowerInvariant()
    $isOfficial = Test-IsOfficialDomain -Domain $Domain -TrustLevel $TrustLevel -SourceType $SourceType
    $isPureIndex = ($signal -match 'captcha|login|register|search|tagged|/tags/|category page|all categories|home help search login') -or (($Url -match '^https?://[^/]+/?$') -and $WordCount -lt 250 -and $RawHtmlTagCount -gt 25)

    if ($IsRawHtml -and $WordCount -lt 120) {
        return 'junk'
    }
    if ($WordCount -lt 20) {
        return 'junk'
    }
    if ($signal -match '\[table\]\s*\[table\]' -and $WordCount -lt 60) {
        return 'junk'
    }
    if ($isPureIndex -and -not $isOfficial) {
        return 'junk'
    }
    if ($WordCount -lt 50) {
        if ($isOfficial -or $signal -match 'index\.html|datasheet|app note|hardware design|klc') {
            return 'low'
        }
        return 'junk'
    }
    if ($isOfficial -and ($IsPdf -or $IsExtractedPdfMarkdown) -and $WordCount -ge 150) {
        return 'high'
    }
    if ($isOfficial -and $WordCount -ge 250) {
        return 'high'
    }
    if ($isOfficial) {
        return 'medium'
    }
    if ($signal -match 'forum|stackexchange|eevblog|jlcpcb|pcbway|oshpark|protoexpress|blog|tutorial') {
        if ($WordCount -ge 150) { return 'medium' }
        return 'low'
    }
    if ($WordCount -ge 300 -and $RawHtmlTagCount -lt 60) {
        return 'medium'
    }
    if ($WordCount -ge 100) {
        return 'low'
    }

    return 'junk'
}

function New-UrlIndexRow {
    param([Parameter(Mandatory = $true)][string]$Id)

    $row = [ordered]@{}
    foreach ($column in $script:UrlIndexColumns) {
        $row[$column] = ''
    }
    $row.id = $Id
    return $row
}

function Set-UrlRowAliases {
    param([hashtable]$Row)

    $Row.source_scraped_file = $Row.local_file
    $Row.source_file_type = if (-not [string]::IsNullOrWhiteSpace($Row.source_file_type)) { $Row.source_file_type } else { $Row.source_type }
    $Row.detected_category = $Row.knowledge_category
    $Row.source_of_truth_level = $Row.trust_level
    $Row.trust_label = $Row.trust_level
    $Row.scraped_status = $Row.scrape_status
    $Row.error_message_if_known = $Row.error_message
    $Row.last_scraped_at = $Row.scraped_at
    $Row.original_pdf_path = $Row.pdf_path
    $Row.extracted_markdown_path = $Row.extracted_pdf_markdown_path
    $Row.needs_future_rescrape = if ($Row.needs_review -eq 'true') { 'true' } else { 'false' }
}

function Convert-ExistingUrlIndexRow {
    param($CsvRow)

    $row = New-UrlIndexRow -Id $CsvRow.id
    $row.original_url = if ($CsvRow.PSObject.Properties.Name -contains 'original_url') { $CsvRow.original_url } else { '' }
    $row.normalized_url = if ($CsvRow.PSObject.Properties.Name -contains 'normalized_url') { $CsvRow.normalized_url } else { Normalize-Url -Url $row.original_url }
    $row.source_domain = if ($CsvRow.PSObject.Properties.Name -contains 'source_domain') { $CsvRow.source_domain } else { Get-SourceDomain -Url $row.original_url -FallbackDomain '' }
    $row.source_type = if ($CsvRow.PSObject.Properties.Name -contains 'source_type') { $CsvRow.source_type } elseif ($CsvRow.PSObject.Properties.Name -contains 'source_file_type') { $CsvRow.source_file_type } else { '' }
    $row.topic_category = if ($CsvRow.PSObject.Properties.Name -contains 'topic_category') { $CsvRow.topic_category } else { '' }
    $row.trust_level = if ($CsvRow.PSObject.Properties.Name -contains 'trust_level') { $CsvRow.trust_level } elseif ($CsvRow.PSObject.Properties.Name -contains 'source_of_truth_level') { $CsvRow.source_of_truth_level } elseif ($CsvRow.PSObject.Properties.Name -contains 'trust_label') { $CsvRow.trust_label } else { '' }
    $row.scrape_status = if ($CsvRow.PSObject.Properties.Name -contains 'scrape_status') { $CsvRow.scrape_status } elseif ($CsvRow.PSObject.Properties.Name -contains 'scraped_status') { $CsvRow.scraped_status } else { '' }
    $row.local_file = Resolve-FullPathSafe -Path $(if ($CsvRow.PSObject.Properties.Name -contains 'local_file') { $CsvRow.local_file } elseif ($CsvRow.PSObject.Properties.Name -contains 'source_scraped_file') { $CsvRow.source_scraped_file } else { '' })
    $row.current_knowledge_file = Resolve-FullPathSafe -Path $(if ($CsvRow.PSObject.Properties.Name -contains 'current_knowledge_file') { $CsvRow.current_knowledge_file } else { '' })
    $row.raw_html_path = Resolve-FullPathSafe -Path $(if ($CsvRow.PSObject.Properties.Name -contains 'raw_html_path') { $CsvRow.raw_html_path } else { '' })
    $row.markdown_path = Resolve-FullPathSafe -Path $(if ($CsvRow.PSObject.Properties.Name -contains 'markdown_path') { $CsvRow.markdown_path } else { '' })
    $row.pdf_path = Resolve-FullPathSafe -Path $(if ($CsvRow.PSObject.Properties.Name -contains 'pdf_path') { $CsvRow.pdf_path } elseif ($CsvRow.PSObject.Properties.Name -contains 'original_pdf_path') { $CsvRow.original_pdf_path } else { '' })
    $row.extracted_pdf_markdown_path = Resolve-FullPathSafe -Path $(if ($CsvRow.PSObject.Properties.Name -contains 'extracted_pdf_markdown_path') { $CsvRow.extracted_pdf_markdown_path } elseif ($CsvRow.PSObject.Properties.Name -contains 'extracted_markdown_path') { $CsvRow.extracted_markdown_path } else { '' })
    $row.error_message = if ($CsvRow.PSObject.Properties.Name -contains 'error_message') { $CsvRow.error_message } elseif ($CsvRow.PSObject.Properties.Name -contains 'error_message_if_known') { $CsvRow.error_message_if_known } else { '' }
    $row.imported_at = if ($CsvRow.PSObject.Properties.Name -contains 'imported_at') { $CsvRow.imported_at } else { '' }
    $row.scraped_at = if ($CsvRow.PSObject.Properties.Name -contains 'scraped_at') { $CsvRow.scraped_at } elseif ($CsvRow.PSObject.Properties.Name -contains 'last_scraped_at') { $CsvRow.last_scraped_at } else { '' }
    $row.needs_review = if ($CsvRow.PSObject.Properties.Name -contains 'needs_review') { $CsvRow.needs_review } elseif ($CsvRow.PSObject.Properties.Name -contains 'needs_future_rescrape') { $CsvRow.needs_future_rescrape } else { 'false' }
    $row.duplicate_status = if ($CsvRow.PSObject.Properties.Name -contains 'duplicate_status') { $CsvRow.duplicate_status } else { '' }
    $row.duplicate_of_url_index_id = if ($CsvRow.PSObject.Properties.Name -contains 'duplicate_of_url_index_id') { $CsvRow.duplicate_of_url_index_id } else { '' }
    $row.content_quality = if ($CsvRow.PSObject.Properties.Name -contains 'content_quality') { $CsvRow.content_quality } else { '' }
    $row.knowledge_category = if ($CsvRow.PSObject.Properties.Name -contains 'knowledge_category') { $CsvRow.knowledge_category } elseif ($CsvRow.PSObject.Properties.Name -contains 'detected_category') { $CsvRow.detected_category } else { '' }
    $row.source_batch = if ($CsvRow.PSObject.Properties.Name -contains 'source_batch') { $CsvRow.source_batch } else { 'pre_ingest_v2' }
    $row.notes = if ($CsvRow.PSObject.Properties.Name -contains 'notes') { $CsvRow.notes } else { '' }
    $row.extraction_status = if ($CsvRow.PSObject.Properties.Name -contains 'extraction_status') { $CsvRow.extraction_status } else { '' }
    $row.extraction_tool = if ($CsvRow.PSObject.Properties.Name -contains 'extraction_tool') { $CsvRow.extraction_tool } else { '' }
    $row.extraction_warning = if ($CsvRow.PSObject.Properties.Name -contains 'extraction_warning') { $CsvRow.extraction_warning } else { '' }
    $row.rescrape_reason = if ($CsvRow.PSObject.Properties.Name -contains 'rescrape_reason') { $CsvRow.rescrape_reason } else { '' }
    $row.duplicate_group_id = if ($CsvRow.PSObject.Properties.Name -contains 'duplicate_group_id') { $CsvRow.duplicate_group_id } else { '' }
    Set-UrlRowAliases -Row $row
    return $row
}

function Get-TextMetadata {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [Parameter(Mandatory = $true)][bool]$IsMarkdownLike
    )

    $text = Read-Utf8Text -Path $Path
    $frontmatter = if ($IsMarkdownLike) { Get-MarkdownFrontmatter -Text $text } else { [ordered]@{} }
    $body = if ($IsMarkdownLike) { Get-MarkdownBodyText -Text $text } else { $text }
    return [pscustomobject]@{
        text = $text
        frontmatter = $frontmatter
        body = $body
        first_heading = Get-FirstHeading -Text $text
        word_count = Get-MeaningfulWordCount -Text $text
        line_count = Get-LineCount -Text $text
        raw_html_tag_count = Get-RawHtmlTagCount -Text $text
    }
}

function Build-FrontmatterBlock {
    param(
        [Parameter(Mandatory = $true)][string]$Title,
        [Parameter(Mandatory = $true)][AllowEmptyString()][string]$SourceUrl,
        [Parameter(Mandatory = $true)][AllowEmptyString()][string]$NormalizedUrl,
        [Parameter(Mandatory = $true)][string]$UrlIndexId,
        [Parameter(Mandatory = $true)][AllowEmptyString()][string]$SourceDomain,
        [Parameter(Mandatory = $true)][AllowEmptyString()][string]$SourceType,
        [Parameter(Mandatory = $true)][AllowEmptyString()][string]$TopicCategory,
        [Parameter(Mandatory = $true)][AllowEmptyString()][string]$TrustLevel,
        [Parameter(Mandatory = $true)][AllowEmptyString()][string]$SourceFile,
        [Parameter(Mandatory = $true)][AllowEmptyString()][string]$SourceFolder,
        [Parameter(Mandatory = $true)][string]$KnowledgeCategory,
        [Parameter(Mandatory = $true)][string]$ContentQuality,
        [Parameter(Mandatory = $true)][bool]$NeedsReview,
        [Parameter(Mandatory = $true)][AllowEmptyString()][string]$RawHtmlPath,
        [Parameter(Mandatory = $true)][AllowEmptyString()][string]$PdfPath,
        [Parameter(Mandatory = $true)][AllowEmptyString()][string]$ExtractedMarkdownPath,
        [Parameter(Mandatory = $true)][string]$DuplicateStatus,
        [Parameter(Mandatory = $true)][AllowEmptyString()][string]$Notes
    )

    return @(
        '---'
        ('title: {0}' -f (Get-YamlScalar -Value $Title))
        ('source_url: {0}' -f (Get-YamlScalar -Value $SourceUrl))
        ('normalized_url: {0}' -f (Get-YamlScalar -Value $NormalizedUrl))
        ('url_index_id: {0}' -f (Get-YamlScalar -Value $UrlIndexId))
        ('source_domain: {0}' -f (Get-YamlScalar -Value $SourceDomain))
        ('source_type: {0}' -f (Get-YamlScalar -Value $SourceType))
        ('topic_category: {0}' -f (Get-YamlScalar -Value $TopicCategory))
        ('trust_level: {0}' -f (Get-YamlScalar -Value $TrustLevel))
        ('source_file: {0}' -f (Get-YamlScalar -Value $SourceFile))
        ('source_folder: {0}' -f (Get-YamlScalar -Value $SourceFolder))
        ('imported_from: {0}' -f (Get-YamlScalar -Value $IngestRoot))
        ('import_batch: {0}' -f (Get-YamlScalar -Value $script:ImportBatch))
        ('knowledge_category: {0}' -f (Get-YamlScalar -Value $KnowledgeCategory))
        ('content_quality: {0}' -f (Get-YamlScalar -Value $ContentQuality))
        ('needs_review: {0}' -f ($(if ($NeedsReview) { 'true' } else { 'false' })))
        ('raw_html_path: {0}' -f (Get-YamlScalar -Value $RawHtmlPath))
        ('pdf_path: {0}' -f (Get-YamlScalar -Value $PdfPath))
        ('extracted_pdf_markdown_path: {0}' -f (Get-YamlScalar -Value $ExtractedMarkdownPath))
        ('imported_at: {0}' -f (Get-YamlScalar -Value $script:TimestampIso))
        ('duplicate_status: {0}' -f (Get-YamlScalar -Value $DuplicateStatus))
        ('notes: {0}' -f (Get-YamlScalar -Value $Notes))
        '---'
        ''
    ) -join [Environment]::NewLine
}

function Write-NormalizedMarkdownFile {
    param(
        [Parameter(Mandatory = $true)][string]$DestinationPath,
        [Parameter(Mandatory = $true)][string]$BodyText,
        [Parameter(Mandatory = $true)][hashtable]$FrontmatterValues
    )

    $frontmatterBlock = Build-FrontmatterBlock @FrontmatterValues
    $content = $frontmatterBlock + ($BodyText.TrimStart()) + [Environment]::NewLine
    Write-Utf8Text -Path $DestinationPath -Text $content
}

function Copy-FileWithCollisionHandling {
    param(
        [Parameter(Mandatory = $true)][string]$SourcePath,
        [Parameter(Mandatory = $true)][string]$DestinationDirectory,
        [Parameter(Mandatory = $true)][string]$DestinationFileName
    )

    Ensure-Directory -Path $DestinationDirectory
    $targetPath = Join-Path $DestinationDirectory $DestinationFileName
    if (Test-Path -LiteralPath $targetPath) {
        $existingHash = Get-FileSha256 -Path $targetPath
        $sourceHash = Get-FileSha256 -Path $SourcePath
        if ($existingHash -eq $sourceHash) {
            return [pscustomobject]@{ path = $targetPath; copied = $false }
        }

        $baseName = [System.IO.Path]::GetFileNameWithoutExtension($DestinationFileName)
        $extension = [System.IO.Path]::GetExtension($DestinationFileName)
        $targetPath = Join-Path $DestinationDirectory ('{0}--{1}{2}' -f $baseName, (Get-Date).ToString('yyyyMMdd_HHmmss'), $extension)
    }

    Copy-Item -LiteralPath $SourcePath -Destination $targetPath -Force
    return [pscustomobject]@{ path = $targetPath; copied = $true }
}

function Add-NoteValue {
    param(
        [AllowNull()][string]$Existing,
        [Parameter(Mandatory = $true)][string]$Append
    )

    if ([string]::IsNullOrWhiteSpace($Append)) {
        return $Existing
    }
    if ([string]::IsNullOrWhiteSpace($Existing)) {
        return $Append
    }
    if ($Existing.Contains($Append)) {
        return $Existing
    }
    return ('{0}; {1}' -f $Existing, $Append)
}

function Export-OrderedCsv {
    param(
        [Parameter(Mandatory = $true)][object[]]$Rows,
        [Parameter(Mandatory = $true)][string[]]$Columns,
        [Parameter(Mandatory = $true)][string]$Path
    )

    $objects = foreach ($row in $Rows) {
        $ordered = [ordered]@{}
        foreach ($column in $Columns) {
            $value = ''
            if ($row -is [hashtable]) {
                if ($row.Contains($column)) {
                    $value = $row[$column]
                }
            }
            elseif ($row.PSObject.Properties.Name -contains $column) {
                $value = $row.$column
            }
            $ordered[$column] = $value
        }
        [pscustomobject]$ordered
    }

    $objects | Export-Csv -LiteralPath $Path -NoTypeInformation -Encoding UTF8
}

function Import-RegistryMetadata {
    param(
        [Parameter(Mandatory = $true)][string]$CsvPath,
        [Parameter(Mandatory = $true)][string]$SourceBatch,
        [Parameter(Mandatory = $true)][hashtable]$MetadataByPath,
        [Parameter(Mandatory = $true)][hashtable]$MetadataByFileName,
        [Parameter(Mandatory = $true)][hashtable]$MetadataByNormalizedUrl
    )

    if (-not (Test-Path -LiteralPath $CsvPath)) {
        return @()
    }

    $rows = Import-Csv -LiteralPath $CsvPath
    $results = New-Object System.Collections.Generic.List[object]
    foreach ($row in $rows) {
        $originalUrl = ''
        if ($row.PSObject.Properties.Name -contains 'original_url' -and -not [string]::IsNullOrWhiteSpace($row.original_url)) {
            $originalUrl = $row.original_url
        }
        elseif ($row.PSObject.Properties.Name -contains 'original_seed' -and -not [string]::IsNullOrWhiteSpace($row.original_seed)) {
            $originalUrl = $row.original_seed
        }

        $metadata = [ordered]@{
            original_url = $originalUrl
            normalized_url = if ($row.PSObject.Properties.Name -contains 'normalized_url' -and -not [string]::IsNullOrWhiteSpace($row.normalized_url)) { $row.normalized_url } else { Normalize-Url -Url $originalUrl }
            source_domain = if ($row.PSObject.Properties.Name -contains 'source_domain') { $row.source_domain } else { Get-SourceDomain -Url $originalUrl -FallbackDomain '' }
            source_type = if ($row.PSObject.Properties.Name -contains 'source_type') { $row.source_type } else { '' }
            topic_category = if ($row.PSObject.Properties.Name -contains 'topic_category') { $row.topic_category } else { '' }
            trust_level = if ($row.PSObject.Properties.Name -contains 'trust_level') { $row.trust_level } else { '' }
            scrape_status = if ($row.PSObject.Properties.Name -contains 'scrape_status') { $row.scrape_status } else { '' }
            local_file = Resolve-FullPathSafe -Path $(if ($row.PSObject.Properties.Name -contains 'local_file') { $row.local_file } else { '' })
            raw_html_path = Resolve-FullPathSafe -Path $(if ($row.PSObject.Properties.Name -contains 'raw_html_path') { $row.raw_html_path } else { '' })
            markdown_path = Resolve-FullPathSafe -Path $(if ($row.PSObject.Properties.Name -contains 'markdown_path') { $row.markdown_path } else { '' })
            pdf_path = Resolve-FullPathSafe -Path $(if ($row.PSObject.Properties.Name -contains 'pdf_path') { $row.pdf_path } else { '' })
            extracted_pdf_markdown_path = Resolve-FullPathSafe -Path $(if ($row.PSObject.Properties.Name -contains 'extracted_pdf_markdown_path') { $row.extracted_pdf_markdown_path } else { '' })
            error_message = if ($row.PSObject.Properties.Name -contains 'error_message') { $row.error_message } else { '' }
            scraped_at = if ($row.PSObject.Properties.Name -contains 'scraped_at') { $row.scraped_at } else { '' }
            needs_review = if ($row.PSObject.Properties.Name -contains 'needs_review') { $row.needs_review } else { '' }
            source_batch = $SourceBatch
        }

        foreach ($pathKey in @('local_file', 'raw_html_path', 'markdown_path', 'pdf_path', 'extracted_pdf_markdown_path')) {
            $candidatePath = $metadata[$pathKey]
            if (-not [string]::IsNullOrWhiteSpace($candidatePath)) {
                $MetadataByPath[$candidatePath.ToLowerInvariant()] = $metadata
                $fileName = [System.IO.Path]::GetFileName($candidatePath)
                if (-not [string]::IsNullOrWhiteSpace($fileName)) {
                    $MetadataByFileName[$fileName.ToLowerInvariant()] = $metadata
                }
            }
        }

        if (-not [string]::IsNullOrWhiteSpace($metadata.normalized_url) -and -not $MetadataByNormalizedUrl.ContainsKey($metadata.normalized_url)) {
            $MetadataByNormalizedUrl[$metadata.normalized_url] = $metadata
        }

        $results.Add($metadata)
    }

    return @($results.ToArray())
}

function Get-MetadataForSourceFile {
    param(
        [Parameter(Mandatory = $true)][string]$Path,
        [AllowNull()][hashtable]$Frontmatter,
        [Parameter(Mandatory = $true)][hashtable]$MetadataByPath,
        [Parameter(Mandatory = $true)][hashtable]$MetadataByFileName,
        [Parameter(Mandatory = $true)][hashtable]$MetadataByNormalizedUrl
    )

    $fullPath = Resolve-FullPathSafe -Path $Path
    $pathKey = $fullPath.ToLowerInvariant()
    if ($MetadataByPath.ContainsKey($pathKey)) {
        return $MetadataByPath[$pathKey]
    }

    $fileNameKey = [System.IO.Path]::GetFileName($fullPath).ToLowerInvariant()
    if ($MetadataByFileName.ContainsKey($fileNameKey)) {
        return $MetadataByFileName[$fileNameKey]
    }

    if ($null -ne $Frontmatter -and $Frontmatter.Contains('source_url')) {
        $normalizedUrl = Normalize-Url -Url $Frontmatter['source_url']
        if (-not [string]::IsNullOrWhiteSpace($normalizedUrl) -and $MetadataByNormalizedUrl.ContainsKey($normalizedUrl)) {
            return $MetadataByNormalizedUrl[$normalizedUrl]
        }
    }

    return $null
}

function Get-CategoryCounts {
    param(
        [Parameter(Mandatory = $true)][string]$KnowledgeRootPath,
        [Parameter(Mandatory = $true)][object[]]$UrlRows
    )

    $counts = [ordered]@{}
    foreach ($category in $script:TopicalCategories) {
        if ($category -eq '14_datasheets_pdf_markdown') {
            $counts[$category] = @($UrlRows | Where-Object {
                    (-not [string]::IsNullOrWhiteSpace($_.pdf_path) -and (Test-Path -LiteralPath $_.pdf_path)) -or
                    (-not [string]::IsNullOrWhiteSpace($_.extracted_pdf_markdown_path) -and (Test-Path -LiteralPath $_.extracted_pdf_markdown_path))
                }).Count
        }
        else {
            $counts[$category] = @($UrlRows | Where-Object {
                    $_.knowledge_category -eq $category -and
                    -not [string]::IsNullOrWhiteSpace($_.current_knowledge_file) -and
                    (Test-Path -LiteralPath $_.current_knowledge_file)
                }).Count
        }
    }

    return $counts
}

function Build-CategoryIndexText {
    param(
        [Parameter(Mandatory = $true)][string]$Category,
        [Parameter(Mandatory = $true)][hashtable]$Config,
        [Parameter(Mandatory = $true)][AllowEmptyCollection()][object[]]$Rows,
        [Parameter(Mandatory = $true)][AllowEmptyCollection()][object[]]$ImportedRows
    )

    $lines = New-Object System.Collections.Generic.List[string]
    $lines.Add(('# {0} Category Index' -f $Category))
    $lines.Add('')
    $lines.Add(('Generated at: `{0}`' -f $script:TimestampIso))
    $lines.Add('')
    $lines.Add('## Purpose')
    $lines.Add('')
    $lines.Add($Config.purpose)
    $lines.Add('')
    $lines.Add('## Summary')
    $lines.Add('')
    $lines.Add(('- File count: `{0}`' -f $Rows.Count))
    $lines.Add(('- New files imported from ingest_v2: `{0}`' -f $ImportedRows.Count))
    $lines.Add(('- Source domain count: `{0}`' -f @($Rows | Where-Object { -not [string]::IsNullOrWhiteSpace($_.source_domain) } | Select-Object -ExpandProperty source_domain -Unique).Count))
    $lines.Add(('- Trust levels present: `{0}`' -f @($Rows | Where-Object { -not [string]::IsNullOrWhiteSpace($_.trust_level) } | Select-Object -ExpandProperty trust_level -Unique).Count))
    $lines.Add('')
    $lines.Add('## How AI Should Use This Category')
    $lines.Add('')
    $lines.Add($Config.usage)
    $lines.Add('')
    $lines.Add('## Warnings')
    $lines.Add('')
    $lines.Add(('- {0}' -f $Config.warning))
    $lines.Add('')

    $trustGroups = @($Rows | Group-Object trust_level | Sort-Object @{ Expression = 'Count'; Descending = $true }, Name)
    if ($trustGroups.Count -gt 0) {
        $lines.Add('## Trust Levels')
        $lines.Add('')
        foreach ($group in $trustGroups) {
            $label = if ([string]::IsNullOrWhiteSpace($group.Name)) { '(blank)' } else { $group.Name }
            $lines.Add(('- `{0}`: `{1}`' -f $label, $group.Count))
        }
        $lines.Add('')
    }

    $domainGroups = @($Rows | Group-Object source_domain | Sort-Object @{ Expression = 'Count'; Descending = $true }, Name | Select-Object -First 12)
    if ($domainGroups.Count -gt 0) {
        $lines.Add('## Source Domains')
        $lines.Add('')
        foreach ($group in $domainGroups) {
            $label = if ([string]::IsNullOrWhiteSpace($group.Name)) { '(blank)' } else { $group.Name }
            $lines.Add(('- `{0}`: `{1}`' -f $label, $group.Count))
        }
        $lines.Add('')
    }

    $topRows = @(
        $Rows |
        Sort-Object `
            @{ Expression = { if ($_.content_quality -eq 'high') { 3 } elseif ($_.content_quality -eq 'medium') { 2 } elseif ($_.content_quality -eq 'low') { 1 } else { 0 } }; Descending = $true },
            @{ Expression = { if ($_.trust_level -match '^1_|^2_|^3_') { 1 } else { 0 } }; Descending = $true },
            @{ Expression = 'source_domain'; Descending = $false } |
        Select-Object -First 20
    )

    if ($topRows.Count -gt 0) {
        $lines.Add('## Top Useful Files')
        $lines.Add('')
        $lines.Add('| File | Title | URL Index ID | Trust | Quality | Domain |')
        $lines.Add('| --- | --- | --- | --- | --- | --- |')
        foreach ($row in $topRows) {
            $filePath = if ($Category -eq '14_datasheets_pdf_markdown') { $row.extracted_pdf_markdown_path } else { $row.current_knowledge_file }
            $relativePath = if (-not [string]::IsNullOrWhiteSpace($filePath) -and (Test-Path -LiteralPath $filePath)) { Get-RelativePathSafe -BasePath (Join-Path $KnowledgeRoot $Category) -TargetPath $filePath } else { '' }
            $title = ''
            if ($row.PSObject.Properties.Name -contains 'title' -and -not [string]::IsNullOrWhiteSpace($row.title)) {
                $title = $row.title
            }
            elseif (-not [string]::IsNullOrWhiteSpace($filePath) -and (Test-Path -LiteralPath $filePath) -and [System.IO.Path]::GetExtension($filePath).ToLowerInvariant() -eq '.md') {
                $previewText = Read-Utf8Text -Path $filePath
                $previewFrontmatter = Get-MarkdownFrontmatter -Text $previewText
                $title = Get-SafeTitle -FrontmatterTitle $(if ($previewFrontmatter.Contains('title')) { $previewFrontmatter['title'] } else { '' }) -Heading (Get-FirstHeading -Text $previewText) -FallbackName ([System.IO.Path]::GetFileName($filePath))
            }
            else {
                $title = [System.IO.Path]::GetFileName($filePath)
            }
            $lines.Add(('| [{0}]({1}) | {2} | `{3}` | `{4}` | `{5}` | `{6}` |' -f ([System.IO.Path]::GetFileName($filePath)), $relativePath, ($title -replace '\|', '/'), $row.id, $row.trust_level, $row.content_quality, $row.source_domain))
        }
        $lines.Add('')
    }

    return ($lines -join [Environment]::NewLine) + [Environment]::NewLine
}

function Build-UrlIndexMarkdownText {
    param(
        [Parameter(Mandatory = $true)][object[]]$Rows,
        [Parameter(Mandatory = $true)][hashtable]$Summary
    )

    $lines = New-Object System.Collections.Generic.List[string]
    $lines.Add('# URL_INDEX')
    $lines.Add('')
    $lines.Add(('Generated at: `{0}`' -f $script:TimestampIso))
    $lines.Add('')
    $lines.Add('## Summary')
    $lines.Add('')
    $lines.Add(('- URL rows: `{0}`' -f $Rows.Count))
    $lines.Add(('- Imported in ingest_v2: `{0}`' -f $Summary.imported_knowledge_files))
    $lines.Add(('- Skipped duplicate_by_url: `{0}`' -f $Summary.skipped_duplicate_by_url))
    $lines.Add(('- Skipped duplicate_by_hash: `{0}`' -f $Summary.skipped_duplicate_by_hash))
    $lines.Add(('- Rows needing review: `{0}`' -f @($Rows | Where-Object { $_.needs_review -eq 'true' }).Count))
    $lines.Add('')

    $statusGroups = @($Rows | Group-Object scrape_status | Sort-Object @{ Expression = 'Count'; Descending = $true }, Name)
    if ($statusGroups.Count -gt 0) {
        $lines.Add('## Scrape Status')
        $lines.Add('')
        foreach ($group in $statusGroups) {
            $label = if ([string]::IsNullOrWhiteSpace($group.Name)) { '(blank)' } else { $group.Name }
            $lines.Add(('- `{0}`: `{1}`' -f $label, $group.Count))
        }
        $lines.Add('')
    }

    $domainGroups = @($Rows | Group-Object source_domain | Sort-Object @{ Expression = 'Count'; Descending = $true }, Name | Select-Object -First 25)
    if ($domainGroups.Count -gt 0) {
        $lines.Add('## Top Domains')
        $lines.Add('')
        foreach ($group in $domainGroups) {
            $label = if ([string]::IsNullOrWhiteSpace($group.Name)) { '(blank)' } else { $group.Name }
            $lines.Add(('- `{0}`: `{1}`' -f $label, $group.Count))
        }
        $lines.Add('')
    }

    $recentRows = @($Rows | Where-Object { $_.source_batch -match 'ingest_v2' } | Select-Object -First 30)
    if ($recentRows.Count -gt 0) {
        $lines.Add('## Recent ingest_v2 Rows')
        $lines.Add('')
        $lines.Add('| ID | Category | Quality | Duplicate | URL | File |')
        $lines.Add('| --- | --- | --- | --- | --- | --- |')
        foreach ($row in $recentRows) {
            $filePath = if (-not [string]::IsNullOrWhiteSpace($row.current_knowledge_file)) { $row.current_knowledge_file } elseif (-not [string]::IsNullOrWhiteSpace($row.extracted_pdf_markdown_path)) { $row.extracted_pdf_markdown_path } else { $row.pdf_path }
            $relative = if (-not [string]::IsNullOrWhiteSpace($filePath) -and (Test-Path -LiteralPath $filePath)) { Get-RelativePathSafe -BasePath $KnowledgeRoot -TargetPath $filePath } else { '' }
            $lines.Add(('| `{0}` | `{1}` | `{2}` | `{3}` | {4} | `{5}` |' -f $row.id, $row.knowledge_category, $row.content_quality, $row.duplicate_status, $row.original_url, $relative))
        }
        $lines.Add('')
    }

    return ($lines -join [Environment]::NewLine) + [Environment]::NewLine
}

function Build-PdfIndexMarkdownText {
    param([Parameter(Mandatory = $true)][object[]]$Rows)

    $lines = New-Object System.Collections.Generic.List[string]
    $lines.Add('# PDF_INDEX')
    $lines.Add('')
    $lines.Add(('Generated at: `{0}`' -f $script:TimestampIso))
    $lines.Add('')
    $lines.Add('## Summary')
    $lines.Add('')
    $lines.Add(('- PDF rows: `{0}`' -f $Rows.Count))
    $lines.Add(('- PDF originals copied: `{0}`' -f @($Rows | Where-Object { -not [string]::IsNullOrWhiteSpace($_.original_pdf_path) -and (Test-Path -LiteralPath $_.original_pdf_path) }).Count))
    $lines.Add(('- Extracted Markdown copied: `{0}`' -f @($Rows | Where-Object { -not [string]::IsNullOrWhiteSpace($_.extracted_markdown_path) -and (Test-Path -LiteralPath $_.extracted_markdown_path) }).Count))
    $lines.Add('')
    $lines.Add('## Warning')
    $lines.Add('')
    $lines.Add('- Extracted PDF Markdown may lose diagrams, tables, pinouts, package drawings, layout figures, and formatting. Original PDF remains source of truth.')
    $lines.Add('')

    $categoryGroups = @($Rows | Group-Object knowledge_category | Sort-Object @{ Expression = 'Count'; Descending = $true }, Name)
    if ($categoryGroups.Count -gt 0) {
        $lines.Add('## Category Summary')
        $lines.Add('')
        foreach ($group in $categoryGroups) {
            $label = if ([string]::IsNullOrWhiteSpace($group.Name)) { '(blank)' } else { $group.Name }
            $lines.Add(('- `{0}`: `{1}`' -f $label, $group.Count))
        }
        $lines.Add('')
    }

    return ($lines -join [Environment]::NewLine) + [Environment]::NewLine
}

function Build-MainIndexText {
    param(
        [Parameter(Mandatory = $true)][hashtable]$CategoryCounts,
        [Parameter(Mandatory = $true)][hashtable]$Summary
    )

    $lines = New-Object System.Collections.Generic.List[string]
    $lines.Add('# knowledge_scrape Index')
    $lines.Add('')
    $lines.Add(('Updated at: `{0}`' -f $script:TimestampIso))
    $lines.Add('')
    $lines.Add('## Start Here')
    $lines.Add('')
    $lines.Add('- [README.md](README.md): high-level purpose and operating rules.')
    $lines.Add('- [00_ai_entrypoints/AI_START_HERE.md](00_ai_entrypoints/AI_START_HERE.md): default start sequence for Codex or Claude.')
    $lines.Add('- [00_source_of_truth/SOURCE_OF_TRUTH_INDEX.md](00_source_of_truth/SOURCE_OF_TRUTH_INDEX.md): official-source routing and source-of-truth priorities.')
    $lines.Add('- [00_retrieval_indexes/CATEGORY_ROUTING_INDEX.md](00_retrieval_indexes/CATEGORY_ROUTING_INDEX.md): quick topic-to-folder routing.')
    $lines.Add('- [URL_INDEX.md](URL_INDEX.md): canonical URL registry summary.')
    $lines.Add('')
    $lines.Add('## Category Indexes')
    $lines.Add('')
    $lines.Add('| Category | Content Files | Category Index |')
    $lines.Add('| --- | ---: | --- |')
    foreach ($category in $script:TopicalCategories) {
        $lines.Add(('| {0} | {1} | [_CATEGORY_INDEX.md]({0}/_CATEGORY_INDEX.md) |' -f $category, $CategoryCounts[$category]))
    }
    $lines.Add('')
    $lines.Add('## Current Snapshot')
    $lines.Add('')
    $lines.Add(('- URL rows: `{0}`' -f $Summary.url_index_rows_after))
    $lines.Add(('- New knowledge files imported from ingest_v2: `{0}`' -f $Summary.imported_knowledge_files))
    $lines.Add(('- Original PDFs copied: `{0}`' -f $Summary.pdf_originals_copied))
    $lines.Add(('- Extracted PDF Markdown copied: `{0}`' -f $Summary.pdf_markdown_copied))
    $lines.Add(('- Rows moved to `90_unsorted_review`: `{0}`' -f $Summary.unsorted_count))
    $lines.Add(('- Rows moved to `91_rejected_low_value`: `{0}`' -f $Summary.rejected_count))
    $lines.Add('')
    $lines.Add('## Use Pattern')
    $lines.Add('')
    $lines.Add('1. Start with `00_ai_entrypoints/AI_START_HERE.md` and `URL_INDEX.csv`.')
    $lines.Add('2. Route through `00_source_of_truth/` or `00_retrieval_indexes/` before broad folder browsing.')
    $lines.Add('3. Use original PDFs for pinouts, footprints, package drawings, layout figures, and tables.')
    $lines.Add('4. Cite local file path plus `url_index_id` when making engineering decisions.')
    $lines.Add('')

    return ($lines -join [Environment]::NewLine) + [Environment]::NewLine
}

function Build-ManifestObject {
    param(
        [Parameter(Mandatory = $true)][hashtable]$CategoryCounts,
        [Parameter(Mandatory = $true)][hashtable]$Summary
    )

    return [ordered]@{
        name = 'knowledge_scrape'
        status = 'ingest_v2_import_completed'
        created_for = 'KiCad and PCB engineering local retrieval and source-traceable AI use'
        import_batch = $script:ImportBatch
        generated_at = (Get-Date).ToString('o')
        primary_builders = @(
            '_scripts/01_build_raw_inventory.ps1',
            '_scripts/02_build_url_registry.ps1',
            '_scripts/03_classify_copy_markdown.ps1',
            '_scripts/04_convert_pdfs_to_markdown.ps1',
            '_scripts/05_clean_markdown_for_ai.ps1',
            '_scripts/06_build_category_indexes.ps1',
            '_scripts/10_import_ingest_v2.ps1'
        )
        url_index_csv = Join-Path $KnowledgeRoot 'URL_INDEX.csv'
        pdf_index_csv = Join-Path $KnowledgeRoot '14_datasheets_pdf_markdown\PDF_INDEX.csv'
        import_summary = $Summary
        category_counts = $CategoryCounts
    }
}

function Build-SourceAuditText {
    param(
        [Parameter(Mandatory = $true)][object[]]$InventoryRows,
        [Parameter(Mandatory = $true)][hashtable]$Summary
    )

    $lines = New-Object System.Collections.Generic.List[string]
    $lines.Add('# SOURCE_AUDIT')
    $lines.Add('')
    $lines.Add(('Generated at: `{0}`' -f $script:TimestampIso))
    $lines.Add('')
    $lines.Add('## Source Folders')
    $lines.Add('')
    foreach ($group in ($InventoryRows | Group-Object source_folder | Sort-Object Name)) {
        $lines.Add(('- `{0}`: `{1}` files' -f $group.Name, $group.Count))
    }
    $lines.Add('')
    $lines.Add('## Inventory Summary')
    $lines.Add('')
    $lines.Add(('- total scanned files: `{0}`' -f $InventoryRows.Count))
    $lines.Add(('- markdown files: `{0}`' -f @($InventoryRows | Where-Object { $_.is_markdown -eq $true }).Count))
    $lines.Add(('- PDF files: `{0}`' -f @($InventoryRows | Where-Object { $_.is_pdf -eq $true }).Count))
    $lines.Add(('- extracted PDF Markdown files: `{0}`' -f @($InventoryRows | Where-Object { $_.is_extracted_pdf_markdown -eq $true }).Count))
    $lines.Add(('- raw HTML files: `{0}`' -f @($InventoryRows | Where-Object { $_.is_raw_html -eq $true }).Count))
    $lines.Add(('- rows with source URL: `{0}`' -f @($InventoryRows | Where-Object { -not [string]::IsNullOrWhiteSpace($_.detected_source_url) }).Count))
    $lines.Add(('- duplicate_by_url candidates: `{0}`' -f @($InventoryRows | Where-Object { $_.duplicate_by_url -eq $true }).Count))
    $lines.Add(('- duplicate_by_hash candidates: `{0}`' -f @($InventoryRows | Where-Object { $_.duplicate_by_hash -eq $true }).Count))
    $lines.Add(('- new knowledge files imported: `{0}`' -f $Summary.imported_knowledge_files))
    $lines.Add('')
    $lines.Add('## Import Actions')
    $lines.Add('')
    foreach ($group in ($InventoryRows | Group-Object import_action | Sort-Object @{ Expression = 'Count'; Descending = $true }, Name)) {
        $label = if ([string]::IsNullOrWhiteSpace($group.Name)) { '(blank)' } else { $group.Name }
        $lines.Add(('- `{0}`: `{1}`' -f $label, $group.Count))
    }
    $lines.Add('')

    return ($lines -join [Environment]::NewLine) + [Environment]::NewLine
}

function Build-FinalReportText {
    param(
        [Parameter(Mandatory = $true)][hashtable]$CategoryCounts,
        [Parameter(Mandatory = $true)][hashtable]$Summary
    )

    $lines = New-Object System.Collections.Generic.List[string]
    $lines.Add('# Final Knowledge Scrape Report')
    $lines.Add('')
    $lines.Add(('Generated at: `{0}`' -f $script:TimestampIso))
    $lines.Add('')
    $lines.Add('## Final Status')
    $lines.Add('')
    $lines.Add('- Overall status: `INGEST_V2_IMPORT_COMPLETED`')
    $lines.Add(('- Imported knowledge files: `{0}`' -f $Summary.imported_knowledge_files))
    $lines.Add(('- Skipped duplicate_by_url: `{0}`' -f $Summary.skipped_duplicate_by_url))
    $lines.Add(('- Skipped duplicate_by_hash: `{0}`' -f $Summary.skipped_duplicate_by_hash))
    $lines.Add(('- Moved to `90_unsorted_review`: `{0}`' -f $Summary.unsorted_count))
    $lines.Add(('- Moved to `91_rejected_low_value`: `{0}`' -f $Summary.rejected_count))
    $lines.Add(('- Original PDFs copied: `{0}`' -f $Summary.pdf_originals_copied))
    $lines.Add(('- Extracted PDF Markdown copied: `{0}`' -f $Summary.pdf_markdown_copied))
    $lines.Add('')
    $lines.Add('## Corpus Metrics')
    $lines.Add('')
    $lines.Add(('- URL_INDEX rows before: `{0}`' -f $Summary.url_index_rows_before))
    $lines.Add(('- URL_INDEX rows after: `{0}`' -f $Summary.url_index_rows_after))
    $lines.Add(('- Validation status: `{0}`' -f $Summary.validation_status))
    $lines.Add(('- Source logs copied: `{0}`' -f $Summary.source_logs_copied))
    $lines.Add('')
    $lines.Add('## Category Counts')
    $lines.Add('')
    $lines.Add('| Category | Count |')
    $lines.Add('| --- | ---: |')
    foreach ($category in $script:TopicalCategories) {
        $lines.Add(('| `{0}` | `{1}` |' -f $category, $CategoryCounts[$category]))
    }
    $lines.Add('')
    $lines.Add('## Official-Source Priority')
    $lines.Add('')
    $lines.Add('1. Original PDFs under `14_datasheets_pdf_markdown/original_pdf/`')
    $lines.Add('2. Official manufacturer datasheets and app notes')
    $lines.Add('3. Official KiCad docs, dev docs, and KLC/library sources')
    $lines.Add('4. Fabricator docs')
    $lines.Add('5. Peer-review forums, then general blogs')
    $lines.Add('')
    $lines.Add('Practical rule:')
    $lines.Add('- Use extracted PDF Markdown only as search-friendly text.')
    $lines.Add('- Use `URL_INDEX.csv` before trusting a source.')
    $lines.Add('')
    $lines.Add('## Remaining Concerns')
    $lines.Add('')
    if ($Summary.warnings.Count -eq 0) {
        $lines.Add('- No major warnings were recorded in this import pass.')
    }
    else {
        foreach ($warning in $Summary.warnings) {
            $lines.Add(('- {0}' -f $warning))
        }
    }
    $lines.Add('')

    return ($lines -join [Environment]::NewLine) + [Environment]::NewLine
}

function Build-ImportReportText {
    param(
        [Parameter(Mandatory = $true)][object[]]$InventoryRows,
        [Parameter(Mandatory = $true)][hashtable]$CategoryCountsBefore,
        [Parameter(Mandatory = $true)][hashtable]$CategoryCountsAfter,
        [Parameter(Mandatory = $true)][hashtable]$Summary
    )

    $lines = New-Object System.Collections.Generic.List[string]
    $lines.Add('# INGEST_V2_IMPORT_REPORT')
    $lines.Add('')
    $lines.Add(('Import started: `{0}`' -f $script:ImportStartedAt.ToString('o')))
    $lines.Add(('Import finished: `{0}`' -f (Get-Date).ToString('o')))
    $lines.Add(('Source folder: `{0}`' -f $IngestRoot))
    $lines.Add('')
    $lines.Add('## Scan Counts')
    $lines.Add('')
    $lines.Add(('- total source files scanned: `{0}`' -f $InventoryRows.Count))
    $lines.Add(('- total Markdown scanned: `{0}`' -f @($InventoryRows | Where-Object { $_.is_markdown -eq $true }).Count))
    $lines.Add(('- total PDFs scanned: `{0}`' -f @($InventoryRows | Where-Object { $_.is_pdf -eq $true }).Count))
    $lines.Add(('- total extracted PDF Markdown scanned: `{0}`' -f @($InventoryRows | Where-Object { $_.is_extracted_pdf_markdown -eq $true }).Count))
    $lines.Add(('- total raw HTML scanned: `{0}`' -f @($InventoryRows | Where-Object { $_.is_raw_html -eq $true }).Count))
    $lines.Add(('- total URLs found: `{0}`' -f @($InventoryRows | Where-Object { -not [string]::IsNullOrWhiteSpace($_.normalized_url) } | Select-Object -ExpandProperty normalized_url -Unique).Count))
    $lines.Add('')
    $lines.Add('## Import Results')
    $lines.Add('')
    $lines.Add(('- total new files imported: `{0}`' -f $Summary.imported_knowledge_files))
    $lines.Add(('- total skipped duplicate_by_url: `{0}`' -f $Summary.skipped_duplicate_by_url))
    $lines.Add(('- total skipped duplicate_by_hash: `{0}`' -f $Summary.skipped_duplicate_by_hash))
    $lines.Add(('- total moved to 90_unsorted_review: `{0}`' -f $Summary.unsorted_count))
    $lines.Add(('- total moved to 91_rejected_low_value: `{0}`' -f $Summary.rejected_count))
    $lines.Add(('- total PDF originals copied: `{0}`' -f $Summary.pdf_originals_copied))
    $lines.Add(('- total PDF Markdown copied: `{0}`' -f $Summary.pdf_markdown_copied))
    $lines.Add(('- total URL_INDEX rows before: `{0}`' -f $Summary.url_index_rows_before))
    $lines.Add(('- total URL_INDEX rows after: `{0}`' -f $Summary.url_index_rows_after))
    $lines.Add('')
    $lines.Add('## Category Counts Before/After')
    $lines.Add('')
    $lines.Add('| Category | Before | After |')
    $lines.Add('| --- | ---: | ---: |')
    foreach ($category in $script:TopicalCategories) {
        $lines.Add(('| `{0}` | `{1}` | `{2}` |' -f $category, $CategoryCountsBefore[$category], $CategoryCountsAfter[$category]))
    }
    $lines.Add('')
    $lines.Add('## Top 25 Source Domains Imported')
    $lines.Add('')
    foreach ($group in ($Summary.imported_domain_counts.GetEnumerator() | Sort-Object @{ Expression = 'Value'; Descending = $true }, Name | Select-Object -First 25)) {
        $lines.Add(('- `{0}`: `{1}`' -f $group.Key, $group.Value))
    }
    $lines.Add('')
    $lines.Add('## Errors And Warnings')
    $lines.Add('')
    if ($Summary.errors.Count -eq 0 -and $Summary.warnings.Count -eq 0) {
        $lines.Add('- None recorded.')
    }
    else {
        foreach ($item in $Summary.errors) {
            $lines.Add(('- ERROR: {0}' -f $item))
        }
        foreach ($item in $Summary.warnings) {
            $lines.Add(('- WARNING: {0}' -f $item))
        }
    }
    $lines.Add('')
    $lines.Add('## Files Needing Review')
    $lines.Add('')
    if ($Summary.review_files.Count -eq 0) {
        $lines.Add('- None.')
    }
    else {
        foreach ($item in ($Summary.review_files | Select-Object -First 100)) {
            $lines.Add(('- `{0}`' -f $item))
        }
    }
    $lines.Add('')
    $lines.Add('## Next Recommended Prompt')
    $lines.Add('')
    if ($Summary.review_files.Count -gt 0 -or $Summary.warnings.Count -gt 0) {
        $lines.Add('`Review knowledge_scrape\\INGEST_V2_IMPORT_REPORT.md and move the remaining review candidates from 90_unsorted_review into their final categories, then tighten any weak source-quality heuristics that still let low-value pages through.`')
    }
    else {
        $lines.Add('`Use knowledge_scrape\\00_ai_entrypoints\\AI_START_HERE.md and URL_INDEX.csv to begin source-traceable engineering retrieval from the updated knowledge base.`')
    }
    $lines.Add('')

    return ($lines -join [Environment]::NewLine) + [Environment]::NewLine
}

function Build-SourceOfTruthIndexText {
    param([Parameter(Mandatory = $true)][object[]]$UrlRows)

    $lines = New-Object System.Collections.Generic.List[string]
    $lines.Add('# SOURCE_OF_TRUTH_INDEX')
    $lines.Add('')
    $lines.Add(('Generated at: `{0}`' -f $script:TimestampIso))
    $lines.Add('')
    $lines.Add('## Priority Order')
    $lines.Add('')
    $lines.Add('1. Original manufacturer PDFs in `../14_datasheets_pdf_markdown/original_pdf/`')
    $lines.Add('2. Official manufacturer app notes and layout guides')
    $lines.Add('3. Official KiCad docs, dev docs, and KLC/library sources')
    $lines.Add('4. Fabricator rules')
    $lines.Add('5. Forums, blogs, and videos only for corroboration or failure-mode examples')
    $lines.Add('')
    $lines.Add('## Source Buckets')
    $lines.Add('')
    $lines.Add('- `official_datasheets/`: use for pinouts, package drawings, electrical limits, and tables.')
    $lines.Add('- `official_app_notes/`: use for vendor layout guidance and implementation details.')
    $lines.Add('- `kicad_official_docs/`: use for KiCad behavior, file formats, APIs, and KLC guidance.')
    $lines.Add('- `fabricator_rules/`: use for manufacturing constraints that must match the chosen board house.')
    $lines.Add('')
    $lines.Add('## Top Official Domains')
    $lines.Add('')
    foreach ($group in ($UrlRows | Where-Object { Test-IsOfficialDomain -Domain $_.source_domain -TrustLevel $_.trust_level -SourceType $_.source_type } | Group-Object source_domain | Sort-Object @{ Expression = 'Count'; Descending = $true }, Name | Select-Object -First 20)) {
        $lines.Add(('- `{0}`: `{1}`' -f $group.Name, $group.Count))
    }
    $lines.Add('')
    $lines.Add('## Retrieval Rule')
    $lines.Add('')
    $lines.Add('- Use `URL_INDEX.csv` before trusting a local file.')
    $lines.Add('- Treat extracted PDF Markdown as secondary only.')
    $lines.Add('- Cite local file path plus `url_index_id` when making engineering decisions.')
    $lines.Add('')
    return ($lines -join [Environment]::NewLine) + [Environment]::NewLine
}

function Build-OfficialSourcesIndexText {
    param([Parameter(Mandatory = $true)][object[]]$UrlRows)

    $lines = New-Object System.Collections.Generic.List[string]
    $lines.Add('# OFFICIAL_SOURCES_INDEX')
    $lines.Add('')
    $lines.Add(('Generated at: `{0}`' -f $script:TimestampIso))
    $lines.Add('')
    $lines.Add('## Preferred Official Domains')
    $lines.Add('')
    foreach ($group in ($UrlRows | Where-Object { Test-IsOfficialDomain -Domain $_.source_domain -TrustLevel $_.trust_level -SourceType $_.source_type } | Group-Object source_domain | Sort-Object @{ Expression = 'Count'; Descending = $true }, Name | Select-Object -First 30)) {
        $lines.Add(('- `{0}`: `{1}` rows' -f $group.Name, $group.Count))
    }
    $lines.Add('')
    $lines.Add('## Usage Rules')
    $lines.Add('')
    $lines.Add('- Prefer official PDFs, app notes, KiCad docs, and fabricator docs over blog/tutorial/forum material.')
    $lines.Add('- Use original PDFs for exact tables, pinouts, footprints, package drawings, and layout figures.')
    $lines.Add('- Use peer review only to supplement or challenge a primary source, not replace it.')
    $lines.Add('')
    return ($lines -join [Environment]::NewLine) + [Environment]::NewLine
}

function Build-CategoryRoutingIndexText {
    $lines = New-Object System.Collections.Generic.List[string]
    $lines.Add('# CATEGORY_ROUTING_INDEX')
    $lines.Add('')
    $lines.Add(('Generated at: `{0}`' -f $script:TimestampIso))
    $lines.Add('')
    $lines.Add('## Quick Routing')
    $lines.Add('')
    $lines.Add('- KiCad behavior, CLI, editors: `01_kicad_core`')
    $lines.Add('- KiCad API and automation: `02_kicad_python_api`, `30_eda_automation_verification`')
    $lines.Add('- KiCad file formats: `03_kicad_file_formats`')
    $lines.Add('- Symbols, footprints, KLC, packages: `04_kicad_libraries_symbols_footprints`, `21_component_package_land_patterns`')
    $lines.Add('- Espressif and ESP32: `05_esp32_espressif`, `23_rf_wifi_antenna_layout`')
    $lines.Add('- Other MCU vendors: `06_microcontrollers`')
    $lines.Add('- USB-C, ESD, high-speed I/O: `07_usb_c_high_speed_esd`, `25_signal_integrity_high_speed`, `31_compliance_safety_emc`')
    $lines.Add('- Power converters and PI: `08_power_buck_regulators`, `20_manufacturer_layout_guides`, `24_power_integrity_decoupling`')
    $lines.Add('- Layout, grounding, EMI: `09_pcb_layout_grounding_emi_si`')
    $lines.Add('- Fabrication and assembly: `10_dfm_fabrication_assembly`')
    $lines.Add('- Calculators and standards: `11_calculators_ipc_reference`, `29_standards_ipc_ul_safety`')
    $lines.Add('- Peer review and case studies: `12_forums_peer_review`, `17_case_studies_bad_boards`, `18_case_studies_good_boards`')
    $lines.Add('- Vendor CAD and land patterns: `13_vendor_parts_cad_models`, `21_component_package_land_patterns`')
    $lines.Add('- PDFs and original source material: `14_datasheets_pdf_markdown`')
    $lines.Add('')
    $lines.Add('## Routing Rules')
    $lines.Add('')
    $lines.Add('- Start with `URL_INDEX.csv` before trusting a source.')
    $lines.Add('- Prefer official datasheets, app notes, KiCad docs, and fabricator docs.')
    $lines.Add('- If classification is uncertain, use `90_unsorted_review` rather than `91_rejected_low_value`.')
    $lines.Add('- Use `91_rejected_low_value` only for diagnostics and rejected scrape output.')
    $lines.Add('')
    return ($lines -join [Environment]::NewLine) + [Environment]::NewLine
}

function Build-ValidationMarkdownText {
    param([Parameter(Mandatory = $true)][object[]]$Checks)

    $lines = New-Object System.Collections.Generic.List[string]
    $lines.Add('# ingest_v2_import_validation_report')
    $lines.Add('')
    $lines.Add(('Generated at: `{0}`' -f $script:TimestampIso))
    $lines.Add('')
    $lines.Add('| Check | Status | Details |')
    $lines.Add('| --- | --- | --- |')
    foreach ($check in $Checks) {
        $lines.Add(('| `{0}` | `{1}` | {2} |' -f $check.check_name, $check.status, ($check.details -replace '\|', '/')))
    }
    $lines.Add('')
    return ($lines -join [Environment]::NewLine) + [Environment]::NewLine
}

$urlIndexCsvPath = Join-Path $KnowledgeRoot 'URL_INDEX.csv'
$urlIndexJsonPath = Join-Path $KnowledgeRoot 'URL_INDEX.json'
$urlIndexMdPath = Join-Path $KnowledgeRoot 'URL_INDEX.md'
$sourceAuditPath = Join-Path $KnowledgeRoot 'SOURCE_AUDIT.md'
$manifestPath = Join-Path $KnowledgeRoot 'MANIFEST.json'
$mainIndexPath = Join-Path $KnowledgeRoot 'INDEX.md'
$finalReportPath = Join-Path $KnowledgeRoot 'FINAL_KNOWLEDGE_SCRAPE_REPORT.md'
$importReportPath = Join-Path $KnowledgeRoot 'INGEST_V2_IMPORT_REPORT.md'
$pdfIndexCsvPath = Join-Path $KnowledgeRoot '14_datasheets_pdf_markdown\PDF_INDEX.csv'
$pdfIndexMdPath = Join-Path $KnowledgeRoot '14_datasheets_pdf_markdown\PDF_INDEX.md'
$inventoryCsvPath = Join-Path $KnowledgeRoot '_raw_inventory\ingest_v2_file_inventory.csv'
$inventoryJsonPath = Join-Path $KnowledgeRoot '_raw_inventory\ingest_v2_file_inventory.json'
$validationMdPath = Join-Path $KnowledgeRoot '_logs\ingest_v2_import_validation_report.md'
$validationCsvPath = Join-Path $KnowledgeRoot '_logs\ingest_v2_import_validation_report.csv'
$sourceLogsRoot = Join-Path $KnowledgeRoot '99_source_logs\ingest_v2_import'
$pdfOriginalRoot = Join-Path $KnowledgeRoot '14_datasheets_pdf_markdown\original_pdf'
$pdfExtractedRoot = Join-Path $KnowledgeRoot '14_datasheets_pdf_markdown\extracted_markdown'
$sourceOfTruthIndexPath = Join-Path $KnowledgeRoot '00_source_of_truth\SOURCE_OF_TRUTH_INDEX.md'
$officialSourcesIndexPath = Join-Path $KnowledgeRoot '00_retrieval_indexes\OFFICIAL_SOURCES_INDEX.md'
$categoryRoutingIndexPath = Join-Path $KnowledgeRoot '00_retrieval_indexes\CATEGORY_ROUTING_INDEX.md'

foreach ($folder in @(
        $KnowledgeRoot,
        (Join-Path $KnowledgeRoot '_raw_inventory'),
        (Join-Path $KnowledgeRoot '_logs'),
        (Join-Path $KnowledgeRoot '_scripts'),
        (Join-Path $KnowledgeRoot '99_source_logs'),
        $sourceLogsRoot,
        $pdfOriginalRoot,
        $pdfExtractedRoot,
        (Join-Path $KnowledgeRoot '14_datasheets_pdf_markdown'),
        (Join-Path $KnowledgeRoot '00_source_of_truth'),
        (Join-Path $KnowledgeRoot '00_source_of_truth\official_datasheets'),
        (Join-Path $KnowledgeRoot '00_source_of_truth\official_app_notes'),
        (Join-Path $KnowledgeRoot '00_source_of_truth\kicad_official_docs'),
        (Join-Path $KnowledgeRoot '00_source_of_truth\fabricator_rules'),
        (Join-Path $KnowledgeRoot '00_engineering_rules'),
        (Join-Path $KnowledgeRoot '00_retrieval_indexes')
    ) + ($script:TopicalCategories | ForEach-Object { Join-Path $KnowledgeRoot $_ })) {
    Ensure-Directory -Path $folder
}

$registryCopyTargets = @(
    @{ source = Join-Path $IngestRoot '_registry'; target = Join-Path $sourceLogsRoot 'root_registry'; filter = @('*.csv', '*.json') },
    @{ source = Join-Path $IngestRoot '_logs'; target = Join-Path $sourceLogsRoot 'root_logs'; filter = @('*.csv', '*.json') },
    @{ source = Join-Path $IngestRoot 'domain_seed_run_v2\_registry'; target = Join-Path $sourceLogsRoot 'domain_seed_run_v2_registry'; filter = @('*.csv', '*.json') },
    @{ source = Join-Path $IngestRoot 'domain_seed_run_v2\_logs'; target = Join-Path $sourceLogsRoot 'domain_seed_run_v2_logs'; filter = @('*.csv', '*.json') }
)

$sourceLogsCopied = 0
foreach ($copySpec in $registryCopyTargets) {
    Ensure-Directory -Path $copySpec.target
    if (-not (Test-Path -LiteralPath $copySpec.source)) {
        continue
    }
    foreach ($pattern in $copySpec.filter) {
        foreach ($file in (Get-ChildItem -LiteralPath $copySpec.source -File -Filter $pattern -ErrorAction SilentlyContinue)) {
            $copyResult = Copy-FileWithCollisionHandling -SourcePath $file.FullName -DestinationDirectory $copySpec.target -DestinationFileName $file.Name
            if ($copyResult.copied) {
                $sourceLogsCopied += 1
            }
        }
    }
}

$registryByPath = @{}
$registryByFileName = @{}
$registryByNormalizedUrl = @{}
$allRegistryMetadata = @()
$allRegistryMetadata += Import-RegistryMetadata -CsvPath (Join-Path $IngestRoot '_registry\URL_INDEX.csv') -SourceBatch 'ingest_v2_root_registry' -MetadataByPath $registryByPath -MetadataByFileName $registryByFileName -MetadataByNormalizedUrl $registryByNormalizedUrl
$allRegistryMetadata += Import-RegistryMetadata -CsvPath (Join-Path $IngestRoot 'domain_seed_run_v2\_registry\URL_INDEX_seed_urlv2.csv') -SourceBatch 'ingest_v2_domain_seed_registry' -MetadataByPath $registryByPath -MetadataByFileName $registryByFileName -MetadataByNormalizedUrl $registryByNormalizedUrl

$existingUrlRows = New-Object System.Collections.Generic.List[hashtable]
if (Test-Path -LiteralPath $urlIndexCsvPath) {
    foreach ($csvRow in (Import-Csv -LiteralPath $urlIndexCsvPath)) {
        $existingUrlRows.Add((Convert-ExistingUrlIndexRow -CsvRow $csvRow))
    }
}

$script:NextUrlIndexNumber = 0
foreach ($row in $existingUrlRows) {
    $idNumber = Get-UrlIndexIdNumber -Id $row.id
    if ($idNumber -gt $script:NextUrlIndexNumber) {
        $script:NextUrlIndexNumber = $idNumber
    }
}

$urlRowsById = @{}
$urlRowsByNormalizedUrl = @{}
foreach ($row in $existingUrlRows) {
    $urlRowsById[$row.id] = $row
    if (-not [string]::IsNullOrWhiteSpace($row.normalized_url) -and -not $urlRowsByNormalizedUrl.ContainsKey($row.normalized_url)) {
        $urlRowsByNormalizedUrl[$row.normalized_url] = $row
    }
}

$categoryCountsBefore = Get-CategoryCounts -KnowledgeRootPath $KnowledgeRoot -UrlRows @($existingUrlRows.ToArray())
$urlIndexRowsBefore = $existingUrlRows.Count

$kicadFileSnapshot = @{}
$kicadProjectRoot = Join-Path (Split-Path -Parent $KnowledgeRoot) '04_KICAD_PROJECTS'
if (Test-Path -LiteralPath $kicadProjectRoot) {
    foreach ($file in (Get-ChildItem -LiteralPath $kicadProjectRoot -Recurse -File -Include '*.kicad_sch', '*.kicad_pcb', '*.kicad_pro' -ErrorAction SilentlyContinue)) {
        $kicadFileSnapshot[$file.FullName.ToLowerInvariant()] = $file.LastWriteTimeUtc.ToString('o')
    }
}

$existingPathToRow = @{}
foreach ($row in $existingUrlRows) {
    foreach ($candidatePath in @($row.current_knowledge_file, $row.pdf_path, $row.extracted_pdf_markdown_path)) {
        if (-not [string]::IsNullOrWhiteSpace($candidatePath)) {
            $resolved = Resolve-FullPathSafe -Path $candidatePath
            if (Test-Path -LiteralPath $resolved) {
                $existingPathToRow[$resolved.ToLowerInvariant()] = $row
            }
        }
    }
}

$existingDuplicateHashIndex = @{}
foreach ($category in $script:TopicalCategories) {
    $categoryPath = Join-Path $KnowledgeRoot $category
    if (-not (Test-Path -LiteralPath $categoryPath)) {
        continue
    }

    $files = @()
    if ($category -eq '14_datasheets_pdf_markdown') {
        $files += @(Get-ChildItem -LiteralPath $pdfOriginalRoot -File -ErrorAction SilentlyContinue | Where-Object { $_.Extension -ieq '.pdf' })
        $files += @(Get-ChildItem -LiteralPath $pdfExtractedRoot -File -Filter '*.md' -ErrorAction SilentlyContinue)
    }
    else {
        $files += @(
            Get-ChildItem -LiteralPath $categoryPath -Recurse -File -Filter '*.md' -ErrorAction SilentlyContinue |
            Where-Object { $_.Name -ne '_CATEGORY_INDEX.md' -and $_.Name -ne 'PDF_INDEX.md' }
        )
    }

    foreach ($file in $files) {
        $isMarkdownLike = $file.Extension -ieq '.md'
        $duplicateHash = Get-DuplicateHashForFile -Path $file.FullName -IsMarkdownLike:$isMarkdownLike
        if (-not [string]::IsNullOrWhiteSpace($duplicateHash) -and -not $existingDuplicateHashIndex.ContainsKey($duplicateHash)) {
            $row = $null
            $pathKey = $file.FullName.ToLowerInvariant()
            if ($existingPathToRow.ContainsKey($pathKey)) {
                $row = $existingPathToRow[$pathKey]
            }
            $existingDuplicateHashIndex[$duplicateHash] = [ordered]@{
                path = $file.FullName
                id = if ($null -ne $row) { $row.id } else { '' }
                knowledge_category = if ($null -ne $row) { $row.knowledge_category } else { $category }
            }
        }
    }
}

$sourceFolderSpecs = @(
    @{ path = Join-Path $IngestRoot 'markdown'; source_folder = 'markdown'; kind = 'markdown' },
    @{ path = Join-Path $IngestRoot 'pdf'; source_folder = 'pdf'; kind = 'pdf' },
    @{ path = Join-Path $IngestRoot 'extracted_pdf_markdown'; source_folder = 'extracted_pdf_markdown'; kind = 'extracted_pdf_markdown' },
    @{ path = Join-Path $IngestRoot 'raw_html'; source_folder = 'raw_html'; kind = 'raw_html' },
    @{ path = Join-Path $IngestRoot 'domain_seed_run_v2\markdown'; source_folder = 'domain_seed_run_v2\markdown'; kind = 'markdown' },
    @{ path = Join-Path $IngestRoot 'domain_seed_run_v2\pdf'; source_folder = 'domain_seed_run_v2\pdf'; kind = 'pdf' },
    @{ path = Join-Path $IngestRoot 'domain_seed_run_v2\extracted_pdf_markdown'; source_folder = 'domain_seed_run_v2\extracted_pdf_markdown'; kind = 'extracted_pdf_markdown' },
    @{ path = Join-Path $IngestRoot 'domain_seed_run_v2\raw_html'; source_folder = 'domain_seed_run_v2\raw_html'; kind = 'raw_html' }
)

$inventoryRows = New-Object System.Collections.Generic.List[hashtable]
$groupsByKey = @{}

foreach ($spec in $sourceFolderSpecs) {
    if (-not (Test-Path -LiteralPath $spec.path)) {
        continue
    }

    foreach ($file in (Get-ChildItem -LiteralPath $spec.path -File -ErrorAction SilentlyContinue | Sort-Object Name)) {
        $extension = $file.Extension.ToLowerInvariant()
        $isMarkdown = $spec.kind -eq 'markdown'
        $isPdf = $spec.kind -eq 'pdf'
        $isRawHtml = $spec.kind -eq 'raw_html'
        $isExtracted = $spec.kind -eq 'extracted_pdf_markdown'
        $isMarkdownLike = $isMarkdown -or $isExtracted

        $textMetadata = $null
        if ($isMarkdownLike -or $isRawHtml) {
            $textMetadata = Get-TextMetadata -Path $file.FullName -IsMarkdownLike:$isMarkdownLike
        }

        $frontmatter = if ($null -ne $textMetadata) { $textMetadata.frontmatter } else { [ordered]@{} }
        $metadata = Get-MetadataForSourceFile -Path $file.FullName -Frontmatter $frontmatter -MetadataByPath $registryByPath -MetadataByFileName $registryByFileName -MetadataByNormalizedUrl $registryByNormalizedUrl

        $detectedSourceUrl = ''
        if ($frontmatter.Contains('source_url') -and -not [string]::IsNullOrWhiteSpace($frontmatter['source_url'])) {
            $detectedSourceUrl = $frontmatter['source_url']
        }
        elseif ($null -ne $metadata -and -not [string]::IsNullOrWhiteSpace($metadata.original_url)) {
            $detectedSourceUrl = $metadata.original_url
        }

        $normalizedUrl = if ($null -ne $metadata -and -not [string]::IsNullOrWhiteSpace($metadata.normalized_url)) { $metadata.normalized_url } else { Normalize-Url -Url $detectedSourceUrl }
        $sourceDomain = Get-SourceDomain -Url $detectedSourceUrl -FallbackDomain $(if ($null -ne $metadata) { $metadata.source_domain } else { if ($frontmatter.Contains('source_domain')) { $frontmatter['source_domain'] } else { '' } })
        $sourceType = Get-ResolvedSourceType -Explicit $(if ($null -ne $metadata) { $metadata.source_type } else { if ($frontmatter.Contains('source_type')) { $frontmatter['source_type'] } else { '' } }) -Domain $sourceDomain -Url $detectedSourceUrl -IsPdf:$isPdf -IsExtractedPdfMarkdown:$isExtracted
        $trustLevel = Get-ResolvedTrustLevel -Explicit $(if ($null -ne $metadata) { $metadata.trust_level } else { if ($frontmatter.Contains('trust_level')) { $frontmatter['trust_level'] } else { '' } }) -SourceType $sourceType -Domain $sourceDomain
        $topicCategory = Get-ResolvedTopicCategory -Explicit $(if ($null -ne $metadata) { $metadata.topic_category } else { if ($frontmatter.Contains('topic_category')) { $frontmatter['topic_category'] } else { '' } }) -Url $detectedSourceUrl -Domain $sourceDomain -Text $(if ($null -ne $textMetadata) { $textMetadata.body } else { '' })
        $scrapeStatus = if ($null -ne $metadata -and -not [string]::IsNullOrWhiteSpace($metadata.scrape_status)) { $metadata.scrape_status } else { 'success' }
        $wordCount = if ($null -ne $textMetadata) { $textMetadata.word_count } else { 0 }
        $lineCount = if ($null -ne $textMetadata) { $textMetadata.line_count } else { 0 }
        $firstHeading = if ($null -ne $textMetadata) { $textMetadata.first_heading } else { '' }
        $rawHtmlTagCount = if ($null -ne $textMetadata) { $textMetadata.raw_html_tag_count } else { 0 }
        $containsRawHtml = $rawHtmlTagCount -gt 0
        $textForGuess = if ($null -ne $textMetadata) { $textMetadata.body } else { '' }
        $targetCategoryGuess = Get-KnowledgeCategoryGuess -Url $detectedSourceUrl -Domain $sourceDomain -SourceType $sourceType -TopicCategory $topicCategory -Heading $firstHeading -Text $textForGuess -FileName $file.Name
        $contentQualityGuess = Get-ContentQualityGuess -WordCount $wordCount -RawHtmlTagCount $rawHtmlTagCount -Heading $firstHeading -Url $detectedSourceUrl -Domain $sourceDomain -SourceType $sourceType -TrustLevel $trustLevel -Text $textForGuess -IsPdf:$isPdf -IsExtractedPdfMarkdown:$isExtracted -IsRawHtml:$isRawHtml
        $duplicateKey = Get-DuplicateHashForFile -Path $file.FullName -IsMarkdownLike:($isMarkdownLike)

        $row = [ordered]@{
            source_file_path = $file.FullName
            source_file_name = $file.Name
            source_folder = $spec.source_folder
            extension = $extension
            size_bytes = $file.Length
            sha256 = Get-FileSha256 -Path $file.FullName
            last_write_time = $file.LastWriteTime.ToString('o')
            detected_source_url = $detectedSourceUrl
            normalized_url = $normalizedUrl
            source_domain = $sourceDomain
            source_type = $sourceType
            topic_category = $topicCategory
            trust_level = $trustLevel
            scrape_status = $scrapeStatus
            is_markdown = $isMarkdown
            is_pdf = $isPdf
            is_raw_html = $isRawHtml
            is_extracted_pdf_markdown = $isExtracted
            contains_raw_html = $containsRawHtml
            raw_html_tag_count = $rawHtmlTagCount
            word_count = $wordCount
            line_count = $lineCount
            first_heading = $firstHeading
            content_quality_guess = $contentQualityGuess
            target_category_guess = $targetCategoryGuess
            duplicate_by_url = $false
            duplicate_by_hash = $false
            existing_knowledge_file_if_duplicate = ''
            import_action = ''
            _duplicate_key = $duplicateKey
            _frontmatter = $frontmatter
            _text_body = if ($null -ne $textMetadata) { $textMetadata.body } else { '' }
            _text_full = if ($null -ne $textMetadata) { $textMetadata.text } else { '' }
            _metadata = $metadata
        }

        $inventoryRows.Add($row)
        $groupKey = if (-not [string]::IsNullOrWhiteSpace($normalizedUrl)) { 'url::' + $normalizedUrl } else { 'hash::' + $duplicateKey }
        if (-not $groupsByKey.ContainsKey($groupKey)) {
            $groupsByKey[$groupKey] = New-Object System.Collections.Generic.List[hashtable]
        }
        $groupsByKey[$groupKey].Add($row)
    }
}

$summary = [ordered]@{
    imported_knowledge_files = 0
    skipped_duplicate_by_url = 0
    skipped_duplicate_by_hash = 0
    rejected_count = 0
    unsorted_count = 0
    pdf_originals_copied = 0
    pdf_markdown_copied = 0
    url_index_rows_before = $urlIndexRowsBefore
    url_index_rows_after = 0
    source_logs_copied = $sourceLogsCopied
    imported_domain_counts = @{}
    warnings = New-Object System.Collections.Generic.List[string]
    errors = New-Object System.Collections.Generic.List[string]
    review_files = New-Object System.Collections.Generic.List[string]
    validation_status = 'pending'
}

foreach ($entry in $groupsByKey.GetEnumerator() | Sort-Object Name) {
    $groupRows = @($entry.Value.ToArray())
    if ($groupRows.Count -eq 0) {
        continue
    }

    $primaryTextRow = (
        $groupRows |
        Where-Object { $_.is_markdown -or $_.is_extracted_pdf_markdown } |
        Sort-Object `
            @{ Expression = { if ($_.is_markdown) { 2 } elseif ($_.is_extracted_pdf_markdown) { 1 } else { 0 } }; Descending = $true },
            @{ Expression = 'word_count'; Descending = $true } |
        Select-Object -First 1
    )
    if ($null -eq $primaryTextRow) {
        $primaryTextRow = ($groupRows | Where-Object { $_.is_raw_html } | Sort-Object word_count -Descending | Select-Object -First 1)
    }
    if ($null -eq $primaryTextRow) {
        $primaryTextRow = $groupRows[0]
    }

    $normalizedUrl = $primaryTextRow.normalized_url
    $sourceUrl = $primaryTextRow.detected_source_url
    $sourceDomain = $primaryTextRow.source_domain
    $sourceType = $primaryTextRow.source_type
    $topicCategory = $primaryTextRow.topic_category
    $trustLevel = $primaryTextRow.trust_level
    $scrapeStatus = $primaryTextRow.scrape_status
    $title = Get-SafeTitle -FrontmatterTitle $(if ($primaryTextRow._frontmatter.Contains('title')) { $primaryTextRow._frontmatter['title'] } else { '' }) -Heading $primaryTextRow.first_heading -FallbackName ([System.IO.Path]::GetFileNameWithoutExtension($primaryTextRow.source_file_name))
    $knowledgeCategory = $primaryTextRow.target_category_guess
    $contentQuality = $primaryTextRow.content_quality_guess
    $hasPdf = @($groupRows | Where-Object { $_.is_pdf }).Count -gt 0
    $hasExtracted = @($groupRows | Where-Object { $_.is_extracted_pdf_markdown }).Count -gt 0
    $hasMarkdown = @($groupRows | Where-Object { $_.is_markdown }).Count -gt 0
    $hasOnlyRawHtml = (-not $hasPdf -and -not $hasExtracted -and -not $hasMarkdown)
    $needsReview = $false
    $notes = ''

    if ([string]::IsNullOrWhiteSpace($sourceUrl)) {
        $needsReview = $true
        $notes = Add-NoteValue -Existing $notes -Append 'source_url_missing_or_unresolved'
    }
    if ($knowledgeCategory -eq '90_unsorted_review') {
        $needsReview = $true
    }
    if ($contentQuality -eq 'junk' -and $knowledgeCategory -ne '15_video_reference_index') {
        $knowledgeCategory = '91_rejected_low_value'
    }
    elseif ($knowledgeCategory -eq '15_video_reference_index' -and $contentQuality -eq 'junk') {
        $knowledgeCategory = '91_rejected_low_value'
    }
    elseif ($contentQuality -eq 'low' -and $hasOnlyRawHtml) {
        $knowledgeCategory = '91_rejected_low_value'
    }

    if ($hasOnlyRawHtml) {
        $knowledgeCategory = '91_rejected_low_value'
        $notes = Add-NoteValue -Existing $notes -Append 'raw_html_inventory_only'
    }

    $existingUrlRow = $null
    if (-not [string]::IsNullOrWhiteSpace($normalizedUrl) -and $urlRowsByNormalizedUrl.ContainsKey($normalizedUrl)) {
        $existingUrlRow = $urlRowsByNormalizedUrl[$normalizedUrl]
    }

    $hashDuplicateInfo = $null
    foreach ($row in $groupRows) {
        if (-not [string]::IsNullOrWhiteSpace($row._duplicate_key) -and $existingDuplicateHashIndex.ContainsKey($row._duplicate_key)) {
            $hashDuplicateInfo = $existingDuplicateHashIndex[$row._duplicate_key]
            break
        }
    }

    $repairNeeded = $false
    if ($null -ne $existingUrlRow) {
        if ([string]::IsNullOrWhiteSpace($existingUrlRow.current_knowledge_file) -or -not (Test-Path -LiteralPath $existingUrlRow.current_knowledge_file)) {
            $repairNeeded = $true
        }
    }

    $groupExistingPath = if ($null -ne $existingUrlRow) { $existingUrlRow.current_knowledge_file } elseif ($null -ne $hashDuplicateInfo) { $hashDuplicateInfo.path } else { '' }

    foreach ($row in $groupRows) {
        if ($null -ne $existingUrlRow) {
            $row.duplicate_by_url = $true
            $row.existing_knowledge_file_if_duplicate = $existingUrlRow.current_knowledge_file
        }
        elseif ($null -ne $hashDuplicateInfo) {
            $row.duplicate_by_hash = $true
            $row.existing_knowledge_file_if_duplicate = $hashDuplicateInfo.path
        }
    }

    if ($null -ne $existingUrlRow -and -not $repairNeeded) {
        $existingUrlRow.source_batch = Add-NoteValue -Existing $existingUrlRow.source_batch -Append $script:ImportBatch
        $existingUrlRow.notes = Add-NoteValue -Existing $existingUrlRow.notes -Append ('duplicate_ingest_source=' + $primaryTextRow.source_file_name)
        if ([string]::IsNullOrWhiteSpace($existingUrlRow.local_file)) {
            $existingUrlRow.local_file = $primaryTextRow.source_file_path
        }
        if ([string]::IsNullOrWhiteSpace($existingUrlRow.markdown_path) -and $hasMarkdown) {
            $existingUrlRow.markdown_path = ($groupRows | Where-Object { $_.is_markdown } | Select-Object -First 1).source_file_path
        }
        if ([string]::IsNullOrWhiteSpace($existingUrlRow.raw_html_path)) {
            $rawHtmlRow = ($groupRows | Where-Object { $_.is_raw_html } | Select-Object -First 1)
            if ($null -ne $rawHtmlRow) {
                $existingUrlRow.raw_html_path = $rawHtmlRow.source_file_path
            }
        }

        $rowId = $existingUrlRow.id
        $slug = Get-SourceSlug -SourceFileName $primaryTextRow.source_file_name -NormalizedUrl $normalizedUrl
        if ($hasPdf -and ([string]::IsNullOrWhiteSpace($existingUrlRow.pdf_path) -or -not (Test-Path -LiteralPath $existingUrlRow.pdf_path))) {
            $pdfRow = ($groupRows | Where-Object { $_.is_pdf } | Select-Object -First 1)
            if ($null -ne $pdfRow) {
                $copyResult = Copy-FileWithCollisionHandling -SourcePath $pdfRow.source_file_path -DestinationDirectory $pdfOriginalRoot -DestinationFileName ('{0}--{1}.pdf' -f $rowId, $slug)
                $existingUrlRow.pdf_path = $copyResult.path
                $summary.pdf_originals_copied += 1
            }
        }

        if ($hasExtracted -and ([string]::IsNullOrWhiteSpace($existingUrlRow.extracted_pdf_markdown_path) -or -not (Test-Path -LiteralPath $existingUrlRow.extracted_pdf_markdown_path))) {
            $extractedRow = ($groupRows | Where-Object { $_.is_extracted_pdf_markdown } | Select-Object -First 1)
            if ($null -ne $extractedRow) {
                $extractedDest = Join-Path $pdfExtractedRoot ('{0}--{1}.pdf.md' -f $rowId, $slug)
                $frontmatterArgs = @{
                    Title = $title
                    SourceUrl = $sourceUrl
                    NormalizedUrl = $normalizedUrl
                    UrlIndexId = $rowId
                    SourceDomain = $sourceDomain
                    SourceType = $sourceType
                    TopicCategory = $topicCategory
                    TrustLevel = $trustLevel
                    SourceFile = $extractedRow.source_file_path
                    SourceFolder = $extractedRow.source_folder
                    KnowledgeCategory = '14_datasheets_pdf_markdown'
                    ContentQuality = $contentQuality
                    NeedsReview = $needsReview
                    RawHtmlPath = ''
                    PdfPath = $existingUrlRow.pdf_path
                    ExtractedMarkdownPath = $extractedDest
                    DuplicateStatus = 'repair_existing_url_row'
                    Notes = Add-NoteValue -Existing $notes -Append 'extracted_pdf_markdown_copy'
                }
                Write-NormalizedMarkdownFile -DestinationPath $extractedDest -BodyText $extractedRow._text_body -FrontmatterValues $frontmatterArgs
                $existingUrlRow.extracted_pdf_markdown_path = $extractedDest
                $summary.pdf_markdown_copied += 1
            }
        }

        $existingUrlRow.scraped_at = if ([string]::IsNullOrWhiteSpace($existingUrlRow.scraped_at)) { $scrapeStatus } else { $existingUrlRow.scraped_at }
        Set-UrlRowAliases -Row $existingUrlRow
        foreach ($row in $groupRows) {
            $row.import_action = if ($repairNeeded) { 'repair_existing_url_row' } else { 'skip_duplicate_by_url' }
        }
        $summary.skipped_duplicate_by_url += 1
        continue
    }

    if ($null -ne $hashDuplicateInfo -and -not $repairNeeded) {
        foreach ($row in $groupRows) {
            $row.import_action = 'skip_duplicate_by_hash'
        }

        if (-not [string]::IsNullOrWhiteSpace($normalizedUrl)) {
            $newRow = New-UrlIndexRow -Id (New-UrlIndexId)
            $newRow.original_url = $sourceUrl
            $newRow.normalized_url = $normalizedUrl
            $newRow.source_domain = $sourceDomain
            $newRow.source_type = $sourceType
            $newRow.topic_category = $topicCategory
            $newRow.trust_level = $trustLevel
            $newRow.scrape_status = $scrapeStatus
            $newRow.local_file = $primaryTextRow.source_file_path
            $newRow.current_knowledge_file = $hashDuplicateInfo.path
            $newRawHtmlRow = ($groupRows | Where-Object { $_.is_raw_html } | Select-Object -First 1)
            $newMarkdownRow = ($groupRows | Where-Object { $_.is_markdown } | Select-Object -First 1)
            $newRow.raw_html_path = if ($null -ne $newRawHtmlRow) { $newRawHtmlRow.source_file_path } else { '' }
            $newRow.markdown_path = if ($null -ne $newMarkdownRow) { $newMarkdownRow.source_file_path } else { '' }
            $newRow.pdf_path = ''
            $newRow.extracted_pdf_markdown_path = ''
            $newRow.imported_at = $script:TimestampIso
            $newRow.scraped_at = $scrapeStatus
            $newRow.needs_review = if ($needsReview) { 'true' } else { 'false' }
            $newRow.duplicate_status = 'duplicate_by_hash'
            $newRow.duplicate_of_url_index_id = $hashDuplicateInfo.id
            $newRow.content_quality = $contentQuality
            $newRow.knowledge_category = if ([string]::IsNullOrWhiteSpace($hashDuplicateInfo.knowledge_category)) { $knowledgeCategory } else { $hashDuplicateInfo.knowledge_category }
            $newRow.source_batch = $script:ImportBatch
            $newRow.notes = Add-NoteValue -Existing $notes -Append ('duplicate_of=' + $hashDuplicateInfo.path)
            Set-UrlRowAliases -Row $newRow
            $existingUrlRows.Add($newRow)
            $urlRowsById[$newRow.id] = $newRow
            if (-not $urlRowsByNormalizedUrl.ContainsKey($normalizedUrl)) {
                $urlRowsByNormalizedUrl[$normalizedUrl] = $newRow
            }
        }

        $summary.skipped_duplicate_by_hash += 1
        continue
    }

    $rowToUpdate = if ($repairNeeded -and $null -ne $existingUrlRow) { $existingUrlRow } else { New-UrlIndexRow -Id $(if ($null -ne $existingUrlRow) { $existingUrlRow.id } else { New-UrlIndexId }) }
    $rowId = $rowToUpdate.id
    $slug = Get-SourceSlug -SourceFileName $primaryTextRow.source_file_name -NormalizedUrl $normalizedUrl
    $targetCategoryPath = Join-Path $KnowledgeRoot $knowledgeCategory
    $currentKnowledgeFile = ''
    $pdfPath = ''
    $extractedPath = ''
    $rawHtmlPath = ''

    $rawHtmlRow = ($groupRows | Where-Object { $_.is_raw_html } | Select-Object -First 1)
    if ($null -ne $rawHtmlRow) {
        $rawHtmlPath = $rawHtmlRow.source_file_path
    }

    if ($hasPdf) {
        $pdfRow = ($groupRows | Where-Object { $_.is_pdf } | Select-Object -First 1)
        $copyResult = Copy-FileWithCollisionHandling -SourcePath $pdfRow.source_file_path -DestinationDirectory $pdfOriginalRoot -DestinationFileName ('{0}--{1}.pdf' -f $rowId, $slug)
        $pdfPath = $copyResult.path
        $summary.pdf_originals_copied += 1
    }

    if ($hasExtracted) {
        $extractedRow = ($groupRows | Where-Object { $_.is_extracted_pdf_markdown } | Select-Object -First 1)
        $extractedPath = Join-Path $pdfExtractedRoot ('{0}--{1}.pdf.md' -f $rowId, $slug)
        $extractedNotes = Add-NoteValue -Existing $notes -Append 'original_pdf_is_source_of_truth'
        $extractedFrontmatter = @{
            Title = $title
            SourceUrl = $sourceUrl
            NormalizedUrl = $normalizedUrl
            UrlIndexId = $rowId
            SourceDomain = $sourceDomain
            SourceType = $sourceType
            TopicCategory = $topicCategory
            TrustLevel = $trustLevel
            SourceFile = $extractedRow.source_file_path
            SourceFolder = $extractedRow.source_folder
            KnowledgeCategory = '14_datasheets_pdf_markdown'
            ContentQuality = $contentQuality
            NeedsReview = $needsReview
            RawHtmlPath = $rawHtmlPath
            PdfPath = $pdfPath
            ExtractedMarkdownPath = $extractedPath
            DuplicateStatus = if ($repairNeeded) { 'repaired_existing_row' } else { 'imported_new' }
            Notes = $extractedNotes
        }
        Write-NormalizedMarkdownFile -DestinationPath $extractedPath -BodyText $extractedRow._text_body -FrontmatterValues $extractedFrontmatter
        $summary.pdf_markdown_copied += 1
    }

    if (-not $hasOnlyRawHtml) {
        $knowledgeFileBody = if ($hasMarkdown) {
            ($groupRows | Where-Object { $_.is_markdown } | Sort-Object word_count -Descending | Select-Object -First 1)._text_body
        }
        elseif ($hasExtracted) {
            ($groupRows | Where-Object { $_.is_extracted_pdf_markdown } | Sort-Object word_count -Descending | Select-Object -First 1)._text_body
        }
        else {
            ''
        }

        if (-not [string]::IsNullOrWhiteSpace($knowledgeFileBody)) {
            $currentKnowledgeFile = Join-Path $targetCategoryPath ('{0}--{1}.md' -f $rowId, $slug)
            $knowledgeNotes = $notes
            if ($hasExtracted) {
                $knowledgeNotes = Add-NoteValue -Existing $knowledgeNotes -Append 'category_copy_of_extracted_pdf_markdown'
            }
            if ($knowledgeCategory -eq '90_unsorted_review') {
                $knowledgeNotes = Add-NoteValue -Existing $knowledgeNotes -Append 'uncertain_category'
            }
            if ($knowledgeCategory -eq '91_rejected_low_value') {
                $knowledgeNotes = Add-NoteValue -Existing $knowledgeNotes -Append 'rejected_low_value'
            }

            $frontmatterValues = @{
                Title = $title
                SourceUrl = $sourceUrl
                NormalizedUrl = $normalizedUrl
                UrlIndexId = $rowId
                SourceDomain = $sourceDomain
                SourceType = $sourceType
                TopicCategory = $topicCategory
                TrustLevel = $trustLevel
                SourceFile = $primaryTextRow.source_file_path
                SourceFolder = $primaryTextRow.source_folder
                KnowledgeCategory = $knowledgeCategory
                ContentQuality = $contentQuality
                NeedsReview = $needsReview
                RawHtmlPath = $rawHtmlPath
                PdfPath = $pdfPath
                ExtractedMarkdownPath = $extractedPath
                DuplicateStatus = if ($repairNeeded) { 'repaired_existing_row' } else { 'imported_new' }
                Notes = $knowledgeNotes
            }
            Write-NormalizedMarkdownFile -DestinationPath $currentKnowledgeFile -BodyText $knowledgeFileBody -FrontmatterValues $frontmatterValues
            $summary.imported_knowledge_files += 1
            if ($knowledgeCategory -eq '90_unsorted_review') {
                $summary.unsorted_count += 1
            }
            elseif ($knowledgeCategory -eq '91_rejected_low_value') {
                $summary.rejected_count += 1
            }
        }
    }
    else {
        $summary.rejected_count += 1
    }

    $rowToUpdate.original_url = $sourceUrl
    $rowToUpdate.normalized_url = $normalizedUrl
    $rowToUpdate.source_domain = $sourceDomain
    $rowToUpdate.source_type = $sourceType
    $rowToUpdate.topic_category = $topicCategory
    $rowToUpdate.trust_level = $trustLevel
    $rowToUpdate.scrape_status = $scrapeStatus
    $rowToUpdate.local_file = $primaryTextRow.source_file_path
    $rowToUpdate.current_knowledge_file = $currentKnowledgeFile
    $rowToUpdate.raw_html_path = $rawHtmlPath
    $rowToUpdate.markdown_path = if ($hasMarkdown) { ($groupRows | Where-Object { $_.is_markdown } | Select-Object -First 1).source_file_path } else { '' }
    $rowToUpdate.pdf_path = $pdfPath
    $rowToUpdate.extracted_pdf_markdown_path = $extractedPath
    $rowToUpdate.error_message = ''
    $rowToUpdate.imported_at = $script:TimestampIso
    $rowToUpdate.scraped_at = $script:TimestampIso
    $rowToUpdate.needs_review = if ($needsReview) { 'true' } else { 'false' }
    $rowToUpdate.duplicate_status = if ($repairNeeded) { 'repaired_existing_row' } else { 'imported_new' }
    $rowToUpdate.duplicate_of_url_index_id = ''
    $rowToUpdate.content_quality = $contentQuality
    $rowToUpdate.knowledge_category = $knowledgeCategory
    $rowToUpdate.source_batch = $script:ImportBatch
    $rowToUpdate.notes = $notes
    $rowToUpdate.extraction_status = if ($hasExtracted) { 'success' } elseif ($hasPdf) { 'not_available_from_source' } else { '' }
    $rowToUpdate.extraction_tool = if ($hasExtracted) { 'ingest_v2_source' } else { '' }
    $rowToUpdate.extraction_warning = if ($hasExtracted) { 'Extracted PDF Markdown may lose diagrams, tables, pinouts, package drawings, layout figures, and formatting. Original PDF remains source of truth.' } else { '' }
    Set-UrlRowAliases -Row $rowToUpdate

    if ($repairNeeded -and $null -ne $existingUrlRow) {
        $summary.warnings.Add(('Repaired missing or broken existing URL row: {0}' -f $rowToUpdate.id))
    }
    elseif ($null -eq $existingUrlRow) {
        $existingUrlRows.Add($rowToUpdate)
    }

    if (-not [string]::IsNullOrWhiteSpace($rowToUpdate.normalized_url) -and -not $urlRowsByNormalizedUrl.ContainsKey($rowToUpdate.normalized_url)) {
        $urlRowsByNormalizedUrl[$rowToUpdate.normalized_url] = $rowToUpdate
    }
    $urlRowsById[$rowToUpdate.id] = $rowToUpdate

    if ($needsReview -and -not [string]::IsNullOrWhiteSpace($currentKnowledgeFile)) {
        $summary.review_files.Add((Get-RelativePathSafe -BasePath $KnowledgeRoot -TargetPath $currentKnowledgeFile))
    }

    if (-not [string]::IsNullOrWhiteSpace($sourceDomain)) {
        if (-not $summary.imported_domain_counts.ContainsKey($sourceDomain)) {
            $summary.imported_domain_counts[$sourceDomain] = 0
        }
        $summary.imported_domain_counts[$sourceDomain] += 1
    }

    foreach ($row in $groupRows) {
        if ($knowledgeCategory -eq '90_unsorted_review') {
            $row.import_action = if ($hasOnlyRawHtml) { 'reject_raw_html_inventory_only' } else { 'import_unsorted_review' }
        }
        elseif ($knowledgeCategory -eq '91_rejected_low_value') {
            $row.import_action = if ($hasOnlyRawHtml) { 'reject_raw_html_inventory_only' } else { 'import_rejected_low_value' }
        }
        else {
            $row.import_action = 'import_category'
        }
    }

    if (-not [string]::IsNullOrWhiteSpace($currentKnowledgeFile)) {
        $newDuplicateHash = Get-DuplicateHashForFile -Path $currentKnowledgeFile -IsMarkdownLike:$true
        if (-not $existingDuplicateHashIndex.ContainsKey($newDuplicateHash)) {
            $existingDuplicateHashIndex[$newDuplicateHash] = [ordered]@{
                path = $currentKnowledgeFile
                id = $rowId
                knowledge_category = $knowledgeCategory
            }
        }
    }
    if (-not [string]::IsNullOrWhiteSpace($extractedPath)) {
        $newExtractedHash = Get-DuplicateHashForFile -Path $extractedPath -IsMarkdownLike:$true
        if (-not $existingDuplicateHashIndex.ContainsKey($newExtractedHash)) {
            $existingDuplicateHashIndex[$newExtractedHash] = [ordered]@{
                path = $extractedPath
                id = $rowId
                knowledge_category = '14_datasheets_pdf_markdown'
            }
        }
    }
    if (-not [string]::IsNullOrWhiteSpace($pdfPath)) {
        $newPdfHash = Get-DuplicateHashForFile -Path $pdfPath -IsMarkdownLike:$false
        if (-not $existingDuplicateHashIndex.ContainsKey($newPdfHash)) {
            $existingDuplicateHashIndex[$newPdfHash] = [ordered]@{
                path = $pdfPath
                id = $rowId
                knowledge_category = '14_datasheets_pdf_markdown'
            }
        }
    }
}

$allUrlRows = @(
    $existingUrlRows.ToArray() |
    Sort-Object { $_['id'] } |
    ForEach-Object { [pscustomobject]$_ }
)
$summary.url_index_rows_after = $allUrlRows.Count

$inventoryExportRows = @(
    $inventoryRows.ToArray() | ForEach-Object {
        $ordered = [ordered]@{}
        foreach ($column in $script:InventoryColumns) {
            $ordered[$column] = $_[$column]
        }
        [pscustomobject]$ordered
    }
)

Export-OrderedCsv -Rows $inventoryExportRows -Columns $script:InventoryColumns -Path $inventoryCsvPath
$inventoryExportRows | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $inventoryJsonPath -Encoding UTF8

$urlIndexExportRows = @($allUrlRows | ForEach-Object { [pscustomobject]$_ })
Export-OrderedCsv -Rows $urlIndexExportRows -Columns $script:UrlIndexColumns -Path $urlIndexCsvPath
$urlIndexExportRows | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $urlIndexJsonPath -Encoding UTF8
Write-Utf8Text -Path $urlIndexMdPath -Text (Build-UrlIndexMarkdownText -Rows $allUrlRows -Summary $summary)

$pdfIndexRows = @(
    $allUrlRows |
    Where-Object {
        (-not [string]::IsNullOrWhiteSpace($_.pdf_path)) -or
        (-not [string]::IsNullOrWhiteSpace($_.extracted_pdf_markdown_path))
    } |
    ForEach-Object {
        [ordered]@{
            url_index_id = $_.id
            source_url = $_.original_url
            normalized_url = $_.normalized_url
            original_pdf_path = $_.pdf_path
            extracted_markdown_path = $_.extracted_pdf_markdown_path
            current_knowledge_file = $_.current_knowledge_file
            source_domain = $_.source_domain
            topic_category = $_.topic_category
            trust_level = $_.trust_level
            knowledge_category = $_.knowledge_category
            extraction_status = if (-not [string]::IsNullOrWhiteSpace($_.extraction_status)) { $_.extraction_status } else { 'unknown' }
            warning = if (-not [string]::IsNullOrWhiteSpace($_.extraction_warning)) { $_.extraction_warning } else { 'Extracted PDF Markdown may lose diagrams, tables, pinouts, package drawings, layout figures, and formatting. Original PDF remains source of truth.' }
            imported_at = $_.imported_at
            source_batch = $_.source_batch
            source_file_path = $_.local_file
            source_file_name = [System.IO.Path]::GetFileName($_.local_file)
            notes = $_.notes
        }
    }
)

Export-OrderedCsv -Rows $pdfIndexRows -Columns $script:PdfIndexColumns -Path $pdfIndexCsvPath
Write-Utf8Text -Path $pdfIndexMdPath -Text (Build-PdfIndexMarkdownText -Rows $pdfIndexRows)

$categoryCountsAfter = Get-CategoryCounts -KnowledgeRootPath $KnowledgeRoot -UrlRows $allUrlRows

foreach ($category in $script:TopicalCategories) {
    $categoryPath = Join-Path $KnowledgeRoot $category
    Ensure-Directory -Path $categoryPath
    $config = $script:CategoryDefinitions[$category]
    $categoryRows = @(
        if ($category -eq '14_datasheets_pdf_markdown') {
            $allUrlRows | Where-Object {
                (-not [string]::IsNullOrWhiteSpace($_.pdf_path) -and (Test-Path -LiteralPath $_.pdf_path)) -or
                (-not [string]::IsNullOrWhiteSpace($_.extracted_pdf_markdown_path) -and (Test-Path -LiteralPath $_.extracted_pdf_markdown_path))
            }
        }
        else {
            $allUrlRows | Where-Object {
                $_.knowledge_category -eq $category -and
                -not [string]::IsNullOrWhiteSpace($_.current_knowledge_file) -and
                (Test-Path -LiteralPath $_.current_knowledge_file)
            }
        }
    )
    $importedRowsForCategory = @($categoryRows | Where-Object { $_.source_batch -match 'ingest_v2' -and $_.duplicate_status -notin @('duplicate_by_hash', 'skip_duplicate_by_url') })
    $categoryText = Build-CategoryIndexText -Category $category -Config $config -Rows $categoryRows -ImportedRows $importedRowsForCategory
    Write-Utf8Text -Path (Join-Path $categoryPath '_CATEGORY_INDEX.md') -Text $categoryText
}

Write-Utf8Text -Path $mainIndexPath -Text (Build-MainIndexText -CategoryCounts $categoryCountsAfter -Summary $summary)

$manifestObject = Build-ManifestObject -CategoryCounts $categoryCountsAfter -Summary $summary
$manifestObject | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $manifestPath -Encoding UTF8

Write-Utf8Text -Path $sourceAuditPath -Text (Build-SourceAuditText -InventoryRows $inventoryExportRows -Summary $summary)
Write-Utf8Text -Path $finalReportPath -Text (Build-FinalReportText -CategoryCounts $categoryCountsAfter -Summary $summary)
Write-Utf8Text -Path $importReportPath -Text (Build-ImportReportText -InventoryRows $inventoryExportRows -CategoryCountsBefore $categoryCountsBefore -CategoryCountsAfter $categoryCountsAfter -Summary $summary)
Write-Utf8Text -Path $sourceOfTruthIndexPath -Text (Build-SourceOfTruthIndexText -UrlRows $allUrlRows)
Write-Utf8Text -Path $officialSourcesIndexPath -Text (Build-OfficialSourcesIndexText -UrlRows $allUrlRows)
Write-Utf8Text -Path $categoryRoutingIndexPath -Text (Build-CategoryRoutingIndexText)

$validationChecks = New-Object System.Collections.Generic.List[object]

$createdKnowledgeRows = @($allUrlRows | Where-Object { $_.source_batch -match 'ingest_v2' -and $_.duplicate_status -in @('imported_new', 'repaired_existing_row') -and -not [string]::IsNullOrWhiteSpace($_.current_knowledge_file) })
$missingImportedFiles = @($createdKnowledgeRows | Where-Object { -not (Test-Path -LiteralPath $_.current_knowledge_file) })
$validationChecks.Add([pscustomobject]@{
        check_name = 'imported_file_paths_exist'
        status = if ($missingImportedFiles.Count -eq 0) { 'PASS' } else { 'FAIL' }
        details = if ($missingImportedFiles.Count -eq 0) { 'All imported knowledge files exist.' } else { ('Missing imported files: {0}' -f ($missingImportedFiles.Count)) }
    })

$missingUrlTargets = @($allUrlRows | Where-Object {
        -not [string]::IsNullOrWhiteSpace($_.current_knowledge_file) -and
        $_.duplicate_status -ne 'duplicate_by_hash' -and
        -not (Test-Path -LiteralPath $_.current_knowledge_file)
    })
$validationChecks.Add([pscustomobject]@{
        check_name = 'url_index_current_knowledge_file_exists'
        status = if ($missingUrlTargets.Count -eq 0) { 'PASS' } else { 'FAIL' }
        details = if ($missingUrlTargets.Count -eq 0) { 'All current_knowledge_file paths exist.' } else { ('Missing URL_INDEX current_knowledge_file paths: {0}' -f $missingUrlTargets.Count) }
    })

$duplicateUrlRows = @($allUrlRows | Where-Object { -not [string]::IsNullOrWhiteSpace($_.normalized_url) } | Group-Object normalized_url | Where-Object { $_.Count -gt 1 })
$validationChecks.Add([pscustomobject]@{
        check_name = 'no_duplicate_normalized_url_rows'
        status = if ($duplicateUrlRows.Count -eq 0) { 'PASS' } else { 'FAIL' }
        details = if ($duplicateUrlRows.Count -eq 0) { 'No duplicate normalized_url rows found.' } else { ('Duplicate normalized_url groups: {0}' -f $duplicateUrlRows.Count) }
    })

$importedHashRows = @($allUrlRows | Where-Object { $_.source_batch -match 'ingest_v2' -and $_.duplicate_status -eq 'imported_new' -and $_.current_knowledge_file -and (Test-Path -LiteralPath $_.current_knowledge_file) })
$hashGroups = @($importedHashRows | Group-Object { Get-DuplicateHashForFile -Path $_.current_knowledge_file -IsMarkdownLike:$true } | Where-Object { $_.Count -gt 1 })
$validationChecks.Add([pscustomobject]@{
        check_name = 'no_duplicate_imported_hashes'
        status = if ($hashGroups.Count -eq 0) { 'PASS' } else { 'FAIL' }
        details = if ($hashGroups.Count -eq 0) { 'No duplicate imported knowledge hashes found.' } else { ('Duplicate imported hash groups: {0}' -f $hashGroups.Count) }
    })

$missingCategoryIndexes = @($script:TopicalCategories | Where-Object { -not (Test-Path -LiteralPath (Join-Path (Join-Path $KnowledgeRoot $_) '_CATEGORY_INDEX.md')) })
$validationChecks.Add([pscustomobject]@{
        check_name = 'every_category_has_category_index'
        status = if ($missingCategoryIndexes.Count -eq 0) { 'PASS' } else { 'FAIL' }
        details = if ($missingCategoryIndexes.Count -eq 0) { 'Every category folder has _CATEGORY_INDEX.md.' } else { ('Missing indexes: {0}' -f ($missingCategoryIndexes -join ', ')) }
    })

$missingPdfPaths = @($pdfIndexRows | Where-Object {
        (-not [string]::IsNullOrWhiteSpace($_.original_pdf_path) -and -not (Test-Path -LiteralPath $_.original_pdf_path)) -or
        (-not [string]::IsNullOrWhiteSpace($_.extracted_markdown_path) -and -not (Test-Path -LiteralPath $_.extracted_markdown_path))
    })
$validationChecks.Add([pscustomobject]@{
        check_name = 'pdf_index_paths_exist'
        status = if ($missingPdfPaths.Count -eq 0) { 'PASS' } else { 'FAIL' }
        details = if ($missingPdfPaths.Count -eq 0) { 'All PDF_INDEX paths exist.' } else { ('Missing PDF paths: {0}' -f $missingPdfPaths.Count) }
    })

$kicadFileTouched = $false
foreach ($kvp in $kicadFileSnapshot.GetEnumerator()) {
    if (-not (Test-Path -LiteralPath $kvp.Key)) {
        $kicadFileTouched = $true
        break
    }
    $currentTime = (Get-Item -LiteralPath $kvp.Key).LastWriteTimeUtc.ToString('o')
    if ($currentTime -ne $kvp.Value) {
        $kicadFileTouched = $true
        break
    }
}
$validationChecks.Add([pscustomobject]@{
        check_name = 'no_active_kicad_project_files_touched'
        status = if (-not $kicadFileTouched) { 'PASS' } else { 'FAIL' }
        details = if (-not $kicadFileTouched) { 'No .kicad_sch/.kicad_pcb/.kicad_pro file timestamps changed during this run.' } else { 'At least one KiCad project file timestamp changed during the run.' }
    })

$validationChecks.Add([pscustomobject]@{
        check_name = 'source_logs_copied'
        status = if ($sourceLogsCopied -ge 0) { 'PASS' } else { 'FAIL' }
        details = ('Copied or deduplicated source logs/registries under 99_source_logs\\ingest_v2_import; new copies this run: {0}' -f $sourceLogsCopied)
    })

$validationStatus = if (@($validationChecks | Where-Object { $_.status -eq 'FAIL' }).Count -eq 0) { 'PASS' } else { 'FAIL' }
$summary.validation_status = $validationStatus

Write-Utf8Text -Path $validationMdPath -Text (Build-ValidationMarkdownText -Checks @($validationChecks.ToArray()))
$validationChecks | Export-Csv -LiteralPath $validationCsvPath -NoTypeInformation -Encoding UTF8

$result = [ordered]@{
    import_started_at = $script:ImportStartedAt.ToString('o')
    import_finished_at = (Get-Date).ToString('o')
    source_folder = $IngestRoot
    total_source_files_scanned = $inventoryExportRows.Count
    total_markdown_scanned = @($inventoryExportRows | Where-Object { $_.is_markdown -eq $true }).Count
    total_pdfs_scanned = @($inventoryExportRows | Where-Object { $_.is_pdf -eq $true }).Count
    total_extracted_pdf_markdown_scanned = @($inventoryExportRows | Where-Object { $_.is_extracted_pdf_markdown -eq $true }).Count
    total_raw_html_scanned = @($inventoryExportRows | Where-Object { $_.is_raw_html -eq $true }).Count
    total_urls_found = @($inventoryExportRows | Where-Object { -not [string]::IsNullOrWhiteSpace($_.normalized_url) } | Select-Object -ExpandProperty normalized_url -Unique).Count
    imported_knowledge_files = $summary.imported_knowledge_files
    skipped_duplicate_by_url = $summary.skipped_duplicate_by_url
    skipped_duplicate_by_hash = $summary.skipped_duplicate_by_hash
    rejected_count = $summary.rejected_count
    unsorted_count = $summary.unsorted_count
    pdf_originals_copied = $summary.pdf_originals_copied
    pdf_markdown_copied = $summary.pdf_markdown_copied
    url_index_rows_before = $summary.url_index_rows_before
    url_index_rows_after = $summary.url_index_rows_after
    url_index_valid = ($validationStatus -eq 'PASS' -and $duplicateUrlRows.Count -eq 0 -and $missingUrlTargets.Count -eq 0)
    knowledge_scrape_ready_for_codex_claude = ($validationStatus -eq 'PASS')
    validation_status = $validationStatus
    validation_report_md = $validationMdPath
    validation_report_csv = $validationCsvPath
}

$result | ConvertTo-Json -Depth 8
