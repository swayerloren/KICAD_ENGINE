[CmdletBinding()]
param(
    [string]$RepoRoot = '',
    [switch]$OfferInstall,
    [switch]$SkipIndexes,
    [switch]$SkipHealthCheck
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($RepoRoot)) {
    $RepoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..\..')).ProviderPath
} else {
    $RepoRoot = (Resolve-Path -LiteralPath $RepoRoot).ProviderPath
}

function Get-PythonCommand {
    $python = Get-Command python -ErrorAction SilentlyContinue
    if ($python) { return $python.Source }
    $python3 = Get-Command python3 -ErrorAction SilentlyContinue
    if ($python3) { return $python3.Source }
    throw 'Python was not found on PATH. Setup cannot run common Python helpers.'
}

$python = Get-PythonCommand
Write-Host "KiCad Engine Windows setup"
Write-Host "Repo root: $RepoRoot"
Write-Host 'This script does not install tools unless -OfferInstall is used and you confirm each install.'

if ($OfferInstall) {
    $installer = Join-Path $PSScriptRoot 'install_missing_windows_tools.ps1'
    & $installer -RepoRoot $RepoRoot -Apply
}

& $python (Join-Path $RepoRoot 'setup\common\create_repo_folders.py') --repo-root $RepoRoot

if (-not $SkipIndexes) {
    & $python (Join-Path $RepoRoot 'setup\common\build_indexes.py') --repo-root $RepoRoot
}

if (-not $SkipHealthCheck) {
    & (Join-Path $RepoRoot 'health_check.ps1') -RepoRoot $RepoRoot
}

& $python (Join-Path $RepoRoot 'setup\common\write_setup_report.py') --repo-root $RepoRoot

Write-Host 'Windows setup completed. Review reports under 05_OUTPUTS before trusting the environment.'
