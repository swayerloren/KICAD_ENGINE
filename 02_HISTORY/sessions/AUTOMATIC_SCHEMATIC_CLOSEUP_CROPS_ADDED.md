# Automatic Schematic Close-Up Crops Added

Date: `2026-05-03`
Session type: visual verification tooling.
KiCad design files edited: `NO`

## Work Completed

- Created `03_TOOLS/kicad/VISUAL_VERIFICATION_WORKFLOW.md`.
- Created `03_TOOLS/kicad/VISUAL_BLOCK_CONFIG_STANDARD.md`.
- Created `03_TOOLS/kicad/run_schematic_visual_check.ps1`.
- Created `03_TOOLS/scripts/visual/generate_schematic_closeups.py`.
- Created `03_TOOLS/scripts/visual/README.md`.
- Created `09_ACCURACY_ENGINE/verification_rules/CLOSE_UP_VISUAL_REVIEW_RULES.md`.
- Updated `09_ACCURACY_ENGINE/checklists/SCHEMATIC_READY_FOR_PCB_CHECKLIST.md`.
- Updated `AGENTS.md`, `README_GPT.md`, and `FOR CHAT GPT.MD`.

## Validation

- PowerShell parser validation passed.
- Python syntax validation passed.
- Active-project read-only smoke test generated full-page exports, crop files, and `CLOSE_UP_REVIEW.md`.
- Health check passed with `PASS=131 WARN=0 FAIL=0`.

## Active Project Result

Autocrops were generated for `ESP32_CSI_WIFI_NODE`, but the visual review status is `FAIL` because visible footprint/datasheet wording was detected in three crop regions. This is gate evidence and does not permit PCB update.

## Remaining Limitations

- Default visual block coordinates are starter normalized windows and may need project-specific tuning.
- SVG text scanning is not OCR.
- Visual crops do not verify footprint correctness, connector orientation, pinout correctness, ERC, DRC, or fabrication readiness.
