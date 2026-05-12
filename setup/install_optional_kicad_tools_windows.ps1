param(
    [switch]$Apply,
    [string[]]$Categories = @("kicad", "fab", "visual")
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$python = "python"
$toolRoot = Join-Path $repoRoot ".tools"
$venvRoot = Join-Path $toolRoot "venvs"

$categoryMap = @{
    "kicad" = "requirements-kicad-tools.txt"
    "fab"    = "requirements-fab-tools.txt"
    "visual" = "requirements-visual-tools.txt"
}

function Invoke-Step([string]$Message, [scriptblock]$Action) {
    Write-Host $Message
    if ($Apply) {
        & $Action
    } else {
        Write-Host "DRY_RUN: $Message"
    }
}

function Install-Category([string]$Category, [string]$RequirementsFile) {
    $requirementsPath = Join-Path $repoRoot $RequirementsFile
    if (-not (Test-Path $requirementsPath)) {
        throw "Missing requirements file: $requirementsPath"
    }

    $venvPath = Join-Path $venvRoot $Category
    Invoke-Step "Create venv $venvPath" {
        & $python -m venv $venvPath
    }

    $venvPython = Join-Path $venvPath "Scripts\\python.exe"
    Invoke-Step "Install requirements from $RequirementsFile" {
        & $venvPython -m pip install --upgrade pip
        & $venvPython -m pip install -r $requirementsPath
    }
}

Write-Host "KiCad Engine optional-tool installer"
Write-Host "Repo root: $repoRoot"
Write-Host "Apply mode: $Apply"
Write-Host "Categories: $($Categories -join ', ')"
Write-Host ""
Write-Host "External-only tools remain manual:"
Write-Host "- KiCad local install / pcbnew runtime"
Write-Host "- freerouting"
Write-Host "- kicad-routing-tools"
Write-Host "- kicad-component-layout"
Write-Host "- kicad-library-utils"
Write-Host ""

if ($Apply) {
    New-Item -ItemType Directory -Force -Path $venvRoot | Out-Null
}

foreach ($category in $Categories) {
    if (-not $categoryMap.ContainsKey($category)) {
        throw "Unknown category: $category"
    }
    Install-Category -Category $category -RequirementsFile $categoryMap[$category]
}

Write-Host ""
Write-Host "Verification command:"
Write-Host "python setup\\verify_optional_kicad_tools.py --dry-run"
