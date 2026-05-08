[CmdletBinding()]
param(
    [string]$WorkspaceRoot = ''
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($WorkspaceRoot)) {
    $scriptsRoot = if ($PSScriptRoot) {
        $PSScriptRoot
    } else {
        Split-Path -Parent $MyInvocation.MyCommand.Path
    }
    $WorkspaceRoot = Split-Path -Parent (Split-Path -Parent $scriptsRoot)
}

if (-not (Test-Path -LiteralPath $WorkspaceRoot -PathType Container)) {
    throw "WorkspaceRoot does not exist: $WorkspaceRoot"
}

$WorkspaceRoot = (Resolve-Path -LiteralPath $WorkspaceRoot).ProviderPath
$reportPath = Join-Path -Path $WorkspaceRoot -ChildPath '03_TOOLS\tool_logs\KICAD_ENGINE_HEALTH_CHECK.md'
$results = New-Object System.Collections.Generic.List[object]

function Add-HealthResult {
    param(
        [ValidateSet('PASS', 'WARN', 'FAIL')]
        [string]$Status,

        [Parameter(Mandatory = $true)]
        [string]$Category,

        [Parameter(Mandatory = $true)]
        [string]$Name,

        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string]$Detail
    )

    $script:results.Add([pscustomobject]@{
        Status = $Status
        Category = $Category
        Name = $Name
        Detail = $Detail
    })
}

function Test-RequiredPath {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Category,

        [Parameter(Mandatory = $true)]
        [string]$RelativePath,

        [ValidateSet('Any', 'File', 'Directory')]
        [string]$PathType = 'Any'
    )

    $fullPath = Join-Path -Path $WorkspaceRoot -ChildPath $RelativePath
    $exists = if ($PathType -eq 'File') {
        Test-Path -LiteralPath $fullPath -PathType Leaf
    } elseif ($PathType -eq 'Directory') {
        Test-Path -LiteralPath $fullPath -PathType Container
    } else {
        Test-Path -LiteralPath $fullPath
    }

    if ($exists) {
        Add-HealthResult -Status 'PASS' -Category $Category -Name $RelativePath -Detail 'Found.'
    } else {
        Add-HealthResult -Status 'FAIL' -Category $Category -Name $RelativePath -Detail 'Missing.'
    }
}

function Get-FirstCommand {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$Names
    )

    foreach ($name in $Names) {
        $command = Get-Command $name -ErrorAction SilentlyContinue
        if ($command) {
            return $command
        }
    }

    return $null
}

function Find-KiCadCli {
    $command = Get-FirstCommand -Names @('kicad-cli', 'kicad-cli.exe')
    if ($command) {
        return [pscustomobject]@{
            Status = 'PATH'
            Path = $command.Source
        }
    }

    $programFilesKiCad = 'C:\Program Files\KiCad'
    if (Test-Path -LiteralPath $programFilesKiCad -PathType Container) {
        $matches = @(
            Get-ChildItem -LiteralPath $programFilesKiCad -Recurse -Filter 'kicad-cli.exe' -File -ErrorAction SilentlyContinue |
                Sort-Object -Property FullName -Descending
        )
        if ($matches.Count -gt 0) {
            return [pscustomobject]@{
                Status = 'FOUND_NOT_ON_PATH'
                Path = $matches[0].FullName
            }
        }
    }

    return [pscustomobject]@{
        Status = 'MISSING'
        Path = ''
    }
}

function Get-ToolIndexStatuses {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path
    )

    $statuses = @{}
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        return $statuses
    }

    $currentHeading = ''
    foreach ($line in Get-Content -LiteralPath $Path) {
        if ($line -match '^(#{2,3})\s+(.+?)\s*$') {
            $currentHeading = $Matches[2].Trim()
            continue
        }

        if (-not [string]::IsNullOrWhiteSpace($currentHeading) -and $line -match '^\-\s+Status:\s*(.+?)\s*$') {
            if (-not $statuses.ContainsKey($currentHeading)) {
                $statuses[$currentHeading] = $Matches[1].Trim()
            }
        }
    }

    return $statuses
}

