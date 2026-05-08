# Routing Stage 1/2 Cleanup Reroute Report

Date: `2026-05-07`

Project: `ESP32_CSI_WIFI_NODE`

Target PCB: `kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

Final classification: `STAGE_1_2_PARTIAL_NEEDS_MORE_REPAIR`

## Scope

Cleanup and reroute only the current Stage 1 and Stage 2 critical power nets:

- `J1/F1/Q1/D3/C2/C5` input/protection path
- `U1/C6/L1/C7/C8` buck/local output path

Explicitly not done in this pass:

- USB routing
- low-speed/control routing
- copper pours/zones
- fabrication/package exports

## Pre-Edit Controls

| Check | Result |
|---|---|
| Prompt counter incremented | `PASS`: `1 -> 2` |
| Maintenance due | `NO` |
| Unsaved KiCad GUI state | `NO_EESCHEMA_WINDOW` |
| Backup created | `YES` |
| Backup path | `99_BACKUPS/pre_codex_edits/20260507_150607_ESP32_CSI_WIFI_NODE_stage1_stage2_cleanup_reroute` |
| Baseline counts | `24` track segments, `2` vias, `0` zones |
| Baseline DRC | `12` violations, `67` unconnected items, schematic parity `0` |

## Cleanup Summary

Removed all existing routed copper on:

- `/+5V_IN`
- `/+5V_FUSED`
- `/+5V_PROTECTED`
- `/BUCK_SW`
- `/BUCK_BST`
- local `+3V3`

Counts:

- Track segments removed: `24`
- Vias removed: `2`
- Track segments added: `26`
- Vias added: `2`

Current board counts:

- Track segments: `26`
- Vias: `2`
- Zones: `0`

Current cleanup-net counts:

| Net | Segments |
|---|---:|
| `/+5V_IN` | 3 |
| `/+5V_FUSED` | 2 |
| `/+5V_PROTECTED` | 11 |
| `/BUCK_SW` | 4 |
| `/BUCK_BST` | 1 |
| `+3V3` | 5 |

## What Was Rerouted

### Stage 1 Power Input

Completed:

- `J1 pad 2 -> F1 pad 1`
- `F1 pad 2 -> Q1 pad 3`
- `Q1 pad 2 -> C5/C2/D3/U1 protected-input cluster`
- `C2/C5/D3/U1` protected-input local copper

Intent used:

- `0.75 mm` on the main `+5V` input/protected trunk where footprint clearance allowed it
- local neck-downs to `0.50/0.40 mm` where the small Q1/U1 geometry required it
- no footprint removal
- no copper pour

### Stage 2 Buck / Local 3V3

Completed:

- local `+3V3` escape from `U1` using one via pair
- `L1 -> C7 -> C8` local output path
- compact local `SW/BST` area reroute attempts with multiple cleanup iterations

Current buck status:

- `+3V3` local output route exists
- `/BUCK_SW` local route exists
- `/BUCK_BST` local route exists
- one `SW/BST` crossing remains and blocks this from being called clean/complete

## Net Status

| Item | Status |
|---|---|
| `/+5V_IN` routed | `YES` |
| `/+5V_FUSED` routed | `YES` |
| `/+5V_PROTECTED` routed | `PARTIAL_LOCAL_ONLY` |
| `/+5V_PROTECTED` note | `TP1` branch remains unrouted |
| `BUCK_SW` routed compactly | `PARTIAL_NO_FINAL_PASS` |
| `BUCK_BST` routed compactly | `PARTIAL_NO_FINAL_PASS` |
| local `+3V3` output routed | `YES` |
| USB may begin | `NO` |
| Copper pour allowed | `NO` |

## Remaining Routing Blockers

1. One real routing defect remains in the buck cluster:
   - `SW/BST` crossing in the `U1/C6/L1` area.
2. `TP1` on `/+5V_PROTECTED` remains unrouted.
3. One 90-degree bend remains in the protected-input cluster angle audit.
4. Known unrelated DRC issue remains:
   - `12 x drill_out_of_range` on `U2 pad 41`.

## Output Files

Reports:

- `reports/ROUTING_STAGE_1_2_CLEANUP_DRC_REPORT.md`
- `reports/ROUTING_QUALITY_ANGLE_AUDIT.md`

Visual evidence:

- `_verification/pcb_visual/routing_stage_1_2_cleanup_top.svg`
- `_verification/pcb_visual/routing_stage_1_2_cleanup_bottom.svg`
- `_verification/pcb_visual/routing_stage_1_2_cleanup_3d_top.png`
- `_verification/pcb_visual/routing_stage_1_2_cleanup_3d_bottom.png`
- `_verification/pcb_visual/routing_stage_1_2_cleanup_power_input_closeup.svg`
- `_verification/pcb_visual/routing_stage_1_2_cleanup_buck_closeup.svg`

## Final Result

`STAGE_1_2_PARTIAL_NEEDS_MORE_REPAIR`

Reason:

- the crude first-pass routing was replaced with cleaner local input and output routing,
- but the buck cluster still has one `SW/BST` crossing and the pass cannot be called clean or USB-ready yet.
