param(
    [string]$KnowledgeRoot = (Split-Path -Parent $PSScriptRoot),
    [string]$UrlIndexCsv = '',
    [switch]$Force
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

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

function ConvertTo-NullableLong {
    param([AllowNull()]$Value)
    if ($null -eq $Value) { return $null }
    $text = $Value.ToString().Trim()
    if ([string]::IsNullOrWhiteSpace($text)) { return $null }
    $parsed = [int64]0
    if ([int64]::TryParse($text, [ref]$parsed)) { return $parsed }
    return $null
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

function Get-UniqueFilePath {
    param(
        [Parameter(Mandatory = $true)][string]$Directory,
        [Parameter(Mandatory = $true)][string]$FileName
    )

    $candidate = Join-Path $Directory $FileName
    if (-not (Test-Path -LiteralPath $candidate)) {
        return $candidate
    }

    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($FileName)
    $extension = [System.IO.Path]::GetExtension($FileName)
    $counter = 2
    while ($true) {
        $nextName = '{0}__rejected_{1}{2}' -f $baseName, $counter, $extension
        $candidate = Join-Path $Directory $nextName
        if (-not (Test-Path -LiteralPath $candidate)) {
            return $candidate
        }
        $counter += 1
    }
}

function ConvertTo-YamlScalar {
    param(
        [AllowNull()]$Value,
        [bool]$AsBoolean = $false
    )

    if ($AsBoolean) {
        if (ConvertTo-Bool $Value) { return 'true' }
        return 'false'
    }

    if ($null -eq $Value) {
        return "''"
    }

    $text = $Value.ToString()
    $text = $text -replace "'", "''"
    return ("'{0}'" -f $text)
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

function Parse-Frontmatter {
    param([AllowNull()][string]$Text)

    $frontmatter = [ordered]@{}
    if ([string]::IsNullOrEmpty($Text)) {
        return [pscustomobject]@{
            frontmatter = $frontmatter
            body = ''
            has_frontmatter = $false
        }
    }

    $trimmed = $Text.TrimStart([char]0xFEFF)
    $match = [regex]::Match($trimmed, '^(?s)---\r?\n(.*?)\r?\n---\r?\n')
    if (-not $match.Success) {
        return [pscustomobject]@{
            frontmatter = $frontmatter
            body = $trimmed
            has_frontmatter = $false
        }
    }

    foreach ($line in ($match.Groups[1].Value -split "\r?\n")) {
        if ($line -match '^\s*([A-Za-z0-9_]+):\s*(.*)\s*$') {
            $key = $Matches[1]
            $value = $Matches[2].Trim()
            if (($value.StartsWith('"') -and $value.EndsWith('"')) -or ($value.StartsWith("'") -and $value.EndsWith("'"))) {
                $value = $value.Substring(1, $value.Length - 2)
                $value = $value -replace "''", "'"
            }
            $frontmatter[$key] = $value
        }
    }

    return [pscustomobject]@{
        frontmatter = $frontmatter
        body = $trimmed.Substring($match.Length)
        has_frontmatter = $true
    }
}

function Build-FrontmatterText {
    param(
        [Parameter(Mandatory = $true)][System.Collections.Specialized.OrderedDictionary]$Frontmatter,
        [Parameter(Mandatory = $true)][string]$Body
    )

    $boolFields = @('future_rescrape_candidate', 'raw_html_removed', 'possible_navigation_noise')
    $lines = New-Object System.Collections.Generic.List[string]
    $lines.Add('---')
    foreach ($key in $Frontmatter.Keys) {
        $value = $Frontmatter[$key]
        $isBool = $boolFields -contains $key
        $lines.Add(('{0}: {1}' -f $key, (ConvertTo-YamlScalar -Value $value -AsBoolean:$isBool)))
    }
    $lines.Add('---')
    $lines.Add('')
    return (($lines -join "`r`n") + $Body)
}

function Protect-CodeBlocks {
    param([AllowNull()][string]$Text)

    $index = 0
    $map = @{}
    $protected = [regex]::Replace($Text, '(?ms)```.*?```', {
            param($match)
            $token = '__CODE_BLOCK_{0}__' -f $index
            $index += 1
            $map[$token] = $match.Value
            return $token
        })

    return [pscustomobject]@{
        text = $protected
        token_map = $map
    }
}

function Restore-CodeBlocks {
    param(
        [Parameter(Mandatory = $true)][string]$Text,
        [Parameter(Mandatory = $true)][hashtable]$TokenMap
    )

    $result = $Text
    foreach ($token in $TokenMap.Keys) {
        $result = $result.Replace($token, $TokenMap[$token])
    }
    return $result
}

function Get-RawHtmlTagCount {
    param([AllowNull()][string]$Text)

    if ([string]::IsNullOrWhiteSpace($Text)) {
        return 0
    }

    $pattern = '(?i)<!DOCTYPE html|</?(html|head|body|div|span|table|thead|tbody|tr|td|th|script|style|iframe|section|article|main|nav|img|svg|path|meta|link|colgroup|col|footer|header|button|form|noscript)\b'
    $count = ([regex]::Matches($Text, $pattern)).Count
    $count += ([regex]::Matches($Text, 'data:image/')).Count
    return $count
}

function Get-WordCount {
    param([AllowNull()][string]$Text)

    if ([string]::IsNullOrWhiteSpace($Text)) {
        return 0
    }

    $normalized = $Text
    $normalized = [regex]::Replace($normalized, '```.*?```', ' ', 'Singleline')
    $normalized = [regex]::Replace($normalized, '\[[^\]]+\]\([^)]+\)', ' ')
    $normalized = [regex]::Replace($normalized, '[^A-Za-z0-9]+', ' ')
    $normalized = [regex]::Replace($normalized, '\s+', ' ').Trim()
    if ([string]::IsNullOrWhiteSpace($normalized)) {
        return 0
    }
    return ($normalized.Split(' ', [System.StringSplitOptions]::RemoveEmptyEntries)).Count
}

function Get-MeaningfulAlphaCount {
    param([AllowNull()][string]$Text)

    if ([string]::IsNullOrWhiteSpace($Text)) {
        return 0
    }
    return ([regex]::Matches($Text, '[A-Za-z]')).Count
}

function Test-UselessContent {
    param(
        [Parameter(Mandatory = $true)][string]$Body,
        [Parameter(Mandatory = $true)][int]$WordCount,
        [Parameter(Mandatory = $true)][int]$AlphaCount,
        [Parameter(Mandatory = $true)][int]$RawHtmlCount,
        [Parameter(Mandatory = $true)][bool]$PossibleNavigationNoise
    )

    if ([string]::IsNullOrWhiteSpace($Body)) { return $true }
    if ($AlphaCount -lt 120) { return $true }
    if ($WordCount -lt 40) { return $true }

    $normalized = $Body.ToLowerInvariant()
    if ($normalized -match 'captcha|please confirm you''re not a robot|enable javascript|cookie|login|log in|sign in|register') {
        if ($WordCount -lt 120) { return $true }
    }

    $tableOnly = [regex]::Replace($normalized, '\[table\]|\[page\s+\d+\]|[^a-z0-9]+', ' ').Trim()
    if ([string]::IsNullOrWhiteSpace($tableOnly)) { return $true }

    if ($PossibleNavigationNoise -and $WordCount -lt 80) { return $true }
    if ($RawHtmlCount -gt 40 -and $WordCount -lt 120) { return $true }
    return $false
}

function Get-ContentQuality {
    param(
        [Parameter(Mandatory = $true)][string]$Body,
        [Parameter(Mandatory = $true)][int]$WordCount,
        [Parameter(Mandatory = $true)][int]$AlphaCount,
        [Parameter(Mandatory = $true)][int]$RawHtmlCount,
        [Parameter(Mandatory = $true)][bool]$PossibleNavigationNoise,
        [Parameter(Mandatory = $true)][bool]$IsRejected
    )

    if ($IsRejected) { return 'junk' }
    if ($AlphaCount -lt 160 -or $WordCount -lt 60) { return 'low' }
    if ($RawHtmlCount -eq 0 -and -not $PossibleNavigationNoise -and $WordCount -ge 250) { return 'high' }
    if ($WordCount -ge 120) { return 'medium' }
    return 'low'
}

function Test-JunkLine {
    param(
        [Parameter(Mandatory = $true)][AllowEmptyString()][string]$Line,
        [Parameter(Mandatory = $true)][hashtable]$DuplicateCounts
    )

    $trimmed = $Line.Trim()
    if ([string]::IsNullOrWhiteSpace($trimmed)) { return $false }

    $lineLower = $trimmed.ToLowerInvariant()
    if ($DuplicateCounts.ContainsKey($lineLower) -and $DuplicateCounts[$lineLower] -gt 2 -and $trimmed.Length -le 100) {
        return $true
    }

    $junkPatterns = @(
        '(?i)enable javascript',
        '(?i)javascript is disabled',
        '(?i)we use cookies',
        '(?i)accept (all )?cookies',
        '(?i)manage (cookie|preferences)',
        '(?i)privacy preferences',
        '(?i)newsletter',
        '(?i)subscribe',
        '(?i)log in',
        '(?i)login',
        '(?i)sign in',
        '(?i)register',
        '(?i)advertisement',
        '(?i)sponsored',
        '(?i)share (this|on)',
        '(?i)follow us',
        '(?i)cookie policy',
        '(?i)all rights reserved',
        '(?i)back to top',
        '(?i)skip to content',
        '(?i)^loading\.\.\.$',
        '(?i)^searching\.\.\.$',
        '(?i)^no matches$',
        '(?i)click to enlarge',
        '(?i)permalink to this (heading|image)'
    )
    foreach ($pattern in $junkPatterns) {
        if ($trimmed -match $pattern -and $trimmed.Length -le 220) {
            return $true
        }
    }

    if ($trimmed -match '^\[!\[.*\]\(data:image') { return $true }
    if ($trimmed -match '^!\[\]\(data:image') { return $true }
    if ($trimmed -match '^\[\[[^]]+\]\]\([^)]+\)$') { return $true }
    if ($trimmed -match '^(home|menu|search|login|register|contact|about|privacy|terms)$') { return $true }

    $socialCount = 0
    foreach ($keyword in @('facebook', 'twitter', 'linkedin', 'pinterest', 'reddit', 'email', 'share')) {
        if ($lineLower -match $keyword) { $socialCount += 1 }
    }
    if ($socialCount -ge 2 -and $trimmed.Length -le 220) {
        return $true
    }

    return $false
}

function Clean-NonCodeText {
    param([Parameter(Mandatory = $true)][AllowEmptyString()][string]$Text)

    $notes = New-Object System.Collections.Generic.List[string]
    $possibleNavigationNoise = $false
    $rawHtmlRemoved = $false

    $clean = $Text
    $beforeHtmlCount = Get-RawHtmlTagCount -Text $clean

    $clean = [regex]::Replace($clean, '(?is)<!--.*?-->', "`r`n")

    $removeWholeTags = @('script', 'style', 'noscript', 'svg', 'nav', 'footer', 'header', 'button', 'form')
    foreach ($tag in $removeWholeTags) {
        $pattern = '(?is)<{0}\b[^>]*>.*?</{0}>' -f $tag
        $updated = [regex]::Replace($clean, $pattern, "`r`n")
        if ($updated -ne $clean) {
            $rawHtmlRemoved = $true
            $notes.Add(('removed_{0}_blocks' -f $tag))
        }
        $clean = $updated
    }

    $junkDivPattern = '(?is)<(div|span)\b[^>]*(cookie|consent|newsletter|subscribe|login|sign|share|social|menu|nav|footer|header|advert|ads|promo|banner|tracking)[^>]*>.*?</\1>'
    $updatedJunkDivs = [regex]::Replace($clean, $junkDivPattern, "`r`n")
    if ($updatedJunkDivs -ne $clean) {
        $rawHtmlRemoved = $true
        $possibleNavigationNoise = $true
        $notes.Add('removed_junk_div_or_span_blocks')
    }
    $clean = $updatedJunkDivs

    $updatedDivs = [regex]::Replace($clean, '(?is)</?div\b[^>]*>', "`r`n")
    if ($updatedDivs -ne $clean) {
        $rawHtmlRemoved = $true
        $notes.Add('stripped_div_tags')
    }
    $clean = $updatedDivs

    $updatedSpans = [regex]::Replace($clean, '(?is)</?span\b[^>]*>', '')
    if ($updatedSpans -ne $clean) {
        $rawHtmlRemoved = $true
        $notes.Add('stripped_span_tags')
    }
    $clean = $updatedSpans

    $updatedMiscOpenClose = [regex]::Replace($clean, '(?is)</?(section|article|main|aside)\b[^>]*>', "`r`n")
    if ($updatedMiscOpenClose -ne $clean) {
        $rawHtmlRemoved = $true
        $notes.Add('stripped_layout_tags')
    }
    $clean = $updatedMiscOpenClose

    $updatedDataImages = [regex]::Replace($clean, '!\[[^\]]*\]\(data:image[^)]*\)', '')
    if ($updatedDataImages -ne $clean) {
        $rawHtmlRemoved = $true
        $possibleNavigationNoise = $true
        $notes.Add('removed_embedded_data_images')
    }
    $clean = $updatedDataImages

    $updatedPermalinks = [regex]::Replace($clean, '\[[^\]]*\]\(#.*?"Permalink to this (heading|image)"\)', '')
    if ($updatedPermalinks -ne $clean) {
        $notes.Add('removed_permalink_links')
    }
    $clean = $updatedPermalinks

    $lines = $clean -split "\r?\n"
    $duplicateCounts = @{}
    foreach ($line in $lines) {
        $key = $line.Trim().ToLowerInvariant()
        if ([string]::IsNullOrWhiteSpace($key)) { continue }
        if (-not $duplicateCounts.ContainsKey($key)) {
            $duplicateCounts[$key] = 0
        }
        $duplicateCounts[$key] += 1
    }

    $filteredLines = New-Object System.Collections.Generic.List[string]
    $removedLineCount = 0
    foreach ($line in $lines) {
        if (Test-JunkLine -Line $line -DuplicateCounts $duplicateCounts) {
            $removedLineCount += 1
            $possibleNavigationNoise = $true
            continue
        }
        $filteredLines.Add($line)
    }
    if ($removedLineCount -gt 0) {
        $notes.Add(('removed_junk_lines={0}' -f $removedLineCount))
    }

    $clean = ($filteredLines -join "`r`n")
    $updatedTableRuns = [regex]::Replace($clean, '(?ms)(^\[TABLE\]\r?\n){2,}', "[TABLE]`r`n")
    if ($updatedTableRuns -ne $clean) {
        $notes.Add('collapsed_table_placeholders')
    }
    $clean = $updatedTableRuns

    $updatedPageRuns = [regex]::Replace($clean, '(?ms)(^\[PAGE\s+\d+\]\r?\n){2,}', '$1')
    $clean = $updatedPageRuns

    $beforeBlankCollapse = $clean
    $clean = [regex]::Replace($clean, '(\r?\n){3,}', "`r`n`r`n")
    if ($clean -ne $beforeBlankCollapse) {
        $notes.Add('collapsed_blank_lines')
    }

    $clean = $clean.Trim() + "`r`n"
    $afterHtmlCount = Get-RawHtmlTagCount -Text $clean
    if ($afterHtmlCount -lt $beforeHtmlCount) {
        $rawHtmlRemoved = $true
    }

    return [pscustomobject]@{
        text = $clean
        raw_html_removed = $rawHtmlRemoved
        possible_navigation_noise = $possibleNavigationNoise
        notes = $notes
        before_html_count = $beforeHtmlCount
        after_html_count = $afterHtmlCount
    }
}

function Replace-PathInDelimitedField {
    param(
        [AllowNull()][string]$Value,
        [Parameter(Mandatory = $true)][string]$OldPath,
        [Parameter(Mandatory = $true)][string]$NewPath
    )

    if ([string]::IsNullOrWhiteSpace($Value)) {
        return $Value
    }

    $parts = @($Value -split ';\s*')
    for ($i = 0; $i -lt $parts.Count; $i += 1) {
        if ($parts[$i] -eq $OldPath) {
            $parts[$i] = $NewPath
        }
    }
    return (($parts | Select-Object -Unique) -join '; ')
}

Ensure-Directory -Path $KnowledgeRoot
$logsDir = Join-Path $KnowledgeRoot '_logs'
$rawInventoryDir = Join-Path $KnowledgeRoot '_raw_inventory'
Ensure-Directory -Path $logsDir
Ensure-Directory -Path $rawInventoryDir

if (-not (Test-Path -LiteralPath $UrlIndexCsv)) {
    throw ('URL_INDEX CSV not found: {0}' -f $UrlIndexCsv)
}

$generatedAt = (Get-Date).ToString('s')
$preCleanManifestPath = Join-Path $logsDir 'pre_clean_backup_manifest.csv'
$cleanLogPath = Join-Path $logsDir 'clean_markdown_log.csv'
$postCleanRawHtmlReportPath = Join-Path $rawInventoryDir 'post_clean_raw_html_report.csv'

$urlRows = @(Import-Csv -LiteralPath $UrlIndexCsv)
$fileToRows = @{}
$targetPaths = New-Object System.Collections.Generic.List[string]

foreach ($row in $urlRows) {
    if ([string]::IsNullOrWhiteSpace($row.current_knowledge_file)) { continue }

    foreach ($relativePath in ($row.current_knowledge_file -split ';\s*')) {
        if ([string]::IsNullOrWhiteSpace($relativePath)) { continue }
        if (-not $relativePath.ToLowerInvariant().EndsWith('.md')) { continue }
        if ($relativePath -match '^(?:_logs|_scripts|_raw_inventory|_source_registry)\\') { continue }
        if ($relativePath -match '^14_datasheets_pdf_markdown\\extracted_markdown\\') { continue }

        $fullPath = Join-Path $KnowledgeRoot $relativePath
        if (-not (Test-Path -LiteralPath $fullPath)) { continue }

        if (-not $fileToRows.ContainsKey($fullPath)) {
            $fileToRows[$fullPath] = New-Object System.Collections.Generic.List[object]
            $targetPaths.Add($fullPath)
        }
        $fileToRows[$fullPath].Add($row)
    }
}

$targetPaths = @($targetPaths | Sort-Object -Unique)

$backupManifestRows = New-Object System.Collections.Generic.List[object]
foreach ($path in $targetPaths) {
    $fileInfo = Get-Item -LiteralPath $path
    $hash = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()
    $rowIds = @($fileToRows[$path] | ForEach-Object { $_.id }) -join '; '
    $relativePath = Get-RelativePath -BasePath $KnowledgeRoot -TargetPath $path
    $backupManifestRows.Add([pscustomobject][ordered]@{
            relative_path = $relativePath
            file_size_bytes = $fileInfo.Length
            last_write_time = $fileInfo.LastWriteTime.ToString('s')
            sha256 = $hash
            url_index_ids = $rowIds
        })
}
$backupManifestRows | Export-Csv -LiteralPath $preCleanManifestPath -NoTypeInformation -Encoding UTF8

$cleanLogRows = New-Object System.Collections.Generic.List[object]
$postCleanRawHtmlRows = New-Object System.Collections.Generic.List[object]

$filesChecked = 0
$filesCleaned = 0
$filesMovedToRejected = 0
$urlIndexUpdatedIds = New-Object System.Collections.Generic.HashSet[string]

foreach ($path in $targetPaths) {
    $filesChecked += 1
    $originalText = Get-SafeText -Path $path
    $parsed = Parse-Frontmatter -Text $originalText
    $frontmatter = [ordered]@{}
    foreach ($key in $parsed.frontmatter.Keys) {
        $frontmatter[$key] = $parsed.frontmatter[$key]
    }

    $protected = Protect-CodeBlocks -Text $parsed.body
    $cleanResult = Clean-NonCodeText -Text $protected.text
    $restoredBody = Restore-CodeBlocks -Text $cleanResult.text -TokenMap $protected.token_map

    $wordCount = Get-WordCount -Text $restoredBody
    $alphaCount = Get-MeaningfulAlphaCount -Text $restoredBody
    $remainingHtmlCount = Get-RawHtmlTagCount -Text $restoredBody
    $originalCategory = if ($frontmatter.Contains('knowledge_category')) { $frontmatter['knowledge_category'] } else { (Split-Path -Leaf (Split-Path -Parent $path)) }
    $isCurrentlyRejected = $originalCategory -eq '91_rejected_low_value'
    $isUseless = Test-UselessContent -Body $restoredBody -WordCount $wordCount -AlphaCount $alphaCount -RawHtmlCount $remainingHtmlCount -PossibleNavigationNoise:$cleanResult.possible_navigation_noise
    $moveToRejected = $isUseless -and -not $isCurrentlyRejected

    $finalPath = $path
    $finalCategory = $originalCategory
    $cleaningNotes = New-Object System.Collections.Generic.List[string]
    foreach ($note in $cleanResult.notes) {
        $cleaningNotes.Add($note)
    }
    if ($moveToRejected) {
        $finalCategory = '91_rejected_low_value'
        $cleaningNotes.Add('moved_to_rejected_after_cleaning')
    }

    $contentQuality = Get-ContentQuality -Body $restoredBody -WordCount $wordCount -AlphaCount $alphaCount -RawHtmlCount $remainingHtmlCount -PossibleNavigationNoise:$cleanResult.possible_navigation_noise -IsRejected:($finalCategory -eq '91_rejected_low_value')

    $frontmatter['cleaned_at'] = $generatedAt
    $frontmatter['raw_html_removed'] = $(if ($cleanResult.raw_html_removed) { 'true' } else { 'false' })
    $frontmatter['possible_navigation_noise'] = $(if ($cleanResult.possible_navigation_noise) { 'true' } else { 'false' })
    $frontmatter['content_quality'] = $contentQuality
    $frontmatter['cleaning_notes'] = (Join-Distinct -Values $cleaningNotes)
    if ($frontmatter.Contains('knowledge_category')) {
        $frontmatter['knowledge_category'] = $finalCategory
    }
    else {
        $frontmatter.Add('knowledge_category', $finalCategory)
    }

    $finalText = Build-FrontmatterText -Frontmatter $frontmatter -Body $restoredBody
    $textChanged = $finalText -ne $originalText

    if ($moveToRejected) {
        $rejectedDir = Join-Path $KnowledgeRoot '91_rejected_low_value'
        Ensure-Directory -Path $rejectedDir
        $destinationPath = Join-Path $rejectedDir ([System.IO.Path]::GetFileName($path))
        if ($destinationPath -ne $path -and (Test-Path -LiteralPath $destinationPath)) {
            if ($Force) {
                Remove-Item -LiteralPath $destinationPath -Force
            }
            else {
                $destinationPath = Get-UniqueFilePath -Directory $rejectedDir -FileName ([System.IO.Path]::GetFileName($path))
            }
        }

        Set-Content -LiteralPath $path -Value $finalText -Encoding UTF8
        if ($destinationPath -ne $path) {
            Move-Item -LiteralPath $path -Destination $destinationPath -Force
            $finalPath = $destinationPath
            $filesMovedToRejected += 1
        }
    }
    else {
        Set-Content -LiteralPath $path -Value $finalText -Encoding UTF8
    }

    if ($textChanged -or $moveToRejected) {
        $filesCleaned += 1
    }

    $relativeOriginalPath = Get-RelativePath -BasePath $KnowledgeRoot -TargetPath $path
    $relativeFinalPath = Get-RelativePath -BasePath $KnowledgeRoot -TargetPath $finalPath

    foreach ($row in $fileToRows[$path]) {
        $row.current_knowledge_file = Replace-PathInDelimitedField -Value $row.current_knowledge_file -OldPath $relativeOriginalPath -NewPath $relativeFinalPath
        $row.content_quality = $contentQuality
        if ($moveToRejected) {
            $row.detected_category = '91_rejected_low_value'
        }
        $existingNotes = $row.notes
        $row.notes = Join-Distinct -Values @($existingNotes, ('cleaned_at={0}' -f $generatedAt), ('raw_html_removed={0}' -f (ConvertTo-Bool $frontmatter['raw_html_removed'])), ('possible_navigation_noise={0}' -f (ConvertTo-Bool $frontmatter['possible_navigation_noise'])))
        [void]$urlIndexUpdatedIds.Add($row.id)
    }

    if ($remainingHtmlCount -gt 0) {
        $associatedIds = @($fileToRows[$path] | ForEach-Object { $_.id }) -join '; '
        $postCleanRawHtmlRows.Add([pscustomobject][ordered]@{
                current_knowledge_file = $relativeFinalPath
                url_index_ids = $associatedIds
                knowledge_category = $finalCategory
                raw_html_tag_count = $remainingHtmlCount
                content_quality = $contentQuality
            })
    }

    $cleanLogRows.Add([pscustomobject][ordered]@{
            original_path = $relativeOriginalPath
            final_path = $relativeFinalPath
            filesize_bytes = (Get-Item -LiteralPath $finalPath).Length
            original_category = $originalCategory
            final_category = $finalCategory
            moved_to_rejected = $moveToRejected
            raw_html_removed = (ConvertTo-Bool $frontmatter['raw_html_removed'])
            possible_navigation_noise = (ConvertTo-Bool $frontmatter['possible_navigation_noise'])
            word_count = $wordCount
            remaining_raw_html_tag_count = $remainingHtmlCount
            content_quality = $contentQuality
            cleaning_notes = $frontmatter['cleaning_notes']
            url_index_ids = @($fileToRows[$path] | ForEach-Object { $_.id }) -join '; '
        })
}

$cleanLogRows | Export-Csv -LiteralPath $cleanLogPath -NoTypeInformation -Encoding UTF8
$postCleanRawHtmlRows | Export-Csv -LiteralPath $postCleanRawHtmlReportPath -NoTypeInformation -Encoding UTF8

$urlRows | Export-Csv -LiteralPath $UrlIndexCsv -NoTypeInformation -Encoding UTF8
$urlIndexJsonPath = Join-Path $KnowledgeRoot 'URL_INDEX.json'
$urlRows | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $urlIndexJsonPath -Encoding UTF8

$linkedUrlCount = @($urlRows | Where-Object { -not [string]::IsNullOrWhiteSpace($_.current_knowledge_file) }).Count
$pdfLinkedUrlCount = @($urlRows | Where-Object { $_.source_file_type -in @('pdf', 'pdf_pdf') -and -not [string]::IsNullOrWhiteSpace($_.current_knowledge_file) }).Count
$pdfExtractionFailures = @($urlRows | Where-Object { $_.source_file_type -in @('pdf', 'pdf_pdf') -and $_.extraction_status -eq 'extraction_failed' }).Count
$pdfsExtracted = @($urlRows | Where-Object { $_.source_file_type -in @('pdf', 'pdf_pdf') -and $_.extraction_status -eq 'success' }).Count
$pdfCountFound = @($urlRows | Where-Object { $_.source_file_type -in @('pdf', 'pdf_pdf') }).Count
$remainingRawHtmlFiles = $postCleanRawHtmlRows.Count

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
$urlIndexMarkdownLines.Add(('- Files cleaned in current pass: `{0}`' -f $filesCleaned))
$urlIndexMarkdownLines.Add(('- Files moved to rejected in current pass: `{0}`' -f $filesMovedToRejected))
$urlIndexMarkdownLines.Add(('- Remaining raw HTML files after cleaning: `{0}`' -f $remainingRawHtmlFiles))
$urlIndexMarkdownLines.Add(('- PDF count found: `{0}`' -f $pdfCountFound))
$urlIndexMarkdownLines.Add(('- PDFs extracted: `{0}`' -f $pdfsExtracted))
$urlIndexMarkdownLines.Add(('- PDF extraction failures: `{0}`' -f $pdfExtractionFailures))
$urlIndexMarkdownLines.Add('')
$urlIndexMarkdownLines.Add('## URL Status Summary')
$urlIndexMarkdownLines.Add('')
foreach ($line in $urlStatusSummaryLines) {
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
$urlIndexMarkdownLines.Add('1. Frontmatter, `source_url`, `normalized_url`, and `url_index_id` are preserved.')
$urlIndexMarkdownLines.Add('2. Code fences are preserved and excluded from HTML/noise stripping.')
$urlIndexMarkdownLines.Add('3. Files that became low-value after cleaning are moved to `91_rejected_low_value` and their `current_knowledge_file` paths are updated in the registry.')

$urlIndexMarkdownPath = Join-Path $KnowledgeRoot 'URL_INDEX.md'
$urlIndexMarkdownLines | Set-Content -LiteralPath $urlIndexMarkdownPath -Encoding UTF8

$indexLines = New-Object System.Collections.Generic.List[string]
$indexLines.Add('# knowledge_scrape Index')
$indexLines.Add('')
$indexLines.Add(('Generated at: `{0}`' -f $generatedAt))
$indexLines.Add('')
$indexLines.Add('- `SOURCE_AUDIT.md`: scrape input inventory summary.')
$indexLines.Add('- `URL_INDEX.csv/json/md`: canonical URL registry with cleaned knowledge-file links.')
$indexLines.Add('- `RESCRAPE_QUEUE.csv`: follow-up scrape targets from the registry builder.')
$indexLines.Add('- `_logs/pre_clean_backup_manifest.csv`: pre-clean file manifest with hashes.')
$indexLines.Add('- `_logs/clean_markdown_log.csv`: per-file cleaning and move actions.')
$indexLines.Add('- `_raw_inventory/post_clean_raw_html_report.csv`: remaining raw HTML findings after cleaning.')
$indexLines.Add('- `14_datasheets_pdf_markdown/PDF_INDEX.csv/md`: PDF extraction inventory and summary.')
$indexLines.Add('')
$indexLines.Add('## Category Counts')
$indexLines.Add('')
$indexLines.Add('| Category | Markdown Files |')
$indexLines.Add('| --- | ---: |')
foreach ($row in $knowledgeCategoryRows) {
    $indexLines.Add(('| {0} | {1} |' -f $row.category, $row.markdown_files))
}
$indexLines.Add('')
$indexLines.Add('## Cleaning Summary')
$indexLines.Add('')
$indexLines.Add(('- Files checked: `{0}`' -f $filesChecked))
$indexLines.Add(('- Files cleaned: `{0}`' -f $filesCleaned))
$indexLines.Add(('- Files moved to rejected: `{0}`' -f $filesMovedToRejected))
$indexLines.Add(('- Remaining raw HTML files: `{0}`' -f $remainingRawHtmlFiles))

$indexPath = Join-Path $KnowledgeRoot 'INDEX.md'
$indexLines | Set-Content -LiteralPath $indexPath -Encoding UTF8

$manifest = [ordered]@{
    name = 'knowledge_scrape'
    status = 'markdown_pdf_import_and_cleaning_completed'
    created_for = 'scrape audit and URL/source inventory'
    content_copy_status = 'markdown_completed'
    pdf_extraction_status = 'completed'
    markdown_cleaning_status = 'completed'
    primary_builders = @(
        '_scripts/01_build_raw_inventory.ps1',
        '_scripts/02_build_url_registry.ps1',
        '_scripts/03_classify_copy_markdown.ps1',
        '_scripts/04_convert_pdfs_to_markdown.ps1',
        '_scripts/05_clean_markdown_for_ai.ps1'
    )
    generated_at = $generatedAt
    url_index_csv = $UrlIndexCsv
    files_checked = $filesChecked
    files_cleaned = $filesCleaned
    files_moved_to_rejected = $filesMovedToRejected
    remaining_raw_html_files = $remainingRawHtmlFiles
    url_index_updated_count = $urlIndexUpdatedIds.Count
    linked_url_count = $linkedUrlCount
    category_counts = [ordered]@{}
}

foreach ($row in $knowledgeCategoryRows) {
    $manifest.category_counts[$row.category] = $row.markdown_files
}

$manifestPath = Join-Path $KnowledgeRoot 'MANIFEST.json'
$manifest | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $manifestPath -Encoding UTF8

[pscustomobject][ordered]@{
    files_checked = $filesChecked
    files_cleaned = $filesCleaned
    files_moved_to_rejected = $filesMovedToRejected
    remaining_raw_html_files = $remainingRawHtmlFiles
    url_index_updated_count = $urlIndexUpdatedIds.Count
} | Format-List