function Get-ToolStatusHealth {
    param(
        [Parameter(Mandatory = $true)]
        [string]$StatusText
    )

    if ([string]::IsNullOrWhiteSpace($StatusText)) {
        return 'FAIL'
    }

    if ($StatusText -match 'BLOCKED|MISSING|FAILED') {
        return 'FAIL'
    }

    if ($StatusText -match 'NOT_ON_PATH|NOT_INSTALLED|NOT_PROJECT_TESTED|CLONED_NOT_INSTALLED|OUTPUT_AUTOMATION_NOT_PROJECT_TESTED|HELP_TESTED_NOT_PROJECT_TESTED|DEGRADED') {
        return 'WARN'
    }

    return 'PASS'
}

function ConvertTo-MarkdownSafeText {
    param(
        [AllowEmptyString()]
        [string]$Text
    )

    return ($Text -replace '\|', '\|')
}

$workspaceFolders = @(
    '.codex',
    '.codex\prompts',
    '00_CODEX_START',
    '01_MEMORY',
    '01_MEMORY\projects',
    '02_HISTORY',
    '02_HISTORY\sessions',
    '02_HISTORY\command_logs',
    '02_HISTORY\design_reviews',
    '02_HISTORY\erc_drc_reports',
    '02_HISTORY\fabrication_reviews',
    '02_HISTORY\project_history',
    '03_TOOLS',
    '03_TOOLS\repos',
    '03_TOOLS\scripts',
    '03_TOOLS\tool_logs',
    '04_KICAD_PROJECTS',
    '04_KICAD_PROJECTS\active',
    '04_KICAD_PROJECTS\templates',
    '05_OUTPUTS',
    '06_DATASHEETS',
    '99_BACKUPS',
    '99_BACKUPS\pre_codex_edits'
)

foreach ($folder in $workspaceFolders) {
    Test-RequiredPath -Category 'Workspace Folder' -RelativePath $folder -PathType 'Directory'
}

Test-RequiredPath -Category 'Root Instruction' -RelativePath 'AGENTS.md' -PathType 'File'
Test-RequiredPath -Category 'Codex Config' -RelativePath '.codex\config.toml' -PathType 'File'

$startupFiles = @(
    '00_CODEX_START\START_HERE.md',
    '00_CODEX_START\SESSION_START_CHECKLIST.md',
    '00_CODEX_START\WORKFLOW_RULES.md',
    '00_CODEX_START\SAFETY_RULES.md',
    '00_CODEX_START\REPO_MAP.md',
    '00_CODEX_START\TOOL_INDEX.md',
    '00_CODEX_START\MEMORY_INDEX.md',
    '00_CODEX_START\HISTORY_INDEX.md',
    '00_CODEX_START\PROJECT_INDEX.md',
    '00_CODEX_START\CURRENT_PROJECT.md'
)

foreach ($file in $startupFiles) {
    Test-RequiredPath -Category 'Startup File' -RelativePath $file -PathType 'File'
}

$promptFiles = @(
    '.codex\prompts\START_CODEX_KICAD_ENGINE.md',
    '.codex\prompts\NEW_KICAD_PROJECT.md',
    '.codex\prompts\REVIEW_EXISTING_PROJECT.md',
    '.codex\prompts\VERIFY_BEFORE_FAB.md',
    '.codex\prompts\INSTALL_KICAD_TOOLS.md'
)

foreach ($file in $promptFiles) {
    Test-RequiredPath -Category 'Prompt File' -RelativePath $file -PathType 'File'
}

$memoryFiles = @(
    '01_MEMORY\GLOBAL_MEMORY.md',
    '01_MEMORY\DESIGN_RULES_MEMORY.md',
    '01_MEMORY\COMPONENT_PREFERENCES.md',
    '01_MEMORY\FAB_HOUSE_PREFERENCES.md',
    '01_MEMORY\CODING_AND_SCRIPTING_RULES.md'
)

foreach ($file in $memoryFiles) {
    Test-RequiredPath -Category 'Memory File' -RelativePath $file -PathType 'File'
}

