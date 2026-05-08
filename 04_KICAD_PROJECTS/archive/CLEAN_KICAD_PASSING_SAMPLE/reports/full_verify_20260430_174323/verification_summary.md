# Full KiCad Verification Summary

Status: COMPLETE_REQUIRES_HUMAN_REVIEW
Project: `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE`
Project file: `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\kicad\test_pads_inside_pads.kicad_pro`
Schematic: `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\kicad\test_pads_inside_pads.kicad_sch`
PCB: `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\kicad\test_pads_inside_pads.kicad_pcb`
KiCad CLI: `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe`
Allow exports after failed checks: `False`
Created: 2026-04-30 17:43:29 -04:00

## Step Results
- backup_kicad_project.ps1: exit code 0, log `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\reports\full_verify_20260430_174323\backup_kicad_project.ps1.log`
- run_erc.ps1: exit code 0, log `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\reports\full_verify_20260430_174323\run_erc.ps1.log`
- export_bom.ps1: exit code 0, log `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\reports\full_verify_20260430_174323\export_bom.ps1.log`
- run_drc.ps1: exit code 0, log `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\reports\full_verify_20260430_174323\run_drc.ps1.log`
- export_gerbers.ps1: exit code 0, log `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\reports\full_verify_20260430_174323\export_gerbers.ps1.log`
- export_drill.ps1: exit code 0, log `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\reports\full_verify_20260430_174323\export_drill.ps1.log`
- export_step.ps1: exit code 0, log `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\CLEAN_KICAD_PASSING_SAMPLE\reports\full_verify_20260430_174323\export_step.ps1.log`

## Release Status
Outputs from this script are not final manufacturing files.
Gerber, drill, and STEP exports are skipped by default unless ERC and DRC pass.
Use `-AllowExportsAfterFailedChecks` only for explicit review-only export testing.
Final release still requires human visual review, BOM review, footprint review, netlist review, datasheet review, connector review, polarity/orientation review, power input/protection review, mounting/mechanical review, board edge clearance review, and fabrication package review.
