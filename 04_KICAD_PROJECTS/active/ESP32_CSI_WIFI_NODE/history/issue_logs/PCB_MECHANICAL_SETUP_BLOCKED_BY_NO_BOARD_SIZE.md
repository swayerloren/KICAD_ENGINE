# PCB_MECHANICAL_SETUP_BLOCKED_BY_NO_BOARD_SIZE

Status: `OPEN`

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

## Issue

PCB mechanical setup is blocked because no synced PCB exists and board size/mechanical constraints are unknown.

## Evidence

- No `.kicad_pcb` file exists.
- `reports/PCB_UPDATE_FROM_SCHEMATIC_REPORT.md` says PCB update was `NOT_RUN_GATE_FAIL`.
- `REQUIREMENTS.md` lists exact board outline dimensions as an open question.
- No `notes/mechanical*.md` file was found.

## Required Resolution

Provide board size, layer count, board thickness, enclosure dimensions, mounting hole geometry, connector edge requirements, antenna/SMA/pigtail mechanical constraints, and test-pad access requirements. Then resolve the schematic-to-PCB gate before PCB creation/update.

