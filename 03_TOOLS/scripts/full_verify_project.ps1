[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectPath,

    [string]$KiCadCliPath = '',

    [string]$OutputRoot = '',

    [switch]$AllowExportsAfterFailedChecks
)

$ErrorActionPreference = 'Stop'
. (Join-Path -Path $PSScriptRoot -ChildPath 'kicad_automation_common.ps1')

function Invoke-KiCadChildScript {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ScriptName,

        [Parameter(Mandatory = $true)]
        [string]$ProjectPath,

        [Parameter(Mandatory = $true)]
        [string]$KiCadCliPath,

        [Parameter(Mandatory = $true)]
        [string]$LogPath
    )

    $scriptPath = Join-Path -Path $PSScriptRoot -ChildPath $ScriptName
    if (-not (Test-Path -LiteralPath $scriptPath -PathType Leaf)) {
        throw "Required child script is missing: $scriptPath"
    }

    $arguments = @(
        '-NoProfile',
        '-ExecutionPolicy', 'Bypass',
        '-File', $scriptPath,
        '-ProjectPath', $ProjectPath,
        '-KiCadCliPath', $KiCadCliPath
    )

    $commandLine = Format-KiCadCommandForLog -ExecutablePath 'powershell.exe' -Arguments $arguments
    Write-KiCadLog -LogPath $LogPath -Message "Running child script: $commandLine"
    $output = @(powershell.exe @arguments 2>&1 | ForEach-Object { $_.ToString() })
    $exitCode = if ($null -ne $LASTEXITCODE) { [int]$LASTEXITCODE } else { 0 }
    $childLog = Join-Path -Path (Split-Path -Parent $LogPath) -ChildPath "$($ScriptName).log"
    Set-Content -LiteralPath $childLog -Value @(
        "COMMAND: $commandLine",
        "STARTED: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')",
        ''
    ) -Encoding UTF8
    if ($output.Count -gt 0) {
        Add-Content -LiteralPath $childLog -Value $output -Encoding UTF8
    } else {
        Add-Content -LiteralPath $childLog -Value '(no output)' -Encoding UTF8
    }
    Add-Content -LiteralPath $childLog -Value "EXIT_CODE: $exitCode" -Encoding UTF8
    Write-KiCadLog -LogPath $LogPath -Message "Child script $ScriptName exit code: $exitCode"

    return [pscustomobject]@{
        Script = $ScriptName
        ExitCode = $exitCode
        Log = $childLog
    }
}

function New-KiCadSkippedResult {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ScriptName,

        [Parameter(Mandatory = $true)]
        [string]$Reason,

        [Parameter(Mandatory = $true)]
        [string]$LogPath
    )

    Write-KiCadLog -LogPath $LogPath -Message "Skipping ${ScriptName}: $Reason"
    return [pscustomobject]@{
        Script = $ScriptName
        ExitCode = 2
        Log = "SKIPPED: $Reason"
    }
}

