# Sample Pipeline Fix Commands

Date: 2026-04-30
Scope: fix KICAD_ENGINE scripts/config/docs found during SAMPLE_KICAD_TEST_PROJECT pipeline testing and rerun sample pipeline.
Rules: no production design, no third-party repo edits, no fabrication-ready outputs, preserve backups.


## Parser check all PowerShell scripts after pipeline fixes

```powershell
Parse all 03_TOOLS\scripts\*.ps1
```
Exit code: 1
Output:
```text
PASS backup_kicad_project.ps1
PASS export_bom.ps1
PASS export_drill.ps1
PASS export_gerbers.ps1
PASS export_step.ps1
PASS find_kicad_project_files.ps1
FAIL full_verify_project.ps1

Extent       ErrorId                           Message                                                                 
------       -------                           -------                                                                 
$ScriptName: InvalidVariableReferenceWithDrive Variable reference is not valid. ':' was not followed by a valid vari...



```

## Parser check all PowerShell scripts after syntax fix

```powershell
Parse all 03_TOOLS\scripts\*.ps1
```
Exit code: 0
Output:
```text
PASS backup_kicad_project.ps1
PASS export_bom.ps1
PASS export_drill.ps1
PASS export_gerbers.ps1
PASS export_step.ps1
PASS find_kicad_project_files.ps1
PASS full_verify_project.ps1
PASS kicad_automation_common.ps1
PASS new_kicad_project_workspace.ps1
PASS run_drc.ps1
PASS run_erc.ps1

```

## Inspect patched full verify export gate

```powershell
Select-String full_verify_project.ps1 for AllowExportsAfterFailedChecks and skip messages
```
Exit code: 0
Output:
```text

LineNumber Line                                                                                                        
---------- ----                                                                                                        
        10     [switch]$AllowExportsAfterFailedChecks                                                                  
        45     Write-KiCadLog -LogPath $LogPath -Message "Running child script: $commandLine"                          
        81     Write-KiCadLog -LogPath $LogPath -Message "Skipping ${ScriptName}: $Reason"                             
       130         $canRunFabricationStyleExports = $AllowExportsAfterFailedChecks -or ($ercPassedOrNotApplicable -a...
       133             if ($AllowExportsAfterFailedChecks -and (-not ($ercPassedOrNotApplicable -and $drcPassed))) {   
       134                 Write-KiCadLog -LogPath $context.LogPath -Message 'AllowExportsAfterFailedChecks was set;...
       140             $reason = 'ERC and DRC must pass before Gerber, drill, or STEP export. Use -AllowExportsAfter...
       167         ('Allow exports after failed checks: `{0}`' -f [bool]$AllowExportsAfterFailedChecks),               
       179     $lines += 'Use `-AllowExportsAfterFailedChecks` only for explicit review-only export testing.'          



```

## Inspect quoted command formatter

```powershell
Select-String kicad_automation_common.ps1 for Format-KiCadCommandForLog
```
Exit code: 0
Output:
```text

> 03_TOOLS\scripts\kicad_automation_common.ps1:109:    $safeTaskName = $TaskName -replace '[^A-Za-z0-9_.-]', '_'
  03_TOOLS\scripts\kicad_automation_common.ps1:110:    $leafName = "${safeTaskName}_${timestamp}"
  03_TOOLS\scripts\kicad_automation_common.ps1:111:    $outputFolder = Join-Path -Path $baseFolder -ChildPath $leafName
  03_TOOLS\scripts\kicad_automation_common.ps1:112:    $suffix = 1
  03_TOOLS\scripts\kicad_automation_common.ps1:113:    while (Test-Path -LiteralPath $outputFolder) {
> 03_TOOLS\scripts\kicad_automation_common.ps1:174:function Format-KiCadCommandForLog {
  03_TOOLS\scripts\kicad_automation_common.ps1:175:    param(
  03_TOOLS\scripts\kicad_automation_common.ps1:176:        [Parameter(Mandatory = $true)]
  03_TOOLS\scripts\kicad_automation_common.ps1:177:        [string]$ExecutablePath,
  03_TOOLS\scripts\kicad_automation_common.ps1:178:
> 03_TOOLS\scripts\kicad_automation_common.ps1:183:    $quotedExecutable = "'{0}'" -f ($ExecutablePath -replace "'", 
"''")
> 03_TOOLS\scripts\kicad_automation_common.ps1:184:    $quotedArguments = @($Arguments | ForEach-Object {
> 03_TOOLS\scripts\kicad_automation_common.ps1:185:        "'{0}'" -f ($_ -replace "'", "''")
  03_TOOLS\scripts\kicad_automation_common.ps1:186:    })
> 03_TOOLS\scripts\kicad_automation_common.ps1:187:    return (@($quotedExecutable) + $quotedArguments) -join ' '
  03_TOOLS\scripts\kicad_automation_common.ps1:188:}
  03_TOOLS\scripts\kicad_automation_common.ps1:189:
  03_TOOLS\scripts\kicad_automation_common.ps1:190:function Invoke-KiCadCliCommand {
  03_TOOLS\scripts\kicad_automation_common.ps1:191:    param(



```

