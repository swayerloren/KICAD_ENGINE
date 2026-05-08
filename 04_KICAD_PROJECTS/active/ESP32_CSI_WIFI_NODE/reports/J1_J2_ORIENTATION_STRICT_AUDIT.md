# J1/J2 Orientation Strict Audit

Status: `ACTIVE_EVIDENCE`

Generated: `2026-05-07T13:50:00-04:00`

Project: `ESP32_CSI_WIFI_NODE`

Scope: audit only after orientation repair. No PCB edits, routing, zones, or fabrication outputs were performed.

## Evidence Reviewed

- `reports/J1_J2_FOOTPRINT_GEOMETRY_ORIENTATION_AUDIT.md`
- `reports/J1_J2_BOTTOM_EDGE_ORIENTATION_REPAIR_REPORT.md`
- `reports/J1_J2_CONNECTOR_ORIENTATION_PROOF.md`
- `_verification/pcb_visual/J1_J2_ORIENTATION_REPAIR_REVIEW.md`
- `reports/BOTTOM_EDGE_CONNECTOR_DRC_REPORT.rpt`
- Current `kicad/ESP32_CSI_WIFI_NODE.kicad_pcb` footprint coordinates and transformed primitive coordinates
- Existing 3D evidence images under `_verification/pcb_visual`

## Board Reference

- Board size: `60.0 mm x 95.0 mm`
- Bottom Edge.Cuts: `Y=95.0 mm`
- Routing status: `BLOCKED`

## Strict Audit Table

| Check | Result | Evidence |
|---|---|---|
| 1. J2 is on bottom edge | `PROVEN` | J2 at `(39.0,91.325)`, footprint edge line transforms to bottom `Y=95.0`. |
| 2. J2 mouth/opening faces down/off-board | `PROVEN` | 3D front/bottom-edge and J2 close-up renders show the USB-C receptacle opening facing off the bottom edge. |
| 3. J2 PCB-edge line aligns to bottom Edge.Cuts | `PROVEN` | J2 `PCB Edge` line transforms to `(44.0,95.0)` through `(34.0,95.0)`. |
| 4. J2 pads are on-board | `PROVEN` | Main USB pads at `Y=87.645`; shell pads at `Y=88.220` and `Y=92.400`, all below bottom edge limit `Y=95.0`. |
| 5. J2 body overhang is correct | `PROVEN_FOR_REVIEW` | 3D render shows connector mouth/body at bottom edge with expected edge exposure; final DRC reports no J2 edge/collision/short issues. |
| 6. J1 is on bottom edge, not side-mounted, or parked/blocker recorded | `BLOCKED_WITH_PLACED_BOTTOM_EDGE_EVIDENCE` | J1 placed at `(14.0,93.2)`, rotation `180 deg`, not side-mounted and not parked; blocker recorded for missing 3D proof. |
| 7. J1 mouth/opening faces down/off-board if placed | `NOT_PROVEN` | 2D footprint geometry supports local front/mouth at bottom edge `(14.0,95.0)`, but the required 3D model is missing. |
| 8. J1 pads are on-board if placed | `PROVEN_2D_ONLY` | J1 pads transform to `(14.0,93.2)`, `(14.0,87.2)`, `(9.3,90.2)`, all on-board. |
| 9. J1 body/courtyard does not collide with J2, holes, or switches | `PROVEN_BY_FINAL_DRC_FOR_LISTED_COLLISIONS` | Final DRC no longer lists J1 collision with MH1/F1/J2/switches; visual 2D/3D blocker evidence still requires LJ review. |
| 10. Missing 3D model cannot be approved | `BLOCKED` | J1 referenced STEP model is not installed; do not approve J1 as mechanically proven. |
| 11. DRC real connector/mechanical issues are listed | `PROVEN` | Final DRC: 12 U2 pad 41 drill-size errors, 1 J1 footprint-library mismatch warning, 78 unconnected items, 0 schematic parity issues. |
| 12. Routing remains blocked | `PROVEN` | Repair report and proof report both classify routing as `NO`; current audit preserves that state. |

## Connector-Specific Findings

### J2 USB-C

`PROVEN`

J2 satisfies bottom-edge placement, mouth direction, PCB-edge indicator alignment, on-board pads, and 3D visual proof. The final DRC report does not list J2 connector shorts, pad overlaps, edge-clearance violations, or mechanical collisions.

### J1 Barrel Jack

`BLOCKED_J1_FOOTPRINT_OR_3D_MODEL_NOT_PROVEN`

J1 is physically placed on the bottom-left edge and is not side-mounted. Its 2D F.Fab/F.CrtYd/pad geometry supports rotation `180 deg`, with the local front/mouth side at `Y=95.0` and pads on-board. However, the barrel-jack 3D model is missing, so J1 cannot be approved as mouth-direction proven.

## Final Classification

`J2_READY_J1_BLOCKED_REPLACEMENT_REQUIRED`

Routing remains blocked.
