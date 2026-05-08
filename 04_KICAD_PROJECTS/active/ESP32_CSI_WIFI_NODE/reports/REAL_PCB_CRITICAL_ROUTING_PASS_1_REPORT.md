# REAL PCB Critical Routing Pass 1 Report

Status: `PARTIAL_SUCCESS_SAFE_POWER_SUBPASS`

Generated: `2026-05-08T08:14:38-04:00`

Project: `ESP32_CSI_WIFI_NODE`

Target PCB: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pcb`

## Scope

This was a real live PCB edit pass. The board file changed.

The pass started from the live repaired board and used copied-board DRC rehearsal before touching the production file.

## Backup And Identity

- Backup path: `99_BACKUPS\pre_codex_edits\20260508_071914_ESP32_CSI_WIFI_NODE_real_pcb_critical_routing_pass_1`
- PCB timestamp before: `2026-05-08 07:05:22 -04:00`
- PCB timestamp after: `2026-05-08 08:14:38 -04:00`
- PCB SHA256 before: `1944B6DDFA7B233B8C231F5441D68B827FA3416B5C0B58A3004DE5C63C797FAC`
- PCB SHA256 after: `D147FD1FFEF47F62B229561052B08C7432EFC549B7752DC7279ECE96E6C6B6A5`
- PCB changed: `YES`

## Action Chosen

Chosen live action: `SAFE_CRITICAL_POWER_ROUTING_SUBPASS`

Why this action was chosen:

- copied-board rehearsals proved that a broad live `BOOT0` and `ESP_EN` routing pass created real DRC crossings and shorts on the current placement
- copied-board rehearsal version `trial_apply_v5` proved that a narrower pass could improve the actual board while holding live DRC at `0` violations
- the safe subset was:
  - complete the live `+3V3` rail connectivity
  - add selective `GND` stitching vias that refill into the existing zones without creating new DRC violations
  - defer `/+5V_PROTECTED` test-point spur, `/BOOT0`, and `/ESP_EN` because those branches did not pass copied-board stop-condition review

## Live Edits Applied

### Routed Or Added

- `+3V3`
  - completed the bottom-side trunk from the existing power area into the upper/right service area
  - connected the `R3` branch
  - connected `U2 pad 2` into the `C3`/`C4` decoupling cluster
  - connected the `R1`/`R2` pull-up cluster into the same rail
  - connected `TP3`
- `GND`
  - added `15` new vias
  - purpose: stitch selected top-side GND pads and open copper regions into the existing two-layer GND zone strategy without breaking DRC

### Deferred On Purpose

- `/+5V_PROTECTED`
  - core protected power path remains accepted from earlier work
  - only the `TP1` spur remains unconnected
  - copied-board rehearsal showed that the clean-looking TP1 spur candidates collided with the newly completed `+3V3` corridor
- `/BOOT0`
  - no live route added in this pass
  - copied-board rehearsal with real geometry created DRC crossings/shorts against the `+3V3` corridor
- `/ESP_EN`
  - no live route added in this pass
  - copied-board rehearsal with real geometry created DRC crossings/shorts against the `+3V3` corridor
- USB D+/D-
  - not touched in this pass

## DRC Result

Evidence file: `reports\REAL_PCB_CRITICAL_ROUTING_PASS_1_DRC.json`

- Violations: `0`
- Unconnected items: `49`

Critical net effect from live DRC:

- `+3V3`: `0` unconnected items after this pass
- `GND`: `17` unconnected items remain, down from `26`
- `/+5V_PROTECTED`: `1` unconnected item remains
- `/BOOT0`: `4` unconnected items remain
- `/ESP_EN`: `5` unconnected items remain

## Board State After Save

- Footprints: `43`
- Tracks: `40`
- Vias: `25`
- Zones: `2`

## Copied-Board Rehearsal Evidence

Rehearsal root: `99_BACKUPS\pre_codex_edits\20260508_071914_ESP32_CSI_WIFI_NODE_real_pcb_critical_routing_pass_1`

Key rehearsal outcomes:

- `trial_apply`: `92` violations, `29` unconnected items
- `trial_apply_v2`: `23` violations, `34` unconnected items
- `trial_apply_v3`: `2` violations, `48` unconnected items
- `trial_apply_v4`: `3` violations, `48` unconnected items
- `trial_apply_v5`: `0` violations, `49` unconnected items

Only `trial_apply_v5` was accepted for the live board.

## Visual Evidence

- full top SVG: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_critical_routing_pass_1_top.svg`
- full top PNG: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_critical_routing_pass_1_top.png`
- full bottom SVG: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_critical_routing_pass_1_bottom.svg`
- full bottom PNG: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\real_pcb_critical_routing_pass_1_bottom.png`
- close-up review: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\REAL_PCB_CRITICAL_ROUTING_PASS_1_REVIEW.md`

## Stop Condition

Routing stopped after the safe power/GND subset because a broader live pass would have violated:

- `a route can only be finished with awkward geometry`
- `trace-by-trace review becomes incomplete`
- `routing quality is visually crude even if DRC does not flag it`

Source rule: `14_LAYOUT_AUTOMATION\REAL_PROJECT_ROUTING_STOP_CONDITIONS.md`

## Exact Next Action

Do not route all remaining nets yet.

Next correct action:

1. perform a dedicated copied-board reroute study for `/BOOT0` and `/ESP_EN`
2. choose clean non-crossing control-net corridors that do not conflict with the now-complete `+3V3` path
3. only then bring the accepted control-net geometry onto the live board
