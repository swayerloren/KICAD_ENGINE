# Bottom Edge Connector Placement Audit

Status: `ACTIVE_BLOCKER`

Generated: `2026-05-07T13:03:00-04:00`

Project: `ESP32_CSI_WIFI_NODE`

Evidence files:

- `reports/BOTTOM_EDGE_CONNECTOR_PLACEMENT_REPAIR_REPORT.md`
- `reports/J1_J2_CONNECTOR_ORIENTATION_PROOF.md`
- `reports/BOTTOM_EDGE_CONNECTOR_DRC_REPORT.md`
- `_verification/pcb_visual/BOTTOM_EDGE_CONNECTOR_REPAIR_REVIEW.md`
- `_verification/pcb_visual/bottom_edge_connector_top.svg`
- `_verification/pcb_visual/bottom_edge_connector_bottom.svg`
- `_verification/pcb_visual/bottom_edge_connector_3d_top.png`
- `_verification/pcb_visual/bottom_edge_connector_3d_front.png`
- `_verification/pcb_visual/bottom_edge_connector_3d_back.png`
- `kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

## Audit Result

| Check | Result | Evidence / Notes |
|---|---|---|
| J2 is on bottom edge | `PASS` | J2 at `(39.0, 89.5)`, bounding box y=`80.321..94.845` on board bottom y=`95.0`. |
| J2 mouth faces down/off-board | `PASS` | 3D top/front/back renders show USB-C receptacle at the bottom edge facing outward. |
| J2 PCB-edge line aligns to bottom Edge.Cuts | `PASS_WITH_REVIEW_NOTE` | J2 body/courtyard reaches y=`94.845` against bottom Edge.Cuts y=`95.0`; 3D render shows correct edge behavior. Exact footprint edge-line graphic should still be visually checked by LJ in KiCad. |
| J1 is on bottom edge or parked/replacement-blocked | `FAIL_PARTIAL` | J1 is bottom-left at `(13.0, 89.0)`, bounding box y=`76.321..94.025`, but it is not parked/replacement-blocked and mouth direction cannot be proven in 3D. |
| J1 is not side-mounted unless LJ approved | `PASS` | J1 was not side-mounted; rotation is `90 deg` with bottom-edge placement. |
| Test pads are not crowded behind J2 | `PASS` | TP1-TP9 are a right-side vertical service row at x=`57.0`, y=`40.0..72.0`. |
| R6/R7/R8/R9 are not mixed into test pads | `PASS` | R6/R7/R8/R9 are in the USB support area, separated from the TP row. |
| U3 is close to J2 | `PASS` | U3 at `(39.0, 78.0)`, directly behind J2. |
| U2 is at top with RF keepout clear | `PASS` | U2 remains at top, antenna/RF region faces the top edge. No zones/traces/vias exist. |
| Mounting holes do not collide with RF or connector areas | `PASS` | MH1/MH2 are bottom corners clear of J1/J2 bodies; MH3/MH4 are side/top-mid and outside U2 RF keepout. |
| No silkscreen over pads/holes | `PASS` | Latest DRC report shows no silkscreen warnings; visual review does not show labels over holes or connector pads. |
| DRC real placement issues listed | `PASS` | Remaining non-routing DRC issue is U2 pad 41 drill size. |

## Hard Blockers

1. `J1_3D_ORIENTATION_PROOF_BLOCKED`

   J1 footprint references `${KICAD9_3DMODEL_DIR}/Connector_BarrelJack.3dshapes/BarrelJack_CUI_PJ-102AH_Horizontal.step`, but the installed KiCad 9 model library does not contain that model. The 3D render therefore cannot prove the barrel jack mouth faces down/off-board.

2. `U2_DRILL_RULE_BLOCKER`

   DRC reports 12 `drill_out_of_range` violations on U2 pad 41: actual hole `0.20 mm`, board minimum `0.30 mm`.

## Expected Non-Blockers For This Phase

- `78` unconnected items are expected because no routing has been performed.
- No routing records, vias, or zones were found in the PCB file during audit.

## Final Classification

`BLOCKED_BY_MECHANICAL_OR_FOOTPRINT_RISK`

Routing remains blocked.
