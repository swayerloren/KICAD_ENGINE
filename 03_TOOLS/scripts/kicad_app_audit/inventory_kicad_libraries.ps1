[CmdletBinding()]
param(
    [string]$KiCadRoot,
    [string]$VersionPreference = "9.0",
    [string]$OutputRoot
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = "Stop"

function Resolve-WorkspaceRoot {
    $current = (Get-Location).Path
    while ($current) {
        if (Test-Path -LiteralPath (Join-Path $current "AGENTS.md")) {
            return $current
        }
        $parent = Split-Path -Parent $current
        if ($parent -eq $current) { break }
        $current = $parent
    }
    return (Get-Location).Path
}

function Resolve-KiCadRoot {
    param([string]$ExplicitRoot, [string]$PreferredVersion)
    if ($ExplicitRoot -and (Test-Path -LiteralPath (Join-Path $ExplicitRoot "share\kicad"))) {
        return (Resolve-Path -LiteralPath $ExplicitRoot).Path
    }

    $preferred = "C:\Program Files\KiCad\$PreferredVersion"
    if (Test-Path -LiteralPath (Join-Path $preferred "share\kicad")) {
        return (Resolve-Path -LiteralPath $preferred).Path
    }

    $installRoot = "C:\Program Files\KiCad"
    if (Test-Path -LiteralPath $installRoot) {
        $candidate = Get-ChildItem -LiteralPath $installRoot -Directory -ErrorAction SilentlyContinue |
            Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName "share\kicad") } |
            Sort-Object Name -Descending |
            Select-Object -First 1
        if ($candidate) { return $candidate.FullName }
    }

    $cmd = Get-Command "kicad-cli.exe" -ErrorAction SilentlyContinue
    if ($cmd) {
        $root = Split-Path -Parent (Split-Path -Parent $cmd.Source)
        if (Test-Path -LiteralPath (Join-Path $root "share\kicad")) {
            return $root
        }
    }

    return $null
}

function Get-LibTableEntries {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) { return @() }
    $text = Get-Content -Raw -LiteralPath $Path
    $matches = [regex]::Matches($text, '\(lib\s+\(name\s+"?([^"\s\)]+)"?\).*?\(uri\s+"?([^"\)]+)"?\)', [System.Text.RegularExpressions.RegexOptions]::Singleline)
    $rows = New-Object System.Collections.Generic.List[object]
    foreach ($match in $matches) {
        $rows.Add([pscustomobject]@{
            Table = $Path
            Name = $match.Groups[1].Value
            Uri = $match.Groups[2].Value
        }) | Out-Null
    }
    return $rows.ToArray()
}

function Add-Heading {
    param([System.Collections.Generic.List[string]]$Lines, [string]$Text, [int]$Level = 2)
    $Lines.Add("") | Out-Null
    $Lines.Add(("#" * $Level) + " " + $Text) | Out-Null
    $Lines.Add("") | Out-Null
}

$workspaceRoot = Resolve-WorkspaceRoot
if (-not $OutputRoot) {
    $OutputRoot = Join-Path $workspaceRoot "05_OUTPUTS\kicad_app_audit"
}
New-Item -ItemType Directory -Force -Path $OutputRoot | Out-Null

$stamp = Get-Date -Format "yyyyMMdd_HHmmss"
$reportPath = Join-Path $OutputRoot "KICAD_LIBRARY_INVENTORY_$stamp.md"
$symbolsCsv = Join-Path $OutputRoot "KICAD_SYMBOL_LIBRARIES_$stamp.csv"
$footprintsCsv = Join-Path $OutputRoot "KICAD_FOOTPRINT_LIBRARIES_$stamp.csv"
$modelsCsv = Join-Path $OutputRoot "KICAD_3DMODEL_FOLDERS_$stamp.csv"
$tablesCsv = Join-Path $OutputRoot "KICAD_LIBRARY_TABLES_$stamp.csv"

$root = Resolve-KiCadRoot -ExplicitRoot $KiCadRoot -PreferredVersion $VersionPreference
$lines = New-Object System.Collections.Generic.List[string]
$lines.Add("# KiCad Library Inventory") | Out-Null
$lines.Add("") | Out-Null
$lines.Add("Created: $(Get-Date -Format o)") | Out-Null
$lines.Add("Workspace: ``$workspaceRoot``") | Out-Null

if (-not $root) {
    Add-Heading -Lines $lines -Text "Result"
    $lines.Add("Status: FAIL") | Out-Null
    $lines.Add("KiCad stock library root was not found. No KiCad commands were run.") | Out-Null
    Set-Content -LiteralPath $reportPath -Value $lines -Encoding UTF8
    Write-Error "KiCad stock library root was not found. Report: $reportPath"
    exit 2
}

