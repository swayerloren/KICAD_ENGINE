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
    param(
        [string]$ExplicitRoot,
        [string]$PreferredVersion
    )

    $checked = New-Object System.Collections.Generic.List[string]

    if ($ExplicitRoot) {
        $checked.Add($ExplicitRoot) | Out-Null
        if (Test-Path -LiteralPath (Join-Path $ExplicitRoot "bin\kicad-cli.exe")) {
            return [pscustomobject]@{ Root = (Resolve-Path -LiteralPath $ExplicitRoot).Path; Checked = $checked }
        }
    }

    $preferred = "C:\Program Files\KiCad\$PreferredVersion"
    $checked.Add($preferred) | Out-Null
    if (Test-Path -LiteralPath (Join-Path $preferred "bin\kicad-cli.exe")) {
        return [pscustomobject]@{ Root = (Resolve-Path -LiteralPath $preferred).Path; Checked = $checked }
    }

    $installRoot = "C:\Program Files\KiCad"
    if (Test-Path -LiteralPath $installRoot) {
        $candidates = Get-ChildItem -LiteralPath $installRoot -Directory -ErrorAction SilentlyContinue |
            Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName "bin\kicad-cli.exe") } |
            Sort-Object Name -Descending

        foreach ($candidate in $candidates) {
            $checked.Add($candidate.FullName) | Out-Null
        }

        if ($candidates) {
            return [pscustomobject]@{ Root = $candidates[0].FullName; Checked = $checked }
        }
    }

    $cmd = Get-Command "kicad-cli.exe" -ErrorAction SilentlyContinue
    if ($cmd) {
        $root = Split-Path -Parent (Split-Path -Parent $cmd.Source)
        $checked.Add($root) | Out-Null
        return [pscustomobject]@{ Root = $root; Checked = $checked }
    }

    return [pscustomobject]@{ Root = $null; Checked = $checked }
}

function Count-Files {
    param([string]$Path, [string]$Filter = "*")
    if (-not (Test-Path -LiteralPath $Path)) { return 0 }
    return (Get-ChildItem -LiteralPath $Path -Recurse -File -Filter $Filter -ErrorAction SilentlyContinue | Measure-Object).Count
}

