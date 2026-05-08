# Issue Log - Schematic Electrical Blockers Remain Open

## Issue

- Date opened: 2026-05-03
- Project: `ESP32_CSI_WIFI_NODE`
- Severity: `HIGH`
- Status: `OPEN`
- Human review required: `YES`

## Summary

The schematic repair pass fixed ERC/connectivity and rail naming issues, but the schematic-to-PCB gate remains `FAIL`.

## Evidence

- Electrical audit: `SCHEMATIC_ELECTRICAL_AUDIT.md`
- Gate status: `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`
- ERC report: `reports/ESP32_CSI_WIFI_NODE_SCHEMATIC_ELECTRICAL_BLOCKERS_ERC.txt`
- Visual review: `reports/SCHEMATIC_CLOSE_UP_VISUAL_REVIEW.md`

## Remaining Blockers

- AO3401A PMOS symbol pin mapping and footprint orientation.
- USB VBUS/backfeed policy.
- USB shield EMC strategy.
- Missing `PRE_SCHEMATIC_BOM_LOCK.md`.
- Missing `SCHEMATIC_READY_PARTS_LIST.md`.
- Missing `NEEDS_REVIEW_BEFORE_SCHEMATIC.md`.
- Unverified footprints/package drawings.
- Connector orientation review.
- Polarity-sensitive component review.
- Regulator passives and USB-C/ESP32 source verification.

## Blocked Actions

Do not update PCB from schematic, place parts, route traces, create zones, or generate manufacturing outputs until `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` is `PASS`.
