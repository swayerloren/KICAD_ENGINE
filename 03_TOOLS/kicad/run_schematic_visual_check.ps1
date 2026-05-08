param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectRoot,

    [string]$SchematicPath = "",
    [string]$OutputRoot = "",
    [string]$KicadCliPath = "",
    [switch]$CreateDefaultConfig,
    [switch]$NoFailOnFindings
)

$ErrorActionPreference = "Stop"

function Resolve-ExistingPath {
    param([string]$PathValue, [string]$Label)
    if (-not (Test-Path -LiteralPath $PathValue)) {
        throw "$Label not found: $PathValue"
    }
    return (Resolve-Path -LiteralPath $PathValue).Path
}

function Find-KicadCli {
    param([string]$RequestedPath)
    if ($RequestedPath -and (Test-Path -LiteralPath $RequestedPath)) {
        return (Resolve-Path -LiteralPath $RequestedPath).Path
    }
    if ($env:KICAD_CLI -and (Test-Path -LiteralPath $env:KICAD_CLI)) {
        return (Resolve-Path -LiteralPath $env:KICAD_CLI).Path
    }
    $candidateRoots = @(
        "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe",
        "C:\Program Files\KiCad\8.0\bin\kicad-cli.exe",
        "C:\Program Files\KiCad\7.0\bin\kicad-cli.exe"
    )
    foreach ($candidate in $candidateRoots) {
        if (Test-Path -LiteralPath $candidate) {
            return (Resolve-Path -LiteralPath $candidate).Path
        }
    }
    $cmd = Get-Command "kicad-cli" -ErrorAction SilentlyContinue
    if ($cmd) {
        return $cmd.Source
    }
    throw "kicad-cli not found. Install KiCad or pass -KicadCliPath. No tools were installed."
}

function Find-Schematic {
    param([string]$Root, [string]$RequestedPath)
    if ($RequestedPath) {
        return Resolve-ExistingPath -PathValue $RequestedPath -Label "Schematic"
    }
    $kicadDir = Join-Path $Root "kicad"
    $candidates = @()
    if (Test-Path -LiteralPath $kicadDir) {
        $candidates += Get-ChildItem -LiteralPath $kicadDir -Filter "*.kicad_sch" -File
    }
    $candidates += Get-ChildItem -LiteralPath $Root -Filter "*.kicad_sch" -File -Recurse -ErrorAction SilentlyContinue
    $unique = $candidates | Sort-Object FullName -Unique
    if ($unique.Count -eq 0) {
        throw "No .kicad_sch file found under project root: $Root"
    }
    if ($unique.Count -gt 1) {
        $listed = ($unique | ForEach-Object { $_.FullName }) -join "; "
        throw "Multiple .kicad_sch files found. Pass -SchematicPath. Found: $listed"
    }
    return $unique[0].FullName
}

function Invoke-Logged {
    param([string[]]$CommandLine, [string]$Label)
    Write-Host "Running $Label..."
    & $CommandLine[0] @($CommandLine[1..($CommandLine.Count - 1)])
    if ($LASTEXITCODE -ne 0) {
        throw "$Label failed with exit code $LASTEXITCODE"
    }
}

$resolvedProjectRoot = Resolve-ExistingPath -PathValue $ProjectRoot -Label "Project root"
$resolvedSchematic = Find-Schematic -Root $resolvedProjectRoot -RequestedPath $SchematicPath
$kicadCli = Find-KicadCli -RequestedPath $KicadCliPath
$toolsRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path
$pythonScript = Join-Path $toolsRoot "scripts\visual\generate_schematic_closeups.py"
if (-not (Test-Path -LiteralPath $pythonScript)) {
    throw "Python visual crop generator not found: $pythonScript"
}

if (-not $OutputRoot) {
    $OutputRoot = Join-Path $resolvedProjectRoot "_verification\schematic_visual"
}
$fullPageDir = Join-Path $OutputRoot "full_page"
$cropsDir = Join-Path $OutputRoot "crops"
$configPath = Join-Path $OutputRoot "visual_blocks.json"
$summaryJson = Join-Path $OutputRoot "CLOSE_UP_REVIEW.json"
$reportsDir = Join-Path $resolvedProjectRoot "reports"
$reviewPath = Join-Path $reportsDir "CLOSE_UP_REVIEW.md"
$projectName = [System.IO.Path]::GetFileNameWithoutExtension($resolvedSchematic)
$pdfPath = Join-Path $fullPageDir "$projectName.pdf"
$fullPngPath = Join-Path $fullPageDir "$projectName.png"

New-Item -ItemType Directory -Path $fullPageDir -Force | Out-Null
New-Item -ItemType Directory -Path $cropsDir -Force | Out-Null
New-Item -ItemType Directory -Path $reportsDir -Force | Out-Null

Invoke-Logged -Label "KiCad schematic SVG export" -CommandLine @(
    $kicadCli,
    "sch",
    "export",
    "svg",
    "--black-and-white",
    "--output",
    $fullPageDir,
    $resolvedSchematic
)

Invoke-Logged -Label "KiCad schematic PDF export" -CommandLine @(
    $kicadCli,
    "sch",
    "export",
    "pdf",
    "--black-and-white",
    "--output",
    $pdfPath,
    $resolvedSchematic
)

$svgCandidates = Get-ChildItem -LiteralPath $fullPageDir -Filter "*.svg" -File | Sort-Object LastWriteTime -Descending
if ($svgCandidates.Count -eq 0) {
    throw "VISUAL_REVIEW_INCOMPLETE: KiCad SVG export did not produce an SVG under $fullPageDir"
}
$svgPath = $svgCandidates[0].FullName

$pythonArgs = @(
    $pythonScript,
    "--source-svg",
    $svgPath,
    "--config",
    $configPath,
    "--crops-dir",
    $cropsDir,
    "--review-output",
    $reviewPath,
    "--json-output",
    $summaryJson,
    "--full-png-output",
    $fullPngPath
)
if ($CreateDefaultConfig) {
    $pythonArgs += "--create-default-config"
}
if ($NoFailOnFindings) {
    $pythonArgs += "--no-fail"
}

Write-Host "Generating close-up crops..."
& python @pythonArgs
$pythonExit = $LASTEXITCODE

if (-not (Test-Path -LiteralPath $reviewPath)) {
    throw "VISUAL_REVIEW_INCOMPLETE: CLOSE_UP_REVIEW.md was not created: $reviewPath"
}
$cropCount = (Get-ChildItem -LiteralPath $cropsDir -Filter "*.svg" -File -ErrorAction SilentlyContinue | Measure-Object).Count
if ($cropCount -eq 0) {
    throw "VISUAL_REVIEW_INCOMPLETE: no close-up SVG crops were created under $cropsDir"
}

if (($pythonExit -ne 0) -and (-not $NoFailOnFindings)) {
    exit $pythonExit
}

Write-Host "Schematic visual check completed."
Write-Host "Full-page SVG: $svgPath"
Write-Host "Full-page PDF: $pdfPath"
Write-Host "Full-page PNG: $fullPngPath"
Write-Host "Crops: $cropsDir"
Write-Host "Review: $reviewPath"
exit 0
