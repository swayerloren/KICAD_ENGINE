# PCB_MECHANICAL_SETUP_BLOCKED_BY_NO_BOARD_SIZE

Status: `BLOCKED_UNTIL_HUMAN_REVIEW`

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

## Gate Failure

PCB mechanical setup cannot proceed.

## Blocking Evidence

- No `.kicad_pcb` file exists.
- PCB is not synced from schematic.
- Board size is unknown.
- Mechanical notes are missing.
- Schematic-to-PCB gate is `FAIL`.

## Blocked Actions

Do not:

- create a board outline;
- set layer count or design constraints as final;
- add mounting holes;
- define connector, antenna, barrel jack, or test-pad keepouts;
- run DRC as if a board exists;
- export PCB visuals;
- route traces.

