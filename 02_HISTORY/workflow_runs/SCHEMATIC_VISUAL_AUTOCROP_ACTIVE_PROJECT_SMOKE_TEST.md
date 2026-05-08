# Workflow Run: Schematic Visual Autocrop Active Project Smoke Test

Date: `2026-05-03`
Status: `SMOKE_TESTED`
Project: `ESP32_CSI_WIFI_NODE`
KiCad design files edited: `NO`

## Command

```powershell
.\03_TOOLS\kicad\run_schematic_visual_check.ps1 -ProjectRoot .\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE -CreateDefaultConfig -NoFailOnFindings
```

## Result

The wrapper exported full-page SVG/PDF, rendered a full-page PNG through the installed browser renderer, generated 13 close-up SVG crops, generated 13 close-up PNG crops, created `visual_blocks.json`, and wrote `reports/CLOSE_UP_REVIEW.md`.

The generated review status is `FAIL`, which is correct gate evidence for the active project because visible field-risk text remains in crop regions.

## Evidence

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/_verification/schematic_visual/CLOSE_UP_REVIEW.json`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/CLOSE_UP_REVIEW.md`
- `02_HISTORY/command_logs/AUTOMATIC_SCHEMATIC_CLOSEUP_CROPS_COMMANDS.md`

## Limits

This workflow run validates crop generation and report creation. It does not approve the schematic, PCB transition, footprints, pinouts, connector orientation, or manufacturing readiness.
