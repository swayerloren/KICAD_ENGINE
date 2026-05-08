# PCB Batch 05 USB Data Routing Report

Status: `BATCH_05_FAILED_FILE_UNCHANGED`

Generated: `2026-05-08T12:13:00-04:00`

Project: `ESP32_CSI_WIFI_NODE`

Target PCB: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`

## Identity

- Backup path: `NO_NEW_BACKUP_CREATED_BLOCKED_BEFORE_EDIT`
- PCB hash before: `7BB955071DCABD9AA6A4B8F71F749AE14DF36F7E041F6C3FE657CDC17C62CF3C`
- PCB hash after: `7BB955071DCABD9AA6A4B8F71F749AE14DF36F7E041F6C3FE657CDC17C62CF3C`
- PCB timestamp before: `2026-05-08 12:06:26 -04:00`
- PCB timestamp after: `2026-05-08 12:06:26 -04:00`
- PCB changed: `NO`

## Stop Decision

- Batch 05 did not start on the live board.
- This stop was based on current live evidence, not stale phase markdown.

## Live Preconditions

- Current live DRC: `0` violations, `20` unconnected items
- Current detectable unrouted nets: `6`
  - `/BOOT0`
  - `/ESP_EN`
  - `/DP_C`
  - `/DP_E`
  - `/DM_C`
  - `/DM_E`
- Current live routing inventory:
  - `67` tracks
  - `32` vias
  - `2` zones

## Exact Stop Reason

- `PCB_BATCH_04_CONTROL_NET_ROUTING_REPORT.md` explicitly records:
  - `Batch 05 USB data routing may begin: NO`
  - exact next action: continue copied-board search for `/BOOT0` and `/ESP_EN`, and only after both control nets are proven clean on the current board should `/DP_C`, `/DP_E`, `/DM_C`, and `/DM_E` be considered
- `LIVE_PROJECT_STATE.json` still records:
  - classification `PCB_EXISTS_PARTIAL_ROUTING_EXISTS_NEEDS_AUDIT`
  - `routing_plan_may_continue: false`
  - unrouted nets still include `/BOOT0` and `/ESP_EN`
- Routing stop-condition rule applies:
  - do not keep routing once the current pass is blocked by required re-plan conditions

## Affected Nets

- blocked control nets:
  - `/BOOT0`
  - `/ESP_EN`
- deferred USB data nets:
  - `/DP_C`
  - `/DP_E`
  - `/DM_C`
  - `/DM_E`

## Why USB Did Not Proceed

- The board is not at a state where USB D+/D- should be layered on top of unresolved control-net routing.
- The last accepted live decision for this project is that `/BOOT0` and `/ESP_EN` must be solved first on copied boards.
- Starting USB data routing now would skip the current live reroute requirement and violate the project’s routing stop logic.

## Verification

- Live PCB exists: `YES`
- Live board hash matches the current post-Batch-04 board: `YES`
- DRC violations introduced in this session: `NO`
- USB data routing attempted live in this session: `NO`

## Final Decision

- Nets routed live: `NONE`
- Vias added live: `0`
- USB routing quality notes:
  - not evaluated on new geometry because no USB data route was allowed to start
  - prior USB-support copper `/CC1`, `/CC2`, and `/SHIELD` remains intact
- Full final routing audit may begin: `NO`
- Exact next action:
  - continue copied-board search for `/BOOT0` and `/ESP_EN`
  - once both control nets hold `0` DRC violations on the current board, revisit USB data routing
