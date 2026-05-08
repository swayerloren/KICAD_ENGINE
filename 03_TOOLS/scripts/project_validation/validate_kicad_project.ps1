[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectPath,

    [string]$OutputDir = '',
    [string]$KiCadCliPath = '',
    [string]$KiCadVersion = '',
    [string]$ComponentDbRoot = '',
    [string]$DatasheetRoot = '',
    [string[]]$Checks = @(),
    [switch]$AllowProjectOutput,
    [switch]$FailOnFail
)

$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonScript = Join-Path -Path $scriptDir -ChildPath 'validate_kicad_project.py'

if (-not (Test-Path -LiteralPath $pythonScript)) {
    throw "Missing Python validator: $pythonScript"
}

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    throw 'Python was not found on PATH. This wrapper does not install tools.'
}

$argsList = @($pythonScript, $ProjectPath)
if ($OutputDir) { $argsList += @('--output-dir', $OutputDir) }
if ($KiCadCliPath) { $argsList += @('--kicad-cli', $KiCadCliPath) }
if ($KiCadVersion) { $argsList += @('--kicad-version', $KiCadVersion) }
if ($ComponentDbRoot) { $argsList += @('--component-db-root', $ComponentDbRoot) }
if ($DatasheetRoot) { $argsList += @('--datasheet-root', $DatasheetRoot) }
if ($Checks.Count -gt 0) { $argsList += @('--checks', ($Checks -join ',')) }
if ($AllowProjectOutput) { $argsList += '--allow-project-output' }
if ($FailOnFail) { $argsList += '--fail-on-fail' }

& $python.Source @argsList
exit $LASTEXITCODE
