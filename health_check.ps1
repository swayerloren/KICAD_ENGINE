[CmdletBinding()]
param(
    [string]$RepoRoot = '',
    [string]$OutputDir = '',
    [string]$PythonPath = '',
    [switch]$NoWrite,
    [switch]$FailOnFail,
    [switch]$FailOnWarn
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($RepoRoot)) {
    $RepoRoot = $PSScriptRoot
} else {
    $RepoRoot = (Resolve-Path -LiteralPath $RepoRoot).ProviderPath
}

if ([string]::IsNullOrWhiteSpace($PythonPath)) {
    $python = Get-Command python -ErrorAction SilentlyContinue
    if (-not $python) {
        $python = Get-Command python3 -ErrorAction SilentlyContinue
    }
    if (-not $python) {
        throw 'Python was not found on PATH. This script does not install tools.'
    }
    $PythonPath = $python.Source
}

$scriptPath = Join-Path $RepoRoot 'health_check.py'
if (-not (Test-Path -LiteralPath $scriptPath -PathType Leaf)) {
    throw "Missing health_check.py: $scriptPath"
}

$argsList = @($scriptPath, '--repo-root', $RepoRoot)
if (-not [string]::IsNullOrWhiteSpace($OutputDir)) {
    $argsList += @('--output-dir', $OutputDir)
}
if ($NoWrite) {
    $argsList += '--no-write'
}
if ($FailOnFail) {
    $argsList += '--fail-on-fail'
}
if ($FailOnWarn) {
    $argsList += '--fail-on-warn'
}

& $PythonPath @argsList
exit $LASTEXITCODE
