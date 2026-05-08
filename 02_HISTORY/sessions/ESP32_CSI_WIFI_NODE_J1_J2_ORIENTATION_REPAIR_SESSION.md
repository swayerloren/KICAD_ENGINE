# ESP32_CSI_WIFI_NODE J1/J2 Orientation Repair Session

Status: `ACTIVE_EVIDENCE`

Date: `2026-05-07`

Project: `ESP32_CSI_WIFI_NODE`

## Scope

Fix J1 and J2 connector orientation using actual footprint geometry. Do not route.

## Startup And Safety

- Read required startup, control-plane, prompt-counter, connector, pill-board, mechanical-clearance, project memory, and prior connector report files.
- Incremented prompt counter from `2` to `3`; maintenance due: `NO`.
- Created pre-edit backup:
  `C:\Users\LJ\GitHub\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\20260507_132053_ESP32_CSI_WIFI_NODE_pre_J1_J2_orientation_repair`
- Phase checker returned `BLOCKED` for Phase 5 because it still keys off a stale schematic-gate prerequisite; current project state says placement/mechanical repair is the next allowed work. This conflict was treated as an explicit LJ-scoped exception for connector repair only.

## PCB Edits

- Changed J2 to position `(39.0,91.325)`, rotation `0 deg`.
- Restored J2 embedded local pad/marker rotations to match the installed KiCad USB-C footprint geometry.
- Changed J1 to position `(14.0,93.2)`, rotation `180 deg`.
- Restored J1 local pad rotations to installed KiCad barrel-jack footprint geometry.
- Moved F1 from `(15.0,78.0)` to `(15.0,77.5)` only to clear J1 connector courtyard/mechanical clearance.

## Verification

- DRC with schematic parity: `13` violations, `78` unconnected items, `0` schematic parity issues.
- Remaining violations are `12` U2 pad 41 drill-size errors plus `1` J1 footprint-library mismatch warning.
- Final DRC has no J2 short/overlap errors and no J1/MH1 hole-clearance errors.
- Top/bottom SVGs and 3D renders were created under `_verification/pcb_visual`.

## Final Classification

`J2_PROVEN_J1_BLOCKED_REPLACEMENT_REQUIRED`

Routing allowed: `NO`
