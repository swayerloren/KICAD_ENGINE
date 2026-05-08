# PCB Final Connectivity Cleanup Report

Status: `SAFE_LOCAL_CLEANUP_APPLIED_PARTIAL`

Generated: `2026-05-08T12:34:25-04:00`

Project: `ESP32_CSI_WIFI_NODE`

Target PCB: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`

## Identity

- Backup path: `99_BACKUPS\pre_codex_edits\20260508_122513_ESP32_CSI_WIFI_NODE_final_connectivity_cleanup`
- PCB hash before: `7BB955071DCABD9AA6A4B8F71F749AE14DF36F7E041F6C3FE657CDC17C62CF3C`
- PCB hash after: `38DB921F4A13FFE0C52F2924E2C3E389D404AAF6D4BE1D8D26377D066ECBFC1D`
- PCB timestamp before: `2026-05-08 12:06:26 -04:00`
- PCB timestamp after: `2026-05-08 12:31:56 -04:00`
- PCB changed: `YES`

## Before Cleanup

- Fresh DRC before edit: `0` violations, `20` unconnected items
- Remaining nets before edit:
  - `/+5V_PROTECTED`
  - `/BOOT0`
  - `/ESP_EN`
  - `/DM_C`
  - `/DM_E`
  - `/DP_C`
  - `/DP_E`

## Copied-Board Rehearsal

### Accepted candidate

- Trial board: `routing_work\20260508_091428\final_connectivity_cleanup_trials\20260508_122929\candidate_control_local.kicad_pcb`
- Rule context fix:
  - copied-board DRC initially showed false `drill_out_of_range` failures until the live `.kicad_pro` was copied beside the trial board
  - authoritative rerun with the live project rule file held `0` violations and `17` unconnected items
- Accepted local routes:
  - `/BOOT0`: `12.175,64.000 -> 12.175,68.000 -> 5.150,68.000 -> 5.150,66.625`
  - `/ESP_EN`: `12.175,53.000 -> 13.775,54.600 -> 13.775,58.500 -> 5.150,58.500 -> 5.150,56.625`

### Rejected candidate

- Trial board: `routing_work\20260508_091428\final_connectivity_cleanup_trials\20260508_122929\candidate_control_usb_local.kicad_pcb`
- Rejected because the rerun with the correct project rule file still produced:
  - `4` real violations
  - `/DM_C` short to `/DM_E`
  - `/DP_C` short to `/DM_C`
  - `2` matching solder-mask bridges

## Live Copper Applied

- `/BOOT0`
  - tied `R2 pad 1` into the upper `SW1 pad 1`
  - left the lower duplicate `SW1 pad 1` open for now
- `/ESP_EN`
  - tied `R1 pad 1` into `C1 pad 2`
  - tied that local control cluster into the upper `SW2 pad 1`
  - left the lower duplicate `SW2 pad 1` open for now

## Verification

- Post-edit DRC: `0` violations, `17` unconnected items
- DRC evidence:
  - precheck: `reports/PCB_FINAL_CONNECTIVITY_CLEANUP_DRC_PRECHECK.json`
  - post-edit: `reports/PCB_FINAL_CONNECTIVITY_CLEANUP_DRC_POST.json`
- Live inventory after cleanup:
  - `74` tracks
  - `32` vias
  - `2` zones

## Result

- Unconnected before: `20`
- Unconnected after: `17`
- Improvement: `3` fewer unconnected items with no DRC regression

## Remaining Intentional Or Expected Open Items

- `SW1 pad 1` duplicate-to-duplicate open
- `SW2 pad 1` duplicate-to-duplicate open

These are currently classified as expected duplicate tactile-switch pads, not must-fix copper gaps.

## Remaining Blockers

- Real must-route items still remain on:
  - `/+5V_PROTECTED`
  - `/BOOT0`
  - `/ESP_EN`
  - `/DM_C`
  - `/DM_E`
  - `/DP_C`
  - `/DP_E`
- The unresolved items are routing work, not stale-report artifacts.
- The rejected USB-local rehearsal proves the current board still needs copied-board planning before any further USB cleanup is applied live.

## Visual Evidence

- Top render: `_verification/pcb_visual/pcb_final_connectivity_cleanup_top.png`
- Bottom render: `_verification/pcb_visual/pcb_final_connectivity_cleanup_bottom.png`
- Review packet: `_verification/pcb_visual/PCB_FINAL_CONNECTIVITY_CLEANUP_REVIEW.md`

## Final Decision

- Final trace audit may begin: `NO`
- Exact next action:
  - continue copied-board planning for the unresolved `/BOOT0` and `/ESP_EN` U2/test-pad spine routes
  - only after those hold `0` DRC violations on the current board should `/DP_C`, `/DP_E`, `/DM_C`, and `/DM_E` be advanced live
