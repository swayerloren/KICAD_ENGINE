# PCB Batch 02 Power Routing Repair Report

Status: `BATCH_02_APPLIED`

Generated: `2026-05-08T10:34:28-04:00`

Project: `ESP32_CSI_WIFI_NODE`

Target PCB: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`

## Identity

- Backup path: `99_BACKUPS\pre_codex_edits\20260508_101143_ESP32_CSI_WIFI_NODE_batch_02_power_routing_repair`
- PCB hash before: `1AA99163F07EC867B98461F88990D059F46ACCBFB1CA4E91E33F9FD49B792489`
- PCB hash after: `2349A4D2679F7ACAE1199FC302E42AAC69B84234CB12214031CFD63993CE172E`
- PCB timestamp before: `2026-05-08 09:51:38 -04:00`
- PCB timestamp after: `2026-05-08 10:33:51 -04:00`
- PCB changed: `YES`

## Scope Chosen

- Accepted unchanged after copied-board proof:
  - `/+5V_IN`
  - `+3V3`
  - `/BUCK_SW`
  - `/BUCK_BST`
- Rerouted live:
  - `/+5V_FUSED`
  - local regulator-input portion of `/+5V_PROTECTED`

## Why This Scope Was Correct

- The copied-board rehearsal proved that straighter `/+5V_IN` candidates violate real clearance against `J1 pad 1 GND`.
- The copied-board rehearsal proved that flattening the left-side `/+5V_PROTECTED` branch violates real clearance against `C2 pad 1 GND`.
- The copied-board rehearsal also proved that the `F1 -> Q1` link and the `C2 -> U1` protected feed can be improved without introducing any new DRC violations.

## Live Copper Changes

### `/+5V_FUSED`

- Old path:
  - `(16.400, 77.500) -> (16.900, 78.000) -> (22.062, 78.000)`
- New path:
  - `(16.400, 77.500) -> (21.562, 77.500) -> (22.062, 78.000)`
- Effect:
  - cleaner power flow from `F1` into `Q1`
  - same `0.75 mm` width
  - one deliberate 45-degree entry instead of the old early stub

### `/+5V_PROTECTED`

- Preserved:
  - `D3 -> C2` branch because copied-board straightening attempts failed clearance
  - `Q1/C5` trunk because it is already compact and DRC-clean
- Repaired:
  - old local feed: `(21.950, 69.500) -> (26.913, 69.500)` at `0.50 mm`, then diagonal and vertical into `U1`
  - new local feed: `(21.950, 69.500) -> (26.400, 69.500)` at `0.75 mm`
  - new neckdown: `(26.400, 69.500) -> (27.863, 69.500) -> (27.863, 70.450)` at `0.50 mm`
- Effect:
  - holds width longer into the regulator input
  - removes the diagonal dogleg into `U1`
  - keeps the left-side clearance-safe geometry intact

## Verification

- DRC result: `FAIL` because connectivity is incomplete, but geometry is clean
- DRC violations: `0`
- DRC unconnected items: `27`
- Detectable unrouted nets remaining: `10`
- Remaining unrouted nets:
  - `/BOOT0`
  - `/CC1`
  - `/CC2`
  - `/DM_C`
  - `/DM_E`
  - `/DP_C`
  - `/DP_E`
  - `/ESP_EN`
  - `/SHIELD`
  - `/U0RXD`
- Live-state evidence: `reports/LIVE_PROJECT_STATE.json`
- DRC evidence: `reports/PCB_BATCH_02_POWER_ROUTING_REPAIR_DRC.json`

## Visual Evidence

- Top SVG: `_verification/pcb_visual/pcb_batch_02_top.svg`
- Bottom SVG: `_verification/pcb_visual/pcb_batch_02_bottom.svg`
- Top PNG: `_verification/pcb_visual/pcb_batch_02_top.png`
- Bottom PNG: `_verification/pcb_visual/pcb_batch_02_bottom.png`

## Visual Result

- Top-side review shows:
  - a cleaner `F1 -> Q1` fused link
  - a wider, straighter protected feed into `U1`
  - no obvious new crowding in the `J1/F1/Q1/C5/C2/U1/L1` power cluster
- Bottom-side review shows no unexpected collateral changes outside the already-routed bottom copper.

## Final Decision

- USB/control routing may begin: `YES_FOR_TARGETED_NEXT_PASS_ONLY`
- Exact next routing batch:
  - `/BOOT0`
  - `/ESP_EN`
  - `/U0RXD`
  - then USB support nets `/CC1`, `/CC2`, and `/SHIELD`
- Still blocked from final review:
  - `27` unconnected items remain
  - `10` detectable unrouted nets remain
