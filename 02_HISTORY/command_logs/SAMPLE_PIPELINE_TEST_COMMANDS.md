# Sample Pipeline Test Commands

Date: 2026-04-30
Scope: create SAMPLE_KICAD_TEST_PROJECT and run verification scripts against harmless sample/test KiCad files.
Rules: no production design, no final fabrication-ready output, no real active project modification.


## KiCad CLI version probe

```powershell
& 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' version
```
Exit code: 0
Output:
```text
9.0.7

```

## Inspect selected sample fixture

```powershell
Get-ChildItem -Recurse 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\pass_minimal_mcu_board' | Select-Object FullName,Length
```
Exit code: 0
Output:
```text

FullName                                                                                                               
--------                                                                                                               
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\pass_minimal_mcu_board\demo....
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\pass_minimal_mcu_board\demo....
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\pass_minimal_mcu_board\demo....



```

## Create or locate SAMPLE_KICAD_TEST_PROJECT workspace

```powershell
& 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\new_kicad_project_workspace.ps1' -ProjectName 'SAMPLE_KICAD_TEST_PROJECT'
```
Exit code: 1
Output:
```text
```
Errors:
```text
C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\new_kicad_project_workspace.ps1 : Cannot bind argument to parameter 'Lines' 
because it is an empty string.
At line:54 char:160
+ ... e'" -AllowFailure -Script { & $ScriptPath -ProjectName $ProjectName }
+                                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidData: (:) [new_kicad_project_workspace.ps1], ParameterBindingValidationException
    + FullyQualifiedErrorId : ParameterArgumentValidationErrorEmptyStringNotAllowed,new_kicad_project_workspace.ps1
 

```

## Confirm sample workspace exists

```powershell
Test-Path 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT'; Get-ChildItem 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT'
```
Exit code: 0
Output:
```text
True

Mode   Length Name       
----   ------ ----       
d-----        bom        
d-----        datasheets 
d-----        fabrication
d-----        history    
d-----        kicad      
d-----        memory     
d-----        notes      
d-----        renders    
d-----        reports    
d-----        scripts    
-a---- 2854   AGENTS.md  
-a---- 1636   README.md  



```

## Copy harmless fixture KiCad files into sample workspace if missing

```powershell
if no .kicad_pro exists under 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\kicad', copy 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\pass_minimal_mcu_board\*' into 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\kicad'
```
Exit code: 0
Output:
```text
Copied fixture files into sample kicad folder.

```

## Sample workspace tree after fixture copy

```powershell
Get-ChildItem -Recurse 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT' | Select-Object FullName,Length
```
Exit code: 0
Output:
```text

FullName                                                                                Length
--------                                                                                ------
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\bom               
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\datasheets        
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication       
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\history           
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\kicad             
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\memory            
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\notes             
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\renders           
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports           
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\scripts           
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\AGENTS.md   2854  
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\README.md   1636  



```

## Record new project script parser check after fix

```powershell
Parse 03_TOOLS\scripts\new_kicad_project_workspace.ps1
```
Exit code: 0
Output:
```text
Parser check passed.

```

## Complete sample memory history and project index records

```powershell
Created PROJECT_MEMORY.md, project_history README.md, and PROJECT_INDEX sample record
```
Exit code: 0
Output:
```text
True
True

LineNumber Line                                                                                           
---------- ----                                                                                           
        40 ## Project: SAMPLE_KICAD_TEST_PROJECT                                                          
        41 - Project path: `04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT`                           
        48 - Related project memory file: `01_MEMORY\projects\SAMPLE_KICAD_TEST_PROJECT\PROJECT_MEMORY.md`
        50 - Project history folder: `02_HISTORY\project_history\SAMPLE_KICAD_TEST_PROJECT`               



```

## Copy harmless fixture files into sample kicad folder correctly

```powershell
Get-ChildItem 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos\kicad-mcp-pro\tests\fixtures\benchmark_projects\pass_minimal_mcu_board' -File | Copy-Item -Destination 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\kicad' -Force
```
Exit code: 0
Output:
```text
Copied: demo.kicad_pcb
Copied: demo.kicad_pro
Copied: demo.kicad_sch

Name           Length
----           ------
demo.kicad_pcb   1092
demo.kicad_pro     26
demo.kicad_sch   1183



```

