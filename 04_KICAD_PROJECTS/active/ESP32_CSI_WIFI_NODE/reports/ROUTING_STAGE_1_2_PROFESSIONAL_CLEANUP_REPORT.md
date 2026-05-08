# Routing Stage 1/2 Professional Cleanup Report

Date: `2026-05-07`

Project: `ESP32_CSI_WIFI_NODE`

Target PCB: `kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

Final classification: `STAGE_1_2_PROFESSIONAL_ROUTING_READY_FOR_USB`

## Scope

This pass repaired only the Stage 1 and Stage 2 local power routing:

- `J1/F1/Q1/D3/C2/C5` input and protected-input routing
- `U1/C6/L1/C7/C8` buck regulator and local `+3V3` output routing

Explicitly not done in this pass:

- USB routing
- low-speed / control / LED / debug routing
- test-pad routing outside the local power-buck cluster
- copper pours
- fabrication/package export

## Pre-Edit Controls

| Check | Result |
|---|---|
| Prompt counter incremented | `PASS`: `3 -> 4` |
| Maintenance due | `NO` |
| Unsaved KiCad GUI state | `NO_EESCHEMA_WINDOW`; no blocking live GUI state was detected before edits |
| Backup created | `YES` |
| Backup path | `99_BACKUPS/pre_codex_edits/20260507_160629_ESP32_CSI_WIFI_NODE_stage1_2_professional_cleanup` |
| Baseline counts | `26` track segments, `2` vias, `0` zones |
| Baseline DRC | `13` violations, `65` unconnected items, schematic parity `0` |

## Cleanup Summary

Removed all existing routed copper on:

- `/+5V_IN`
- `/+5V_FUSED`
- `/+5V_PROTECTED`
- `/BUCK_SW`
- `/BUCK_BST`
- local `+3V3`

Counts:

- Track segments removed: `26`
- Vias removed: `2`
- Track segments added: `24`
- Vias added: `2`

Current board counts:

- Track segments: `24`
- Vias: `2`
- Zones: `0`

## Local Placement Corrections

No footprints were deleted.

Local cluster corrections applied:

- `Q1`: rotated from `0 deg` to `180 deg`
- `C2`: rotated from `90 deg` to `0 deg`
- `C5`: rotated from `90 deg` to `0 deg`
- `C6`: moved from `(27.000, 64.500)` to `(32.400, 68.725)` and rotated from `0 deg` to `90 deg`

Reason:

- `Q1/C2/C5` power-pad orientation was corrected to allow a cleaner protected-input trunk without routing through capacitor ground pads.
- `C6` was moved into the `U1/L1` gap so `BUCK_SW` and `BUCK_BST` could be routed compactly without the prior crossing.

## Net Status

| Item | Status |
|---|---|
| `/+5V_IN` routed cleanly | `YES` |
| `/+5V_FUSED` routed cleanly | `YES` |
| `/+5V_PROTECTED` routed cleanly | `YES`, for the Stage 1 local cluster |
| `/+5V_PROTECTED` note | `TP1` remains intentionally open because test-pad routing was explicitly deferred |
| `/BUCK_SW` short / compact | `YES` |
| `/BUCK_BST` short / compact | `YES` |
| `+3V3` local output routed cleanly | `YES` |
| Stage 3 USB routing may begin | `YES`, from the Stage 1/2 routing-quality perspective under the current routing-continuation exception |
| Copper pour allowed | `NO` |

## Routing Notes

### Stage 1 Power Input

Completed:

- `J1 pad 2 -> F1 pad 1`
- `F1 pad 2 -> Q1 pad 3`
- `Q1 pad 2 -> C5/C2 protected-input trunk`
- `protected-input branch -> D3`
- `protected-input branch -> U1 pads 2 and 3`

Routing intent used:

- `0.75 mm` on the main input/protected trunk where footprint geometry allowed it
- `0.50 mm` only at the small `U1` protected-input entry
- no harsh 90-degree corners
- no long U-shaped protected-input detours

### Stage 2 Buck / Local 3V3

Completed:

- `U1 SW -> C6 -> L1` compact local route
- `U1 BST -> C6` compact local route
- `U1 +3V3 -> via pair -> L1/C7/C8` local output route
- `C7 -> C8` local output distribution path

Routing intent used:

- `C6` relocated specifically to eliminate the prior `SW/BST` crossing
- `BUCK_SW` kept on a short direct top-side path
- `BUCK_BST` kept short and local to `U1/C6`
- the `+3V3` via pair was intentionally retained because a fully top-side entry into `L1 pad 2` was clearance-limited by the inductor pad geometry

## Verification Result

### DRC

Authoritative post-route DRC:

- `reports/ROUTING_STAGE_1_2_PROFESSIONAL_DRC_LIVE.rpt`

Result:

- `12` violations total
- all `12` are the pre-existing `drill_out_of_range` violations on `U2 pad 41`
- no new shorts
- no new clearance violations
- no `tracks_crossing` violations remain

### Schematic Parity

- `PASS`
- `0` schematic parity issues

### Remaining Unrouted Items

- `65` unconnected items remain overall
- these are outside the scope of this pass except for the intentionally deferred `TP1` test-pad branch on `/+5V_PROTECTED`
- USB, CC, shield, and low-speed/control/debug/test/LED nets remain open by instruction

## Visual Evidence

Top / bottom routed board renders:

- `_verification/pcb_visual/routing_stage_1_2_professional_top.png`
- `_verification/pcb_visual/routing_stage_1_2_professional_bottom.png`

Close-up review images:

- `_verification/pcb_visual/routing_stage_1_2_professional_input_power_closeup.png`
- `_verification/pcb_visual/routing_stage_1_2_professional_buck_closeup.png`
- `_verification/pcb_visual/routing_stage_1_2_professional_3v3_closeup.png`

## Final Result

`STAGE_1_2_PROFESSIONAL_ROUTING_READY_FOR_USB`

Reason:

- the Stage 1 input path and Stage 2 buck/local-output routing were rebuilt into a clean, DRC-safe local result,
- the prior `SW/BST` crossing is gone,
- no exact 90-degree bends remain in the routed Stage 1/2 nets,
- the only remaining DRC violations are the unrelated pre-existing `U2 pad 41` drill-rule items,
- and copper pours remain intentionally blocked.
