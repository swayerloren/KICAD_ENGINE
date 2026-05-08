# J1 Barrel Jack Orientation Audit

Status: `ACTIVE_BLOCKER`

Generated: `2026-05-07`

Project: `ESP32_CSI_WIFI_NODE`

Scope: strict read-only audit after the J1 barrel-jack orientation repair. No KiCad design files were edited. No routing, copper zones, fabrication outputs, BOM, CPL, drill, STEP, or Gerbers were generated.

## Final Classification

`J1_BLOCKED_NEEDS_VERIFIED_3D_MODEL_OR_DIFFERENT_FOOTPRINT`

Reason: J1 is `PROVEN_2D` from actual footprint geometry, but final J1 approval remains blocked because the exact PJ-102AH 3D model referenced by the footprint is missing and cannot be used to prove mouth direction in 3D.

Routing allowed: `NO`

## Evidence Reviewed

- PCB file inspected read-only: `kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`
- Connector rules: `09_ACCURACY_ENGINE\pcb_rules\CONNECTOR_EDGE_ORIENTATION_RULES.md`
- Mechanical rules: `09_ACCURACY_ENGINE\pcb_rules\PCB_MECHANICAL_CLEARANCE_RULES.md`
- Repair report: `reports\J1_BARREL_JACK_ORIENTATION_REPAIR_REPORT.md`
- Connector proof: `reports\J1_J2_CONNECTOR_ORIENTATION_PROOF.md`
- DRC report: `reports\J1_BARREL_JACK_ORIENTATION_REPAIR_DRC.rpt`
- Visual record: `_verification\pcb_visual\J1_BARREL_JACK_ORIENTATION_REVIEW.md`

## Board And Footprint Facts

- Board edge bounding box: `X=0.0..60.0 mm`, `Y=0.0..95.0 mm`
- Bottom Edge.Cuts: `Y=95.0 mm`
- J1 footprint: `Connector_BarrelJack:BarrelJack_CUI_PJ-102AH_Horizontal`
- J1 position: `(14.0, 80.8)`
- J1 rotation: `0 deg`
- Known part-orientation fact from LJ: for the CUI/PJ-102AH-style horizontal barrel jack, the 3-pin solder-leg side is the back side; the female barrel opening is the opposite/front side.

## J1 Footprint Geometry Proof

| Feature | Actual footprint geometry | Board transform at `(14.0,80.8)`, `0 deg` | Audit result |
|---|---|---|---|
| 3-pin solder/back side | pads at local `(0,0)`, `(0,6)`, `(4.7,3)` | pads at `(14.0,80.8)`, `(14.0,86.8)`, `(18.7,83.8)` | `PROVEN_2D`: back side faces up/inward into PCB |
| Female barrel opening/front side | opposite long-body side at local `+Y`; F.Fab max `Y=13.7`; F.CrtYd max `Y=14.2` | F.Fab front reaches `Y=94.5`; courtyard front reaches `Y=95.0` | `PROVEN_2D`: female opening faces bottom/off-board |
| Pads on PCB | all pad centers are local `Y=0..6` and local `X=0..4.7` | all pad centers inside board limits `0 <= X <= 60`, `0 <= Y <= 95` | `PROVEN` |
| Side-mounted | footprint is placed on bottom edge, not left or right edge | opening/front side aligns to bottom edge `Y=95.0` | `PROVEN_NOT_SIDE_MOUNTED` |

## 3D Proof Status

Referenced model:

`${KICAD9_3DMODEL_DIR}/Connector_BarrelJack.3dshapes/BarrelJack_CUI_PJ-102AH_Horizontal.step`

Resolved installed path checked:

`C:\Program Files\KiCad\9.0\share\kicad\3dmodels\Connector_BarrelJack.3dshapes\BarrelJack_CUI_PJ-102AH_Horizontal.step`

Result: `MISSING`

3D proof status: `NOT_PROVEN`

The existing 3D screenshots may show the board and other available models, but they do not prove J1 mouth direction because the exact PJ-102AH barrel-jack STEP model is missing. No generic or adjacent barrel-jack model is accepted as proof in this audit.

## Collision And Clearance Audit

J1 courtyard from actual footprint geometry transforms to approximately:

- `X=9.0..20.5 mm`
- `Y=79.0..95.0 mm`

Nearby checked features:

| Item | Position / evidence | J1 conflict status |
|---|---|---|
| J2 USB-C | `(39.0,91.325)`, bottom edge | `NO_COLLISION_PROVEN_BY_SEPARATION_AND_DRC` |
| MH1 | `(4.0,91.0)` | `NO_COLLISION_PROVEN_BY_SEPARATION_AND_DRC` |
| MH2 | `(56.0,91.0)` | `NO_COLLISION_PROVEN_BY_SEPARATION_AND_DRC` |
| SW1 | `(6.0,64.0)`, rotation `90 deg` | `NO_COLLISION_PROVEN_BY_SEPARATION_AND_DRC` |
| SW2 | `(6.0,54.0)`, rotation `90 deg` | `NO_COLLISION_PROVEN_BY_SEPARATION_AND_DRC` |
| TP1-TP9 | right-side row at `X=57.0`, `Y=40.0..72.0` | `NO_COLLISION_PROVEN_BY_SEPARATION_AND_DRC` |

The reviewed post-repair DRC report lists no J1-specific errors or warnings and reports `0 Footprint errors`. Remaining DRC errors are the known U2 pad-41 drill-size violations, not J1 placement collisions.

## J2 Regression Check

- J2 footprint: `Connector_USB:USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal`
- J2 position: `(39.0,91.325)`
- J2 rotation: `0 deg`
- J2 PCB Edge user line transforms from local `(5.0,3.675)` and `(-5.0,3.675)` to board points `(44.0,95.0)` and `(34.0,95.0)`.
- Result: `J2_REMAINS_PROVEN_BOTTOM_EDGE_MOUTH_DOWN_OFF_BOARD`

## DRC Status

Reviewed existing post-repair DRC:

- DRC violations: `12`
- Unconnected pads: `78`
- Footprint errors: `0`
- J1-specific errors/warnings: `0`
- Known open DRC issue: `12 x drill_out_of_range` on U2 pad 41, actual hole `0.2000 mm`, minimum `0.3000 mm`

Unconnected pads are expected because routing remains blocked and was not performed.

## Audit Result

J1 female barrel opening direction is `PROVEN_2D` from the actual footprint primitives and LJ's known physical orientation fact. The 3-pin solder/back side is `PROVEN_2D` to face inward/up into the PCB, and all J1 pads remain on-board.

Final approval is blocked because 3D mouth-direction proof is missing:

`J1_BLOCKED_NEEDS_VERIFIED_3D_MODEL_OR_DIFFERENT_FOOTPRINT`