$shareKicad = Join-Path $root "share\kicad"
$symbolsRoot = Join-Path $shareKicad "symbols"
$footprintsRoot = Join-Path $shareKicad "footprints"
$modelsRoot = Join-Path $shareKicad "3dmodels"
$templateRoot = Join-Path $shareKicad "template"
$userConfigRoot = Join-Path $env:APPDATA "kicad\$VersionPreference"

$symbolRows = if (Test-Path -LiteralPath $symbolsRoot) {
    Get-ChildItem -LiteralPath $symbolsRoot -File -Filter "*.kicad_sym" -ErrorAction SilentlyContinue |
        Sort-Object Name |
        Select-Object Name, FullName, Length, LastWriteTime
} else { @() }

$footprintRows = if (Test-Path -LiteralPath $footprintsRoot) {
    Get-ChildItem -LiteralPath $footprintsRoot -Directory -Filter "*.pretty" -ErrorAction SilentlyContinue |
        Sort-Object Name |
        Select-Object Name, FullName, LastWriteTime, @{n="Footprints";e={(Get-ChildItem -LiteralPath $_.FullName -File -Filter "*.kicad_mod" -ErrorAction SilentlyContinue | Measure-Object).Count}}
} else { @() }

$modelRows = if (Test-Path -LiteralPath $modelsRoot) {
    Get-ChildItem -LiteralPath $modelsRoot -Directory -Filter "*.3dshapes" -ErrorAction SilentlyContinue |
        Sort-Object Name |
        Select-Object Name, FullName, LastWriteTime, @{n="StepFiles";e={(Get-ChildItem -LiteralPath $_.FullName -File -Include "*.step","*.stp" -ErrorAction SilentlyContinue | Measure-Object).Count}}, @{n="WrlFiles";e={(Get-ChildItem -LiteralPath $_.FullName -File -Filter "*.wrl" -ErrorAction SilentlyContinue | Measure-Object).Count}}
} else { @() }

$tablePaths = @(
    (Join-Path $templateRoot "sym-lib-table"),
    (Join-Path $templateRoot "fp-lib-table"),
    (Join-Path $userConfigRoot "sym-lib-table"),
    (Join-Path $userConfigRoot "fp-lib-table"),
    (Join-Path $userConfigRoot "design-block-lib-table")
)

$tableEntries = New-Object System.Collections.Generic.List[object]
foreach ($tablePath in $tablePaths) {
    foreach ($entry in (Get-LibTableEntries -Path $tablePath)) {
        $tableEntries.Add($entry) | Out-Null
    }
}

$symbolRows | Export-Csv -LiteralPath $symbolsCsv -NoTypeInformation -Encoding UTF8
$footprintRows | Export-Csv -LiteralPath $footprintsCsv -NoTypeInformation -Encoding UTF8
$modelRows | Export-Csv -LiteralPath $modelsCsv -NoTypeInformation -Encoding UTF8
$tableEntries | Export-Csv -LiteralPath $tablesCsv -NoTypeInformation -Encoding UTF8

Add-Heading -Lines $lines -Text "Result"
$lines.Add("Status: PASS") | Out-Null
$lines.Add("KiCad root: ``$root``") | Out-Null

Add-Heading -Lines $lines -Text "Counts"
$lines.Add("- Symbol libraries: $(@($symbolRows).Count)") | Out-Null
$lines.Add("- Footprint library folders: $(@($footprintRows).Count)") | Out-Null
$lines.Add("- Footprints: $((@($footprintRows) | Measure-Object -Property Footprints -Sum).Sum)") | Out-Null
$lines.Add("- 3D model folders: $(@($modelRows).Count)") | Out-Null
$lines.Add("- 3D model files counted in STEP/STP/WRL columns: $((@($modelRows) | Measure-Object -Property StepFiles -Sum).Sum + (@($modelRows) | Measure-Object -Property WrlFiles -Sum).Sum)") | Out-Null
$lines.Add("- Library table entries parsed: $($tableEntries.Count)") | Out-Null

Add-Heading -Lines $lines -Text "Output Files"
$lines.Add("- ``$symbolsCsv``") | Out-Null
$lines.Add("- ``$footprintsCsv``") | Out-Null
$lines.Add("- ``$modelsCsv``") | Out-Null
$lines.Add("- ``$tablesCsv``") | Out-Null

Add-Heading -Lines $lines -Text "Safety"
$lines.Add("- This script does not delete files.") | Out-Null
$lines.Add("- This script does not write to `C:\Program Files\KiCad`.") | Out-Null
$lines.Add("- This script does not run KiCad executables.") | Out-Null
$lines.Add("- CSV reports are written only to the selected output folder.") | Out-Null

Set-Content -LiteralPath $reportPath -Value $lines -Encoding UTF8
Write-Host "Report written: $reportPath"
exit 0
