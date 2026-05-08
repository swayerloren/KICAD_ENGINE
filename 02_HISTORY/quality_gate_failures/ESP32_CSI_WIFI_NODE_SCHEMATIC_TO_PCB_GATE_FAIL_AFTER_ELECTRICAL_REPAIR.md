# Quality Gate Failure - ESP32_CSI_WIFI_NODE Schematic To PCB Gate

## Status

- Date: 2026-05-03
- Project: `ESP32_CSI_WIFI_NODE`
- Gate: `SCHEMATIC_TO_PCB_GATE`
- Result: `FAIL`

## Summary

ERC is clean after schematic repair, but the schematic-to-PCB gate did not pass.

## Blocking Reasons

- AO3401A PMOS pin mapping and footprint orientation unresolved.
- USB VBUS/backfeed policy unresolved.
- USB shield EMC strategy unresolved.
- BOM lock input file missing.
- Schematic-ready parts input file missing.
- Needs-review input file missing.
- Footprints not assigned and verified to package drawings.
- Connector orientation review incomplete.
- Polarity-sensitive part review incomplete.
- Regulator passives and USB-C/ESP32 source verification incomplete.

## Blocked Actions

Do not update PCB from schematic, place parts, route traces, create zones, or generate manufacturing outputs until the gate is `PASS`.