## Fix rerun: find_kicad_project_files.ps1

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\find_kicad_project_files.ps1' -ProjectPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT' -KiCadCliPath 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe'
```
Exit code: 0
Output:
```text
[2026-04-30 16:41:54] ProjectPath: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT
[2026-04-30 16:41:54] KiCad CLI: C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
[2026-04-30 16:41:54] Output folder: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\find_kicad_project_files_20260430_164154
[2026-04-30 16:41:54] Inventory report: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\find_kicad_project_files_20260430_164154\kicad_project_files.md
Summary: found 1 project file(s), 1 schematic file(s), and 1 PCB file(s).
Report folder: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\find_kicad_project_files_20260430_164154

```

## Fix rerun: backup_kicad_project.ps1

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\backup_kicad_project.ps1' -ProjectPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT' -KiCadCliPath 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe'
```
Exit code: 0
Output:
```text
[2026-04-30 16:41:55] ProjectPath: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT
[2026-04-30 16:41:55] KiCad CLI: C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
[2026-04-30 16:41:55] Backup folder: C:\Users\LJ\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\demo_20260430_164155
[2026-04-30 16:41:55] Copied file: kicad\demo.kicad_pcb
[2026-04-30 16:41:55] Copied file: kicad\demo.kicad_pro
[2026-04-30 16:41:55] Copied file: kicad\demo.kicad_sch
Summary: backed up 3 item(s).
Backup folder: C:\Users\LJ\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\demo_20260430_164155

```

## Fix rerun: run_erc.ps1

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\run_erc.ps1' -ProjectPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT' -KiCadCliPath 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe'
```
Exit code: 5
Output:
```text
[2026-04-30 16:41:55] ProjectPath: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT
[2026-04-30 16:41:55] KiCad CLI: C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
[2026-04-30 16:41:55] Output folder: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_164155
[2026-04-30 16:41:55] Running: 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' 'sch' 'erc' '--output' 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_164155\erc_report.txt' '--format' 'report' '--exit-code-violations' 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\kicad\demo.kicad_sch'
[2026-04-30 16:41:56] Command exit code: 5
Summary: ERC status FAILED_OR_VIOLATIONS_REPORTED, exit code 5.
Report folder: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_164155

```

## Fix rerun: run_drc.ps1

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\run_drc.ps1' -ProjectPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT' -KiCadCliPath 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe'
```
Exit code: 5
Output:
```text
[2026-04-30 16:41:57] ProjectPath: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT
[2026-04-30 16:41:57] KiCad CLI: C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
[2026-04-30 16:41:57] Output folder: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_164157
[2026-04-30 16:41:57] Running: 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' 'pcb' 'drc' '--output' 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_164157\drc_report.txt' '--format' 'report' '--exit-code-violations' 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\kicad\demo.kicad_pcb'
[2026-04-30 16:41:57] Command exit code: 5
Summary: DRC status FAILED_OR_VIOLATIONS_REPORTED, exit code 5.
Report folder: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_164157

```

## Fix rerun: full_verify_project.ps1 default gated exports

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\full_verify_project.ps1' -ProjectPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT' -KiCadCliPath 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe'
```
Exit code: 1
Output:
```text
[2026-04-30 16:41:58] ProjectPath: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT
[2026-04-30 16:41:58] KiCad CLI: C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
[2026-04-30 16:41:58] Output folder: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\full_verify_20260430_164158
[2026-04-30 16:41:58] Located .kicad_pro: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\kicad\demo.kicad_pro
[2026-04-30 16:41:58] Located .kicad_sch: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\kicad\demo.kicad_sch
[2026-04-30 16:41:58] Located .kicad_pcb: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\kicad\demo.kicad_pcb
[2026-04-30 16:41:58] Running child script: 'powershell.exe' '-NoProfile' '-ExecutionPolicy' 'Bypass' '-File' 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\backup_kicad_project.ps1' '-ProjectPath' 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT' '-KiCadCliPath' 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe'
[2026-04-30 16:41:59] Child script backup_kicad_project.ps1 exit code: 0
[2026-04-30 16:41:59] Running child script: 'powershell.exe' '-NoProfile' '-ExecutionPolicy' 'Bypass' '-File' 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\run_erc.ps1' '-ProjectPath' 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT' '-KiCadCliPath' 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe'
[2026-04-30 16:42:00] Child script run_erc.ps1 exit code: 5
[2026-04-30 16:42:00] Running child script: 'powershell.exe' '-NoProfile' '-ExecutionPolicy' 'Bypass' '-File' 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\export_bom.ps1' '-ProjectPath' 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT' '-KiCadCliPath' 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe'
[2026-04-30 16:42:01] Child script export_bom.ps1 exit code: 0
[2026-04-30 16:42:01] Running child script: 'powershell.exe' '-NoProfile' '-ExecutionPolicy' 'Bypass' '-File' 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\run_drc.ps1' '-ProjectPath' 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT' '-KiCadCliPath' 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe'
[2026-04-30 16:42:02] Child script run_drc.ps1 exit code: 5
[2026-04-30 16:42:02] Skipping export_gerbers.ps1: ERC and DRC must pass before Gerber, drill, or STEP export. Use -AllowExportsAfterFailedChecks only for explicit review-only export testing.
[2026-04-30 16:42:02] Skipping export_drill.ps1: ERC and DRC must pass before Gerber, drill, or STEP export. Use -AllowExportsAfterFailedChecks only for explicit review-only export testing.
[2026-04-30 16:42:02] Skipping export_step.ps1: ERC and DRC must pass before Gerber, drill, or STEP export. Use -AllowExportsAfterFailedChecks only for explicit review-only export testing.
Summary: full verification status INCOMPLETE_OR_FAILED with 5 incomplete or failed step(s).
Summary file: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\full_verify_20260430_164158\verification_summary.md

