<#
.SYNOPSIS
Run the KiCad Engine project gate runner.

.DESCRIPTION
This wrapper calls run_project_gate.py in read-only evidence aggregation mode.
It does not edit KiCad files, run ERC/DRC, or generate fabrication outputs.

.PARAMETER ProjectPath
Path to the project directory to inspect.

.PARAMETER OutputDir
Optional output directory. Default is 05_OUTPUTS/gate_runs/<timestamp>/.

.PARAMETER Gates
Optional comma-separated gate IDs to run.

.PARAMETER VerboseOutput
Print blocker details while running.

.EXAMPLE
.\03_TOOLS\scripts\project_gate\run_project_gate.ps1 -ProjectPath "19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board"
#>

param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectPath,

    [string]$OutputDir,

    [string]$Gates,

    [switch]$VerboseOutput
)

$ErrorActionPreference = "Stop"

$ResolvedProjectPath = (Resolve-Path -Path $ProjectPath).Path
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PythonScript = Join-Path $ScriptDir "run_project_gate.py"

if (-not (Test-Path -LiteralPath $PythonScript)) {
    Write-Error "Missing Python gate runner: $PythonScript"
}

$PythonCommand = Get-Command python -ErrorAction SilentlyContinue
if (-not $PythonCommand) {
    $PythonCommand = Get-Command python3 -ErrorAction SilentlyContinue
}
if (-not $PythonCommand) {
    Write-Error "Python was not found in PATH."
}

$PythonArgs = @(
    $PythonScript,
    "--project-path",
    $ResolvedProjectPath
)

if ($OutputDir) {
    $PythonArgs += @("--output-dir", $OutputDir)
}
if ($Gates) {
    $PythonArgs += @("--gates", $Gates)
}
if ($VerboseOutput) {
    $PythonArgs += "--verbose"
}

Write-Host "KiCad Engine Project Gate Runner" -ForegroundColor Cyan
Write-Host "Mode: read-only evidence aggregation" -ForegroundColor Gray
Write-Host "Project: $ResolvedProjectPath" -ForegroundColor Gray
Write-Host ""

& $PythonCommand.Source @PythonArgs
exit $LASTEXITCODE
