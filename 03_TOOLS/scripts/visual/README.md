# Visual Scripts

## Purpose

This folder contains read-only visual verification helpers for KiCad Engine.

`generate_schematic_closeups.py` turns a full-page KiCad schematic SVG export into configured close-up crop files and a `CLOSE_UP_REVIEW.md` report.

## Inputs

- Full-page KiCad schematic SVG export.
- Project visual block config:

`_verification/schematic_visual/visual_blocks.json`

## Outputs

- SVG crops under a crops folder.
- PNG crops when an SVG renderer is available.
- `CLOSE_UP_REVIEW.md`.
- Optional JSON summary.

## Safety

- Does not edit `.kicad_sch`, `.kicad_pro`, `.kicad_pcb`, symbols, footprints, or manufacturing outputs.
- Does not click, type, or automate the KiCad GUI.
- Detects visible text from the exported SVG. It is not a substitute for human review.

## Example

```powershell
python .\03_TOOLS\scripts\visual\generate_schematic_closeups.py `
  --source-svg ".\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_visual\full_page\ESP32_CSI_WIFI_NODE.svg" `
  --config ".\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_visual\visual_blocks.json" `
  --crops-dir ".\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_visual\crops" `
  --review-output ".\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\CLOSE_UP_REVIEW.md" `
  --json-output ".\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\schematic_visual\CLOSE_UP_REVIEW.json" `
  --create-default-config
```

Use `03_TOOLS/kicad/run_schematic_visual_check.ps1` for the normal KiCad Engine wrapper that exports SVG/PDF first.
