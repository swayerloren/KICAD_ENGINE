# Command Log - Golden Path Sample Gate Run

Date: `2026-05-03`

Workspace: `C:\Users\LJ\GitHub\KICAD_ENGINE`

## Commands Run

### Startup And Inspection

- Read required startup and task files with `Get-Content`.
- Inspected promoted sample folder and reports with `Get-ChildItem`.
- Inspected schematic symbol placements with `Select-String`.
- Confirmed `C:\Program Files\KiCad\9.0\bin\kicad-cli.exe` exists.

### Backup

Created backup:

`99_BACKUPS/pre_codex_edits/20260503_145319_tomasr8_attiny85_dev_board_pre_golden_path_gate`

### Schematic Checks

```powershell
python 03_TOOLS/scripts/kicad_schematic_checks/check_schematic_annotation.py --schematic <sample>/attiny85.kicad_sch --output <sample>/reports/ANNOTATION_CHECK.md --json-output <sample>/reports/ANNOTATION_CHECK.json --no-fail
python 03_TOOLS/scripts/kicad_schematic_checks/check_schematic_completeness.py --schematic <sample>/attiny85.kicad_sch --project-root <sample> --output <sample>/reports/SCHEMATIC_COMPLETENESS_CHECK.md --json-output <sample>/reports/SCHEMATIC_COMPLETENESS_CHECK.json --no-fail
python 03_TOOLS/scripts/kicad_schematic_checks/check_bom_lock_alignment.py --schematic <sample>/attiny85.kicad_sch --output <sample>/reports/BOM_LOCK_ALIGNMENT_CHECK.md --json-output <sample>/reports/BOM_LOCK_ALIGNMENT_CHECK.json --no-fail
python 03_TOOLS/scripts/kicad_schematic_checks/check_needs_review_markers.py --schematic <sample>/attiny85.kicad_sch --output <sample>/reports/NEEDS_REVIEW_MARKERS_CHECK.md --json-output <sample>/reports/NEEDS_REVIEW_MARKERS_CHECK.json --no-fail
```

Results:

- Annotation: `PASS`
- Completeness: `FAIL`
- BOM lock alignment: `FAIL`
- Needs-review markers: `FAIL_EXPECTED_BLOCKER`

### ERC And Schematic Visual

```powershell
kicad-cli sch erc --format report --severity-all --output <sample>/_verification/kicad_cli/erc_after_repair.rpt <sample>/attiny85.kicad_sch
03_TOOLS/kicad/run_schematic_visual_check.ps1 -ProjectRoot <sample> -SchematicPath <sample>/attiny85.kicad_sch -OutputRoot <sample>/_verification/schematic_visual -KicadCliPath C:\Program Files\KiCad\9.0\bin\kicad-cli.exe -NoFailOnFindings
```

Results:

- ERC: `FAIL`, 6 messages, 1 error, 5 warnings.
- Schematic visual export and close-up crops: `PASS`.

### DRC, PCB Visual, Project Validation

```powershell
kicad-cli pcb drc --format report --severity-all --schematic-parity --output <sample>/_verification/kicad_cli/drc_after_repair.rpt <sample>/attiny85.kicad_pcb
kicad-cli pcb export svg --mode-single --fit-page-to-board --exclude-drawing-sheet --layers F.Cu,F.SilkS,F.Mask,Edge.Cuts --output <sample>/_verification/pcb_visual/attiny85_top_NOT_FINAL.svg <sample>/attiny85.kicad_pcb
kicad-cli pcb export svg --mode-single --fit-page-to-board --exclude-drawing-sheet --mirror --layers B.Cu,B.SilkS,B.Mask,Edge.Cuts --output <sample>/_verification/pcb_visual/attiny85_bottom_NOT_FINAL.svg <sample>/attiny85.kicad_pcb
python 03_TOOLS/scripts/project_validation/validate_kicad_project.py <sample>/attiny85.kicad_pro --allow-project-output --output-dir <sample>/reports/project_validation --kicad-cli C:\Program Files\KiCad\9.0\bin\kicad-cli.exe
```

Results:

- DRC: `FAIL`, 15 DRC violations, 13 schematic parity issues, 0 unconnected pads.
- PCB visual export: `PASS`.
- Project validation after validator parser fix: `WARN`.

### BOM And PCB Close-Ups

```powershell
kicad-cli sch export bom --output <sample>/_verification/bom/attiny85_BOM_NOT_FINAL.csv <sample>/attiny85.kicad_sch
python 03_TOOLS/scripts/visual/generate_schematic_closeups.py --source-svg <sample>/_verification/pcb_visual/attiny85_top_NOT_FINAL.svg --config <sample>/_verification/pcb_visual/visual_blocks.json --crops-dir <sample>/_verification/pcb_visual/crops --review-output <sample>/reports/PCB_CLOSE_UP_REVIEW.md --json-output <sample>/_verification/pcb_visual/PCB_CLOSE_UP_REVIEW.json --full-png-output <sample>/_verification/pcb_visual/attiny85_top_NOT_FINAL.png --no-fail
```

Results:

- BOM export: `PASS_REVIEW_ONLY`
- PCB close-up crop generation: `PASS_WITH_WARNINGS`

### Validation And Failed Attempts

```powershell
python -m py_compile 03_TOOLS/scripts/project_validation/validate_kicad_project.py
git status --short -- 19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board 03_TOOLS/scripts/project_validation/validate_kicad_project.py
python 03_TOOLS/scripts/indexing/build_memory_index.py --repo-root .
python 03_TOOLS/scripts/indexing/build_history_index.py --repo-root .
python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py --repo-root .
python 03_TOOLS/scripts/indexing/build_known_problems.py --repo-root .
```

Results:

- Python compile: `PASS`
- `git status`: `FAILED_NOT_A_GIT_REPOSITORY`
- Memory/history/AI-quality/known-problems indexes rebuilt.

### Output Safety Checks

```powershell
Select-String -Path 19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/**/* -Pattern FAB_READY,FAB READY,FABREADY,FINAL_FAB,MANUFACTURING_READY -SimpleMatch
Get-ChildItem 19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board -Recurse -File | Where-Object { $_.Extension -in '.gbr','.ger','.drl','.pos','.step','.stp' }
```

Results:

- No fabrication-ready claim strings were found.
- No generated Gerber, drill, pick-and-place, STEP, or STP files were found in the promoted sample copy.

No commands installed tools, downloaded datasheets, ran live web scraping, generated Gerbers, or wrote into imported originals.
