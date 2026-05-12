# ESP32_CSI_WIFI_NODE Schematic Layout Fail

Date: `2026-05-10`
Scope: `Read-only schematic layout engine dry-run`
Project: `ESP32_CSI_WIFI_NODE`

## Summary

The new schematic layout engine classified the active schematic as
`FAIL` with readability score `39 / 100`.

## Main Findings

- Visual flow: `FAIL`
- Local wire usage: `FAIL`
- Power flow is not cleanly left-to-right from input to buck to ESP32.
- USB-C block is in the upper-right instead of a lower connector-support
  region.
- Repeated local labels remain in the ESP32, reset/boot, and test/debug
  blocks.
- The test/debug block still presents USB signal labels as repeated local text
  instead of a cleaner grouped wiring pattern.

## Evidence

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_layout/20260510_113053/SCHEMATIC_LAYOUT_REVIEW.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_layout/20260510_113053/schematic_readability_score.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_layout/20260510_113053/visual_flow.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/schematic_layout/20260510_113053/local_wire_usage.md`

## Consequence

Schematic readability cleanup is still required before the schematic should be
treated as professionally organized or ready for any future schematic-to-PCB
rework cycle.
