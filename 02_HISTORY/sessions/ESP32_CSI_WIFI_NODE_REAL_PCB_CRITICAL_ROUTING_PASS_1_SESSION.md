# ESP32_CSI_WIFI_NODE Real PCB Critical Routing Pass 1 Session

Date: `2026-05-08`

## Task

Route critical nets on the real `ESP32_CSI_WIFI_NODE.kicad_pcb` only after the repair pass, while keeping the board DRC-safe.

## What Happened

1. confirmed the live board existed and matched the repaired pre-pass hash `1944B6DDFA7B233B8C231F5441D68B827FA3416B5C0B58A3004DE5C63C797FAC`
2. confirmed the pre-edit backup folder existed: `99_BACKUPS\pre_codex_edits\20260508_071914_ESP32_CSI_WIFI_NODE_real_pcb_critical_routing_pass_1`
3. rehearsed multiple routing candidates on copied boards under the backup folder
4. rejected copied-board candidates that produced real DRC crossings/shorts on `/BOOT0`, `/ESP_EN`, and the `TP1` spur
5. accepted a smaller live pass that completed `+3V3` and improved `GND` while preserving `0` DRC violations
6. applied the accepted candidate to the real `.kicad_pcb`
7. reran live DRC and exported fresh board visuals

## Final Live Result

- PCB hash after live save: `D147FD1FFEF47F62B229561052B08C7432EFC549B7752DC7279ECE96E6C6B6A5`
- DRC violations: `0`
- Unconnected items: `49`
- `+3V3` unconnected items: `0`
- `GND` unconnected items: `17`

## Deferred Work

- `/BOOT0`
- `/ESP_EN`
- `/+5V_PROTECTED` `TP1` branch

Reason:

- copied-board rehearsals with those branches created real DRC crossings or shorts on the current live geometry

## Evidence

- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\REAL_PCB_CRITICAL_ROUTING_PASS_1_REPORT.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\REAL_PCB_CRITICAL_TRACE_AUDIT.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\REAL_PCB_CRITICAL_ROUTING_PASS_1_DRC.json`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\pcb_visual\REAL_PCB_CRITICAL_ROUTING_PASS_1_REVIEW.md`
