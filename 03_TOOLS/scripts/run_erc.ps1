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
    $context = New-KiCadScriptContext -ProjectPath $ProjectPath -TaskName 'erc' -FolderKind 'reports' -OutputRoot $OutputRoot -KiCadCliPath $KiCadCliPath
    $files = Find-KiCadProjectFiles -ProjectPath $context.ProjectPath
    $projectFilePath = Select-SingleKiCadProjectFile -ProjectFiles $files
    $schematicPath = Select-MainSchematicFile -ProjectFiles $files -ProjectFilePath $projectFilePath

    if (-not $schematicPath) {
        throw 'No .kicad_sch file was found. ERC was not run.'
    }

    $reportPath = Join-Path -Path $context.OutputFolder -ChildPath 'erc_report.txt'
    $arguments = @('sch', 'erc', '--output', $reportPath, '--format', 'report', '--exit-code-violations', $schematicPath)
    $result = Invoke-KiCadCliCommand -KiCadCliPath $context.KiCadCliPath -Arguments $arguments -LogPath $context.LogPath

    $summaryPath = Join-Path -Path $context.OutputFolder -ChildPath 'erc_summary.md'
    $status = if ($result.ExitCode -eq 0) { 'PASS_OR_NO_CLI_REPORTED_VIOLATIONS' } else { 'FAILED_OR_VIOLATIONS_REPORTED' }
    Write-SummaryMarkdown -Path $summaryPath -Lines @(
        '# ERC Summary',
        '',
        "Status: $status",
        "Exit code: $($result.ExitCode)",
        ('Project: `{0}`' -f $context.ProjectPath),
        ('Schematic: `{0}`' -f $schematicPath),
        ('Report: `{0}`' -f $reportPath),
        ('Command log: `{0}`' -f $result.CommandLog),
        '',
        'This script does not edit KiCad source files.'
    )

    Write-Output "Summary: ERC status $status, exit code $($result.ExitCode)."
    Write-Output "Report folder: $($context.OutputFolder)"
    if ($result.ExitCode -ne 0) {
        exit $result.ExitCode
    }
    exit 0
} catch {
    if ($null -ne $context) {
        $message = $_.Exception.Message
        Write-KiCadLog -LogPath $context.LogPath -Message "ERC failed before completion: $message"
        $summaryPath = Join-Path -Path $context.OutputFolder -ChildPath 'erc_summary.md'
        Write-SummaryMarkdown -Path $summaryPath -Lines @(
            '# ERC Summary',
            '',
            'Status: FAILED_BEFORE_ERC_COMPLETED',
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
