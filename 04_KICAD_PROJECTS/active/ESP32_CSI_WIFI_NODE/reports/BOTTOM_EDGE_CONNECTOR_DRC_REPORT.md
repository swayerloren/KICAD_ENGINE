# Bottom Edge Connector DRC Report

Status: `ACTIVE_EVIDENCE`

Generated: `2026-05-07T13:35:00-04:00`

Project: `ESP32_CSI_WIFI_NODE`

Raw DRC report: `reports/BOTTOM_EDGE_CONNECTOR_DRC_REPORT.rpt`

## Command

```powershell
kicad-cli pcb drc '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb' --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\BOTTOM_EDGE_CONNECTOR_DRC_REPORT.rpt' --format report --schematic-parity
```

## Result

- DRC violations: `13`
- Unconnected items: `78`
- Schematic parity issues: `0`

## Remaining DRC Categories

| Count | Category | Status |
|---:|---|---|
| 12 | U2 pad 41 `drill_out_of_range`, actual `0.2000 mm`, board minimum `0.3000 mm` | `PRE_EXISTING_BLOCKER` |
| 1 | J1 `lib_footprint_mismatch` warning | `BLOCKED_J1_FOOTPRINT_OR_3D_MODEL_NOT_PROVEN` |

## Connector Orientation DRC Notes

- Final DRC no longer reports J2 pad shorts, J2 pad overlaps, or J2 solder-mask bridge errors after restoring the embedded J2 footprint geometry to match the installed KiCad footprint.
- Final DRC no longer reports J1/MH1 hole-clearance errors after moving J1 to `(14.0,93.2)` and moving F1 to `(15.0,77.5)`.
- Unconnected items are expected because routing was not performed.

## Routing Status

`ROUTING_ALLOWED: NO`
