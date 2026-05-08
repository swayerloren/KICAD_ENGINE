[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectPath,

    [string]$KiCadCliPath = '',

    [string]$OutputRoot = ''
)

$ErrorActionPreference = 'Stop'
. (Join-Path -Path $PSScriptRoot -ChildPath 'kicad_automation_common.ps1')

$context = $null
try {
    $context = New-KiCadScriptContext -ProjectPath $ProjectPath -TaskName 'drc' -FolderKind 'reports' -OutputRoot $OutputRoot -KiCadCliPath $KiCadCliPath
    $files = Find-KiCadProjectFiles -ProjectPath $context.ProjectPath
    $projectFilePath = Select-SingleKiCadProjectFile -ProjectFiles $files
    $pcbPath = Select-MainPcbFile -ProjectFiles $files -ProjectFilePath $projectFilePath

    if (-not $pcbPath) {
        throw 'No .kicad_pcb file was found. DRC was not run.'
    }

    $reportPath = Join-Path -Path $context.OutputFolder -ChildPath 'drc_report.txt'
    $arguments = @('pcb', 'drc', '--output', $reportPath, '--format', 'report', '--exit-code-violations', $pcbPath)
    $result = Invoke-KiCadCliCommand -KiCadCliPath $context.KiCadCliPath -Arguments $arguments -LogPath $context.LogPath

    $summaryPath = Join-Path -Path $context.OutputFolder -ChildPath 'drc_summary.md'
    $status = if ($result.ExitCode -eq 0) { 'PASS_OR_NO_CLI_REPORTED_VIOLATIONS' } else { 'FAILED_OR_VIOLATIONS_REPORTED' }
    Write-SummaryMarkdown -Path $summaryPath -Lines @(
        '# DRC Summary',
        '',
        "Status: $status",
        "Exit code: $($result.ExitCode)",
        ('Project: `{0}`' -f $context.ProjectPath),
        ('PCB: `{0}`' -f $pcbPath),
        ('Report: `{0}`' -f $reportPath),
        ('Command log: `{0}`' -f $result.CommandLog),
        '',
        'This script does not edit KiCad source files.'
    )

    Write-Output "Summary: DRC status $status, exit code $($result.ExitCode)."
    Write-Output "Report folder: $($context.OutputFolder)"
    if ($result.ExitCode -ne 0) {
        exit $result.ExitCode
    }
    exit 0
} catch {
    if ($null -ne $context) {
        $message = $_.Exception.Message
        Write-KiCadLog -LogPath $context.LogPath -Message "DRC failed before completion: $message"
        $summaryPath = Join-Path -Path $context.OutputFolder -ChildPath 'drc_summary.md'
        Write-SummaryMarkdown -Path $summaryPath -Lines @(
            '# DRC Summary',
            '',
            'Status: FAILED_BEFORE_DRC_COMPLETED',
            'Exit code: 1',
            ('Project: `{0}`' -f $context.ProjectPath),
            ('Reason: {0}' -f $message),
            ('Script log: `{0}`' -f $context.LogPath),
            '',
            'This script does not edit KiCad source files.'
        )
    }
    Write-Error $_.Exception.Message
    exit 1
}
