# PCB Intelligence-Based Placement Repair Report

Status: `ACTIVE_BLOCKER`

Generated: `2026-05-07T12:56:21-04:00`

Project: `ESP32_CSI_WIFI_NODE`

Supersedes: prior `55 x 90 mm` intelligence placement report with side-mounted J1.

Current relevance: records the bottom-edge connector placement repair. Routing remains blocked.

## Scope

- PCB edited: `YES`
- Routing performed: `NO`
- Zones created: `NO`
- Fabrication outputs generated: `NO`

## Backup

`C:\Users\LJ\GitHub\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\20260507_124915_ESP32_CSI_WIFI_NODE_pre_bottom_edge_connector_repair`

## Placement Result

| Item | Result |
|---|---|
| Board outline | `60.0 mm x 95.0 mm`, pill/dev-board style. |
| U2 ESP32 module | Top placement retained; antenna/RF keepout faces top edge. |
| J2 USB-C | Bottom edge, footprint rotation `90 deg`, pads inside board, 3D model renders with receptacle facing off-board at the bottom edge. |
| J1 barrel jack | Bottom-left edge attempted and placed at `(13.0, 89.0)`, rotation `90 deg`, pads inside board. |
| J1 3D proof | `BLOCKED`: footprint references `${KICAD9_3DMODEL_DIR}/Connector_BarrelJack.3dshapes/BarrelJack_CUI_PJ-102AH_Horizontal.step`, but that installed model was not found, so mouth direction cannot be proven in 3D. |
| J1 side-mounted | `NO` |
| USB cluster | U3 is behind J2; R6/R7 are near J2; R8/R9 are between U3 and U2 side of the USB path. |
| Power cluster | Compact bottom-left to mid-board chain: J1, F1, Q1, D3/C2/C5, U1/C6/L1/C7/C8. |
| Test pads | TP1-TP9 are in a clean right-side vertical row, not behind J2 and not mixed into USB passives. |
| Mounting holes | Four holes retained; none are in the RF keepout or connector body areas. |

## DRC Summary

KiCad DRC was run with schematic parity.

- DRC violations: `12`
- Unconnected items: `78`
- Schematic parity issues: `0`

The `78` unconnected items are expected because this task intentionally did not route.

Remaining non-routing DRC issue:

- `12 x drill_out_of_range`: U2 pad 41 holes are `0.20 mm` while board setup minimum hole is `0.30 mm`.

## Classification

`BLOCKED_BY_MECHANICAL_OR_FOOTPRINT_RISK`

Reason: J2 orientation is proven in 2D/3D, and J1 is bottom-edge in 2D, but J1 cannot be proven in 3D because its KiCad 3D model is missing from the installed model library. Routing remains blocked.
