# Bottom Edge Connector Placement Repair Report

Status: `ACTIVE_BLOCKER`

Generated: `2026-05-07T12:56:21-04:00`

Project: `ESP32_CSI_WIFI_NODE`

Evidence files:

- `kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`
- `_verification/pcb_visual/bottom_edge_connector_top.svg`
- `_verification/pcb_visual/bottom_edge_connector_bottom.svg`
- `_verification/pcb_visual/bottom_edge_connector_3d_top.png`
- `_verification/pcb_visual/bottom_edge_connector_3d_front.png`
- `_verification/pcb_visual/bottom_edge_connector_3d_back.png`
- `reports/BOTTOM_EDGE_CONNECTOR_DRC_REPORT.rpt`

## Backup

`C:\Users\LJ\GitHub\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\20260507_124915_ESP32_CSI_WIFI_NODE_pre_bottom_edge_connector_repair`

## Work Performed

- Incremented project prompt counter from `1` to `2`; maintenance is not due.
- Created a project backup before editing.
- Kept the board as a pill/dev-board layout and widened it to `60.0 mm x 95.0 mm`.
- Moved J2 USB-C to the bottom edge.
- Attempted J1 barrel jack on the bottom edge and placed it bottom-left.
- Moved test pads to a clean right-side vertical row.
- Cleaned local component spacing for USB support and power cluster placement.
- Hid/repositioned cluttering reference/value text where needed.
- Did not route traces.
- Did not create zones.
- Did not generate Gerbers, drill files, BOM, CPL, or STEP.

## Placement Coordinates

| Ref | Placement |
|---|---|
| J1 | `(13.0, 89.0)`, rotation `90 deg`, bottom-left footprint placement |
| J2 | `(39.0, 89.5)`, rotation `90 deg`, bottom-edge USB-C placement |
| U2 | `(30.0, 28.0)`, rotation `0 deg`, RF/antenna area facing top edge |
| U3 | `(39.0, 78.0)`, behind J2 |
| R6/R7 | `(31.5, 81.5)` and `(46.0, 81.5)`, close to J2 |
| R8/R9 | `(33.0, 75.0)` and `(45.0, 75.0)`, between U3 and U2 path |
| TP1-TP9 | Right-side vertical row from y=`40.0` to `72.0` at x=`57.0` |

## Connector Status

| Connector | Status |
|---|---|
| J2 USB-C bottom edge | `PASS`: 2D and 3D evidence show bottom-edge placement and mouth facing off-board. |
| J1 barrel jack bottom edge | `PARTIAL`: 2D footprint is bottom-left with pads inside board; 3D body did not render. |
| J1 side-mounted | `NO` |
| J1 replacement blocker | `NOT ASSERTED`: J1 physically fits in 2D, but 3D proof is blocked by missing model. |

## DRC Result

- `12` DRC violations
- `78` unconnected items
- `0` schematic parity issues

The remaining DRC violations are all U2 pad 41 drill-size rule violations. The unconnected items are expected before routing.

## Final Classification

`BLOCKED_BY_MECHANICAL_OR_FOOTPRINT_RISK`

J2 is ready for LJ visual review. J1 is not side-mounted, but J1 orientation cannot be called fully acceptable until the barrel jack 3D model is available or LJ accepts 2D footprint/courtyard evidence for this connector.