function Count-Directories {
    param([string]$Path, [string]$Filter = "*")
    if (-not (Test-Path -LiteralPath $Path)) { return 0 }
    return (Get-ChildItem -LiteralPath $Path -Recurse -Directory -Filter $Filter -ErrorAction SilentlyContinue | Measure-Object).Count
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
$reportPath = Join-Path $OutputRoot "KICAD_WINDOWS_APP_AUDIT_$stamp.md"
$jsonPath = Join-Path $OutputRoot "KICAD_WINDOWS_APP_AUDIT_$stamp.json"

$resolved = Resolve-KiCadRoot -ExplicitRoot $KiCadRoot -PreferredVersion $VersionPreference
$lines = New-Object System.Collections.Generic.List[string]
$lines.Add("# KiCad Windows Installed App Audit") | Out-Null
$lines.Add("") | Out-Null
$lines.Add("Created: $(Get-Date -Format o)") | Out-Null
$lines.Add("Workspace: ``$workspaceRoot``") | Out-Null

Add-Heading -Lines $lines -Text "Checked Roots"
foreach ($path in $resolved.Checked) {
    $lines.Add("- ``$path``") | Out-Null
}

if (-not $resolved.Root) {
    Add-Heading -Lines $lines -Text "Result"
    $lines.Add("Status: FAIL") | Out-Null
    $lines.Add("") | Out-Null
    $lines.Add("KiCad was not found. No KiCad commands were run.") | Out-Null
    Set-Content -LiteralPath $reportPath -Value $lines -Encoding UTF8
    @{ status = "FAIL"; reason = "KiCad not found"; checked = $resolved.Checked } | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $jsonPath -Encoding UTF8
    Write-Error "KiCad was not found. Report: $reportPath"
    exit 2
}

$root = $resolved.Root
$bin = Join-Path $root "bin"
$share = Join-Path $root "share"
$shareKicad = Join-Path $share "kicad"
$etc = Join-Path $root "etc"
$lib = Join-Path $root "lib"
$symbols = Join-Path $shareKicad "symbols"
$footprints = Join-Path $shareKicad "footprints"
$models = Join-Path $shareKicad "3dmodels"
$templates = Join-Path $shareKicad "template"
$demos = Join-Path $shareKicad "demos"
$scripting = Join-Path $shareKicad "scripting"

$required = @($bin, $share, $shareKicad, $etc, $lib)
$pathRows = foreach ($path in $required) {
    $item = Get-Item -LiteralPath $path -ErrorAction SilentlyContinue
    [pscustomobject]@{ Path = $path; Exists = [bool]$item; Type = if ($item) { if ($item.PSIsContainer) { "Directory" } else { "File" } } else { "Missing" } }
}

$exeRows = if (Test-Path -LiteralPath $bin) {
    Get-ChildItem -LiteralPath $bin -File -Filter "*.exe" -ErrorAction SilentlyContinue |
        Sort-Object Name |
        Select-Object Name, Length, LastWriteTime, @{n="ProductVersion";e={$_.VersionInfo.ProductVersion}}, @{n="FileVersion";e={$_.VersionInfo.FileVersion}}
} else { @() }

$assetRows = @(
    [pscustomobject]@{ Area = "symbols"; Path = $symbols; Exists = (Test-Path -LiteralPath $symbols); Directories = Count-Directories $symbols; Files = Count-Files $symbols; KeyFiles = Count-Files $symbols "*.kicad_sym" },
    [pscustomobject]@{ Area = "footprints"; Path = $footprints; Exists = (Test-Path -LiteralPath $footprints); Directories = Count-Directories $footprints "*.pretty"; Files = Count-Files $footprints; KeyFiles = Count-Files $footprints "*.kicad_mod" },
    [pscustomobject]@{ Area = "3dmodels"; Path = $models; Exists = (Test-Path -LiteralPath $models); Directories = Count-Directories $models "*.3dshapes"; Files = Count-Files $models; KeyFiles = (Count-Files $models "*.step") + (Count-Files $models "*.stp") + (Count-Files $models "*.wrl") },
    [pscustomobject]@{ Area = "templates"; Path = $templates; Exists = (Test-Path -LiteralPath $templates); Directories = Count-Directories $templates; Files = Count-Files $templates; KeyFiles = Count-Files $templates "*.kicad_pro" },
    [pscustomobject]@{ Area = "demos"; Path = $demos; Exists = (Test-Path -LiteralPath $demos); Directories = Count-Directories $demos; Files = Count-Files $demos; KeyFiles = Count-Files $demos "*.kicad_pro" },
    [pscustomobject]@{ Area = "scripting"; Path = $scripting; Exists = (Test-Path -LiteralPath $scripting); Directories = Count-Directories $scripting; Files = Count-Files $scripting; KeyFiles = Count-Files $scripting "*.py" }
)

$userConfigRoot = Join-Path $env:APPDATA "kicad\$VersionPreference"
$userRows = @(
    [pscustomobject]@{ Path = $userConfigRoot; Exists = (Test-Path -LiteralPath $userConfigRoot) },
    [pscustomobject]@{ Path = (Join-Path $userConfigRoot "sym-lib-table"); Exists = (Test-Path -LiteralPath (Join-Path $userConfigRoot "sym-lib-table")) },
    [pscustomobject]@{ Path = (Join-Path $userConfigRoot "fp-lib-table"); Exists = (Test-Path -LiteralPath (Join-Path $userConfigRoot "fp-lib-table")) },
    [pscustomobject]@{ Path = (Join-Path $userConfigRoot "kicad_common.json"); Exists = (Test-Path -LiteralPath (Join-Path $userConfigRoot "kicad_common.json")) }
)

Add-Heading -Lines $lines -Text "Result"
$lines.Add("Status: PASS") | Out-Null
$lines.Add("KiCad root: ``$root``") | Out-Null

Add-Heading -Lines $lines -Text "Installed Paths"
$lines.Add(($pathRows | Format-Table -AutoSize | Out-String -Width 220)) | Out-Null

Add-Heading -Lines $lines -Text "Executable Inventory"
$lines.Add(($exeRows | Format-Table -AutoSize | Out-String -Width 260)) | Out-Null

Add-Heading -Lines $lines -Text "Stock Asset Inventory"
$lines.Add(($assetRows | Format-Table -AutoSize | Out-String -Width 260)) | Out-Null

Add-Heading -Lines $lines -Text "User Config Discovery"
$lines.Add(($userRows | Format-Table -AutoSize | Out-String -Width 260)) | Out-Null

Add-Heading -Lines $lines -Text "Safety"
$lines.Add("- This script does not delete files.") | Out-Null
$lines.Add("- This script does not write to `C:\Program Files\KiCad`.") | Out-Null
$lines.Add("- This script does not run KiCad executables.") | Out-Null
$lines.Add("- Reports are written only to the selected output folder.") | Out-Null

Set-Content -LiteralPath $reportPath -Value $lines -Encoding UTF8

$json = [pscustomobject]@{
    created = (Get-Date -Format o)
    workspaceRoot = $workspaceRoot
    kicadRoot = $root
    checkedRoots = @($resolved.Checked)
    paths = @($pathRows)
    executables = @($exeRows)
    assets = @($assetRows)
    userConfig = @($userRows)
}
$json | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $jsonPath -Encoding UTF8

Write-Host "Report written: $reportPath"
Write-Host "JSON written: $jsonPath"
exit 0