$context = $null
try {
    $context = New-KiCadScriptContext -ProjectPath $ProjectPath -TaskName 'full_verify' -FolderKind 'reports' -OutputRoot $OutputRoot -KiCadCliPath $KiCadCliPath
    $files = Find-KiCadProjectFiles -ProjectPath $context.ProjectPath
    $projectFilePath = Select-SingleKiCadProjectFile -ProjectFiles $files
    $schematicPath = Select-MainSchematicFile -ProjectFiles $files -ProjectFilePath $projectFilePath
    $pcbPath = Select-MainPcbFile -ProjectFiles $files -ProjectFilePath $projectFilePath
    $results = New-Object System.Collections.Generic.List[object]

    Write-KiCadLog -LogPath $context.LogPath -Message "Located .kicad_pro: $projectFilePath"
    if ($schematicPath) {
        Write-KiCadLog -LogPath $context.LogPath -Message "Located .kicad_sch: $schematicPath"
    } else {
        Write-KiCadLog -LogPath $context.LogPath -Message 'No schematic found. ERC and BOM will be skipped.'
    }
    if ($pcbPath) {
        Write-KiCadLog -LogPath $context.LogPath -Message "Located .kicad_pcb: $pcbPath"
    } else {
        Write-KiCadLog -LogPath $context.LogPath -Message 'No PCB found. DRC, Gerber, drill, and STEP exports will be skipped.'
    }

    $results.Add((Invoke-KiCadChildScript -ScriptName 'backup_kicad_project.ps1' -ProjectPath $context.ProjectPath -KiCadCliPath $context.KiCadCliPath -LogPath $context.LogPath))

    $ercResult = $null
    $drcResult = $null

    if ($schematicPath) {
        $ercResult = Invoke-KiCadChildScript -ScriptName 'run_erc.ps1' -ProjectPath $context.ProjectPath -KiCadCliPath $context.KiCadCliPath -LogPath $context.LogPath
        $results.Add($ercResult)
        $results.Add((Invoke-KiCadChildScript -ScriptName 'export_bom.ps1' -ProjectPath $context.ProjectPath -KiCadCliPath $context.KiCadCliPath -LogPath $context.LogPath))
    } else {
        $results.Add((New-KiCadSkippedResult -ScriptName 'run_erc.ps1' -Reason 'No schematic was found.' -LogPath $context.LogPath))
        $results.Add((New-KiCadSkippedResult -ScriptName 'export_bom.ps1' -Reason 'No schematic was found.' -LogPath $context.LogPath))
    }

    if ($pcbPath) {
        $drcResult = Invoke-KiCadChildScript -ScriptName 'run_drc.ps1' -ProjectPath $context.ProjectPath -KiCadCliPath $context.KiCadCliPath -LogPath $context.LogPath
        $results.Add($drcResult)

        $ercPassedOrNotApplicable = (-not $schematicPath) -or ($null -ne $ercResult -and $ercResult.ExitCode -eq 0)
        $drcPassed = ($null -ne $drcResult -and $drcResult.ExitCode -eq 0)
        $canRunFabricationStyleExports = $AllowExportsAfterFailedChecks -or ($ercPassedOrNotApplicable -and $drcPassed)

        if ($canRunFabricationStyleExports) {
            if ($AllowExportsAfterFailedChecks -and (-not ($ercPassedOrNotApplicable -and $drcPassed))) {
                Write-KiCadLog -LogPath $context.LogPath -Message 'AllowExportsAfterFailedChecks was set; running manufacturing-style exports as NOT FINAL review outputs despite failed checks.'
            }
            $results.Add((Invoke-KiCadChildScript -ScriptName 'export_gerbers.ps1' -ProjectPath $context.ProjectPath -KiCadCliPath $context.KiCadCliPath -LogPath $context.LogPath))
            $results.Add((Invoke-KiCadChildScript -ScriptName 'export_drill.ps1' -ProjectPath $context.ProjectPath -KiCadCliPath $context.KiCadCliPath -LogPath $context.LogPath))
            $results.Add((Invoke-KiCadChildScript -ScriptName 'export_step.ps1' -ProjectPath $context.ProjectPath -KiCadCliPath $context.KiCadCliPath -LogPath $context.LogPath))
        } else {
            $reason = 'ERC and DRC must pass before Gerber, drill, or STEP export. Use -AllowExportsAfterFailedChecks only for explicit review-only export testing.'
            $results.Add((New-KiCadSkippedResult -ScriptName 'export_gerbers.ps1' -Reason $reason -LogPath $context.LogPath))
            $results.Add((New-KiCadSkippedResult -ScriptName 'export_drill.ps1' -Reason $reason -LogPath $context.LogPath))
            $results.Add((New-KiCadSkippedResult -ScriptName 'export_step.ps1' -Reason $reason -LogPath $context.LogPath))
        }
    } else {
        $results.Add((New-KiCadSkippedResult -ScriptName 'run_drc.ps1' -Reason 'No PCB was found.' -LogPath $context.LogPath))
        $results.Add((New-KiCadSkippedResult -ScriptName 'export_gerbers.ps1' -Reason 'No PCB was found.' -LogPath $context.LogPath))
        $results.Add((New-KiCadSkippedResult -ScriptName 'export_drill.ps1' -Reason 'No PCB was found.' -LogPath $context.LogPath))
        $results.Add((New-KiCadSkippedResult -ScriptName 'export_step.ps1' -Reason 'No PCB was found.' -LogPath $context.LogPath))
    }

    $summaryPath = Join-Path -Path $context.OutputFolder -ChildPath 'verification_summary.md'
    $failureCount = @($results | Where-Object { $_.ExitCode -ne 0 }).Count
    $overallStatus = if ($failureCount -eq 0) { 'COMPLETE_REQUIRES_HUMAN_REVIEW' } else { 'INCOMPLETE_OR_FAILED' }
    $schematicSummary = if ($schematicPath) { $schematicPath } else { 'NONE' }
    $pcbSummary = if ($pcbPath) { $pcbPath } else { 'NONE' }

    $lines = @(
        '# Full KiCad Verification Summary',
        '',
        "Status: $overallStatus",
        ('Project: `{0}`' -f $context.ProjectPath),
        ('Project file: `{0}`' -f $projectFilePath),
        ('Schematic: `{0}`' -f $schematicSummary),
        ('PCB: `{0}`' -f $pcbSummary),
        ('KiCad CLI: `{0}`' -f $context.KiCadCliPath),
        ('Allow exports after failed checks: `{0}`' -f [bool]$AllowExportsAfterFailedChecks),
        "Created: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')",
        '',
        '## Step Results'
    )
    foreach ($result in $results) {
        $lines += ('- {0}: exit code {1}, log `{2}`' -f $result.Script, $result.ExitCode, $result.Log)
    }
    $lines += ''
    $lines += '## Release Status'
    $lines += 'Outputs from this script are not final manufacturing files.'
    $lines += 'Gerber, drill, and STEP exports are skipped by default unless ERC and DRC pass.'
    $lines += 'Use `-AllowExportsAfterFailedChecks` only for explicit review-only export testing.'
    $lines += 'Final release still requires human visual review, BOM review, footprint review, netlist review, datasheet review, connector review, polarity/orientation review, power input/protection review, mounting/mechanical review, board edge clearance review, and fabrication package review.'
    Write-SummaryMarkdown -Path $summaryPath -Lines $lines

    Write-Output "Summary: full verification status $overallStatus with $failureCount incomplete or failed step(s)."
    Write-Output "Summary file: $summaryPath"
    if ($failureCount -ne 0) {
        exit 1
    }
    exit 0
} catch {
    if ($null -ne $context) {
        $message = $_.Exception.Message
        Write-KiCadLog -LogPath $context.LogPath -Message "Full verification failed before completion: $message"
        $summaryPath = Join-Path -Path $context.OutputFolder -ChildPath 'verification_summary.md'
        Write-SummaryMarkdown -Path $summaryPath -Lines @(
            '# Full KiCad Verification Summary',
            '',
            'Status: FAILED_BEFORE_COMPLETION',
            ('Project: `{0}`' -f $context.ProjectPath),
            ('KiCad CLI: `{0}`' -f $context.KiCadCliPath),
            ('Reason: {0}' -f $message),
            ('Script log: `{0}`' -f $context.LogPath),
            "Created: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')",
            '',
            'Outputs from this script are not final manufacturing files.'
        )
    }
    Write-Error $_.Exception.Message
    exit 1
}