$toolRepos = @(
    '03_TOOLS\repos\kicad-mcp-pro',
    '03_TOOLS\repos\kicad-happy',
    '03_TOOLS\repos\KiCAD-MCP-Server',
    '03_TOOLS\repos\KiBot',
    '03_TOOLS\repos\InteractiveHtmlBom',
    '03_TOOLS\repos\PcbDraw',
    '03_TOOLS\repos\kicanvas'
)

foreach ($repo in $toolRepos) {
    Test-RequiredPath -Category 'Tool Repo' -RelativePath $repo -PathType 'Directory'
}

$verificationScripts = @(
    '03_TOOLS\scripts\run_erc.ps1',
    '03_TOOLS\scripts\run_drc.ps1',
    '03_TOOLS\scripts\export_gerbers.ps1',
    '03_TOOLS\scripts\export_drill.ps1',
    '03_TOOLS\scripts\export_step.ps1',
    '03_TOOLS\scripts\export_bom.ps1',
    '03_TOOLS\scripts\full_verify_project.ps1',
    '03_TOOLS\scripts\backup_kicad_project.ps1',
    '03_TOOLS\scripts\find_kicad_project_files.ps1',
    '03_TOOLS\scripts\kicad_automation_common.ps1'
)

foreach ($scriptPath in $verificationScripts) {
    Test-RequiredPath -Category 'Verification Script' -RelativePath $scriptPath -PathType 'File'
}

$toolIndexPath = Join-Path -Path $WorkspaceRoot -ChildPath '00_CODEX_START\TOOL_INDEX.md'
$toolStatuses = Get-ToolIndexStatuses -Path $toolIndexPath
$expectedToolStatusNames = @(
    'KiCad',
    'kicad-cli',
    'Codex CLI/App',
    'Workspace PowerShell Automation Scripts',
    'kicad-mcp-pro',
    'kicad-happy',
    'KiCAD-MCP-Server',
    'KiBot',
    'InteractiveHtmlBom',
    'PcbDraw',
    'KiCanvas'
)

foreach ($toolName in $expectedToolStatusNames) {
    if ($toolStatuses.ContainsKey($toolName)) {
        $statusText = [string]$toolStatuses[$toolName]
        Add-HealthResult -Status (Get-ToolStatusHealth -StatusText $statusText) -Category 'Tool Index Status' -Name $toolName -Detail $statusText
    } else {
        Add-HealthResult -Status 'FAIL' -Category 'Tool Index Status' -Name $toolName -Detail 'No status entry found in TOOL_INDEX.md.'
    }
}

$kiCadCli = Find-KiCadCli
if ($kiCadCli.Status -eq 'PATH') {
    Add-HealthResult -Status 'PASS' -Category 'Runtime Tool' -Name 'kicad-cli' -Detail "Found on PATH: $($kiCadCli.Path)"
} elseif ($kiCadCli.Status -eq 'FOUND_NOT_ON_PATH') {
    Add-HealthResult -Status 'WARN' -Category 'Runtime Tool' -Name 'kicad-cli' -Detail "Found but not on PATH: $($kiCadCli.Path)"
} else {
    Add-HealthResult -Status 'FAIL' -Category 'Runtime Tool' -Name 'kicad-cli' -Detail 'Not found on PATH or under C:\Program Files\KiCad.'
}

$pythonCommand = Get-FirstCommand -Names @('python', 'python.exe')
$pyLauncher = Get-FirstCommand -Names @('py', 'py.exe')
if ($pythonCommand) {
    Add-HealthResult -Status 'PASS' -Category 'Runtime Tool' -Name 'Python' -Detail "Found python command: $($pythonCommand.Source)"
} elseif ($pyLauncher) {
    Add-HealthResult -Status 'WARN' -Category 'Runtime Tool' -Name 'Python' -Detail "python is not on PATH, but Windows py launcher exists: $($pyLauncher.Source)"
} else {
    Add-HealthResult -Status 'FAIL' -Category 'Runtime Tool' -Name 'Python' -Detail 'No python command or py launcher found.'
}

