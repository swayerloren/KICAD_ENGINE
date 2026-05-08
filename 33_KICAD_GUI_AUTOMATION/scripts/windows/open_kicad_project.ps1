param(
    [Parameter(Mandatory=$true)]
    [string]$ProjectPath,

    [Parameter(Mandatory=$true)]
    [string]$SchematicPath,

    [string]$PythonPath = ".\03_TOOLS\python_envs\windows_gui\Scripts\python.exe",

    [switch]$Live
)

$ErrorActionPreference = "Stop"

$scriptPath = Join-Path $PSScriptRoot "open_kicad_project.py"
$argsList = @($scriptPath, "--project", $ProjectPath, "--schematic", $SchematicPath)
if ($Live) { $argsList += "--live" }

& $PythonPath @argsList
exit $LASTEXITCODE

