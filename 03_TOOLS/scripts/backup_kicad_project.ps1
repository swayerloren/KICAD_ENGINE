[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectPath,

    [string]$KiCadCliPath = '',

    [string]$OutputRoot = ''
)

$ErrorActionPreference = 'Stop'
. (Join-Path -Path $PSScriptRoot -ChildPath 'kicad_automation_common.ps1')

try {
    $resolvedProjectPath = Resolve-KiCadProjectPath -ProjectPath $ProjectPath
    $resolvedCliPath = Resolve-KiCadCliPath -KiCadCliPath $KiCadCliPath
    $workspaceRoot = Get-KiCadAutomationWorkspaceRoot
    $files = Find-KiCadProjectFiles -ProjectPath $resolvedProjectPath
    $projectFilePath = Select-SingleKiCadProjectFile -ProjectFiles $files
    $projectName = [System.IO.Path]::GetFileNameWithoutExtension($projectFilePath)
    $timestamp = Get-Date -Format 'yyyyMMdd_HHmmss'

    if ([string]::IsNullOrWhiteSpace($OutputRoot)) {
        $backupBase = Join-Path -Path $workspaceRoot -ChildPath '99_BACKUPS\pre_codex_edits'
    } else {
        $backupBase = $OutputRoot
    }

    New-Item -ItemType Directory -Force -Path $backupBase | Out-Null
    $backupFolder = Join-Path -Path $backupBase -ChildPath "${projectName}_$timestamp"
    $suffix = 1
    while (Test-Path -LiteralPath $backupFolder) {
        $backupFolder = Join-Path -Path $backupBase -ChildPath "${projectName}_${timestamp}_$suffix"
        $suffix++
    }
    New-Item -ItemType Directory -Path $backupFolder | Out-Null

    $logPath = Join-Path -Path $backupFolder -ChildPath 'backup_log.txt'
    New-Item -ItemType File -Path $logPath -Force | Out-Null
    Write-KiCadLog -LogPath $logPath -Message "ProjectPath: $resolvedProjectPath"
    Write-KiCadLog -LogPath $logPath -Message "KiCad CLI: $resolvedCliPath"
    Write-KiCadLog -LogPath $logPath -Message "Backup folder: $backupFolder"

    $fileItems = @()
    $fileItems += $files.ProjectFiles
    $fileItems += $files.SchematicFiles
    $fileItems += $files.PcbFiles
    $fileItems += $files.SymbolLibraries
    $fileItems += $files.SymbolTables
    $fileItems += $files.FootprintTables
    $fileItems += $files.LocalFootprintFiles
    $fileItems = @($fileItems | Sort-Object -Property FullName -Unique)

    $directoryItems = @($files.FootprintLibraries | Sort-Object -Property FullName -Unique)
    $copied = New-Object System.Collections.Generic.List[string]

    foreach ($item in $fileItems) {
        $relativePath = $item.FullName.Substring($resolvedProjectPath.Length).TrimStart('\')
        $destinationPath = Join-Path -Path $backupFolder -ChildPath $relativePath
        $destinationDirectory = Split-Path -Parent $destinationPath
        New-Item -ItemType Directory -Force -Path $destinationDirectory | Out-Null
        Copy-Item -LiteralPath $item.FullName -Destination $destinationPath
        $copied.Add($relativePath)
        Write-KiCadLog -LogPath $logPath -Message "Copied file: $relativePath"
    }

    foreach ($directory in $directoryItems) {
        $relativePath = $directory.FullName.Substring($resolvedProjectPath.Length).TrimStart('\')
        $destinationPath = Join-Path -Path $backupFolder -ChildPath $relativePath
        $destinationDirectory = Split-Path -Parent $destinationPath
        New-Item -ItemType Directory -Force -Path $destinationDirectory | Out-Null
        Copy-Item -LiteralPath $directory.FullName -Destination $destinationPath -Recurse
        $copied.Add($relativePath)
        Write-KiCadLog -LogPath $logPath -Message "Copied directory: $relativePath"
    }

    $manifestPath = Join-Path -Path $backupFolder -ChildPath 'backup_manifest.md'
    $manifest = @(
        '# KiCad Project Backup Manifest',
        '',
        ('Project path: `{0}`' -f $resolvedProjectPath),
        ('KiCad CLI: `{0}`' -f $resolvedCliPath),
        ('Backup folder: `{0}`' -f $backupFolder),
        "Created: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')",
        '',
        '## Copied Items'
    )
    if ($copied.Count -eq 0) {
        $manifest += '- None copied.'
    } else {
        $manifest += @($copied | Sort-Object -Unique | ForEach-Object { '- `{0}`' -f $_ })
    }
    Write-SummaryMarkdown -Path $manifestPath -Lines $manifest

    Write-Output "Summary: backed up $($copied.Count) item(s)."
    Write-Output "Backup folder: $backupFolder"
    exit 0
} catch {
    Write-Error $_.Exception.Message
    exit 1
}
