# Quality Gate Failure: ESP32_CSI_WIFI_NODE Schematic Checker Reports

Record kind: `quality_gate_failure`
Created: `2026-05-03T07:54:00`
Scope: `project`
Project: `ESP32_CSI_WIFI_NODE`
Severity: `BLOCKER`
Confidence: `HIGH`
Claim status: `VERIFIED_BY_FILE`
Risk label: `BLOCKED_UNTIL_HUMAN_REVIEW`
Gate result: `BLOCKED_UNTIL_HUMAN_REVIEW`
Human review required: `YES`

## Summary

The active project checker reports are failing and must block PCB update/layout/routing.

## Evidence

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_ANNOTATION_CHECK.json`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_COMPLETENESS_CHECK.json`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_BOM_LOCK_ALIGNMENT_CHECK.json`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/SCHEMATIC_NEEDS_REVIEW_MARKER_CHECK.json`

## Required Follow-Up

- Resolve or formally block missing footprints, missing BOM-lock evidence, and unresolved `NEEDS_REVIEW`/`BLOCKED` markers.
- Do not update PCB from schematic until the active project's schematic-to-PCB gate status is exactly `PASS`.