```

## Fix rerun: collect latest sample pipeline artifacts

```powershell
List latest sample report, backup, bom, fabrication folders
```
Exit code: 0
Output:
```text
Latest reports:

Name                                     FullName                                                                      
----                                     --------                                                                      
full_verify_20260430_164158              C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT...
drc_20260430_164201                      C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT...
erc_20260430_164159                      C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT...
drc_20260430_164157                      C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT...
erc_20260430_164155                      C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT...
find_kicad_project_files_20260430_164154 C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT...
full_verify_20260430_163412              C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT...
drc_20260430_163414                      C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT...
erc_20260430_163413                      C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT...
drc_20260430_163409                      C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT...
erc_20260430_163408                      C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT...
find_kicad_project_files_20260430_163406 C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT...

Latest backups:
                                         C:\Users\LJ\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\demo_20260430_164159      
                                         C:\Users\LJ\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\demo_20260430_164155      
                                         C:\Users\LJ\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\demo_20260430_163413      
                                         C:\Users\LJ\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\demo_20260430_163407      
                                         C:\Users\LJ\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\demo_20260430_163249      

Latest BOM outputs:
                                         C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT...
                                         C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT...

Latest fabrication outputs:
                                         C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT...
                                         C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT...
                                         C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT...



```

## Inspect final full verification summary

```powershell
Get-Content -LiteralPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\full_verify_20260430_164158\verification_summary.md' -Raw
```
Exit code: 0
Output:
```text
Status: INCOMPLETE_OR_FAILED
Allow exports after failed checks: `False`
export_gerbers.ps1: exit code 2, log `SKIPPED: ERC and DRC must pass before Gerber, drill, or STEP export. Use -AllowExportsAfterFailedChecks only for explicit review-only export testing.`
export_drill.ps1: exit code 2, log `SKIPPED: ERC and DRC must pass before Gerber, drill, or STEP export. Use -AllowExportsAfterFailedChecks only for explicit review-only export testing.`
export_step.ps1: exit code 2, log `SKIPPED: ERC and DRC must pass before Gerber, drill, or STEP export. Use -AllowExportsAfterFailedChecks only for explicit review-only export testing.`
Gerber, drill, and STEP exports are skipped by default unless ERC and DRC pass.
```

## Inspect final output folders

```powershell
Get-ChildItem -LiteralPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication' -Directory | Sort-Object LastWriteTime -Descending | Select-Object -First 10 Name,FullName,LastWriteTime
Get-ChildItem -LiteralPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\bom' -Directory | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name,FullName,LastWriteTime
```
Exit code: 0
Output:
```text
No new fabrication folder was created by the 16:41:58 full verification rerun.
Latest fabrication folders remain the earlier NOT_FINAL review artifacts from 16:34.
Latest BOM folder is bom_20260430_164200.
```

## Final parser check all PowerShell scripts

```powershell
Parse all 03_TOOLS\scripts\*.ps1
```
Exit code: 0
Output:
```text
PASS backup_kicad_project.ps1
PASS export_bom.ps1
PASS export_drill.ps1
PASS export_gerbers.ps1
PASS export_step.ps1
PASS find_kicad_project_files.ps1
PASS full_verify_project.ps1
PASS kicad_automation_common.ps1
PASS new_kicad_project_workspace.ps1
PASS run_drc.ps1
PASS run_erc.ps1
```
