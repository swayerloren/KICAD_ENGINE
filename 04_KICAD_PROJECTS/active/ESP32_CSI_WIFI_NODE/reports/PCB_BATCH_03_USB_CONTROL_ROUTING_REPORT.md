# PCB Batch 03 USB Control Routing Report

Status: `BATCH_03_APPLIED`

Generated: `2026-05-08T11:26:44-04:00`

Project: `ESP32_CSI_WIFI_NODE`

Target PCB: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`

## Identity

- Backup path: `99_BACKUPS\pre_codex_edits\20260508_112350_ESP32_CSI_WIFI_NODE_batch_03_usb_control_routing_resume`
- PCB hash before: `2349A4D2679F7ACAE1199FC302E42AAC69B84234CB12214031CFD63993CE172E`
- PCB hash after: `22ED35E8FF9CC96F16014B66A2DCF669520D10A7A3C005ACEC3C68F29B9CF3F4`
- PCB timestamp before: `2026-05-08 10:33:51 -04:00`
- PCB timestamp after: `2026-05-08 11:25:47 -04:00`
- PCB changed: `YES`

## Resume Scope

- Resumed the interrupted `PCB_BATCH_03_USB_CONTROL_ROUTING` pass from the existing routing-work packet.
- Inspected and repaired `03_TOOLS\scripts\pcb_routing\esp32_csi_usb_control_batch_03.py` before live use.
- Applied only the copied-board-proven USB-support subset:
  - `/CC1`
  - `/CC2`
  - `/SHIELD`
- Deferred the remaining USB/control nets because no copied-board rehearsal for them stayed at `0` DRC violations on the current board.

## Script Repair

- Fixed unsafe via-summary logic in `esp32_csi_usb_control_batch_03.py`.
- The prior version called KiCad's via-width API without a layer argument during summary extraction.
- The repaired version uses a safe layer-aware helper so the script exits cleanly and emits deterministic JSON after apply.

## Live Copper Applied

### `/CC1`

- Routed on `F.Cu`
- Path:
  - `(37.750, 87.645) -> (37.750, 84.800) -> (32.325, 81.500)`
- Vias added: `0`
- Result:
  - `J2 A5` now connects directly to `R6 pad 2`

### `/CC2`

- Routed on `F.Cu`
- Path:
  - `(40.750, 87.645) -> (40.750, 84.000) -> (46.825, 84.000) -> (46.825, 81.500)`
- Vias added: `0`
- Result:
  - `J2 B5` now connects directly to `R7 pad 2`

### `/SHIELD`

- Routed on `B.Cu`
- Paths:
  - `(34.680, 88.220) -> (34.680, 92.400) -> (43.320, 92.400) -> (43.320, 88.220)`
  - `(43.320, 88.220) -> (51.825, 78.000)`
- Vias added:
  - `(34.680, 88.220)`
  - `(43.320, 88.220)`
  - `(51.825, 78.000)`
- Result:
  - `J2` shell pads now tie back to `R5 pad 2` through the bottom-side shield run

## Verification

- DRC result: `FAIL` by connectivity only
- DRC violations: `0`
- Unconnected items after: `21`
- Detectable unrouted nets after: `7`
- Live routing inventory after:
  - `62` tracks
  - `32` vias
  - `2` zones
- Live state evidence: `reports/LIVE_PROJECT_STATE.json`
- DRC evidence: `reports/PCB_BATCH_03_USB_CONTROL_ROUTING_DRC_FINAL.json`

## Remaining Unrouted Nets

- `/BOOT0`
- `/DM_C`
- `/DM_E`
- `/DP_C`
- `/DP_E`
- `/ESP_EN`
- `/U0RXD`

## Unconnected Bucket Summary

- `/+5V_PROTECTED`: `1`
- `/BOOT0`: `4`
- `/DM_C`: `3`
- `/DM_E`: `2`
- `/DP_C`: `3`
- `/DP_E`: `2`
- `/ESP_EN`: `5`
- `/U0RXD`: `1`

## Deferred Nets

- `/BOOT0`
- `/ESP_EN`
- `/U0RXD`
- `/DP_C`
- `/DP_E`
- `/DM_C`
- `/DM_E`

## Visual Evidence

- 2D top SVG: `_verification/pcb_visual/pcb_batch_03_usb_control_top.svg`
- 2D bottom SVG: `_verification/pcb_visual/pcb_batch_03_usb_control_bottom.svg`
- 3D top PNG: `_verification/pcb_visual/pcb_batch_03_usb_control_top.png`
- 3D bottom PNG: `_verification/pcb_visual/pcb_batch_03_usb_control_bottom.png`
- Review packet: `_verification/pcb_visual/PCB_BATCH_03_USB_CONTROL_ROUTING_REVIEW.md`

## Final Decision

- Batch 04 may begin: `YES_FOR_TARGETED_REHEARSAL_AND_LIVE_APPLY_ONLY`
- Exact next action:
  - rehearse `/BOOT0`, `/ESP_EN`, and `/U0RXD` on copied boards first
  - only if each stays at `0` DRC violations, carry those nets into the live board
  - continue to hold `/DP_C`, `/DP_E`, `/DM_C`, and `/DM_E` until the connector/U3/series-resistor geometry is proven clean on the current board
