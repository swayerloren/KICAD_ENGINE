[CmdletBinding()]
param(
    [string]$RepoRoot = '',
    [string]$OutputDir = ''
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($RepoRoot)) {
    $RepoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..\..')).ProviderPath
} else {
    $RepoRoot = (Resolve-Path -LiteralPath $RepoRoot).ProviderPath
}

$healthCheck = Join-Path $RepoRoot 'health_check.ps1'
if (-not (Test-Path -LiteralPath $healthCheck -PathType Leaf)) {
    throw "Missing health_check.ps1: $healthCheck"
}

$params = @{
    RepoRoot = $RepoRoot
}
if (-not [string]::IsNullOrWhiteSpace($OutputDir)) {
    $params.OutputDir = $OutputDir
}

Write-Host "Running read-only Windows requirements check for $RepoRoot"
& $healthCheck @params
exit $LASTEXITCODE
