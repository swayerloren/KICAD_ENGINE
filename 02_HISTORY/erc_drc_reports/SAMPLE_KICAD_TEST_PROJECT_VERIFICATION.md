# SAMPLE_KICAD_TEST_PROJECT Verification

Date: 2026-04-30

Project path: `04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT`

KiCad CLI: `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe`

Command log: `02_HISTORY\command_logs\SAMPLE_PIPELINE_TEST_COMMANDS.md`

## Script Results

| Step | Result | Notes |
| --- | --- | --- |
| `find_kicad_project_files.ps1` | PASS | Found 1 `.kicad_pro`, 1 `.kicad_sch`, and 1 `.kicad_pcb`. |
| `backup_kicad_project.ps1` | PASS | Backed up 3 KiCad files. |
| `run_erc.ps1` | FAIL_WITH_VIOLATIONS | KiCad CLI exited 5; ERC report was written. |
| `run_drc.ps1` | FAIL_WITH_VIOLATIONS | KiCad CLI exited 5; DRC report was written. |
| `full_verify_project.ps1` | INCOMPLETE_OR_FAILED | Backup, BOM, Gerber, drill, and STEP child steps passed; ERC and DRC failed with exit code 5. |

## Key Output Paths

- Inventory report: `04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\find_kicad_project_files_20260430_163406\kicad_project_files.md`
- Backup folder: `99_BACKUPS\pre_codex_edits\demo_20260430_163407`
- Full verification backup folder: `99_BACKUPS\pre_codex_edits\demo_20260430_163413`
- ERC report: `04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_163408\erc_report.txt`
- DRC report: `04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_163409\drc_report.txt`
- Full verification summary: `04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\full_verify_20260430_163412\verification_summary.md`
- BOM output: `04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\bom\bom_20260430_163414\demo_bom.csv`
- Gerber output: `04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\gerbers_NOT_FINAL_20260430_163415`
- Drill output: `04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\drill_NOT_FINAL_20260430_163416`
- STEP output: `04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\fabrication\step_NOT_FINAL_20260430_163417`

## ERC Summary

ERC report: `04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\erc_20260430_163408\erc_report.txt`

- Messages: 7
- Errors: 1
- Warnings: 6
- Primary error: dangling wire.
- Warnings included dangling global labels, unconnected wire endpoints, and missing footprint links.

## DRC Summary

DRC report: `04_KICAD_PROJECTS\active\SAMPLE_KICAD_TEST_PROJECT\reports\drc_20260430_163409\drc_report.txt`

- DRC violations: 3
- Unconnected pads: 0
- Footprint errors: 0
- Reported violations were missing footprint libraries or footprints in the local KiCad configuration.

## Release Status

NOT FINAL. This sample project is not fabrication-ready. Generated fabrication-style outputs were created only for pipeline testing and were placed in `NOT_FINAL` folders.
