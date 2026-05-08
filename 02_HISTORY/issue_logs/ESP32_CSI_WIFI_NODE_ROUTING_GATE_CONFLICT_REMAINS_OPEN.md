# Issue Log - ESP32_CSI_WIFI_NODE Routing Gate Conflict Remains Open

Status: `OPEN_RISK`

Date: `2026-05-07`

## Problem

`ESP32_CSI_WIFI_NODE` currently has conflicting status sources:

- `memory/CURRENT_PROJECT_STATE.md` says Stage 1/2 routing is complete and Stage 3 USB is next.
- `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` still says `Gate result: FAIL`.
- the phase checker therefore blocks Phase 8 routing.

## Impact

Future agents can be misled into editing the PCB because the project summary and the authoritative phase gate disagree.

## Current Safe Interpretation

The hard gate wins. Do not perform new PCB routing edits until the schematic-to-PCB gate evidence and phase-gate logic are reconciled or LJ explicitly approves and records an exception under repo rules.

