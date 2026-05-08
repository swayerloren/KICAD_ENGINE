[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string]$ProjectName
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'

function Get-WorkspaceRoot {
    $scriptsRoot = if ($PSScriptRoot) {
        $PSScriptRoot
    } else {
        Split-Path -Parent $MyInvocation.MyCommand.Path
    }

    $toolsRoot = Split-Path -Parent $scriptsRoot
    return (Split-Path -Parent $toolsRoot)
}

function Get-SafeProjectName {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Name
    )

    $trimmed = $Name.Trim()
    if ([string]::IsNullOrWhiteSpace($trimmed)) {
        throw 'ProjectName cannot be empty.'
    }

    if ($trimmed -in @('.', '..')) {
        throw 'ProjectName cannot be . or ..'
    }

    $invalidChars = [System.IO.Path]::GetInvalidFileNameChars()
    foreach ($char in $trimmed.ToCharArray()) {
        if ($invalidChars -contains $char) {
            throw "ProjectName contains an invalid path character: $char"
        }
    }

    return $trimmed
}

function Set-TemplatePlaceholders {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,

        [Parameter(Mandatory = $true)]
        [string]$Name,

        [Parameter(Mandatory = $true)]
        [string]$ProjectPath
    )

    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        return
    }

    $content = Get-Content -LiteralPath $Path -Raw
    $content = $content.Replace('PROJECT_NAME', $Name)
    $content = $content.Replace('PROJECT_PATH', $ProjectPath)
    Set-Content -LiteralPath $Path -Value $content -Encoding UTF8
}

function New-FileIfMissing {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,

        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string[]]$Lines
    )

    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        Set-Content -LiteralPath $Path -Value $Lines -Encoding UTF8
    }
}

$workspaceRoot = Get-WorkspaceRoot
$workspaceRoot = (Resolve-Path -LiteralPath $workspaceRoot).ProviderPath
$safeProjectName = Get-SafeProjectName -Name $ProjectName

$templatePath = Join-Path -Path $workspaceRoot -ChildPath '04_KICAD_PROJECTS\templates\STANDARD_KICAD_PROJECT_TEMPLATE'
$activeRoot = Join-Path -Path $workspaceRoot -ChildPath '04_KICAD_PROJECTS\active'
$projectPath = Join-Path -Path $activeRoot -ChildPath $safeProjectName
$memoryPath = Join-Path -Path $workspaceRoot -ChildPath (Join-Path -Path '01_MEMORY\projects' -ChildPath $safeProjectName)
$historyPath = Join-Path -Path $workspaceRoot -ChildPath (Join-Path -Path '02_HISTORY\project_history' -ChildPath $safeProjectName)
$projectIndexPath = Join-Path -Path $workspaceRoot -ChildPath '00_CODEX_START\PROJECT_INDEX.md'

if (-not (Test-Path -LiteralPath $templatePath -PathType Container)) {
    throw "Project template folder does not exist: $templatePath"
}

if (Test-Path -LiteralPath $projectPath) {
    throw "Project already exists. Nothing was overwritten: $projectPath"
}

New-Item -ItemType Directory -Force -Path $activeRoot | Out-Null
New-Item -ItemType Directory -Path $projectPath | Out-Null

Get-ChildItem -LiteralPath $templatePath -Force | ForEach-Object {
    Copy-Item -LiteralPath $_.FullName -Destination $projectPath -Recurse -Force
}

foreach ($folder in @('kicad', 'datasheets', 'bom', 'fabrication', 'renders', 'reports', 'notes', 'scripts', 'memory', 'history')) {
    New-Item -ItemType Directory -Force -Path (Join-Path -Path $projectPath -ChildPath $folder) | Out-Null
}

Set-TemplatePlaceholders -Path (Join-Path -Path $projectPath -ChildPath 'README.md') -Name $safeProjectName -ProjectPath $projectPath
Set-TemplatePlaceholders -Path (Join-Path -Path $projectPath -ChildPath 'AGENTS.md') -Name $safeProjectName -ProjectPath $projectPath

New-Item -ItemType Directory -Force -Path $memoryPath | Out-Null
New-FileIfMissing -Path (Join-Path -Path $memoryPath -ChildPath 'PROJECT_MEMORY.md') -Lines @(
    "# $safeProjectName Project Memory",
    '',
    'Durable project decisions, constraints, and preferences belong here.',
    '',
    'Do not store command logs or secrets in this file.'
)

New-Item -ItemType Directory -Force -Path $historyPath | Out-Null
New-FileIfMissing -Path (Join-Path -Path $historyPath -ChildPath 'README.md') -Lines @(
    "# $safeProjectName Project History",
    '',
    'Project-specific session summaries, reviews, command notes, and milestone history belong here.',
    '',
    'Do not store secrets in this folder.'
)

if (-not (Test-Path -LiteralPath $projectIndexPath -PathType Leaf)) {
    throw "PROJECT_INDEX.md was not found: $projectIndexPath"
}

$relativeProjectPath = "04_KICAD_PROJECTS\active\$safeProjectName"
$relativeMemoryPath = "01_MEMORY\projects\$safeProjectName\PROJECT_MEMORY.md"
$relativeHistoryPath = "02_HISTORY\project_history\$safeProjectName"
$indexContent = Get-Content -LiteralPath $projectIndexPath -Raw

if ($indexContent -notmatch [regex]::Escape("## Project: $safeProjectName")) {
    Add-Content -LiteralPath $projectIndexPath -Encoding UTF8 -Value @(
        '',
        "## Project: $safeProjectName",
        ('- Project path: `{0}`' -f $relativeProjectPath),
        '- Status: CREATED_NOT_ACTIVE',
        '- Board purpose: TBD',
        '- KiCad version: TBD',
        '- Important electrical constraints: TBD',
        '- Important mechanical constraints: TBD',
        '- Fabrication constraints: TBD',
        ('- Related project memory file: `{0}`' -f $relativeMemoryPath),
        '- Latest review or verification report: NONE',
        ('- Project history folder: `{0}`' -f $relativeHistoryPath)
    )
}

Write-Output "Created project workspace: $projectPath"
Write-Output "Created project memory folder: $memoryPath"
Write-Output "Created project history folder: $historyPath"
Write-Output "Updated project index: $projectIndexPath"
Write-Output ''
Write-Output 'Next steps:'
Write-Output '1. Review the new project README.md and AGENTS.md.'
Write-Output '2. Update CURRENT_PROJECT.md only if this project should become active.'
Write-Output '3. Add or create KiCad files under the project kicad folder.'
Write-Output '4. Before protected KiCad edits, confirm backup, verification plan, and rollback plan.'
