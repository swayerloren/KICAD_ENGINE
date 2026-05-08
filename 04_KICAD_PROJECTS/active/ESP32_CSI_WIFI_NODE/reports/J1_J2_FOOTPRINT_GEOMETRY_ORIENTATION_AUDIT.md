# J1/J2 Footprint Geometry Orientation Audit

Status: `ACTIVE_EVIDENCE`

Generated: `2026-05-07T13:35:00-04:00`

Project: `ESP32_CSI_WIFI_NODE`

Target PCB: `kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

## Scope

Connector-orientation repair only. No routing, no zones, no Gerbers, no BOM/CPL/STEP export.

## Board Edge

- Board size: `60.0 mm x 95.0 mm`
- Bottom Edge.Cuts: line from `(60, 95)` to `(0, 95)`
- Bottom direction in current board coordinates: increasing `Y`

## J2 USB-C Footprint Geometry

| Item | Evidence | Result |
|---|---|---|
| Footprint | `Connector_USB:USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal` | `PROVEN` |
| Installed library footprint loaded | `C:\Program Files\KiCad\9.0\share\kicad\footprints\Connector_USB.pretty\USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal.kicad_mod` | `PROVEN` |
| 3D model exists | `C:\Program Files\KiCad\9.0\share\kicad\3dmodels\Connector_USB.3dshapes\USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal.step` | `PROVEN` |
| F.Fab body | local rectangle `(-4.47,-3.675)` to `(4.47,3.675)` | body front/edge at local `+Y` |
| Dwgs.User PCB Edge | local line `(5,3.675)` to `(-5,3.675)`, text `PCB Edge` at `(0,3.1)` | expected PCB edge is local `+Y` |
| Pads | USB pads at local `Y=-3.68`; shell pads at local `Y=-3.105` and `Y=1.075` | electrical pads stay above edge when rotation is `0` |
| Chosen rotation | `0 deg` | `PROVEN` |
| PCB edge alignment | transformed PCB Edge line `(44.0,95.0)` to `(34.0,95.0)` | `PROVEN` |
| Pads on-board | A1 `(35.8,87.645)`, A12 `(42.2,87.645)` | `PROVEN` |
| 3D mouth direction | `j2_orientation_repair_3d_closeup.png`, `j1_j2_orientation_repair_3d_bottom_edge_front.png` | `PROVEN` |

The embedded J2 footprint copy contained local pad rotations from the previous bad placement. Those local rotations created DRC pad shorts after the parent footprint was moved to the geometry-proven `0 deg` bottom-edge orientation. The embedded J2 local pad/marker rotations were restored to the installed KiCad footprint geometry so the PCB Edge line, pads, and 3D model agree.

## J1 Barrel Jack Footprint Geometry

| Item | Evidence | Result |
|---|---|---|
| Footprint | `Connector_BarrelJack:BarrelJack_CUI_PJ-102AH_Horizontal` | `PROVEN` |
| Installed library footprint loaded | `C:\Program Files\KiCad\9.0\share\kicad\footprints\Connector_BarrelJack.pretty\BarrelJack_CUI_PJ-102AH_Horizontal.kicad_mod` | `PROVEN` |
| 3D model exists | referenced model is not present in installed KiCad 9 model tree | `NOT_PROVEN` |
| F.Fab body | front/chamfer area around local `Y=-0.7..0.3`; rear/body extends to local `Y=13.7` | mouth/front side inferred from footprint geometry |
| F.CrtYd | front local `Y=-1.8`; rear local `Y=14.2` | expected overhang/front side is local `-Y` |
| Pads | pad1 local `(0,0)`, pad2 `(0,6)`, pad3 `(4.7,3)` | pads stay on-board when rotation is `180` |
| Chosen rotation | `180 deg` | `PROVEN_2D_ONLY` |
| Mouth/front position | local front courtyard midpoint transforms to `(14.0,95.0)` | `PROVEN_2D_ONLY` |
| Rear/body direction | local rear courtyard midpoint transforms to `(14.0,79.0)` | `PROVEN_2D_ONLY` |
| Pads on-board | pad1 `(14.0,93.2)`, pad2 `(14.0,87.2)`, pad3 `(9.3,90.2)` | `PROVEN_2D_ONLY` |
| 3D mouth direction | missing installed STEP model | `NOT_PROVEN` |

J1 is not side-mounted. J1 remains bottom-left. Because the referenced 3D model is missing, J1 mouth direction is `PROVEN_2D_ONLY`, not 3D-proven.

## Rotation Trials

| Connector | 0 deg | 90 deg | 180 deg | 270 deg | Selected |
|---|---|---|---|---|---|
| J2 | PCB Edge line aligns to bottom Edge.Cuts; pads remain on-board; 3D mouth faces down | previous placement did not align PCB Edge line to bottom | would put PCB Edge line at top-side direction | would put PCB Edge line vertical, not bottom | `0 deg` |
| J1 | mouth/front local `-Y` faces up, not bottom | side-facing orientation | mouth/front local `-Y` faces bottom; pads remain on-board | side-facing orientation | `180 deg` |

## Classification

`J2_PROVEN_J1_BLOCKED_REPLACEMENT_REQUIRED`

Reason: J2 is proven by footprint geometry and 3D render. J1 is repaired to the only 2D geometry-consistent bottom-edge rotation, but installed 3D mouth proof is blocked by the missing barrel-jack model.