$nodeCommand = Get-FirstCommand -Names @('node', 'node.exe')
if ($nodeCommand) {
    Add-HealthResult -Status 'PASS' -Category 'Runtime Tool' -Name 'Node' -Detail "Found: $($nodeCommand.Source)"
} else {
    Add-HealthResult -Status 'FAIL' -Category 'Runtime Tool' -Name 'Node' -Detail 'Node was not found on PATH.'
}

$gitCommand = Get-FirstCommand -Names @('git', 'git.exe')
if ($gitCommand) {
    Add-HealthResult -Status 'PASS' -Category 'Runtime Tool' -Name 'Git' -Detail "Found: $($gitCommand.Source)"
} else {
    Add-HealthResult -Status 'FAIL' -Category 'Runtime Tool' -Name 'Git' -Detail 'Git was not found on PATH.'
}

$passCount = @($results | Where-Object { $_.Status -eq 'PASS' }).Count
$warnCount = @($results | Where-Object { $_.Status -eq 'WARN' }).Count
$failCount = @($results | Where-Object { $_.Status -eq 'FAIL' }).Count

$reportDirectory = Split-Path -Parent $reportPath
if (-not (Test-Path -LiteralPath $reportDirectory -PathType Container)) {
    throw "Health check report folder is missing: $reportDirectory"
}

$markdown = New-Object System.Collections.Generic.List[string]
$markdown.Add('# KiCad Engine Health Check')
$markdown.Add('')
$markdown.Add("Created: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')")
$markdown.Add(('Workspace root: `{0}`' -f $WorkspaceRoot))
$markdown.Add('')
$markdown.Add('## Summary')
$markdown.Add('')
$markdown.Add("- PASS: $passCount")
$markdown.Add("- WARN: $warnCount")
$markdown.Add("- FAIL: $failCount")
$markdown.Add('')
$markdown.Add('## Results')
$markdown.Add('')
$markdown.Add('| Status | Category | Check | Detail |')
$markdown.Add('| --- | --- | --- | --- |')
foreach ($result in $results) {
    $markdown.Add(('| {0} | {1} | {2} | {3} |' -f
        (ConvertTo-MarkdownSafeText -Text $result.Status),
        (ConvertTo-MarkdownSafeText -Text $result.Category),
        (ConvertTo-MarkdownSafeText -Text $result.Name),
        (ConvertTo-MarkdownSafeText -Text $result.Detail)))
}

$failures = @($results | Where-Object { $_.Status -eq 'FAIL' })
$warnings = @($results | Where-Object { $_.Status -eq 'WARN' })

$markdown.Add('')
$markdown.Add('## Blockers')
$markdown.Add('')
if ($failures.Count -eq 0) {
    $markdown.Add('- None.')
} else {
    foreach ($failure in $failures) {
        $markdown.Add(('- {0}: {1} - {2}' -f $failure.Category, $failure.Name, $failure.Detail))
    }
}

$markdown.Add('')
$markdown.Add('## Warnings')
$markdown.Add('')
if ($warnings.Count -eq 0) {
    $markdown.Add('- None.')
} else {
    foreach ($warning in $warnings) {
        $markdown.Add(('- {0}: {1} - {2}' -f $warning.Category, $warning.Name, $warning.Detail))
    }
}

$markdown.Add('')
$markdown.Add('## Safety Notes')
$markdown.Add('')
$markdown.Add('- This health check does not modify KiCad project files.')
$markdown.Add('- This health check does not install tools.')
$markdown.Add('- This health check does not delete files.')
$markdown.Add('- This health check writes only this report file.')

Set-Content -LiteralPath $reportPath -Value $markdown -Encoding UTF8

Write-Output ''
Write-Output 'KiCad Engine Health Check'
Write-Output "Workspace root: $WorkspaceRoot"
Write-Output "Report: $reportPath"
Write-Output ''
$results |
    Sort-Object @{ Expression = { @{ FAIL = 0; WARN = 1; PASS = 2 }[$_.Status] } }, Category, Name |
    Select-Object Status, Category, Name, Detail |
    Format-Table -AutoSize

Write-Output "Summary: PASS=$passCount WARN=$warnCount FAIL=$failCount"

if ($failCount -gt 0) {
    exit 1
}

exit 0
