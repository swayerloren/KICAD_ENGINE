# J1 Barrel Jack Orientation Audit Review

Status: `ACTIVE_BLOCKER`

Generated: `2026-05-07`

Scope: read-only visual evidence index for the J1 barrel-jack orientation audit. No new screenshots or fabrication outputs were generated during this audit.

## Review Classification

`J1_BLOCKED_NEEDS_VERIFIED_3D_MODEL_OR_DIFFERENT_FOOTPRINT`

## Existing Visual Evidence Reviewed

| File | Review use | Audit status |
|---|---|---|
| `j1_barrel_orientation_repair_top.svg` | 2D top-side footprint and bottom-edge review | `USABLE_FOR_2D_GEOMETRY_REVIEW` |
| `j1_barrel_orientation_repair_bottom.svg` | 2D bottom reference | `REFERENCE_ONLY` |
| `j1_barrel_orientation_repair_3d_bottom_front.png` | 3D board angle after repair | `J1_3D_PROOF_NOT_ACCEPTED_MODEL_MISSING` |
| `j1_barrel_orientation_repair_3d_top.png` | 3D board overview after repair | `J1_3D_PROOF_NOT_ACCEPTED_MODEL_MISSING` |
| `j2_orientation_repair_3d_closeup.png` | J2 USB-C 3D close-up | `J2_REMAINS_PROVEN` |
| `j1_j2_orientation_repair_3d_bottom_edge_front.png` | bottom-edge 3D reference | `J2_REFERENCE_AND_J1_BLOCKER_CONTEXT` |

## J1 2D Geometry Review

- J1 is `Connector_BarrelJack:BarrelJack_CUI_PJ-102AH_Horizontal`.
- J1 is at `(14.0,80.8)`, rotation `0 deg`.
- The known CUI/PJ-102AH-style physical orientation says the 3-pin solder-leg side is the back side.
- J1 pads are the local pad cluster at `(0,0)`, `(0,6)`, and `(4.7,3)`.
- Those pads transform to `(14.0,80.8)`, `(14.0,86.8)`, and `(18.7,83.8)`, so the back side faces inward/up into the PCB.
- The opposite/front side is the long-body local `+Y` side.
- F.Fab front max transforms to `Y=94.5`; F.CrtYd front max transforms to `Y=95.0`, matching the bottom edge.
- Result: `J1_ORIENTATION_PROVEN_2D_ONLY`

## 3D Review Limitation

Referenced model:

`${KICAD9_3DMODEL_DIR}/Connector_BarrelJack.3dshapes/BarrelJack_CUI_PJ-102AH_Horizontal.step`

Installed model status: `MISSING`

Result: `J1_3D_PROOF_MISSING`

The 3D screenshots cannot prove the J1 mouth direction until the exact PJ-102AH model is available and rendered, or J1 is replaced with a verified footprint/model set.

## Routing Status

Routing allowed: `NO`

Copper zones allowed: `NO`

