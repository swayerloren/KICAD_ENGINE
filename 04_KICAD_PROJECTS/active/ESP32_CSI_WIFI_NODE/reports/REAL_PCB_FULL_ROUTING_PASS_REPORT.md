# REAL PCB Full Routing Pass Report

Status: `PARTIAL_SUCCESS_SAFE_NON_CRITICAL_SUBSET`

Generated: `2026-05-08T09:00:00-04:00`

Project: `ESP32_CSI_WIFI_NODE`

Target PCB: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`

## Preconditions

- Critical routing pass changed the live PCB hash from `1944B6DDFA7B233B8C231F5441D68B827FA3416B5C0B58A3004DE5C63C797FAC` to `D147FD1FFEF47F62B229561052B08C7432EFC549B7752DC7279ECE96E6C6B6A5`.
- Critical-pass DRC did not get worse: `0` violations, `49` unconnected items.
- Live non-critical routing proceeded from the real repaired board, not from stale gate markdown.

## Backup And Identity

- Backup path: `99_BACKUPS\pre_codex_edits\20260508_082440_ESP32_CSI_WIFI_NODE_real_pcb_full_routing_pass`
- PCB SHA256 before: `D147FD1FFEF47F62B229561052B08C7432EFC549B7752DC7279ECE96E6C6B6A5`
- PCB SHA256 after: `5E6486A2C188B68207C9FF4692618AE81BF322355ACAEE686146EF075330C2F6`
- PCB changed: `YES`

## Action Chosen

Chosen action: `SAFE_NON_CRITICAL_NET_SUBSET_ONLY`

Why:

- copied-board rehearsals showed that a broad non-critical routing pass reintroduced DRC errors
- the accepted copied-board subset held `0` violations and reduced unconnected items from `49` to `44`
- the live board only received the subset that passed copied-board rehearsal cleanly

## Live Edits Applied

Routed live:

- `/PLED`
- `/SLED`
- `/STATUS_LED`
- `/U0TXD`
- `unconnected-(J2-VBUS-PadA4)` pad-pair tie inside `J2`

Script evidence:

- `03_TOOLS\scripts\pcb_routing\esp32_csi_full_routing_pass_1.py`
- live script output:
  - `TRACKS_ADDED=13`
  - `VIAS_ADDED=4`
  - `/PLED`: `1` track
  - `/SLED`: `1` track
  - `/STATUS_LED`: `5` tracks, `2` vias
  - `/U0TXD`: `3` tracks
  - `unconnected-(J2-VBUS-PadA4)`: `3` tracks, `2` vias

## Deferred After Rehearsal

These nets were not applied live because copied-board rehearsals still produced crossings, shorts, or clearance conflicts:

- `/U0RXD`
- `/BOOT0`
- `/ESP_EN`
- `/+5V_PROTECTED` test-point spur at `TP1`
- `/CC1`
- `/CC2`
- `/SHIELD`
- `GND` cleanup beyond the existing accepted subset
- USB D+/D- related nets: `/DM_C`, `/DM_E`, `/DP_C`, `/DP_E`

## DRC Result

Primary evidence: `reports\REAL_PCB_FULL_ROUTING_PASS_DRC.json`

- Violations: `0`
- Unconnected items: `44`

## Board State After Save

- PCB timestamp after: `2026-05-08 08:59:46 -04:00`
- Footprints: `43`
- Tracks: `53`
- Vias: `29`
- Zones: `2`

## Remaining Connectivity Buckets

- `GND`: `17`
- `/ESP_EN`: `5`
- `/BOOT0`: `4`
- `/SHIELD`: `4`
- `/DM_C`: `3`
- `/DP_C`: `3`
- `/DM_E`: `2`
- `/DP_E`: `2`
- `/+5V_PROTECTED`: `1`
- `/CC1`: `1`
- `/CC2`: `1`
- `/U0RXD`: `1`

## Visual Evidence

- top SVG: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_full_routing_top.svg`
- top PNG: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_full_routing_top.png`
- bottom SVG: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_full_routing_bottom.svg`
- bottom PNG: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_full_routing_bottom.png`
- review packet: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\REAL_PCB_FULL_ROUTING_REVIEW.md`

## Stop Condition

Routing stopped after the accepted subset because additional non-critical nets still failed copied-board rehearsal against the current live `+3V3`, `GND`, USB, and service-row geometry.

Current next action:

- run a copied-board reroute study for `/BOOT0`, `/ESP_EN`, `/U0RXD`, `TP1 /+5V_PROTECTED`, `CC1/CC2`, and `SHIELD`
- only apply live geometry that preserves `0` DRC violations

## Final Review Readiness

Final PCB review may begin: `NO`

Reason:

- the board is still at `44` unconnected items and is not fully routed
- remaining live blockers are real board-state blockers, not stale markdown blockers
