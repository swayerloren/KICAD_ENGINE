Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'

$script:KiCadAutomationScriptsRoot = if ($PSScriptRoot) {
    $PSScriptRoot
} else {
    Split-Path -Parent $MyInvocation.MyCommand.Path
}

function Get-KiCadAutomationWorkspaceRoot {
    $toolsRoot = Split-Path -Parent $script:KiCadAutomationScriptsRoot
    return (Split-Path -Parent $toolsRoot)
}

function Resolve-KiCadProjectPath {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ProjectPath
    )

    if ([string]::IsNullOrWhiteSpace($ProjectPath)) {
        throw 'ProjectPath is required.'
    }

    if (-not (Test-Path -LiteralPath $ProjectPath -PathType Container)) {
        throw "ProjectPath does not exist or is not a directory: $ProjectPath"
    }

    return (Resolve-Path -LiteralPath $ProjectPath).ProviderPath
}

function Resolve-KiCadCliPath {
    param(
        [string]$KiCadCliPath = ''
    )

    if (-not [string]::IsNullOrWhiteSpace($KiCadCliPath)) {
        if (-not (Test-Path -LiteralPath $KiCadCliPath -PathType Leaf)) {
            throw "Specified KiCad CLI path does not exist: $KiCadCliPath"
        }

        return (Resolve-Path -LiteralPath $KiCadCliPath).ProviderPath
    }

    $command = Get-Command 'kicad-cli' -ErrorAction SilentlyContinue
    if (-not $command) {
        $command = Get-Command 'kicad-cli.exe' -ErrorAction SilentlyContinue
    }
    if ($command) {
        return $command.Source
    }

    $programFilesKiCad = 'C:\Program Files\KiCad'
    if (Test-Path -LiteralPath $programFilesKiCad -PathType Container) {
        $matches = @(
            Get-ChildItem -LiteralPath $programFilesKiCad -Recurse -Filter 'kicad-cli.exe' -File -ErrorAction SilentlyContinue |
                Sort-Object -Property FullName -Descending
        )
        if ($matches.Count -gt 0) {
            return $matches[0].FullName
        }
    }

    throw 'kicad-cli was not found on PATH or under C:\Program Files\KiCad. Install KiCad or provide -KiCadCliPath. No source files were changed.'
}

function New-KiCadTimestampedFolder {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ProjectPath,

        [Parameter(Mandatory = $true)]
        [string]$TaskName,

        [ValidateSet('reports', 'fabrication', 'bom', 'outputs')]
        [string]$FolderKind = 'reports',

        [string]$OutputRoot = ''
    )

    $workspaceRoot = Get-KiCadAutomationWorkspaceRoot
    $projectName = Split-Path -Leaf $ProjectPath

    if (-not [string]::IsNullOrWhiteSpace($OutputRoot)) {
        $baseFolder = $OutputRoot
    } elseif ($FolderKind -eq 'reports') {
        $baseFolder = Join-Path -Path $ProjectPath -ChildPath 'reports'
    } elseif ($FolderKind -eq 'fabrication') {
        $projectFabFolder = Join-Path -Path $ProjectPath -ChildPath 'fabrication'
        if (Test-Path -LiteralPath $projectFabFolder -PathType Container) {
            $baseFolder = $projectFabFolder
        } else {
            $baseFolder = Join-Path -Path $workspaceRoot -ChildPath (Join-Path -Path '05_OUTPUTS' -ChildPath (Join-Path -Path $projectName -ChildPath 'fabrication'))
        }
    } elseif ($FolderKind -eq 'bom') {
        $projectBomFolder = Join-Path -Path $ProjectPath -ChildPath 'bom'
        if (Test-Path -LiteralPath $projectBomFolder -PathType Container) {
            $baseFolder = $projectBomFolder
        } else {
            $baseFolder = Join-Path -Path $workspaceRoot -ChildPath (Join-Path -Path '05_OUTPUTS' -ChildPath (Join-Path -Path $projectName -ChildPath 'bom'))
        }
    } else {
        $baseFolder = Join-Path -Path $workspaceRoot -ChildPath (Join-Path -Path '05_OUTPUTS' -ChildPath $projectName)
    }

    New-Item -ItemType Directory -Force -Path $baseFolder | Out-Null

    $timestamp = Get-Date -Format 'yyyyMMdd_HHmmss'
    $safeTaskName = $TaskName -replace '[^A-Za-z0-9_.-]', '_'
    $leafName = "${safeTaskName}_${timestamp}"
    $outputFolder = Join-Path -Path $baseFolder -ChildPath $leafName
    $suffix = 1
    while (Test-Path -LiteralPath $outputFolder) {
        $outputFolder = Join-Path -Path $baseFolder -ChildPath "${leafName}_$suffix"
        $suffix++
    }

    New-Item -ItemType Directory -Path $outputFolder | Out-Null
    return $outputFolder
}

