# ESP32_CSI_WIFI_NODE Auto Layout Sandbox Run Blocked

Status: `OPEN`

Date: `2026-05-07`

## Summary

The requested automatic PCB layout sandbox run was blocked before variant generation.

## Exact Blockers

1. `AUTO_BLOCKED_SCHEMATIC_GATE_FAIL`
   - `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`
   - current status: `Gate result: FAIL`
2. `AUTO_BLOCKED_MISSING_FOOTPRINTS`
   - `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/FOOTPRINT_PACKAGE_GATE_REPORT.md`
   - current status: `Physical symbols with assigned footprints: 0`
   - current status: `Physical symbols with blank footprint fields: 43`

## Impact

- No new layout variants were generated in this run.
- No re-scoring was performed in this run.
- No auto-selected passing variant was produced in this run.
- Real PCB update, placement, and routing remain blocked.

## Required Resolution

1. Close the upstream schematic-to-PCB gate to exact `PASS`.
2. Assign footprints to all physical schematic symbols.
3. Re-run the automatic sandbox only after those two blockers are cleared.
