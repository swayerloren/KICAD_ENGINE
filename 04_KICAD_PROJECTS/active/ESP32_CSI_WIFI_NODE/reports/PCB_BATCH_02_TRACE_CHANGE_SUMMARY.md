# PCB Batch 02 Trace Change Summary

Status: `LIVE_APPLY_COMPLETE`

Generated: `2026-05-08T10:15:29-04:00`

Project: `ESP32_CSI_WIFI_NODE`

Target PCB: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`

## Batch Identity

- Backup path: `99_BACKUPS\pre_codex_edits\20260508_101143_ESP32_CSI_WIFI_NODE_batch_02_power_routing_repair`
- PCB hash before: `1AA99163F07EC867B98461F88990D059F46ACCBFB1CA4E91E33F9FD49B792489`
- PCB timestamp before: `2026-05-08 09:51:38 -04:00`
- Pre-edit DRC baseline: `0` violations, `27` unconnected items

## Before State

### `+3V3`

- Scope classification: `ACCEPTED_FOR_THIS_BATCH_UNLESS_REHEARSAL_PROVES_A_BETTER_LOCAL_FIX`
- Existing state:
  - distributed rail with both `F.Cu` and `B.Cu` segments plus multiple vias
  - local regulator output leaves `U1 pad 1` by a short `F.Cu` diagonal to a via at `(26.113, 66.800)`
  - long `B.Cu` trunk runs through the board power spine before returning to `F.Cu` near `L1/C7/C8`
- Key existing geometry:
  - `F.Cu` `(27.863, 68.550) -> (26.113, 66.800)` width `0.50 mm`
  - `B.Cu` `(26.113, 66.800) -> (38.475, 66.550)` width `0.50 mm`
  - `F.Cu` `(38.475, 66.550) -> (38.475, 69.500)` width `0.50 mm`
  - `F.Cu` `(42.000, 63.025) -> (48.000, 63.025)` width `0.50 mm`
- Existing vias: `(26.500, 43.225)`, `(13.825, 64.000)`, `(13.825, 53.000)`, `(26.113, 66.800)`, `(38.475, 69.500)`, `(38.475, 66.550)`, `(39.825, 58.000)`, `(21.500, 43.050)`, `(57.000, 48.000)`, `(21.250, 24.010)`
- Reason not selected for immediate rip-up:
  - rail is already electrically functional
  - it is no longer the highest-risk geometry blocker
  - ripping it up would destabilize a broad fanout beyond the requested power/protection cleanup pass

### `/+5V_IN`

- Scope classification: `SELECTED_FOR_REROUTE`
- Existing state:
  - three-segment `F.Cu` feed from `J1 pad 2` to `F1 pad 1`
  - visible left-right jog that consumes corridor space with no routing benefit
- Existing geometry:
  - `(14.000, 86.800) -> (11.800, 84.600)` width `0.75 mm`
  - `(11.800, 84.600) -> (11.800, 79.300)` width `0.75 mm`
  - `(11.800, 79.300) -> (13.600, 77.500)` width `0.75 mm`
- Old path summary: `J1 pad 2 doglegs left, runs vertically, then doglegs back right into F1`
- Planned new path summary: `single vertical drop from J1 with one short 45-degree entry into F1`

### `/+5V_FUSED`

- Scope classification: `SELECTED_FOR_REROUTE`
- Existing state:
  - short `F.Cu` tie between `F1 pad 2` and `Q1 pad 3`
  - electrically acceptable, but the batch will normalize it to the same clean 45-degree style as the rest of the repaired path
- Existing geometry:
  - `(16.400, 77.500) -> (16.900, 78.000)` width `0.75 mm`
  - `(16.900, 78.000) -> (22.062, 78.000)` width `0.75 mm`
- Old path summary: `very short 45-degree stub then long horizontal run into Q1`
- Planned new path summary: `long horizontal run from F1 followed by one 45-degree entry into Q1`

### `/+5V_PROTECTED`

- Scope classification: `SELECTED_FOR_REROUTE`
- Existing state:
  - main protected rail is present on `F.Cu`
  - topology is workable, but the branch from `D3` into the `C2/U1` node includes an awkward detour and the regulator input leg narrows early
- Existing geometry:
  - `(14.000, 67.500) -> (17.500, 71.000)` width `0.75 mm`
  - `(17.500, 71.000) -> (21.500, 71.000)` width `0.75 mm`
  - `(21.500, 71.000) -> (22.475, 70.025)` width `0.75 mm`
  - `(22.475, 70.025) -> (22.475, 74.000)` width `0.75 mm`
  - `(22.475, 74.000) -> (23.938, 75.463)` width `0.75 mm`
  - `(23.938, 75.463) -> (23.938, 77.050)` width `0.75 mm`
  - `(22.475, 70.025) -> (21.950, 69.500)` width `0.75 mm`
  - `(21.950, 69.500) -> (26.913, 69.500)` width `0.50 mm`
  - `(26.913, 69.500) -> (27.863, 70.450)` width `0.50 mm`
  - `(27.863, 70.450) -> (27.863, 69.500)` width `0.50 mm`
- Old path summary: `Q1 -> C5 trunk is acceptable, but the D3 branch detours high before dropping into C2/U1 and the regulator input narrows too soon`
- Planned new path summary:
  - `D3 -> C2: short 45-degree rise into a direct horizontal protected-rail spine`
  - `C2 -> Q1/C5: preserve the compact vertical/45-degree trunk`
  - `C2 -> U1 pads 2/3: keep the wider rail as long as practical, then neck down only at the regulator pins`

### `/BUCK_SW`

- Scope classification: `ACCEPTED_NO_CHANGE`
- Existing geometry:
  - `(30.137, 69.500) -> (32.400, 69.500)` width `0.50 mm`
  - `(32.400, 69.500) -> (35.525, 69.500)` width `0.50 mm`
- Accepted reason:
  - already short, local, straight, and compact between `U1`, `C6`, and `L1`

### `/BUCK_BST`

- Scope classification: `ACCEPTED_NO_CHANGE`
- Existing geometry:
  - `(30.137, 68.550) -> (30.737, 67.950)` width `0.25 mm`
  - `(30.737, 67.950) -> (32.400, 67.950)` width `0.25 mm`
- Accepted reason:
  - already short, local, and appropriate for the bootstrap capacitor link

## Edit Intent

- Rip up and reroute only:
  - `/+5V_IN`
  - `/+5V_FUSED`
  - `/+5V_PROTECTED`
- Preserve without geometry changes unless rehearsal shows a clearly superior local repair:
  - `+3V3`
  - `/BUCK_SW`
  - `/BUCK_BST`

## Update Notes

- This file was created before any live copper edit in batch 02.

## Rehearsal Findings

- Rejected rehearsal 1:
  - direct `/+5V_IN` simplification at `x=14.000` created a real short and solder-mask bridge against `J1 pad 1 GND`
  - direct `/+5V_PROTECTED` flattening through the `C2` centerline created a real short and solder-mask bridge against `C2 pad 1 GND`
- Rejected rehearsal 2:
  - shifted `/+5V_IN` corridor at `x=12.200` still violated `J1` GND clearance by `0.125 mm`
  - lifted `/+5V_PROTECTED` branch at `y=70.000` still shorted against `C2 pad 1 GND`
- Accepted rehearsal:
  - keep `/+5V_IN` unchanged because the current offset is justified by real `J1` GND clearance
  - keep the `D3 -> C2` protected branch geometry because the current shape is justified by real `C2` GND clearance
  - reroute `/+5V_FUSED` and only the local `C2 -> U1` protected-rail feed

## After State

### `/+5V_IN`

- Result: `ACCEPTED_NO_CHANGE`
- Final geometry remains:
  - `(14.000, 86.800) -> (11.800, 84.600)` width `0.75 mm`
  - `(11.800, 84.600) -> (11.800, 79.300)` width `0.75 mm`
  - `(11.800, 79.300) -> (13.600, 77.500)` width `0.75 mm`
- Accepted reason:
  - copied-board rehearsal proved that straighter variants collide with `J1 pad 1 GND` clearance

### `/+5V_FUSED`

- Result: `REROUTED`
- Final geometry:
  - `(16.400, 77.500) -> (21.562, 77.500)` width `0.75 mm`
  - `(21.562, 77.500) -> (22.062, 78.000)` width `0.75 mm`
- Change summary:
  - old: short 45-degree exit from `F1`, then long horizontal run
  - new: long horizontal run from `F1`, then one clean 45-degree entry into `Q1`

### `/+5V_PROTECTED`

- Result: `PARTIAL_LOCAL_REROUTE`
- Final geometry:
  - preserved left branch: `(14.000, 67.500) -> (17.500, 71.000) -> (21.500, 71.000) -> (22.475, 70.025)` width `0.75 mm`
  - preserved Q1/C5 trunk: `(22.475, 70.025) -> (22.475, 74.000) -> (23.938, 75.463) -> (23.938, 77.050)` width `0.75 mm`
  - preserved node entry: `(22.475, 70.025) -> (21.950, 69.500)` width `0.75 mm`
  - repaired regulator feed: `(21.950, 69.500) -> (26.400, 69.500)` width `0.75 mm`
  - neckdown into `U1`: `(26.400, 69.500) -> (27.863, 69.500) -> (27.863, 70.450)` width `0.50 mm`
- Change summary:
  - old local feed narrowed too early and used a diagonal dogleg into `U1`
  - new local feed stays wide longer and enters `U1` orthogonally with a short neckdown only at the pins

### `+3V3`, `/BUCK_SW`, `/BUCK_BST`

- Result: `ACCEPTED_NO_CHANGE`
- Why:
  - copied-board rehearsal did not prove a safer or cleaner local improvement without disturbing working geometry outside the requested power/protection scope

## Batch Outcome

- PCB hash before: `1AA99163F07EC867B98461F88990D059F46ACCBFB1CA4E91E33F9FD49B792489`
- PCB hash after: `2349A4D2679F7ACAE1199FC302E42AAC69B84234CB12214031CFD63993CE172E`
- Live DRC after apply: `0` violations, `27` unconnected items
- Detectable unrouted nets after apply: `10`
- USB/control routing may begin next: `YES_FOR_TARGETED_NEXT_PASS_ONLY`