function Write-KiCadLog {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Message,

        [string]$LogPath = ''
    )

    $line = '[{0}] {1}' -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $Message
    Write-Host $line

    if (-not [string]::IsNullOrWhiteSpace($LogPath)) {
        Add-Content -LiteralPath $LogPath -Value $line -Encoding UTF8
    }
}

function New-KiCadScriptContext {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ProjectPath,

        [Parameter(Mandatory = $true)]
        [string]$TaskName,

        [ValidateSet('reports', 'fabrication', 'bom', 'outputs')]
        [string]$FolderKind = 'reports',

        [string]$OutputRoot = '',

        [string]$KiCadCliPath = ''
    )

    $resolvedProjectPath = Resolve-KiCadProjectPath -ProjectPath $ProjectPath
    $resolvedCliPath = Resolve-KiCadCliPath -KiCadCliPath $KiCadCliPath
    $outputFolder = New-KiCadTimestampedFolder -ProjectPath $resolvedProjectPath -TaskName $TaskName -FolderKind $FolderKind -OutputRoot $OutputRoot
    $logPath = Join-Path -Path $outputFolder -ChildPath 'script.log'
    New-Item -ItemType File -Path $logPath -Force | Out-Null

    Write-KiCadLog -LogPath $logPath -Message "ProjectPath: $resolvedProjectPath"
    Write-KiCadLog -LogPath $logPath -Message "KiCad CLI: $resolvedCliPath"
    Write-KiCadLog -LogPath $logPath -Message "Output folder: $outputFolder"

    return [pscustomobject]@{
        ProjectPath = $resolvedProjectPath
        ProjectName = Split-Path -Leaf $resolvedProjectPath
        KiCadCliPath = $resolvedCliPath
        OutputFolder = $outputFolder
        LogPath = $logPath
        WorkspaceRoot = Get-KiCadAutomationWorkspaceRoot
    }
}

function Format-KiCadCommandForLog {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ExecutablePath,

        [Parameter(Mandatory = $true)]
        [string[]]$Arguments
    )

    $quotedExecutable = "'{0}'" -f ($ExecutablePath -replace "'", "''")
    $quotedArguments = @($Arguments | ForEach-Object {
        "'{0}'" -f ($_ -replace "'", "''")
    })
    return (@($quotedExecutable) + $quotedArguments) -join ' '
}

function Invoke-KiCadCliCommand {
    param(
        [Parameter(Mandatory = $true)]
        [string]$KiCadCliPath,

        [Parameter(Mandatory = $true)]
        [string[]]$Arguments,

        [Parameter(Mandatory = $true)]
        [string]$LogPath
    )

    $commandLog = Join-Path -Path (Split-Path -Parent $LogPath) -ChildPath 'kicad_cli_output.log'
    $commandLine = Format-KiCadCommandForLog -ExecutablePath $KiCadCliPath -Arguments $Arguments
    Write-KiCadLog -LogPath $LogPath -Message "Running: $commandLine"
    Add-Content -LiteralPath $commandLog -Value "COMMAND: $commandLine" -Encoding UTF8

    $output = @(& $KiCadCliPath @Arguments 2>&1 | ForEach-Object { $_.ToString() })
    $exitCode = if ($null -ne $LASTEXITCODE) { [int]$LASTEXITCODE } else { 0 }

    if ($output.Count -gt 0) {
        Add-Content -LiteralPath $commandLog -Value $output -Encoding UTF8
    } else {
        Add-Content -LiteralPath $commandLog -Value '(no output)' -Encoding UTF8
    }
    Add-Content -LiteralPath $commandLog -Value "EXIT_CODE: $exitCode" -Encoding UTF8

    Write-KiCadLog -LogPath $LogPath -Message "Command exit code: $exitCode"

    return [pscustomobject]@{
        ExitCode = $exitCode
        CommandLog = $commandLog
        Output = $output
    }
}

function Find-KiCadProjectFiles {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ProjectPath
    )

    $excludePattern = '\\(reports|review_outputs|Codex Review Outputs|reference_original_inventory|learning|notes|fabrication|renders|bom|05_OUTPUTS|99_BACKUPS|original_fiverr_outputs_snapshot|[^\\]+-backups)(\\|$)'
    $allFiles = @(
        Get-ChildItem -LiteralPath $ProjectPath -Recurse -File -ErrorAction SilentlyContinue |
            Where-Object { $_.FullName -notmatch $excludePattern } |
            Sort-Object -Property FullName
    )

    $prettyDirs = @(
        Get-ChildItem -LiteralPath $ProjectPath -Recurse -Directory -Filter '*.pretty' -ErrorAction SilentlyContinue |
            Where-Object { $_.FullName -notmatch $excludePattern } |
            Sort-Object -Property FullName
    )

    return [pscustomobject]@{
        ProjectFiles = @($allFiles | Where-Object { $_.Extension -eq '.kicad_pro' })
        SchematicFiles = @($allFiles | Where-Object { $_.Extension -eq '.kicad_sch' })
        PcbFiles = @($allFiles | Where-Object { $_.Extension -eq '.kicad_pcb' })
        SymbolLibraries = @($allFiles | Where-Object { $_.Extension -in @('.kicad_sym', '.lib', '.dcm') })
        SymbolTables = @($allFiles | Where-Object { $_.Name -eq 'sym-lib-table' })
        FootprintTables = @($allFiles | Where-Object { $_.Name -eq 'fp-lib-table' })
        FootprintLibraries = $prettyDirs
        LocalFootprintFiles = @($allFiles | Where-Object { $_.Extension -eq '.kicad_mod' })
    }
}

