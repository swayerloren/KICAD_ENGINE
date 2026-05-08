# CLEAN_KICAD_PASSING_SAMPLE Verification

Date: 2026-04-30

Project path: `04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE`

KiCad CLI: `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe`

Command log: `02_HISTORY\command_logs\CLEAN_SAMPLE_SUCCESS_PATH_COMMANDS.md`

## Script Results

| Step | Result | Notes |
| --- | --- | --- |
| `find_kicad_project_files.ps1` | PASS | Found 1 `.kicad_pro`, 1 `.kicad_sch`, and 1 `.kicad_pcb`. |
| `backup_kicad_project.ps1` | PASS | Backed up 9 source/library items to `99_BACKUPS\pre_codex_edits\test_pads_inside_pads_20260430_174304`. |
| `run_erc.ps1` | PASS | KiCad CLI exited 0. |
| `run_drc.ps1` | PASS | KiCad CLI exited 0. |
| `full_verify_project.ps1` | PASS | Backup, ERC, BOM, DRC, Gerber, drill, and STEP child steps all exited 0. |

## Key Output Paths

- Inventory report: `04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\reports\find_kicad_project_files_20260430_174259\kicad_project_files.md`
- Backup folder: `99_BACKUPS\pre_codex_edits\test_pads_inside_pads_20260430_174304`
- Full verification backup folder: `99_BACKUPS\pre_codex_edits\test_pads_inside_pads_20260430_174324`
- ERC report: `04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\reports\erc_20260430_174309\erc_report.txt`
- DRC report: `04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\reports\drc_20260430_174315\drc_report.txt`
- Full verification summary: `04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\reports\full_verify_20260430_174323\verification_summary.md`
- BOM output: `04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\bom\bom_20260430_174325`
- Gerber output: `04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\fabrication\gerbers_NOT_FINAL_20260430_174327`
- Drill output: `04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\fabrication\drill_NOT_FINAL_20260430_174328`
- STEP output: `04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\fabrication\step_NOT_FINAL_20260430_174328`

## ERC Summary

ERC report: `04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\reports\erc_20260430_174309\erc_report.txt`

- Messages: 0
- Errors: 0
- Warnings: 0

## DRC Summary

DRC report: `04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\reports\drc_20260430_174315\drc_report.txt`

- DRC violations: 0
- Unconnected pads: 0
- Footprint errors: 0

## Full Success Path

Validated. `full_verify_project.ps1` reached `COMPLETE_REQUIRES_HUMAN_REVIEW` with 0 incomplete or failed steps. Gerber, drill, and STEP exports were allowed because ERC and DRC both passed.

## Release Status

NOT FINAL. This fixture validates tooling only. Generated output is not a manufacturing release.

