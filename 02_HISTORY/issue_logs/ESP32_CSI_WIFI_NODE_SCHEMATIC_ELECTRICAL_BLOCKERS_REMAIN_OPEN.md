# Issue Log - ESP32_CSI_WIFI_NODE Schematic Electrical Blockers Remain Open

## Issue

- Date opened: 2026-05-03
- Project: `ESP32_CSI_WIFI_NODE`
- Severity: `HIGH`
- Status: `OPEN`
- Human review required: `YES`

## Summary

The 2026-05-03 schematic electrical repair pass cleaned ERC to 0 errors and 0 warnings, but the schematic-to-PCB gate remains `FAIL` due to unresolved high-risk review blockers.

## Evidence

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/SCHEMATIC_ELECTRICAL_AUDIT.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/ESP32_CSI_WIFI_NODE_SCHEMATIC_ELECTRICAL_BLOCKERS_ERC.txt`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_CLOSE_UP_VISUAL_REVIEW.md`

## Remaining Blockers

- AO3401A PMOS pin mapping and footprint orientation.
- USB VBUS/backfeed policy.
- USB shield EMC strategy.
- Missing BOM lock / parts / needs-review input files.
- Unverified footprints/package drawings.
- Connector orientation and polarity-sensitive part review.
- Regulator passives and USB-C/ESP32 source verification.

## Required To Close

Resolve the remaining blockers with source-backed evidence and update the project gate file to `PASS`.