function Select-SingleKiCadProjectFile {
    param(
        [Parameter(Mandatory = $true)]
        [object]$ProjectFiles
    )

    if ($ProjectFiles.ProjectFiles.Count -eq 0) {
        throw 'No .kicad_pro file was found under ProjectPath.'
    }
    if ($ProjectFiles.ProjectFiles.Count -gt 1) {
        $paths = ($ProjectFiles.ProjectFiles | ForEach-Object { $_.FullName }) -join '; '
        throw "Multiple .kicad_pro files were found. Use a specific project folder. Files: $paths"
    }

    return $ProjectFiles.ProjectFiles[0].FullName
}

function Select-MainSchematicFile {
    param(
        [Parameter(Mandatory = $true)]
        [object]$ProjectFiles,

        [string]$ProjectFilePath = ''
    )

    if ($ProjectFiles.SchematicFiles.Count -eq 0) {
        return $null
    }

    if (-not [string]::IsNullOrWhiteSpace($ProjectFilePath)) {
        $projectBaseName = [System.IO.Path]::GetFileNameWithoutExtension($ProjectFilePath)
        $projectDirectory = Split-Path -Parent $ProjectFilePath
        $preferredPath = Join-Path -Path $projectDirectory -ChildPath "$projectBaseName.kicad_sch"
        $preferred = @($ProjectFiles.SchematicFiles | Where-Object { $_.FullName -eq $preferredPath })
        if ($preferred.Count -eq 1) {
            return $preferred[0].FullName
        }
    }

    if ($ProjectFiles.SchematicFiles.Count -eq 1) {
        return $ProjectFiles.SchematicFiles[0].FullName
    }

    $paths = ($ProjectFiles.SchematicFiles | ForEach-Object { $_.FullName }) -join '; '
    throw "Multiple schematic files were found and no main schematic could be inferred. Files: $paths"
}

function Select-MainPcbFile {
    param(
        [Parameter(Mandatory = $true)]
        [object]$ProjectFiles,

        [string]$ProjectFilePath = ''
    )

    if ($ProjectFiles.PcbFiles.Count -eq 0) {
        return $null
    }

    if (-not [string]::IsNullOrWhiteSpace($ProjectFilePath)) {
        $projectBaseName = [System.IO.Path]::GetFileNameWithoutExtension($ProjectFilePath)
        $projectDirectory = Split-Path -Parent $ProjectFilePath
        $preferredPath = Join-Path -Path $projectDirectory -ChildPath "$projectBaseName.kicad_pcb"
        $preferred = @($ProjectFiles.PcbFiles | Where-Object { $_.FullName -eq $preferredPath })
        if ($preferred.Count -eq 1) {
            return $preferred[0].FullName
        }
    }

    if ($ProjectFiles.PcbFiles.Count -eq 1) {
        return $ProjectFiles.PcbFiles[0].FullName
    }

    $paths = ($ProjectFiles.PcbFiles | ForEach-Object { $_.FullName }) -join '; '
    throw "Multiple PCB files were found and no main PCB could be inferred. Files: $paths"
}

function Write-NotFinalMarker {
    param(
        [Parameter(Mandatory = $true)]
        [string]$OutputFolder,

        [Parameter(Mandatory = $true)]
        [string]$Reason
    )

    $markerPath = Join-Path -Path $OutputFolder -ChildPath 'NOT_FINAL_README.md'
    $content = @(
        '# Not Final Manufacturing Output',
        '',
        "Created: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')",
        '',
        'These files are generated automation outputs only.',
        'They are not final manufacturing release files.',
        '',
        "Reason: $Reason",
        '',
        'Final release requires ERC, DRC, BOM, footprint, netlist, datasheet, connector, polarity, power input, mechanical, and visual review gates to be complete.'
    )
    Set-Content -LiteralPath $markerPath -Value $content -Encoding UTF8
    return $markerPath
}

function Write-SummaryMarkdown {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,

        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string[]]$Lines
    )

    Set-Content -LiteralPath $Path -Value $Lines -Encoding UTF8
}
