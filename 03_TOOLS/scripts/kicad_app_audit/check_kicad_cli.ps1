[CmdletBinding()]
param(
    [string]$KiCadRoot,
    [string]$KiCadCliPath,
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

function Resolve-KiCadCli {
    param(
        [string]$Root,
        [string]$ExplicitCli,
        [string]$PreferredVersion
    )

    $checked = New-Object System.Collections.Generic.List[string]

    if ($ExplicitCli) {
        $checked.Add($ExplicitCli) | Out-Null
        if (Test-Path -LiteralPath $ExplicitCli) {
            return [pscustomobject]@{ Path = (Resolve-Path -LiteralPath $ExplicitCli).Path; Checked = $checked }
        }
    }

    if ($Root) {
        $candidate = Join-Path $Root "bin\kicad-cli.exe"
        $checked.Add($candidate) | Out-Null
        if (Test-Path -LiteralPath $candidate) {
            return [pscustomobject]@{ Path = (Resolve-Path -LiteralPath $candidate).Path; Checked = $checked }
        }
    }

    $preferred = "C:\Program Files\KiCad\$PreferredVersion\bin\kicad-cli.exe"
    $checked.Add($preferred) | Out-Null
    if (Test-Path -LiteralPath $preferred) {
        return [pscustomobject]@{ Path = (Resolve-Path -LiteralPath $preferred).Path; Checked = $checked }
    }

    $installRoot = "C:\Program Files\KiCad"
    if (Test-Path -LiteralPath $installRoot) {
        $candidates = Get-ChildItem -LiteralPath $installRoot -Directory -ErrorAction SilentlyContinue |
            ForEach-Object {
                $cli = Join-Path $_.FullName "bin\kicad-cli.exe"
                $checked.Add($cli) | Out-Null
                if (Test-Path -LiteralPath $cli) { Get-Item -LiteralPath $cli }
            } |
            Sort-Object FullName -Descending

        if ($candidates) {
            return [pscustomobject]@{ Path = $candidates[0].FullName; Checked = $checked }
        }
    }

    $cmd = Get-Command "kicad-cli.exe" -ErrorAction SilentlyContinue
    if ($cmd) {
        $checked.Add($cmd.Source) | Out-Null
        return [pscustomobject]@{ Path = $cmd.Source; Checked = $checked }
    }

    return [pscustomobject]@{ Path = $null; Checked = $checked }
}

$workspaceRoot = Resolve-WorkspaceRoot
if (-not $OutputRoot) {
    $OutputRoot = Join-Path $workspaceRoot "02_HISTORY\command_logs"
}
New-Item -ItemType Directory -Force -Path $OutputRoot | Out-Null

$stamp = Get-Date -Format "yyyyMMdd_HHmmss"
$reportPath = Join-Path $OutputRoot "KICAD_CLI_VERSION_CHECK_$stamp.md"

$resolved = Resolve-KiCadCli -Root $KiCadRoot -ExplicitCli $KiCadCliPath -PreferredVersion $VersionPreference

$lines = New-Object System.Collections.Generic.List[string]
$lines.Add("# KiCad CLI Version Check") | Out-Null
$lines.Add("") | Out-Null
$lines.Add("Created: $(Get-Date -Format o)") | Out-Null
$lines.Add("Workspace: ``$workspaceRoot``") | Out-Null
$lines.Add("") | Out-Null
$lines.Add("## Checked Paths") | Out-Null
foreach ($path in $resolved.Checked) {
    $lines.Add("- ``$path``") | Out-Null
}
$lines.Add("") | Out-Null

if (-not $resolved.Path) {
    $lines.Add("## Result") | Out-Null
    $lines.Add("") | Out-Null
    $lines.Add("Status: FAIL") | Out-Null
    $lines.Add("") | Out-Null
    $lines.Add("No `kicad-cli.exe` was found. No KiCad commands were run.") | Out-Null
    Set-Content -LiteralPath $reportPath -Value $lines -Encoding UTF8
    Write-Error "kicad-cli.exe was not found. Report: $reportPath"
    exit 2
}

$output = & $resolved.Path version 2>&1
$exitCode = $LASTEXITCODE

$lines.Add("## Result") | Out-Null
$lines.Add("") | Out-Null
$lines.Add("Status: $(if ($exitCode -eq 0) { 'PASS' } else { 'FAIL' })") | Out-Null
$lines.Add("Executable: ``$($resolved.Path)``") | Out-Null
$lines.Add("Exit code: ``$exitCode``") | Out-Null
$lines.Add("") | Out-Null
$lines.Add("## Command Run") | Out-Null
$lines.Add("") | Out-Null
$lines.Add("Only this command was run:") | Out-Null
$lines.Add("") | Out-Null
$lines.Add("``````powershell") | Out-Null
$lines.Add("& `"$($resolved.Path)`" version") | Out-Null
$lines.Add("``````") | Out-Null
$lines.Add("") | Out-Null
$lines.Add("## Output") | Out-Null
$lines.Add("") | Out-Null
$lines.Add("``````text") | Out-Null
foreach ($line in $output) {
    $lines.Add([string]$line) | Out-Null
}
$lines.Add("``````") | Out-Null
$lines.Add("") | Out-Null
$lines.Add("## Safety") | Out-Null
$lines.Add("") | Out-Null
$lines.Add("- No project files were inspected or modified.") | Out-Null
$lines.Add("- No files were written under `C:\Program Files\KiCad`.") | Out-Null
$lines.Add("- No ERC, DRC, export, GUI, package manager, or plugin command was run.") | Out-Null

Set-Content -LiteralPath $reportPath -Value $lines -Encoding UTF8
Write-Host "Report written: $reportPath"
exit $exitCode
