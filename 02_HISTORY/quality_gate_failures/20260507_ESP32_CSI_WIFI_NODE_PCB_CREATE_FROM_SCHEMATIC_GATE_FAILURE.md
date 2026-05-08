# Quality Gate Failure: ESP32_CSI_WIFI_NODE PCB Create From Schematic

Date: 2026-05-07

Gate: `SCHEMATIC_TO_PCB_GATE`

Result: `FAIL`

## Evidence

- `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`: `Gate result: FAIL`
- `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`: `PCB update allowed: NO`
- `PRE_SCHEMATIC_BOM_LOCK.md`: `Schematic footprint assignment can safely proceed now: NO`
- `SCHEMATIC_READY_PARTS_LIST.md`: `NOT_READY_FOR_AUTOMATIC_FOOTPRINT_ASSIGNMENT`

## Decision

Do not create/update PCB from schematic until the gate is exact `PASS` or LJ provides an explicit logged gate exception.

