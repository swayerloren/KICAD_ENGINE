# ESP32_CSI_WIFI_NODE Connector Orientation Proof Blocked

Record kind: `issue_log`
Status: `OPEN`
Created: `2026-05-10T09:05:00-04:00`
Scope: `project`
Project: `ESP32_CSI_WIFI_NODE`

## Summary

The new mechanical-orientation truth layer correctly blocks routing progression on `ESP32_CSI_WIFI_NODE` because `J1` barrel-jack orientation is not fully proven yet.

## Details

1. `J2` USB-C passes the new truth audit: mouth faces off-board, edge alignment is verified, and the 3D model resolves.
2. `U2` ESP32 antenna keepout passes the new outward-facing audit.
3. `J1` barrel jack now remains `NEEDS_HUMAN_REVIEW` because the 3D model reference exists but the model file does not resolve on this machine.
4. The latest prelayout gate therefore reports `0` passing variants and blocks both placement continuation and routing continuation.
5. This is the intended safety behavior: connector proof may not rely on XY position or rotation alone.

## Source Or Evidence

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/mechanical_orientation/20260510_connector_orientation_audit.json`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/mechanical_orientation/20260510_barrel_jack_orientation_audit.json`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/prelayout_engine/20260510_090120/prelayout_gate_result.json`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/prelayout_engine/20260510_090120/scores/variant_01.score.json`

## Verification Status

`VERIFIED_WORKFLOW` for the audit behavior and gate block. Human follow-up is still required to resolve `J1` mechanical proof.

## Secret Check

No secrets should be stored in this record.
