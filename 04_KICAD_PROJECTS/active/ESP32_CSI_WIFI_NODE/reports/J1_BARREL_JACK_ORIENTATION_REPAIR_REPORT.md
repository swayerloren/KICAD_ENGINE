# J1 Barrel Jack Orientation Repair Report

Status: `ACTIVE_EVIDENCE`

Generated: `2026-05-07T13:49:21-04:00`

Project: `ESP32_CSI_WIFI_NODE`

Target PCB: `kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`

Scope: J1 barrel-jack orientation repair only. No schematic edits, no routing, no copper zones, and no fabrication outputs were performed.

## Backup

`C:\Users\LJ\GitHub\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\20260507_134800_ESP32_CSI_WIFI_NODE_pre_J1_barrel_orientation_repair`

## Correction Applied

LJ correction: for the CUI/PJ-102AH-style horizontal barrel jack, the 3-pin solder-leg side is the connector back side. The female barrel plug opening is the opposite/front side.

The installed KiCad footprint geometry supports this:

- Pads are clustered at local `Y=0`, `Y=3`, and `Y=6`.
- The long body extends to local `Y=13.7` on `F.Fab` and local `Y=14.2` on `F.CrtYd`.
- Therefore the pad cluster is the 3-pin solder/back side.
- The opposite long-body end at local `+Y` is the female barrel opening/front side.

## J1 Placement Change

| Item | Before | After |
|---|---|---|
| Footprint | `Connector_BarrelJack:BarrelJack_CUI_PJ-102AH_Horizontal` | `Connector_BarrelJack:BarrelJack_CUI_PJ-102AH_Horizontal` |
| Position | `(14.0, 93.2)` | `(14.0, 80.8)` |
| Rotation | `180 deg` | `0 deg` |
| Female barrel opening side | local `+Y`, transformed inward/up before repair | local `+Y`, transformed to bottom edge |
| 3-pin solder/back side | local pad cluster `Y=0..6`, transformed nearest bottom before repair | local pad cluster `Y=0..6`, transformed inward into PCB |
| Side-mounted | `NO` | `NO` |

## New Geometry Proof

Board bottom edge: `Y=95.0 mm`

| Feature | Local footprint evidence | New transformed board location | Result |
|---|---|---|---|
| Female barrel opening/front side | `F.Fab` long-body/front end at local `Y=13.7`; `F.CrtYd` end at local `Y=14.2` | `F.Fab` front at `Y=94.5`; courtyard opening side midpoint at `(14.0,95.0)` | `PROVEN_2D` |
| 3-pin solder/back side | pads at local `(0,0)`, `(0,6)`, `(4.7,3)` | pad1 `(14.0,80.8)`, pad2 `(14.0,86.8)`, pad3 `(18.7,83.8)` | `PROVEN_ON_BOARD` |
| Pads on-board | pad cluster local `Y=0..6` | all pad coordinates are inside board limits `0 <= X <= 60`, `0 <= Y <= 95` | `PROVEN` |
| Opening faces bottom/off-board | local `+Y` side transformed to board bottom `Y=95.0` | female opening/front side at bottom edge | `PROVEN_2D` |

## 3D Model Status

Referenced model:

`${KICAD9_3DMODEL_DIR}/Connector_BarrelJack.3dshapes/BarrelJack_CUI_PJ-102AH_Horizontal.step`

Resolved installed path checked:

`C:\Program Files\KiCad\9.0\share\kicad\3dmodels\Connector_BarrelJack.3dshapes\BarrelJack_CUI_PJ-102AH_Horizontal.step`

Result: `MISSING`

No alternate 3D model was substituted because the requested proof requires the correct CUI/PJ-102AH-style barrel jack, not a generic or adjacent barrel-jack model.

3D proof status: `BLOCKED_J1_3D_MODEL_MISSING`

## DRC

Command output:

- `reports\J1_BARREL_JACK_ORIENTATION_REPAIR_DRC.rpt`
- `reports\J1_BARREL_JACK_ORIENTATION_REPAIR_DRC.console.txt`

Result:

- DRC violations: `12`
- Unconnected items: `78`
- Schematic parity issues: `0`
- J1-specific DRC errors/warnings: `0`

Remaining DRC issue:

- `12 x drill_out_of_range` on U2 pad 41: actual hole `0.2000 mm`, board minimum `0.3000 mm`.

Unconnected items are expected because routing was not performed.

## Visual Evidence

- `_verification\pcb_visual\j1_barrel_orientation_repair_top.svg`
- `_verification\pcb_visual\j1_barrel_orientation_repair_bottom.svg`
- `_verification\pcb_visual\j1_barrel_orientation_repair_3d_bottom_front.png`
- `_verification\pcb_visual\j1_barrel_orientation_repair_3d_top.png`
- `_verification\pcb_visual\J1_BARREL_JACK_ORIENTATION_REVIEW.md`

The 3D images are useful for the board/other rendered models, but they cannot prove J1 body mouth direction because the correct J1 STEP model is missing.

## Final Classification

`J1_FIXED_2D_ORIENTATION_PROVEN__3D_MODEL_PROOF_BLOCKED`

Routing allowed: `NO`

