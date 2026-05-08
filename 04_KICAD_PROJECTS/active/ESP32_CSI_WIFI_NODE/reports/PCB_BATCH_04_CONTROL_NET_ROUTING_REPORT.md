# PCB Batch 04 Control Net Routing Report

Status: `BATCH_04_APPLIED_PARTIAL_CONTROL_SUBSET`

Generated: `2026-05-08T12:06:57-04:00`

Project: `ESP32_CSI_WIFI_NODE`

Target PCB: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`

## Identity

- Backup path: `99_BACKUPS\pre_codex_edits\20260508_114318_ESP32_CSI_WIFI_NODE_batch_04_control_net_routing`
- PCB hash before: `22ED35E8FF9CC96F16014B66A2DCF669520D10A7A3C005ACEC3C68F29B9CF3F4`
- PCB hash after: `7BB955071DCABD9AA6A4B8F71F749AE14DF36F7E041F6C3FE657CDC17C62CF3C`
- PCB timestamp before: `2026-05-08 11:25:47 -04:00`
- PCB timestamp after: `2026-05-08 12:06:26 -04:00`
- PCB changed: `YES`

## Requested Scope

- Rehearse `/BOOT0`, `/ESP_EN`, and `/U0RXD` on copied boards first.
- Apply only the subset that preserves `0` DRC violations on the current board.
- Keep `/DP_C`, `/DP_E`, `/DM_C`, and `/DM_E` deferred in this batch.

## Rehearsal Outcome

- `/U0RXD`:
  - final copied-board candidate `x1_42p0_ymid_61p0_x2_55p0` held `0` violations and `20` unconnected items
  - exact proven path:
    - `38.750,27.820 -> 42.000,27.820 -> 42.000,61.000 -> 55.000,61.000 -> 55.000,64.000 -> 57.000,64.000`
- `/BOOT0`:
  - focused front-side search did not produce a `0`-violation candidate
  - best current search floor: `4` violations, `17` unconnected items
  - recurring blockers:
    - front-side crossing into the existing `/U0TXD` riser when trying to reach `TP4`
    - shorts and solder-mask bridges near the `R2` / left-button cluster
- `/ESP_EN`:
  - focused front-side cluster search did not produce a `0`-violation candidate
  - best current search floor: `19` violations, `16` unconnected items
  - recurring blockers:
    - `GND` shorts
    - `+3V3` shorts
    - repeated solder-mask bridges around the `R1` / `C1` / `SW2` cluster

## Live Copper Applied

### `/U0RXD`

- Routed on `F.Cu`
- Path:
  - `(38.750, 27.820) -> (42.000, 27.820)`
  - `(42.000, 27.820) -> (42.000, 61.000)`
  - `(42.000, 61.000) -> (55.000, 61.000)`
  - `(55.000, 61.000) -> (55.000, 64.000)`
  - `(55.000, 64.000) -> (57.000, 64.000)`
- Vias added: `0`
- Result:
  - `U2 pad 36` now connects directly to `TP7`

## Deferred Nets

- `/BOOT0`
- `/ESP_EN`
- `/DP_C`
- `/DP_E`
- `/DM_C`
- `/DM_E`

## Verification

- DRC result: `FAIL` by connectivity only
- DRC violations: `0`
- Unconnected items after: `20`
- Detectable unrouted nets after: `6`
- Live routing inventory after:
  - `67` tracks
  - `32` vias
  - `2` zones
- Live state evidence: `reports/LIVE_PROJECT_STATE.json`
- DRC evidence: `reports/PCB_BATCH_04_CONTROL_NET_ROUTING_DRC.json`

## Remaining Unrouted Nets

- `/BOOT0`
- `/DM_C`
- `/DM_E`
- `/DP_C`
- `/DP_E`
- `/ESP_EN`

## Unconnected Bucket Summary

- `/+5V_PROTECTED`: `1`
- `/BOOT0`: `4`
- `/DM_C`: `3`
- `/DM_E`: `2`
- `/DP_C`: `3`
- `/DP_E`: `2`
- `/ESP_EN`: `5`

## Visual Evidence

- 2D top SVG: `_verification/pcb_visual/pcb_batch_04_control_top.svg`
- 2D bottom SVG: `_verification/pcb_visual/pcb_batch_04_control_bottom.svg`
- 3D top PNG: `_verification/pcb_visual/pcb_batch_04_control_top.png`
- 3D bottom PNG: `_verification/pcb_visual/pcb_batch_04_control_bottom.png`
- Review packet: `_verification/pcb_visual/PCB_BATCH_04_CONTROL_NET_ROUTING_REVIEW.md`

## Final Decision

- Batch 05 USB data routing may begin: `NO`
- Exact next action:
  - continue copied-board search for `/BOOT0` and `/ESP_EN`
  - only after both control nets are proven clean on the current board should `/DP_C`, `/DP_E`, `/DM_C`, and `/DM_E` be considered
