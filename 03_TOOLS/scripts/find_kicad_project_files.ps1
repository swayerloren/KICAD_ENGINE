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
    $context = New-KiCadScriptContext -ProjectPath $ProjectPath -TaskName 'find_kicad_project_files' -FolderKind 'reports' -OutputRoot $OutputRoot -KiCadCliPath $KiCadCliPath
    $files = Find-KiCadProjectFiles -ProjectPath $context.ProjectPath

    $jsonPath = Join-Path -Path $context.OutputFolder -ChildPath 'kicad_project_files.json'
    $reportPath = Join-Path -Path $context.OutputFolder -ChildPath 'kicad_project_files.md'

    $data = [pscustomobject]@{
        project_path = $context.ProjectPath
        kicad_cli = $context.KiCadCliPath
        project_files = @($files.ProjectFiles | ForEach-Object { $_.FullName })
        schematic_files = @($files.SchematicFiles | ForEach-Object { $_.FullName })
        pcb_files = @($files.PcbFiles | ForEach-Object { $_.FullName })
        symbol_libraries = @($files.SymbolLibraries | ForEach-Object { $_.FullName })
        symbol_tables = @($files.SymbolTables | ForEach-Object { $_.FullName })
        footprint_tables = @($files.FootprintTables | ForEach-Object { $_.FullName })
        footprint_libraries = @($files.FootprintLibraries | ForEach-Object { $_.FullName })
        local_footprint_files = @($files.LocalFootprintFiles | ForEach-Object { $_.FullName })
    }
    $data | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $jsonPath -Encoding UTF8

    $lines = @(
        '# KiCad Project File Inventory',
        '',
        ('Project path: `{0}`' -f $context.ProjectPath),
        ('KiCad CLI: `{0}`' -f $context.KiCadCliPath),
        "Created: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')",
        '',
        '## Counts',
        "- .kicad_pro: $($files.ProjectFiles.Count)",
        "- .kicad_sch: $($files.SchematicFiles.Count)",
        "- .kicad_pcb: $($files.PcbFiles.Count)",
        "- symbol libraries: $($files.SymbolLibraries.Count)",
        "- symbol tables: $($files.SymbolTables.Count)",
        "- footprint tables: $($files.FootprintTables.Count)",
        "- footprint libraries: $($files.FootprintLibraries.Count)",
        "- loose footprint files: $($files.LocalFootprintFiles.Count)",
        '',
        '## Files'
    )

    foreach ($group in @(
        @{ Name = '.kicad_pro'; Items = $files.ProjectFiles },
        @{ Name = '.kicad_sch'; Items = $files.SchematicFiles },
        @{ Name = '.kicad_pcb'; Items = $files.PcbFiles },
        @{ Name = 'symbol libraries'; Items = $files.SymbolLibraries },
        @{ Name = 'symbol tables'; Items = $files.SymbolTables },
        @{ Name = 'footprint tables'; Items = $files.FootprintTables },
        @{ Name = 'footprint libraries'; Items = $files.FootprintLibraries },
        @{ Name = 'loose footprint files'; Items = $files.LocalFootprintFiles }
    )) {
        $lines += ''
        $lines += "### $($group.Name)"
        if ($group.Items.Count -eq 0) {
            $lines += '- None found.'
        } else {
            $lines += @($group.Items | ForEach-Object { '- `{0}`' -f $_.FullName })
        }
    }

    Write-SummaryMarkdown -Path $reportPath -Lines $lines
    Write-KiCadLog -LogPath $context.LogPath -Message "Inventory report: $reportPath"
    Write-Output "Summary: found $($files.ProjectFiles.Count) project file(s), $($files.SchematicFiles.Count) schematic file(s), and $($files.PcbFiles.Count) PCB file(s)."
    Write-Output "Report folder: $($context.OutputFolder)"
    exit 0
} catch {
    Write-Error $_.Exception.Message
    exit 1
}
