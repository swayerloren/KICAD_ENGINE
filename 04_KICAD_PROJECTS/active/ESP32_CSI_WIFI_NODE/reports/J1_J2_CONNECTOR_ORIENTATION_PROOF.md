# J1/J2 Connector Orientation Proof

Status: `ACTIVE_EVIDENCE`

Generated: `2026-05-07T13:49:21-04:00`

Project: `ESP32_CSI_WIFI_NODE`

## Board

- Board size: `60.0 mm x 95.0 mm`
- Bottom edge: `Edge.Cuts` at `Y=95.0 mm`
- Routing allowed: `NO`

## Proof Table

| Check | J2 USB-C | J1 Barrel Jack |
|---|---|---|
| Footprint | `Connector_USB:USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal` | `Connector_BarrelJack:BarrelJack_CUI_PJ-102AH_Horizontal` |
| Position | `(39.0, 91.325)` | `(14.0, 80.8)` |
| Chosen rotation | `0 deg` | `0 deg` |
| Mouth/opening direction proof | `PROVEN`: 3D close-up and front view show USB-C opening facing downward/off-board | `PROVEN_2D_ONLY`: LJ correction states the 3-pin solder-leg pad cluster is the back side; the opposite long-body side at local `+Y` transforms to the bottom edge |
| PCB edge alignment | `PROVEN`: footprint `PCB Edge` line transforms to `(34.0,95.0)` through `(44.0,95.0)` | `N/A`: barrel jack footprint has no explicit `PCB Edge` text/line |
| Pads on-board | `PROVEN`: USB pad row at `Y=87.645`, shell pads at `Y=88.220` and `Y=92.400` | `PROVEN`: pads at `(14.0,80.8)`, `(14.0,86.8)`, `(18.7,83.8)` |
| 3D model | `PROVEN`: installed STEP found and rendered | `NOT_PROVEN`: referenced STEP missing from installed KiCad 9 model library |
| Side-mounted | `NO` | `NO` |
| Parked outside board | `NO` | `NO` |

## J2 Result

`PROVEN`

J2 is on the bottom edge. Its footprint `PCB Edge` indicator is aligned to bottom Edge.Cuts, pads remain on-board, U3/R6/R7/R8/R9 remain behind/above J2, and 3D renders show the USB-C opening facing downward/off-board.

## J1 Result

`J1_FIXED_2D_ORIENTATION_PROVEN__3D_MODEL_PROOF_BLOCKED`

J1 was corrected after LJ identified the prior interpretation error. The 3-pin solder-leg pad cluster at local `Y=0..6` is the back side and now faces inward into the PCB. The opposite long-body/female-opening side at local `+Y` now faces the bottom edge/off-board. J1 is not side-mounted and is not parked outside the board. However, the installed KiCad model library does not contain `${KICAD9_3DMODEL_DIR}/Connector_BarrelJack.3dshapes/BarrelJack_CUI_PJ-102AH_Horizontal.step`, so J1 cannot be 3D-proven.

## Evidence Images

- `_verification/pcb_visual/j1_j2_orientation_repair_top.svg`
- `_verification/pcb_visual/j1_j2_orientation_repair_bottom.svg`
- `_verification/pcb_visual/j1_j2_orientation_repair_3d_full_top.png`
- `_verification/pcb_visual/j1_j2_orientation_repair_3d_bottom_edge_front.png`
- `_verification/pcb_visual/j2_orientation_repair_3d_closeup.png`
- `_verification/pcb_visual/j1_orientation_repair_3d_blocker_closeup.png`
- `_verification/pcb_visual/j1_barrel_orientation_repair_top.svg`
- `_verification/pcb_visual/j1_barrel_orientation_repair_bottom.svg`
- `_verification/pcb_visual/j1_barrel_orientation_repair_3d_bottom_front.png`
- `_verification/pcb_visual/j1_barrel_orientation_repair_3d_top.png`

## Final Classification

`J2_PROVEN_J1_FIXED_2D_PROOF_ONLY_3D_BLOCKED`
