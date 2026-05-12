param(
    [string]$KnowledgeRoot = (Split-Path -Parent $PSScriptRoot),
    [string]$UrlIndexCsv = ''
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($UrlIndexCsv)) {
    $UrlIndexCsv = Join-Path $KnowledgeRoot 'URL_INDEX.csv'
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

function Parse-FrontmatterPreview {
    param([string[]]$Lines)

    $frontmatter = [ordered]@{}
    $bodyLines = New-Object System.Collections.Generic.List[string]
    if ($null -eq $Lines -or $Lines.Count -eq 0) {
        return [pscustomobject]@{
            frontmatter = $frontmatter
            body_lines = @()
        }
    }

    if ($Lines[0].Trim() -ne '---') {
        return [pscustomobject]@{
            frontmatter = $frontmatter
            body_lines = $Lines
        }
    }

    $endIndex = -1
    for ($i = 1; $i -lt $Lines.Count; $i += 1) {
        if ($Lines[$i].Trim() -eq '---') {
            $endIndex = $i
            break
        }
        if ($Lines[$i] -match '^\s*([A-Za-z0-9_]+):\s*(.*)\s*$') {
            $key = $Matches[1]
            $value = $Matches[2].Trim()
            if (($value.StartsWith("'") -and $value.EndsWith("'")) -or ($value.StartsWith('"') -and $value.EndsWith('"'))) {
                $value = $value.Substring(1, $value.Length - 2)
                $value = $value -replace "''", "'"
            }
            $frontmatter[$key] = $value
        }
    }

    if ($endIndex -ge 0) {
        for ($i = $endIndex + 1; $i -lt $Lines.Count; $i += 1) {
            $bodyLines.Add($Lines[$i])
        }
    }
    else {
        foreach ($line in $Lines) {
            $bodyLines.Add($line)
        }
    }

    return [pscustomobject]@{
        frontmatter = $frontmatter
        body_lines = @($bodyLines)
    }
}

function Get-FirstHeading {
    param([string[]]$Lines)

    foreach ($line in $Lines) {
        if ($line -match '^\s*#{1,6}\s+(.+?)\s*$') {
            return $Matches[1].Trim()
        }
    }
    return $null
}

function Get-FirstNonEmptyLine {
    param([string[]]$Lines)

    foreach ($line in $Lines) {
        $trimmed = $line.Trim()
        if (-not [string]::IsNullOrWhiteSpace($trimmed)) {
            return $trimmed
        }
    }
    return $null
}

function Get-QualityRank {
    param([string]$Quality)

    switch ($Quality) {
        'high' { return 4 }
        'medium' { return 3 }
        'low' { return 2 }
        'unknown' { return 1 }
        'junk' { return 0 }
        default { return 1 }
    }
}

function Get-TruthRank {
    param([string]$SourceOfTruth)

    if ($SourceOfTruth -match '^(\d+)_') {
        $level = [int]$Matches[1]
        return (9 - $level)
    }
    return 0
}

function Get-StatusRank {
    param([string]$Status)

    switch ($Status) {
        'success' { return 6 }
        'needs_rescrape' { return 4 }
        'unknown' { return 3 }
        'not_found_in_outputs' { return 2 }
        'failed' { return 1 }
        'rejected' { return 0 }
        default { return 0 }
    }
}

function Get-FileUsefulnessScore {
    param([pscustomobject]$Record)

    $score = 0
    $score += (Get-TruthRank -SourceOfTruth $Record.source_of_truth_level) * 20
    $score += (Get-QualityRank -Quality $Record.content_quality) * 15
    if ($Record.scraped_status -eq 'success') { $score += 20 }
    if ($Record.scraped_status -eq 'needs_rescrape') { $score += 8 }
    if ($Record.source_domain -match '(^|\.)(kicad\.org|docs\.kicad\.org|dev-docs\.kicad\.org|espressif\.com|ti\.com|microchip\.com|st\.com|raspberrypi\.com|silabs\.com|infineon\.com|renesas\.com|onsemi\.com|rohm\.com|we-online\.com|jlcpcb\.com|pcbway\.com|oshpark\.com|eurocircuits\.com)$') {
        $score += 12
    }

    $text = ('{0} {1} {2}' -f $Record.title, $Record.source_url, $Record.sample_text).ToLowerInvariant()
    foreach ($keyword in @('datasheet', 'reference manual', 'technical reference manual', 'hardware design', 'app note', 'design guide', 'layout', 'usb', 'esd', 'buck', 'drc', 'erc', 'footprint', 'symbol', 'antenna')) {
        if ($text.Contains($keyword)) {
            $score += 4
        }
    }

    if ($Record.category -eq '91_rejected_low_value') {
        $score -= 40
    }
    if ($Record.category -eq '12_forums_peer_review') {
        $score -= 15
    }
    if ($Record.category -eq '15_video_reference_index') {
        $score -= 20
    }
    if ($Record.content_quality -eq 'junk') {
        $score -= 20
    }
    return $score
}

function Get-RowScore {
    param($Row)

    $score = 0
    $score += (Get-TruthRank -SourceOfTruth $Row.source_of_truth_level) * 20
    $score += (Get-QualityRank -Quality $Row.content_quality) * 10
    $score += (Get-StatusRank -Status $Row.scraped_status) * 8
    if (-not [string]::IsNullOrWhiteSpace($Row.current_knowledge_file)) { $score += 8 }
    if ($Row.needs_future_rescrape -eq 'true') { $score -= 2 }
    return $score
}

function Get-PlainTopicTokens {
    param(
        [string[]]$Texts,
        [int]$MaxCount = 12
    )

    $stopwords = @(
        'the','and','for','with','from','that','this','into','using','used','use','how','when','where','which','will','should','must','can','not',
        'are','was','were','have','has','had','its','their','there','here','than','then','into','onto','over','under','about','after','before',
        'through','within','without','between','also','only','more','most','some','many','each','such','other','same','these','those','your',
        'page','pages','table','tables','figure','figures','section','sections','chapter','appendix','document','documents','guide','guidelines',
        'manual','reference','references','application','note','notes','design','file','files','folder','folders','source','sources','local',
        'markdown','pdf','kicad','pcb','board','series','version','html','data','output','index','category','categories','value','low','high',
        'medium','unknown','url','urls','www','com','org','net','https','http','en','pdfpdf','javascript','home','main','void','20void',
        'warning','warnings','truth','original','extraction','formatting','incomplete','drawings','diagrams','pinouts','tables'
    )
    $stopSet = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
    foreach ($word in $stopwords) { [void]$stopSet.Add($word) }

    $counts = @{}
    foreach ($text in $Texts) {
        if ([string]::IsNullOrWhiteSpace($text)) { continue }
        $normalized = $text.ToLowerInvariant()
        $normalized = $normalized -replace '[^a-z0-9\+\-_/ ]', ' '
        foreach ($token in ($normalized -split '\s+')) {
            if ([string]::IsNullOrWhiteSpace($token)) { continue }
            if ($token.Length -lt 3) { continue }
            if ($token -match '^\d+$') { continue }
            if ($token.Contains('/')) { continue }
            if ($token -match '^www') { continue }
            if ($token -match '^page\d+$') { continue }
            if ($stopSet.Contains($token)) { continue }
            if (-not $counts.ContainsKey($token)) {
                $counts[$token] = 0
            }
            $counts[$token] += 1
        }
    }

    return @(
        $counts.GetEnumerator() |
        Sort-Object -Property @{ Expression = 'Value'; Descending = $true }, @{ Expression = 'Key'; Descending = $false } |
        Select-Object -First $MaxCount |
        ForEach-Object { $_.Key }
    )
}

function Get-CategoryConfig {
    param([string]$Category)

    $map = @{
        '01_kicad_core' = @{
            purpose = 'Official KiCad core manuals, editor behavior, CLI references, and tool usage documentation.'
            usage = 'Start here for KiCad behavior, pcbnew, eeschema, GerbView, CLI usage, and official workflow questions.'
            warning = 'Prefer this folder over forums for KiCad behavior questions.'
        }
        '02_kicad_python_api' = @{
            purpose = 'KiCad Python API, pcbnew scripting, bindings, and automation references.'
            usage = 'Use this folder before proposing automation, scripted edits, or KiCad API usage.'
            warning = 'API examples still need verification against the target KiCad version.'
        }
        '03_kicad_file_formats' = @{
            purpose = 'KiCad file-format structure, S-expression format details, and schema-like references.'
            usage = 'Use this folder when parsing, generating, or diffing KiCad project files programmatically.'
            warning = 'Do not modify live design files until the format assumptions are verified.'
        }
        '04_kicad_libraries_symbols_footprints' = @{
            purpose = 'KiCad library conventions, KLC-style rules, symbols, footprints, and package references.'
            usage = 'Use this folder for footprint policy, symbol conventions, and library-quality decisions.'
            warning = 'Library entries are not proof. Cross-check package and land pattern against the original datasheet PDF.'
        }
        '05_esp32_espressif' = @{
            purpose = 'Espressif datasheets, technical reference manuals, and ESP32 hardware design guidance.'
            usage = 'Start here for ESP32-family selection, pin functions, power domains, RF notes, and hardware design rules.'
            warning = 'Pinouts, antenna rules, and layout guidance should still be confirmed in the original PDF when details matter.'
        }
        '06_microcontrollers' = @{
            purpose = 'Non-Espressif MCU vendor references, datasheets, and device-family documentation.'
            usage = 'Use this folder for STM32, Microchip, RP2040, RP2350, Nordic, Renesas, Infineon, WCH, and similar MCU questions.'
            warning = 'Part-number and package variants matter. Verify exact pinout and package from the original vendor PDF.'
        }
        '07_usb_c_high_speed_esd' = @{
            purpose = 'USB, USB-C, differential routing, ESD protection, and high-speed layout material.'
            usage = 'Use this folder for connector-side protection, pair routing, return path, and interface-layout decisions.'
            warning = 'USB-C role logic and ESD placement should be checked against official controller, connector, and protection sources.'
        }
        '08_power_buck_regulators' = @{
            purpose = 'Switch-mode power, buck regulators, power components, and layout-focused application material.'
            usage = 'Use this folder for regulator choice, power-stage layout, switching-loop control, and related app notes.'
            warning = 'Buck layout decisions should be backed by datasheet and app-note references, not generic blog advice.'
        }
        '09_pcb_layout_grounding_emi_si' = @{
            purpose = 'General PCB layout, grounding, EMI, EMC, RF, and signal-integrity guidance.'
            usage = 'Use this folder for return path, decoupling placement, crosstalk, grounding, and antenna-adjacent layout questions.'
            warning = 'Treat broad layout advice as context. Cross-check critical rules against the actual interface or component datasheet.'
        }
        '10_dfm_fabrication_assembly' = @{
            purpose = 'Fabrication and assembly constraints, board-house guidance, and DFM-related rules.'
            usage = 'Use this folder for annular ring, solder mask, panelization, stackup, assembly, and manufacturability checks.'
            warning = 'Fabricator rules differ. Always match the final recommendation to the actual selected board house.'
        }
        '11_calculators_ipc_reference' = @{
            purpose = 'Trace, impedance, and IPC-style calculator references and supporting notes.'
            usage = 'Use this folder for quick calculations and starting values for current, width, impedance, and clearances.'
            warning = 'Calculators are starting points only and must be checked against real stackup, copper weight, and thermal assumptions.'
        }
        '12_forums_peer_review' = @{
            purpose = 'Forum and peer-review material with design discussions and troubleshooting context.'
            usage = 'Use this folder after official sources to gather peer-review patterns, pitfalls, or alternative approaches.'
            warning = 'Forum material is not primary authority. Do not base final engineering claims on this folder alone.'
        }
        '13_vendor_parts_cad_models' = @{
            purpose = 'Vendor and marketplace parts portals, CAD models, and component library sources.'
            usage = 'Use this folder to locate part models, supplier references, or library-download paths.'
            warning = 'Vendor models and marketplace footprints still require package, pin-1, and land-pattern verification.'
        }
        '14_datasheets_pdf_markdown' = @{
            purpose = 'Canonical PDF corpus: original PDFs, extracted Markdown, and extraction logs.'
            usage = 'Use this folder to search extracted PDF text quickly, then open the original PDF for exact engineering details.'
            warning = 'Extracted Markdown is not the source of truth for pinouts, figures, tables, or package drawings.'
        }
        '15_video_reference_index' = @{
            purpose = 'Video and media-reference pointers.'
            usage = 'Use this folder only as a pointer to videos or media sources after higher-trust sources are checked.'
            warning = 'Video references are not authoritative engineering proof.'
        }
        '90_unsorted_review' = @{
            purpose = 'Temporary holding area for files that have not been confidently categorized.'
            usage = 'Use this folder only when triaging uncertain content or improving classification coverage.'
            warning = 'Files here are unresolved by definition and should not be treated as polished references.'
        }
        '91_rejected_low_value' = @{
            purpose = 'Low-value scrape artifacts such as search pages, noisy navigation pages, captcha pages, and weak-content output.'
            usage = 'Use this folder only to diagnose coverage gaps, scrape quality problems, or duplicate sources.'
            warning = 'Do not treat this folder as engineering authority without corroboration from higher-trust sources.'
        }
    }

    if ($map.ContainsKey($Category)) {
        return $map[$Category]
    }

    return @{
        purpose = 'Category-specific knowledge folder.'
        usage = 'Use this folder when it clearly matches the topic and a higher-trust folder is not more appropriate.'
        warning = 'Cross-check claims against URL_INDEX and higher-trust sources.'
    }
}

function Test-RowMatchesCategory {
    param(
        $Row,
        [string]$Category
    )

    if ($Category -eq '14_datasheets_pdf_markdown') {
        return (
            $Row.source_file_type -in @('pdf', 'pdf_pdf') -or
            -not [string]::IsNullOrWhiteSpace($Row.original_pdf_path) -or
            -not [string]::IsNullOrWhiteSpace($Row.extracted_markdown_path)
        )
    }

    if ($Row.detected_category -eq $Category) {
        return $true
    }

    if (-not [string]::IsNullOrWhiteSpace($Row.current_knowledge_file)) {
        foreach ($path in ($Row.current_knowledge_file -split ';\s*')) {
            if ($path.StartsWith($Category + '\', [System.StringComparison]::OrdinalIgnoreCase)) {
                return $true
            }
        }
    }

    return $false
}

function Get-FileRecordsForCategory {
    param(
        [string]$Category,
        [string]$CategoryPath,
        $IdToRow,
        $RelativePathToRows
    )

    if (-not (Test-Path -LiteralPath $CategoryPath)) {
        return @()
    }

    if ($Category -eq '14_datasheets_pdf_markdown') {
        $searchRoot = Join-Path $CategoryPath 'extracted_markdown'
        if (-not (Test-Path -LiteralPath $searchRoot)) {
            return @()
        }
        $files = @(Get-ChildItem -LiteralPath $searchRoot -File -Filter '*.md' | Sort-Object Name)
    }
    else {
        $files = @(
            Get-ChildItem -LiteralPath $CategoryPath -Recurse -File -Filter '*.md' |
            Where-Object {
                $_.Name -ne '_CATEGORY_INDEX.md' -and
                $_.Name -ne 'PDF_INDEX.md'
            } |
            Sort-Object FullName
        )
    }

    $records = New-Object System.Collections.Generic.List[object]
    foreach ($file in $files) {
        $relativePath = Get-RelativePath -BasePath $KnowledgeRoot -TargetPath $file.FullName
        $lines = @(Get-Content -LiteralPath $file.FullName -TotalCount 40)
        $preview = Parse-FrontmatterPreview -Lines $lines
        $frontmatter = $preview.frontmatter
        $title = if ($frontmatter.Contains('title') -and -not [string]::IsNullOrWhiteSpace($frontmatter['title'])) {
            $frontmatter['title']
        }
        else {
            $heading = Get-FirstHeading -Lines $preview.body_lines
            if (-not [string]::IsNullOrWhiteSpace($heading)) {
                $heading
            }
            else {
                [System.IO.Path]::GetFileNameWithoutExtension($file.Name)
            }
        }

        $sampleLines = @(
            $preview.body_lines |
            Where-Object {
                $_ -notmatch '^\s*>\s*PDF extraction warning:' -and
                $_ -notmatch '^\s*\[PAGE\s+\d+\]\s*$'
            } |
            Select-Object -First 20
        )
        $firstTextLine = Get-FirstNonEmptyLine -Lines $sampleLines
        $sampleText = (($sampleLines -join ' ') -replace '\s+', ' ').Trim()
        $urlIndexId = if ($frontmatter.Contains('url_index_id')) { $frontmatter['url_index_id'] } else { '' }

        $row = $null
        if (-not [string]::IsNullOrWhiteSpace($urlIndexId) -and $IdToRow.ContainsKey($urlIndexId)) {
            $row = $IdToRow[$urlIndexId]
        }
        elseif ($RelativePathToRows.ContainsKey($relativePath)) {
            $row = @($RelativePathToRows[$relativePath])[0]
            if ($null -ne $row -and [string]::IsNullOrWhiteSpace($urlIndexId)) {
                $urlIndexId = $row.id
            }
        }

        $sourceDomain = ''
        $sourceTruthLevel = ''
        $contentQuality = ''
        $scrapedStatus = ''
        $sourceUrl = ''

        if ($null -ne $row) {
            $sourceDomain = $row.source_domain
            $sourceTruthLevel = $row.source_of_truth_level
            $contentQuality = $row.content_quality
            $scrapedStatus = $row.scraped_status
            $sourceUrl = if (-not [string]::IsNullOrWhiteSpace($row.original_url)) { $row.original_url } else { $row.normalized_url }
        }

        if ([string]::IsNullOrWhiteSpace($sourceDomain) -and $frontmatter.Contains('source_domain')) { $sourceDomain = $frontmatter['source_domain'] }
        if ([string]::IsNullOrWhiteSpace($sourceTruthLevel) -and $frontmatter.Contains('source_of_truth_level')) { $sourceTruthLevel = $frontmatter['source_of_truth_level'] }
        if ([string]::IsNullOrWhiteSpace($contentQuality) -and $frontmatter.Contains('content_quality')) { $contentQuality = $frontmatter['content_quality'] }
        if ([string]::IsNullOrWhiteSpace($sourceUrl) -and $frontmatter.Contains('source_url')) { $sourceUrl = $frontmatter['source_url'] }

        $record = [pscustomobject][ordered]@{
            category = $Category
            relative_path = $relativePath
            file_name = $file.Name
            title = $title
            first_text_line = $firstTextLine
            sample_text = $sampleText
            url_index_id = $urlIndexId
            source_url = $sourceUrl
            source_domain = $sourceDomain
            source_of_truth_level = $sourceTruthLevel
            content_quality = if ([string]::IsNullOrWhiteSpace($contentQuality)) { 'unknown' } else { $contentQuality }
            scraped_status = if ([string]::IsNullOrWhiteSpace($scrapedStatus)) { 'unknown' } else { $scrapedStatus }
        }

        Add-Member -InputObject $record -MemberType NoteProperty -Name usefulness_score -Value (Get-FileUsefulnessScore -Record $record)
        $records.Add($record)
    }

    return @($records.ToArray())
}

function Write-CategoryIndex {
    param(
        [string]$Category,
        [string]$CategoryPath,
        [hashtable]$Config,
        [object[]]$FileRecords,
        [object[]]$CategoryRows,
        [string]$GeneratedAt
    )

    $lines = New-Object System.Collections.Generic.List[string]
    $lines.Add(('# {0} Category Index' -f $Category))
    $lines.Add('')
    $lines.Add(('Generated at: `{0}`' -f $GeneratedAt))
    $lines.Add('')
    $lines.Add('## Purpose')
    $lines.Add('')
    $lines.Add($Config.purpose)
    $lines.Add('')
    $lines.Add('## Summary')
    $lines.Add('')

    $fileCount = $FileRecords.Count
    $sourceDomainCount = @(
        $FileRecords |
        Where-Object { -not [string]::IsNullOrWhiteSpace($_.source_domain) } |
        Select-Object -ExpandProperty source_domain -Unique
    ).Count
    $rowCount = $CategoryRows.Count
    $failedLikeCount = @($CategoryRows | Where-Object { $_.scraped_status -in @('failed', 'not_found_in_outputs', 'needs_rescrape') }).Count
    $lowQualityCount = @($CategoryRows | Where-Object { $_.content_quality -in @('low', 'junk') }).Count

    $lines.Add(('- File count: `{0}`' -f $fileCount))
    if ($Category -eq '14_datasheets_pdf_markdown') {
        $pdfOriginalCount = @(
            Get-ChildItem -LiteralPath (Join-Path $CategoryPath 'original_pdf') -File -ErrorAction SilentlyContinue |
            Where-Object { $_.Name.ToLowerInvariant().EndsWith('.pdf') -or $_.Name.ToLowerInvariant().EndsWith('.pdf.pdf') }
        ).Count
        $lines.Add(('- Original PDF count: `{0}`' -f $pdfOriginalCount))
    }
    $lines.Add(('- Source domain count: `{0}`' -f $sourceDomainCount))
    $lines.Add(('- URL_INDEX rows associated with category: `{0}`' -f $rowCount))
    $lines.Add(('- Failed, missing, or rescrape-needed URLs: `{0}`' -f $failedLikeCount))
    $lines.Add(('- Low or junk quality URL_INDEX rows: `{0}`' -f $lowQualityCount))
    $lines.Add('')

    $lines.Add('## Trust-Level Summary')
    $lines.Add('')
    $trustSummary = @(
        $FileRecords |
        Group-Object source_of_truth_level |
        Sort-Object -Property @{ Expression = 'Count'; Descending = $true }, @{ Expression = 'Name'; Descending = $false }
    )
    if ($trustSummary.Count -eq 0) {
        $trustSummary = @(
            $CategoryRows |
            Group-Object source_of_truth_level |
            Sort-Object -Property @{ Expression = 'Count'; Descending = $true }, @{ Expression = 'Name'; Descending = $false }
        )
    }

    if ($trustSummary.Count -eq 0) {
        $lines.Add('- No trust metadata available yet.')
    }
    else {
        foreach ($group in $trustSummary) {
            $label = if ([string]::IsNullOrWhiteSpace($group.Name)) { '(unknown)' } else { $group.Name }
            $lines.Add(('- `{0}`: `{1}`' -f $label, $group.Count))
        }
    }
    $lines.Add('')

    $lines.Add('## Top 25 Useful-Looking Files')
    $lines.Add('')
    if ($FileRecords.Count -eq 0) {
        $lines.Add('- No local Markdown files currently in this category.')
    }
    else {
        $lines.Add('| File | Title | URL_INDEX ID | Trust | Quality | Domain |')
        $lines.Add('| --- | --- | --- | --- | --- | --- |')
        foreach ($record in ($FileRecords | Sort-Object -Property @{ Expression = 'usefulness_score'; Descending = $true }, @{ Expression = 'title'; Descending = $false } | Select-Object -First 25)) {
            $fullTargetPath = Join-Path $KnowledgeRoot $record.relative_path
            $linkTarget = Get-RelativePath -BasePath $CategoryPath -TargetPath $fullTargetPath
            $fileLink = '[{0}]({1})' -f $record.file_name, ($linkTarget.Replace('\', '/'))
            $titleText = if ([string]::IsNullOrWhiteSpace($record.title)) { '(untitled)' } else { $record.title.Replace('|', '\|') }
            $idText = if ([string]::IsNullOrWhiteSpace($record.url_index_id)) { '' } else { $record.url_index_id }
            $trustText = if ([string]::IsNullOrWhiteSpace($record.source_of_truth_level)) { '' } else { $record.source_of_truth_level }
            $qualityText = if ([string]::IsNullOrWhiteSpace($record.content_quality)) { '' } else { $record.content_quality }
            $domainText = if ([string]::IsNullOrWhiteSpace($record.source_domain)) { '' } else { $record.source_domain }
            $lines.Add(('| {0} | {1} | `{2}` | `{3}` | `{4}` | `{5}` |' -f $fileLink, $titleText, $idText, $trustText, $qualityText, $domainText))
        }
    }
    $lines.Add('')

    $lines.Add('## Top Source URLs From URL_INDEX')
    $lines.Add('')
    $urlRows = @(
        $CategoryRows |
        Sort-Object @{ Expression = { Get-RowScore $_ }; Descending = $true }, @{ Expression = 'id'; Descending = $false }
    )
    if ($urlRows.Count -eq 0) {
        $lines.Add('- No matching URL_INDEX rows found for this category.')
    }
    else {
        foreach ($row in ($urlRows | Select-Object -First 10)) {
            $urlText = if (-not [string]::IsNullOrWhiteSpace($row.original_url)) { $row.original_url } else { $row.normalized_url }
            $lines.Add(('- `{0}` `{1}` `{2}` `{3}`' -f $row.id, $row.scraped_status, $row.content_quality, $urlText))
        }
    }
    $lines.Add('')

    $lines.Add('## Common Topics Found')
    $lines.Add('')
    $topicTexts = @(
        $FileRecords |
        ForEach-Object { '{0} {1} {2}' -f $_.title, $_.file_name, $_.sample_text }
    )
    $topicTokens = @(Get-PlainTopicTokens -Texts $topicTexts -MaxCount 12)
    if ($topicTokens.Count -eq 0) {
        $lines.Add('- No reliable topic tokens found yet.')
    }
    else {
        $lines.Add(('- `{0}`' -f ($topicTokens -join '`, `')))
    }
    $lines.Add('')

    $lines.Add('## How Codex Or Claude Should Use This Folder')
    $lines.Add('')
    $lines.Add(('- {0}' -f $Config.usage))
    if ($Category -eq '14_datasheets_pdf_markdown') {
        $lines.Add('- Search extracted Markdown first, then confirm details in the original PDF before making a precise engineering claim.')
    }
    elseif ($Category -eq '91_rejected_low_value') {
        $lines.Add('- Use this folder only when diagnosing scrape failures, duplicates, or missing coverage in higher-trust folders.')
    }
    else {
        $lines.Add('- Use the local file plus `source_url` and `url_index_id` to keep claims traceable back to `URL_INDEX`.')
    }
    $lines.Add('')

    $lines.Add('## Warnings')
    $lines.Add('')
    $warnings = New-Object System.Collections.Generic.List[string]
    $warnings.Add($Config.warning)
    if ($CategoryRows.Count -gt 0) {
        $lowOrJunkRatio = ($lowQualityCount / [double]$CategoryRows.Count)
        if ($lowOrJunkRatio -ge 0.25) {
            $warnings.Add(('A significant share of associated URLs are low or junk quality: {0} of {1}.' -f $lowQualityCount, $CategoryRows.Count))
        }
    }
    if ($Category -in @('12_forums_peer_review', '15_video_reference_index')) {
        $warnings.Add('Do not treat this folder as primary engineering authority without corroboration from datasheets or official docs.')
    }
    foreach ($warning in ($warnings | Select-Object -Unique)) {
        $lines.Add(('- {0}' -f $warning))
    }
    $lines.Add('')

    $lines.Add('## Future Scraping Notes')
    $lines.Add('')
    if ($CategoryRows.Count -eq 0) {
        $lines.Add('- No category-linked URL_INDEX rows are currently tracked.')
    }
    else {
        $needsRescrapeCount = @($CategoryRows | Where-Object { $_.needs_future_rescrape -eq 'true' }).Count
        $rejectedCount = @($CategoryRows | Where-Object { $_.scraped_status -eq 'rejected' }).Count
        if ($failedLikeCount -eq 0 -and $needsRescrapeCount -eq 0 -and $rejectedCount -eq 0) {
            $lines.Add('- No strong future-scrape signal in current URL_INDEX rows for this category.')
        }
        else {
            if ($failedLikeCount -gt 0) {
                $lines.Add(('- `{0}` URLs are failed, missing, or marked `needs_rescrape`.' -f $failedLikeCount))
            }
            if ($needsRescrapeCount -gt 0) {
                $lines.Add(('- `{0}` URLs are explicitly flagged for future rescrape.' -f $needsRescrapeCount))
            }
            if ($rejectedCount -gt 0) {
                $lines.Add(('- `{0}` URLs are rejected and should only be revisited if a better canonical source is found.' -f $rejectedCount))
            }
            $lines.Add('- Review `RESCRAPE_QUEUE.csv` before adding or replacing sources for this category.')
        }
    }

    $outputPath = Join-Path $CategoryPath '_CATEGORY_INDEX.md'
    $lines | Set-Content -LiteralPath $outputPath -Encoding UTF8
}

if (-not (Test-Path -LiteralPath $UrlIndexCsv)) {
    throw ('URL_INDEX.csv not found: {0}' -f $UrlIndexCsv)
}

$generatedAt = (Get-Date).ToString('s')
$categoryNames = @(
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
    '14_datasheets_pdf_markdown',
    '15_video_reference_index',
    '90_unsorted_review',
    '91_rejected_low_value'
)

$urlRows = @(Import-Csv -LiteralPath $UrlIndexCsv)
$idToRow = @{}
$relativePathToRows = @{}

foreach ($row in $urlRows) {
    if (-not [string]::IsNullOrWhiteSpace($row.id)) {
        $idToRow[$row.id] = $row
    }

    $pathFields = @()
    if (-not [string]::IsNullOrWhiteSpace($row.current_knowledge_file)) {
        $pathFields += @($row.current_knowledge_file -split ';\s*')
    }
    if (-not [string]::IsNullOrWhiteSpace($row.extracted_markdown_path)) {
        $pathFields += $row.extracted_markdown_path
    }

    foreach ($relativePath in $pathFields) {
        if ([string]::IsNullOrWhiteSpace($relativePath)) { continue }
        if (-not $relativePathToRows.ContainsKey($relativePath)) {
            $relativePathToRows[$relativePath] = New-Object System.Collections.Generic.List[object]
        }
        $relativePathToRows[$relativePath].Add($row)
    }
}

$categoryFileCounts = [ordered]@{}
$categoryIndexRows = New-Object System.Collections.Generic.List[object]

foreach ($category in $categoryNames) {
    $categoryPath = Join-Path $KnowledgeRoot $category
    $config = Get-CategoryConfig -Category $category
    $fileRecords = @(Get-FileRecordsForCategory -Category $category -CategoryPath $categoryPath -IdToRow $idToRow -RelativePathToRows $relativePathToRows)
    $categoryRows = @($urlRows | Where-Object { Test-RowMatchesCategory -Row $_ -Category $category })

    Write-CategoryIndex -Category $category -CategoryPath $categoryPath -Config $config -FileRecords $fileRecords -CategoryRows $categoryRows -GeneratedAt $generatedAt

    $categoryFileCounts[$category] = $fileRecords.Count
    $categoryIndexRows.Add([pscustomobject][ordered]@{
            category = $category
            file_count = $fileRecords.Count
            url_index_rows = $categoryRows.Count
            category_index_file = ('{0}\_CATEGORY_INDEX.md' -f $category)
        })
}

$allTopLevelCategories = [ordered]@{
    '00_ai_entrypoints' = @(Get-ChildItem -LiteralPath (Join-Path $KnowledgeRoot '00_ai_entrypoints') -File -Filter '*.md' | Where-Object { $_.Name -ne '.gitkeep' }).Count
    '00_source_of_truth' = @(Get-ChildItem -LiteralPath (Join-Path $KnowledgeRoot '00_source_of_truth') -Recurse -File -Filter '*.md' -ErrorAction SilentlyContinue | Where-Object { $_.Name -ne '.gitkeep' }).Count
    '00_engineering_rules' = @(Get-ChildItem -LiteralPath (Join-Path $KnowledgeRoot '00_engineering_rules') -Recurse -File -Filter '*.md' -ErrorAction SilentlyContinue | Where-Object { $_.Name -ne '.gitkeep' }).Count
    '00_retrieval_indexes' = @(Get-ChildItem -LiteralPath (Join-Path $KnowledgeRoot '00_retrieval_indexes') -Recurse -File -Filter '*.md' -ErrorAction SilentlyContinue | Where-Object { $_.Name -ne '.gitkeep' }).Count
}
foreach ($row in $categoryIndexRows) {
    $allTopLevelCategories[$row.category] = $row.file_count
}
$allTopLevelCategories['99_source_logs'] = @(Get-ChildItem -LiteralPath (Join-Path $KnowledgeRoot '99_source_logs') -Recurse -File -Filter '*.md' -ErrorAction SilentlyContinue).Count

$indexLines = New-Object System.Collections.Generic.List[string]
$indexLines.Add('# knowledge_scrape Index')
$indexLines.Add('')
$indexLines.Add(('Updated at: `{0}`' -f $generatedAt))
$indexLines.Add('')
$indexLines.Add('## Start Here')
$indexLines.Add('')
$indexLines.Add('- [README.md](README.md): high-level purpose and operating rules.')
$indexLines.Add('- [00_ai_entrypoints/AI_START_HERE.md](00_ai_entrypoints/AI_START_HERE.md): default start sequence for Codex or Claude.')
$indexLines.Add('- [00_source_of_truth/SOURCE_OF_TRUTH_INDEX.md](00_source_of_truth/SOURCE_OF_TRUTH_INDEX.md): preferred official-source routing and source-of-truth usage.')
$indexLines.Add('- [00_engineering_rules/PCB_LAYOUT_RULES.md](00_engineering_rules/PCB_LAYOUT_RULES.md): compact engineering-rule entrypoints for repeated design decisions.')
$indexLines.Add('- [00_retrieval_indexes/CATEGORY_ROUTING_INDEX.md](00_retrieval_indexes/CATEGORY_ROUTING_INDEX.md): quick retrieval routing across folders, source tiers, and rejected recovery.')
$indexLines.Add('- [00_ai_entrypoints/KNOWLEDGE_MAP.md](00_ai_entrypoints/KNOWLEDGE_MAP.md): folder-by-folder usage map.')
$indexLines.Add('- [00_ai_entrypoints/SOURCE_TRUST_RULES.md](00_ai_entrypoints/SOURCE_TRUST_RULES.md): source hierarchy and mandatory cross-check rules.')
$indexLines.Add('- [00_ai_entrypoints/URL_REGISTRY_USAGE.md](00_ai_entrypoints/URL_REGISTRY_USAGE.md): how to use and maintain `URL_INDEX`.')
$indexLines.Add('')
$indexLines.Add('## Core Artifacts')
$indexLines.Add('')
$indexLines.Add('- `SOURCE_AUDIT.md`: scrape input inventory summary.')
$indexLines.Add('- `URL_INDEX.csv/json/md`: canonical URL registry with cleaned knowledge-file links.')
$indexLines.Add('- `RESCRAPE_QUEUE.csv`: follow-up scrape targets and recommended recovery methods.')
$indexLines.Add('- `FINAL_KNOWLEDGE_SCRAPE_REPORT.md`: scrape QA and readiness summary.')
$indexLines.Add('- `STRUCTURE_IMPROVEMENT_REPORT.md`: recovery/move report for the knowledge-base usability pass.')
$indexLines.Add('- `_scripts/06_build_category_indexes.ps1`: category-index builder.')
$indexLines.Add('- `14_datasheets_pdf_markdown/PDF_INDEX.csv/md`: PDF extraction inventory and summary.')
$indexLines.Add('')
$indexLines.Add('## Category Indexes')
$indexLines.Add('')
$indexLines.Add('| Category | Content Files | Category Index |')
$indexLines.Add('| --- | ---: | --- |')
foreach ($row in $categoryIndexRows) {
    $indexLines.Add(('| {0} | {1} | [{2}]({3}) |' -f $row.category, $row.file_count, '_CATEGORY_INDEX.md', ($row.category_index_file.Replace('\', '/'))))
}
$indexLines.Add('')
$indexLines.Add('## Category Counts')
$indexLines.Add('')
$indexLines.Add('| Category | Content Files |')
$indexLines.Add('| --- | ---: |')
foreach ($entry in $allTopLevelCategories.GetEnumerator()) {
    $indexLines.Add(('| {0} | {1} |' -f $entry.Key, $entry.Value))
}
$indexLines.Add('')
$indexLines.Add('## Current Snapshot')
$indexLines.Add('')
$linkedUrlCount = @($urlRows | Where-Object { -not [string]::IsNullOrWhiteSpace($_.current_knowledge_file) }).Count
$pdfLinkedUrlCount = @($urlRows | Where-Object { $_.source_file_type -in @('pdf', 'pdf_pdf') -and -not [string]::IsNullOrWhiteSpace($_.extracted_markdown_path) }).Count
$remainingHtmlCount = @(Import-Csv -LiteralPath (Join-Path $KnowledgeRoot '_raw_inventory\post_clean_raw_html_report.csv') -ErrorAction SilentlyContinue).Count
$indexLines.Add(('- URLs linked to knowledge files: `{0}`' -f $linkedUrlCount))
$indexLines.Add(('- PDF URL rows linked to extracted Markdown: `{0}`' -f $pdfLinkedUrlCount))
$indexLines.Add(('- Category indexes built in current pass: `{0}`' -f $categoryIndexRows.Count))
$indexLines.Add(('- Remaining raw HTML files after cleaning: `{0}`' -f $remainingHtmlCount))
$indexLines.Add('')
$indexLines.Add('## Use Pattern')
$indexLines.Add('')
$indexLines.Add('1. Start with `URL_INDEX.md`, this file, and `00_ai_entrypoints/KNOWLEDGE_MAP.md`.')
$indexLines.Add('2. Open the relevant `_CATEGORY_INDEX.md` before opening raw content files.')
$indexLines.Add('3. Use the local file path, `source_url`, and `url_index_id` to keep engineering claims traceable.')
$indexLines.Add('4. Use `91_rejected_low_value/` only for scrape diagnostics and gap analysis.')

$indexPath = Join-Path $KnowledgeRoot 'INDEX.md'
$indexLines | Set-Content -LiteralPath $indexPath -Encoding UTF8

$manifestPath = Join-Path $KnowledgeRoot 'MANIFEST.json'
$manifest = $null
if (Test-Path -LiteralPath $manifestPath) {
    $manifest = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json
}
else {
    $manifest = [pscustomobject]@{}
}

if ($null -eq $manifest.primary_builders) {
    Add-Member -InputObject $manifest -MemberType NoteProperty -Name primary_builders -Value @()
}
$builderList = New-Object System.Collections.Generic.List[string]
foreach ($builder in @($manifest.primary_builders)) {
    if ([string]::IsNullOrWhiteSpace($builder)) { continue }
    if (-not $builderList.Contains($builder)) { $builderList.Add($builder) }
}
if (-not $builderList.Contains('_scripts/06_build_category_indexes.ps1')) {
    $builderList.Add('_scripts/06_build_category_indexes.ps1')
}
$manifest.primary_builders = @($builderList)

$manifest | Add-Member -NotePropertyName category_index_status -NotePropertyValue 'completed' -Force
$manifest | Add-Member -NotePropertyName category_index_generated_at -NotePropertyValue $generatedAt -Force
$manifest | Add-Member -NotePropertyName category_index_count -NotePropertyValue $categoryIndexRows.Count -Force
$manifest | Add-Member -NotePropertyName generated_at -NotePropertyValue $generatedAt -Force
$manifest | Add-Member -NotePropertyName category_counts -NotePropertyValue $allTopLevelCategories -Force

$manifest | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $manifestPath -Encoding UTF8

[pscustomobject][ordered]@{
    category_index_count = $categoryIndexRows.Count
    category_counts = $allTopLevelCategories
} | ConvertTo-Json -Depth 6
