[CmdletBinding()]
param(
    [string]$RepoRoot = '',
    [string[]]$Tools = @('git', 'python', 'node', 'vscode', 'kicad'),
    [switch]$DryRun,
    [switch]$Apply
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'

Write-Host 'KiCad Engine Windows optional installer'
Write-Host 'Default mode is DRY-RUN. Pass -Apply to allow install prompts.'
Write-Host 'This script asks before each install when -Apply is used. It does not store API keys or install paid tools.'
if (-not $Apply) {
    $DryRun = $true
}

$winget = Get-Command winget -ErrorAction SilentlyContinue
if (-not $winget) {
    Write-Warning 'winget was not found. Install tools manually from official vendor sources.'
    exit 2
}

$toolMap = @{
    git = @{
        Command = 'git'
        Package = 'Git.Git'
        Display = 'Git'
    }
    python = @{
        Command = 'python'
        Package = 'Python.Python.3.12'
        Display = 'Python'
    }
    node = @{
        Command = 'node'
        Package = 'OpenJS.NodeJS.LTS'
        Display = 'Node.js LTS'
    }
    vscode = @{
        Command = 'code'
        Package = 'Microsoft.VisualStudioCode'
        Display = 'Visual Studio Code'
    }
    kicad = @{
        Command = 'kicad-cli'
        Package = 'KiCad.KiCad'
        Display = 'KiCad'
    }
}

foreach ($tool in $Tools) {
    if (-not $toolMap.ContainsKey($tool)) {
        Write-Warning "Unknown tool key skipped: $tool"
        continue
    }

    $entry = $toolMap[$tool]
    $command = Get-Command $entry.Command -ErrorAction SilentlyContinue
    if ($command) {
        Write-Host "$($entry.Display) already appears available: $($command.Source)"
        continue
    }

    $packageId = $entry.Package
    Write-Host ""
    Write-Host "Missing: $($entry.Display)"
    Write-Host "Proposed command:"
    Write-Host "winget install --id $packageId --exact --source winget"

    if ($DryRun) {
        Write-Host 'Dry run only. Not installing. Re-run with -Apply to allow a confirmation prompt.'
        continue
    }

    $answer = Read-Host "Type YES to install $($entry.Display) with winget"
    if ($answer -ne 'YES') {
        Write-Host "Skipped $($entry.Display)."
        continue
    }

    & $winget.Source install --id $packageId --exact --source winget
    if ($LASTEXITCODE -ne 0) {
        Write-Warning "winget returned exit code $LASTEXITCODE for $($entry.Display)."
    }
}

Write-Host 'Installer finished. Restart VS Code or your terminal if PATH changed.'
