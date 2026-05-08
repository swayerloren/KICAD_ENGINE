[CmdletBinding()]
param(
    [string]$SourceRoot,
    [string]$PayloadRoot,
    [int]$MaxFileSizeMB = 5,
    [switch]$NoClean
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

if (-not $SourceRoot) {
    $SourceRoot = (Resolve-Path -LiteralPath (Join-Path $ScriptDir "..\..")).Path
}

if (-not $PayloadRoot) {
    $PayloadRoot = $ScriptDir
}

$Python = Get-Command python -ErrorAction SilentlyContinue
if (-not $Python) {
    throw "Python was not found on PATH. Install Python or run build_payload.py with an explicit Python interpreter."
}

$ArgsList = @(
    (Join-Path $ScriptDir "build_payload.py"),
    "--source-root", $SourceRoot,
    "--payload-root", $PayloadRoot,
    "--max-file-size-mb", [string]$MaxFileSizeMB
)

if ($NoClean) {
    $ArgsList += "--no-clean"
}

& $Python.Source @ArgsList
exit $LASTEXITCODE
