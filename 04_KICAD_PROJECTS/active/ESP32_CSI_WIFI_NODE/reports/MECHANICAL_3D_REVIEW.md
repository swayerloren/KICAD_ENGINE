# ESP32_CSI_WIFI_NODE Mechanical / 3D Review

Date: 2026-05-07

Mode: `READ_ONLY`

Output status: `NOT_FINAL`

Schematic edited: `NO`

PCB edited: `NO`

STEP export attempted: `NO`

STEP export result: `NOT_CREATED_NO_PCB`

Final classification: `MECHANICAL_REVIEW_BLOCKED`

## Evidence Reviewed

- `AGENTS.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `00_CODEX_START/CURRENT_PROJECT.md`
- `reports/FINAL_PCB_AUDIT_BEFORE_FAB.md`
- `reports/PRODUCTION_RISK_REGISTER.md`
- `reports/JLCPCB_DFM_DFA_REVIEW.md`
- `reports/PCB_SELECTED_LAYOUT_PLAN.md`
- `Test-Path kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`: `False`

## STEP Export Decision

STEP export was not attempted because no `.kicad_pcb` source file exists. Creating `renders/NOT_FINAL_STEP_REVIEW/` without a real STEP artifact would be misleading, so that folder was not created.

Expected future output path if a valid PCB exists:

`renders/NOT_FINAL_STEP_REVIEW/ESP32_CSI_WIFI_NODE_NOT_FINAL.step`

## Mechanical Checklist

| # | Check | Status | Evidence | Required closure |
|---:|---|---:|---|---|
| 1 | Export STEP if possible as NOT_FINAL review output | `BLOCKED_NO_PCB` | No `.kicad_pcb` exists. | Create PCB only after schematic-to-PCB gate passes, then export STEP as `NOT_FINAL`. |
| 2 | Check 3D models missing | `BLOCKED_NO_PCB` | No board footprints exist to inspect for 3D model links. | After PCB exists, run STEP export and inspect KiCad missing-model warnings. |
| 3 | Check barrel jack edge position | `BLOCKED_NO_PLACEMENT` | J1 exact MPN/drawing unresolved; layout plan only proposes bottom-left edge. | Verify exact barrel jack drawing, plug insertion clearance, enclosure panel cutout, and overhang. |
| 4 | Check USB-C edge position | `BLOCKED_NO_PLACEMENT` | J2 exact suffix/drawing unresolved; layout plan only proposes bottom-right edge. | Verify shell tabs, board-edge setback, connector centerline, and enclosure opening. |
| 5 | Check USB-C plug clearance | `BLOCKED_NO_3D` | No board outline, connector model, or enclosure exists. | Verify plug body, cable bend, panel wall, and adjacent barrel jack clearance in 3D. |
| 6 | Check pigtail/U.FL/SMA antenna path | `BLOCKED_NO_3D` | ESP32-S3-WROOM-1U U.FL/pigtail clearance is an open risk; no placement/keepout exists. | Define pigtail bend radius, SMA bulkhead location, cable strain relief, and RF keepout. |
| 7 | Check ESP32 module keepout | `BLOCKED_NO_PCB` | No keepout exists; module footprint equivalence still requires review. | Verify WROOM-1U land pattern, antenna/U.FL clearance, copper keepout, and enclosure clearance. |
| 8 | Check mounting hole spacing and screw size | `BLOCKED_NO_MECHANICAL_DEFINITION` | MH1-MH4 require final screw size, NPTH/plated intent, standoff/washer clearance. | Confirm screw size, standoff OD, washer OD, and hole diameter before board outline lock. |
| 9 | Check mounting holes relative to board edge | `BLOCKED_NO_BOARD_OUTLINE` | No board outline or mounting hole placement exists. | Place holes with explicit edge offsets and keepouts; run DRC/mechanical review. |
| 10 | Check board thickness assumptions | `NEEDS_DECISION` | No stackup/order profile is locked. | Decide nominal board thickness, likely 1.6 mm unless enclosure/connectors require otherwise; verify connector fit. |
| 11 | Check tall components | `BLOCKED_NO_3D` | Exact connector, inductor, capacitor, switch, and module heights are unresolved. | Select exact MPNs and verify height against enclosure and cable paths. |
| 12 | Check component collisions | `BLOCKED_NO_PLACEMENT` | No placement/courtyard/3D model exists. | Place components and run DRC plus 3D visual collision inspection. |
| 13 | Check test pad access | `BLOCKED_NO_PLACEMENT` | TP1-TP9 access remains open; no enclosure or placement exists. | Define probe direction and enclosure access; keep USB D+/D- pads out or short if used. |
| 14 | Check LED visibility | `BLOCKED_NO_PLACEMENT` | D2/D3 exact LED color/package missing; no enclosure/window or placement exists. | Select LEDs, place near visible edge/window, and verify viewing angle/light pipe need. |
| 15 | Check button access | `BLOCKED_NO_PLACEMENT` | SW1/SW2 exact tactile switch MPNs missing; no enclosure access exists. | Select switches and verify actuator direction, button cap/pinhole access, and panel clearance. |
| 16 | Check silkscreen orientation/readability | `BLOCKED_NO_PCB` | No PCB silkscreen exists. | After placement, review reference/value text, polarity marks, connector labels, and edge readability. |

## Mechanical Planning Notes From Selected Layout Plan

- Selected plan: `Plan B - Connector-Edge Optimized Board`
- Planning board size: `72 mm x 40 mm`
- Acceptable planning range: `68 mm x 38 mm` to `78 mm x 45 mm`
- Barrel jack planning location: bottom-left edge
- USB-C planning location: bottom-right edge
- ESP32 module planning location: upper-right quadrant
- RF/pigtail clearance side: top or right edge
- Mounting holes: four corner holes, planning offset about `5 mm` from each edge

These are planning assumptions only. They are not verified dimensions and must not be used for enclosure fabrication.

## Final Classification

`MECHANICAL_REVIEW_BLOCKED`

Reason: no PCB, board outline, placement, mounting holes, 3D model set, STEP export, enclosure model, or connector drawings are available for mechanical verification.
