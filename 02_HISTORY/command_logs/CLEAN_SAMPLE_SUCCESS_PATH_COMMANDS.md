# Clean Sample Success Path Commands

Date: 2026-04-30

Workspace: `C:\Users\LJ\KICAD_ENGINE`

## Read Required Context

```powershell
Get-Content -LiteralPath '02_HISTORY\sessions\SAMPLE_PIPELINE_TEST_SESSION.md' -Raw
Get-Content -LiteralPath '02_HISTORY\sessions\SAMPLE_PIPELINE_FIX_SESSION.md' -Raw
Get-Content -LiteralPath '03_TOOLS\tool_logs\PIPELINE_FIX_REPORT.md' -Raw
Get-Content -LiteralPath '03_TOOLS\scripts\full_verify_project.ps1' -Raw
```

Result: prior failure-path behavior and full verification success criteria were reviewed.

## Locate Candidate Fixtures

```powershell
Get-ChildItem -LiteralPath 'C:\Program Files\KiCad\9.0' -Recurse -Directory | Where-Object { $_.FullName -match 'demo|example|template|sample' }
Get-ChildItem -LiteralPath 'C:\Program Files\KiCad\9.0' -Recurse -Filter '*.kicad_pro' -File
Get-ChildItem -LiteralPath 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\repos' -Recurse -Filter '*.kicad_pro' -File
```

Result: installed KiCad demos and local tool-repo sample projects were found.

## Candidate Test: KiBot `resistor_tht`

```powershell
Copy KiBot kicad_9 resistor_tht project files to:
C:\Users\LJ\KICAD_ENGINE\05_OUTPUTS\clean_sample_candidate_tests\resistor_tht_20260430_173726
& 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' sch erc --output '<candidate>\reports\erc_report.txt' --format report --exit-code-violations '<candidate>\resistor_tht.kicad_sch'
& 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' pcb drc --output '<candidate>\reports\drc_report.txt' --format report --exit-code-violations '<candidate>\resistor_tht.kicad_pcb'
```

Result:

```text
ERC exit: 5; 99 messages, 98 errors, 1 warning.
DRC exit: 5; 49 DRC violations/warnings.
Classification: sample design quality/library mismatch, not script bug.
```

## Candidate Batch Test: KiBot KiCad 9 Samples

```powershell
Copy '03_TOOLS\repos\KiBot\tests\board_samples\kicad_9' to:
05_OUTPUTS\clean_sample_candidate_tests\kibot_kicad9_20260430_173845
Loop over copied .kicad_pro files and run direct KiCad CLI ERC/DRC when same-base schematic/PCB exist.
```

Result:

```text
No KiBot copied candidate had both ERC=0 and DRC=0.
Closest: test_points had ERC=0, DRC=5.
```

## Candidate Batch Test: Installed KiCad Demos

```powershell
Copy each installed KiCad demo project directory to:
05_OUTPUTS\clean_sample_candidate_tests\installed_demos_20260430_173955
Loop over copied .kicad_pro files and run direct KiCad CLI ERC/DRC when same-base schematic/PCB exist.
```

Result:

```text
Passing candidates:
- complex_hierarchy\complex_hierarchy.kicad_pro
- ecc83\ecc83-pp_v2.kicad_pro
- test_pads_inside_pads\test_pads_inside_pads.kicad_pro
```

Selected candidate: `test_pads_inside_pads`, because it is the smallest passing installed KiCad demo.

## Create Disposable Sample Workspace

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\new_kicad_project_workspace.ps1' -ProjectName 'CLEAN_KICAD_PASSING_SAMPLE'
```

Exit code: 0

Result:

```text
Created project workspace: C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE
Created project memory folder: C:\Users\LJ\KICAD_ENGINE\01_MEMORY\projects\CLEAN_KICAD_PASSING_SAMPLE
Created project history folder: C:\Users\LJ\KICAD_ENGINE\02_HISTORY\project_history\CLEAN_KICAD_PASSING_SAMPLE
Updated project index: C:\Users\LJ\KICAD_ENGINE\00_CODEX_START\PROJECT_INDEX.md
```

## Copy Installed KiCad Demo Into Sample Workspace

```powershell
Copy-Item -Path 'C:\Program Files\KiCad\9.0\share\kicad\demos\test_pads_inside_pads\*' -Destination 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\kicad' -Recurse -Force
```

Result: copied one project, one schematic, one PCB, local symbol table/library, footprint table, and local footprint library.

## Run Inventory

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\find_kicad_project_files.ps1' -ProjectPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE'
```

Exit code: 0

Result:

```text
Found 1 project file, 1 schematic file, and 1 PCB file.
Report folder: 04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\reports\find_kicad_project_files_20260430_174259
```

## Run Backup

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\backup_kicad_project.ps1' -ProjectPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE'
```

Exit code: 0

Result:

```text
Backed up 9 item(s).
Backup folder: 99_BACKUPS\pre_codex_edits\test_pads_inside_pads_20260430_174304
```

## Run ERC

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\run_erc.ps1' -ProjectPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE'
```

Exit code: 0

Result:

```text
ERC status PASS_OR_NO_CLI_REPORTED_VIOLATIONS.
Report folder: 04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\reports\erc_20260430_174309
```

## Run DRC

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\run_drc.ps1' -ProjectPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE'
```

Exit code: 0

Result:

```text
DRC status PASS_OR_NO_CLI_REPORTED_VIOLATIONS.
Report folder: 04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\reports\drc_20260430_174315
```

## Run Full Verification

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File 'C:\Users\LJ\KICAD_ENGINE\03_TOOLS\scripts\full_verify_project.ps1' -ProjectPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE'
```

Exit code: 0

Result:

```text
Status: COMPLETE_REQUIRES_HUMAN_REVIEW
Incomplete/failed steps: 0
Summary file: 04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\reports\full_verify_20260430_174323\verification_summary.md
```

## Confirm NOT_FINAL Outputs

```powershell
Get-ChildItem -LiteralPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\fabrication' -Directory
Get-ChildItem -LiteralPath 'C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\fabrication' -Recurse -Filter 'NOT_FINAL_README.md' -File
```

Result:

```text
gerbers_NOT_FINAL_20260430_174327
drill_NOT_FINAL_20260430_174328
step_NOT_FINAL_20260430_174328
All contain NOT_FINAL_README.md markers.
```

