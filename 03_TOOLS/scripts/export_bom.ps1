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
    $context = New-KiCadScriptContext -ProjectPath $ProjectPath -TaskName 'bom' -FolderKind 'bom' -OutputRoot $OutputRoot -KiCadCliPath $KiCadCliPath
    $files = Find-KiCadProjectFiles -ProjectPath $context.ProjectPath
    $projectFilePath = Select-SingleKiCadProjectFile -ProjectFiles $files
    $schematicPath = Select-MainSchematicFile -ProjectFiles $files -ProjectFilePath $projectFilePath

    if (-not $schematicPath) {
        throw 'No .kicad_sch file was found. BOM export was not run.'
    }

    $projectName = [System.IO.Path]::GetFileNameWithoutExtension($projectFilePath)
    $bomPath = Join-Path -Path $context.OutputFolder -ChildPath "${projectName}_bom.csv"
    $arguments = @('sch', 'export', 'bom', '--output', $bomPath, $schematicPath)
    $result = Invoke-KiCadCliCommand -KiCadCliPath $context.KiCadCliPath -Arguments $arguments -LogPath $context.LogPath

    $summaryPath = Join-Path -Path $context.OutputFolder -ChildPath 'bom_export_summary.md'
    $status = if ($result.ExitCode -eq 0) { 'EXPORTED_REQUIRES_REVIEW' } else { 'FAILED' }
    Write-SummaryMarkdown -Path $summaryPath -Lines @(
        '# BOM Export Summary',
        '',
        "Status: $status",
        "Exit code: $($result.ExitCode)",
        ('Project: `{0}`' -f $context.ProjectPath),
        ('Schematic: `{0}`' -f $schematicPath),
        ('BOM file: `{0}`' -f $bomPath),
        ('Command log: `{0}`' -f $result.CommandLog),
        '',
        'This BOM requires component, footprint, datasheet, sourcing, and DNP review before fabrication release.'
    )

    Write-Output "Summary: BOM export status $status, exit code $($result.ExitCode)."
    Write-Output "Output folder: $($context.OutputFolder)"
    if ($result.ExitCode -ne 0) {
        exit $result.ExitCode
    }
    exit 0
} catch {
    Write-Error $_.Exception.Message
    exit 1
}
