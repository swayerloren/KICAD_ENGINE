# J1 Barrel Jack Orientation Review

Status: `ACTIVE_EVIDENCE`

Generated: `2026-05-07T13:49:21-04:00`

Project: `ESP32_CSI_WIFI_NODE`

Scope: visual evidence record for J1 barrel-jack orientation repair. No routing, zones, or fabrication outputs were created.

## Visual Files

| File | Purpose | Status |
|---|---|---|
| `j1_barrel_orientation_repair_top.svg` | Top 2D view showing J1 F.Fab/F.SilkS/F.CrtYd and bottom Edge.Cuts | `CREATED` |
| `j1_barrel_orientation_repair_bottom.svg` | Bottom 2D reference view | `CREATED` |
| `j1_barrel_orientation_repair_3d_bottom_front.png` | 3D bottom/front board view | `CREATED_WITH_J1_3D_BLOCKED` |
| `j1_barrel_orientation_repair_3d_top.png` | 3D top board view | `CREATED_WITH_J1_3D_BLOCKED` |

## Review Notes

- J1 was changed from `(14.0,93.2)`, rotation `180 deg`, to `(14.0,80.8)`, rotation `0 deg`.
- The female barrel opening/front side is the long-body side opposite the 3-pin solder-leg pad cluster.
- The 3-pin solder/back side is the pad cluster at local `Y=0`, `Y=3`, and `Y=6`.
- After repair, the female opening/front side is at the bottom edge: local `+Y` courtyard side transforms to `(14.0,95.0)`.
- After repair, the 3-pin solder/back side faces inward: pads transform to `(14.0,80.8)`, `(14.0,86.8)`, and `(18.7,83.8)`.
- J1 is not side-mounted.
- J1 pads remain on-board.
- The correct J1 STEP model is missing, so the 3D render cannot prove J1 mouth direction.

## 3D Proof Status

`BLOCKED_J1_3D_MODEL_MISSING`

Do not approve J1 from 3D until the correct PJ-102AH-style model is available and rendered.

Routing allowed: `NO`