## Sample kicad source inventory before verification scripts

```powershell
Get-ChildItem 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\kicad' -Recurse -File | Select Name, Length
```
Exit code: 0
Output:
```text

Name           Length
----           ------
demo.kicad_pcb   1092
demo.kicad_pro     26
demo.kicad_sch   1183



```

## Run find_kicad_project_files.ps1 on sample project

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\find_kicad_project_files.ps1' -ProjectPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT' -KiCadCliPath 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe'
```
Exit code: 1
Output:
```text
```
Errors:
```text
powershell.exe : C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\find_kicad_project_files.ps1 : The property 'ProjectPath' 
cannot be found on 
At line:49 char:268
+ ... e -Script { powershell.exe -NoProfile -ExecutionPolicy Bypass -File ( ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (C:\Users\LJ\KIC...ot be found on :String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 
this object. Verify that the property exists.
At C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\find_kicad_project_files.ps1:80 char:5
+     Write-Error $_.Exception.Message
+     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Write-Error], WriteErrorException
    + FullyQualifiedErrorId : Microsoft.PowerShell.Commands.WriteErrorException,find_kicad_project_files.ps1
 

```

## Run backup_kicad_project.ps1 on sample project

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\backup_kicad_project.ps1' -ProjectPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT' -KiCadCliPath 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe'
```
Exit code: 1
Output:
```text
[2026-04-30 16:32:49] ProjectPath: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT
[2026-04-30 16:32:49] KiCad CLI: C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
[2026-04-30 16:32:49] Backup folder: C:\Users\LJ\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\demo_20260430_163249
[2026-04-30 16:32:49] Copied file: kicad\demo.kicad_pcb
[2026-04-30 16:32:49] Copied file: kicad\demo.kicad_pro
[2026-04-30 16:32:49] Copied file: kicad\demo.kicad_sch

```
Errors:
```text
powershell.exe : C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\backup_kicad_project.ps1 : Cannot bind argument to 
parameter 'Lines' because 
At line:50 char:260
+ ... e -Script { powershell.exe -NoProfile -ExecutionPolicy Bypass -File ( ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (C:\Users\LJ\KIC...Lines' because :String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 
it is an empty string.
At C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\backup_kicad_project.ps1:99 char:5
+     Write-Error $_.Exception.Message
+     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Write-Error], WriteErrorException
    + FullyQualifiedErrorId : Microsoft.PowerShell.Commands.WriteErrorException,backup_kicad_project.ps1
 

```

## Run run_erc.ps1 on sample project

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\run_erc.ps1' -ProjectPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT' -KiCadCliPath 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe'
```
Exit code: 1
Output:
```text
```
Errors:
```text
powershell.exe : C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\run_erc.ps1 : The property 'ProjectPath' cannot be found on 
this object. 
At line:51 char:234
+ ... e -Script { powershell.exe -NoProfile -ExecutionPolicy Bypass -File ( ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (C:\Users\LJ\KIC...n this object. :String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 
Verify that the property exists.
At C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\run_erc.ps1:50 char:5
+     Write-Error $_.Exception.Message
+     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Write-Error], WriteErrorException
    + FullyQualifiedErrorId : Microsoft.PowerShell.Commands.WriteErrorException,run_erc.ps1
 

```

## Run run_drc.ps1 on sample project

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\run_drc.ps1' -ProjectPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT' -KiCadCliPath 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe'
```
Exit code: 1
Output:
```text
```
Errors:
```text
powershell.exe : C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\run_drc.ps1 : The property 'ProjectPath' cannot be found on 
this object. 
At line:52 char:234
+ ... e -Script { powershell.exe -NoProfile -ExecutionPolicy Bypass -File ( ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (C:\Users\LJ\KIC...n this object. :String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 
Verify that the property exists.
At C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\run_drc.ps1:50 char:5
+     Write-Error $_.Exception.Message
+     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Write-Error], WriteErrorException
    + FullyQualifiedErrorId : Microsoft.PowerShell.Commands.WriteErrorException,run_drc.ps1
 

```

## Run full_verify_project.ps1 on sample project

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\full_verify_project.ps1' -ProjectPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT' -KiCadCliPath 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe'
```
Exit code: 1
Output:
```text
```
Errors:
```text
powershell.exe : C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\full_verify_project.ps1 : The property 'ProjectPath' cannot 
be found on this 
At line:53 char:258
+ ... e -Script { powershell.exe -NoProfile -ExecutionPolicy Bypass -File ( ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (C:\Users\LJ\KIC... found on this :String) [], RemoteException
    + FullyQualifiedErrorId : NativeCommandError
 
object. Verify that the property exists.
At C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\full_verify_project.ps1:134 char:5
+     Write-Error $_.Exception.Message
+     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Write-Error], WriteErrorException
    + FullyQualifiedErrorId : Microsoft.PowerShell.Commands.WriteErrorException,full_verify_project.ps1
 

```

## Sample reports and outputs inventory after script runs

```powershell
Get-ChildItem sample reports/bom/fabrication plus 99_BACKUPS sample entries
```
Exit code: 1
Output:
```text
[reports] C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports

FullName                                                                                                               
--------                                                                                                               
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_163251                
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_163250                
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\find_kicad_project_files_2026043...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\full_verify_20260430_163252        
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_163251\script.log     
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_163250\script.log     
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\find_kicad_project_files_2026043...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\full_verify_20260430_163252\scri...
[bom] C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\bom
[fabrication] C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication
[renders] C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\renders
[backups]
C:\Users\LJ\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\demo_20260430_163249                                               



```

## Parser check after common helper fixes

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

## Rerun find_kicad_project_files.ps1 after fixes

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\find_kicad_project_files.ps1' -ProjectPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT' -KiCadCliPath 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe'
```
Exit code: 0
Output:
```text
[2026-04-30 16:34:06] ProjectPath: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT
[2026-04-30 16:34:06] KiCad CLI: C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
[2026-04-30 16:34:06] Output folder: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\find_kicad_project_files_20260430_163406
[2026-04-30 16:34:06] Inventory report: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\find_kicad_project_files_20260430_163406\kicad_project_files.md
Summary: found 1 project file(s), 1 schematic file(s), and 1 PCB file(s).
Report folder: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\find_kicad_project_files_20260430_163406

```

## Rerun backup_kicad_project.ps1 after fixes

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\backup_kicad_project.ps1' -ProjectPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT' -KiCadCliPath 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe'
```
Exit code: 0
Output:
```text
[2026-04-30 16:34:07] ProjectPath: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT
[2026-04-30 16:34:07] KiCad CLI: C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
[2026-04-30 16:34:07] Backup folder: C:\Users\LJ\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\demo_20260430_163407
[2026-04-30 16:34:07] Copied file: kicad\demo.kicad_pcb
[2026-04-30 16:34:07] Copied file: kicad\demo.kicad_pro
[2026-04-30 16:34:07] Copied file: kicad\demo.kicad_sch
Summary: backed up 3 item(s).
Backup folder: C:\Users\LJ\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\demo_20260430_163407

```

## Rerun run_erc.ps1 after fixes

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\run_erc.ps1' -ProjectPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT' -KiCadCliPath 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe'
```
Exit code: 5
Output:
```text
[2026-04-30 16:34:08] ProjectPath: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT
[2026-04-30 16:34:08] KiCad CLI: C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
[2026-04-30 16:34:08] Output folder: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_163408
[2026-04-30 16:34:08] Running: 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' sch erc --output C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_163408\erc_report.txt --format report --exit-code-violations C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\kicad\demo.kicad_sch
[2026-04-30 16:34:09] Command exit code: 5
Summary: ERC status FAILED_OR_VIOLATIONS_REPORTED, exit code 5.
Report folder: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_163408

```

## Rerun run_drc.ps1 after fixes

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\run_drc.ps1' -ProjectPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT' -KiCadCliPath 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe'
```
Exit code: 5
Output:
```text
[2026-04-30 16:34:09] ProjectPath: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT
[2026-04-30 16:34:09] KiCad CLI: C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
[2026-04-30 16:34:09] Output folder: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_163409
[2026-04-30 16:34:09] Running: 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' pcb drc --output C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_163409\drc_report.txt --format report --exit-code-violations C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\kicad\demo.kicad_pcb
[2026-04-30 16:34:11] Command exit code: 5
Summary: DRC status FAILED_OR_VIOLATIONS_REPORTED, exit code 5.
Report folder: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_163409

```

## Rerun full_verify_project.ps1 after fixes

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\full_verify_project.ps1' -ProjectPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT' -KiCadCliPath 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe'
```
Exit code: 1
Output:
```text
[2026-04-30 16:34:12] ProjectPath: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT
[2026-04-30 16:34:12] KiCad CLI: C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
[2026-04-30 16:34:12] Output folder: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\full_verify_20260430_163412
[2026-04-30 16:34:12] Located .kicad_pro: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\kicad\demo.kicad_pro
[2026-04-30 16:34:12] Located .kicad_sch: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\kicad\demo.kicad_sch
[2026-04-30 16:34:12] Located .kicad_pcb: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\kicad\demo.kicad_pcb
[2026-04-30 16:34:12] Running child script: powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\backup_kicad_project.ps1 -ProjectPath C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT -KiCadCliPath C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
[2026-04-30 16:34:13] Child script backup_kicad_project.ps1 exit code: 0
[2026-04-30 16:34:13] Running child script: powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\run_erc.ps1 -ProjectPath C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT -KiCadCliPath C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
[2026-04-30 16:34:13] Child script run_erc.ps1 exit code: 5
[2026-04-30 16:34:13] Running child script: powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\export_bom.ps1 -ProjectPath C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT -KiCadCliPath C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
[2026-04-30 16:34:14] Child script export_bom.ps1 exit code: 0
[2026-04-30 16:34:14] Running child script: powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\run_drc.ps1 -ProjectPath C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT -KiCadCliPath C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
[2026-04-30 16:34:15] Child script run_drc.ps1 exit code: 5
[2026-04-30 16:34:15] Running child script: powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\export_gerbers.ps1 -ProjectPath C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT -KiCadCliPath C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
[2026-04-30 16:34:16] Child script export_gerbers.ps1 exit code: 0
[2026-04-30 16:34:16] Running child script: powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\export_drill.ps1 -ProjectPath C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT -KiCadCliPath C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
[2026-04-30 16:34:16] Child script export_drill.ps1 exit code: 0
[2026-04-30 16:34:16] Running child script: powershell.exe -NoProfile -ExecutionPolicy Bypass -File C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\export_step.ps1 -ProjectPath C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT -KiCadCliPath C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
[2026-04-30 16:34:17] Child script export_step.ps1 exit code: 0
Summary: full verification status INCOMPLETE_OR_FAILED with 2 incomplete or failed step(s).
Summary file: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\full_verify_20260430_163412\verification_summary.md

```

## Sample reports and outputs inventory after rerun

```powershell
Get-ChildItem sample reports/bom/fabrication plus 99_BACKUPS sample entries
```
Exit code: 0
Output:
```text
[reports] C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports

FullName                                                                                                               
--------                                                                                                               
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_163251                
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_163409                
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_163414                
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_163250                
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_163408                
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_163413                
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\find_kicad_project_files_2026043...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\find_kicad_project_files_2026043...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\full_verify_20260430_163252        
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\full_verify_20260430_163412        
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_163251\script.log     
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_163409\drc_report.txt 
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_163409\drc_summary.md 
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_163409\kicad_cli_ou...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_163409\script.log     
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_163414\drc_report.txt 
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_163414\drc_summary.md 
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_163414\kicad_cli_ou...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_163414\script.log     
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_163250\script.log     
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_163408\erc_report.txt 
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_163408\erc_summary.md 
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_163408\kicad_cli_ou...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_163408\script.log     
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_163413\erc_report.txt 
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_163413\erc_summary.md 
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_163413\kicad_cli_ou...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_163413\script.log     
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\find_kicad_project_files_2026043...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\find_kicad_project_files_2026043...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\find_kicad_project_files_2026043...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\find_kicad_project_files_2026043...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\full_verify_20260430_163252\scri...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\full_verify_20260430_163412\back...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\full_verify_20260430_163412\expo...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\full_verify_20260430_163412\expo...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\full_verify_20260430_163412\expo...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\full_verify_20260430_163412\expo...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\full_verify_20260430_163412\run_...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\full_verify_20260430_163412\run_...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\full_verify_20260430_163412\scri...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\full_verify_20260430_163412\veri...
[bom] C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\bom
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\bom\bom_20260430_163414                    
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\bom\bom_20260430_163414\bom_export_summa...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\bom\bom_20260430_163414\demo_bom.csv       
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\bom\bom_20260430_163414\kicad_cli_output...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\bom\bom_20260430_163414\script.log         
[fabrication] C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\drill_NOT_FINAL_20260430_163416
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\step_NOT_FINAL_20260430_163417 
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\drill_NOT_FINAL_20260430_163...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\drill_NOT_FINAL_20260430_163...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\drill_NOT_FINAL_20260430_163...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\drill_NOT_FINAL_20260430_163...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\drill_NOT_FINAL_20260430_163...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\drill_NOT_FINAL_20260430_163...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_1...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\step_NOT_FINAL_20260430_1634...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\step_NOT_FINAL_20260430_1634...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\step_NOT_FINAL_20260430_1634...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\step_NOT_FINAL_20260430_1634...
C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\step_NOT_FINAL_20260430_1634...
[renders] C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\renders
[backups]
C:\Users\LJ\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\demo_20260430_163413                                               
C:\Users\LJ\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\demo_20260430_163407                                               
C:\Users\LJ\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\demo_20260430_163249                                               



```

## Final required file presence check

```powershell
Test required sample pipeline outputs
```
Exit code: 0
Output:
```text

Path                                                                    Exists
----                                                                    ------
04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\kicad\demo.kicad_pro   True
04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\kicad\demo.kicad_sch   True
04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\kicad\demo.kicad_pcb   True
01_MEMORY\projects\SAMPLE_KICAD_TEST_PROJECT\PROJECT_MEMORY.md            True
02_HISTORY\project_history\SAMPLE_KICAD_TEST_PROJECT\README.md            True
02_HISTORY\design_reviews\SAMPLE_KICAD_TEST_PROJECT_REVIEW.md             True
02_HISTORY\erc_drc_reports\SAMPLE_KICAD_TEST_PROJECT_VERIFICATION.md      True
02_HISTORY\sessions\SAMPLE_PIPELINE_TEST_SESSION.md                       True
02_HISTORY\command_logs\SAMPLE_PIPELINE_TEST_COMMANDS.md                  True



```

## Final sample pipeline status extraction

```powershell
Read key status reports
```
Exit code: 0
Output:
```text
TOOL_INDEX status:

Line                                                                                                                   
----                                                                                                                   
- Sample pipeline status: Tested on `04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT` on 2026-04-30. Inventory an...
- Script fixes from sample test: `new_kicad_project_workspace.ps1` now allows blank markdown lines in generated file...

PROJECT_INDEX status:
## Project: SAMPLE_KICAD_TEST_PROJECT                                                                                  
- Project path: `04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT`                                                   
- Status: SAMPLE_PIPELINE_TEST_COMPLETE_NOT_FAB_READY                                                                  
- Related project memory file: `01_MEMORY\projects\SAMPLE_KICAD_TEST_PROJECT\PROJECT_MEMORY.md`                        
- Latest review or verification report: `02_HISTORY\erc_drc_reports\SAMPLE_KICAD_TEST_PROJECT_VERIFICATION.md`         
- Project history folder: `02_HISTORY\project_history\SAMPLE_KICAD_TEST_PROJECT`                                       

Full verify status:
Status: INCOMPLETE_OR_FAILED                                                                                           
- backup_kicad_project.ps1: exit code 0, log `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PR...
- run_erc.ps1: exit code 5, log `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports...
- export_bom.ps1: exit code 0, log `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\repo...
- run_drc.ps1: exit code 5, log `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports...
- export_gerbers.ps1: exit code 0, log `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\...
- export_drill.ps1: exit code 0, log `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\re...
- export_step.ps1: exit code 0, log `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\rep...



```
