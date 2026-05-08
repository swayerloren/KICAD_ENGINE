# Before After Hash Log

Status: `BASELINE_ONLY`

Generated: `2026-05-08T09:37:20-04:00`

## Baseline Entry

| Stage | PCB Timestamp | PCB SHA256 | Notes |
| --- | --- | --- | --- |
| `before_prep_snapshot` | `2026-05-08 08:59:46 -04:00` | `5E6486A2C188B68207C9FF4692618AE81BF322355ACAEE686146EF075330C2F6` | `live board copied into routing_work and backup created; no live edit in prep task` |

## Rollback Sources

- Backup: `99_BACKUPS\pre_codex_edits\20260508_091428_ESP32_CSI_WIFI_NODE_routing_work_prep`
- Working snapshot: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\routing_work\20260508_091428\ESP32_CSI_WIFI_NODE.kicad_pcb`

## Batch 01 Pre-Edit Entry

| Stage | PCB Timestamp | PCB SHA256 | Notes |
| --- | --- | --- | --- |
| `before_batch_01_drc_and_gnd_repair` | `2026-05-08 08:59:46 -04:00` | `5E6486A2C188B68207C9FF4692618AE81BF322355ACAEE686146EF075330C2F6` | `new backup required before live GND zone connection repair` |
| `after_batch_01_drc_and_gnd_repair` | `2026-05-08 09:51:38 -04:00` | `1AA99163F07EC867B98461F88990D059F46ACCBFB1CA4E91E33F9FD49B792489` | `live PCB saved after changing both GND zones from thermal to full pad connection` |
| `before_batch_02_power_routing_repair` | `2026-05-08 09:51:38 -04:00` | `1AA99163F07EC867B98461F88990D059F46ACCBFB1CA4E91E33F9FD49B792489` | `new backup required before ripping up and rerouting the live power path` |
| `after_batch_02_power_routing_repair` | `2026-05-08 10:33:51 -04:00` | `2349A4D2679F7ACAE1199FC302E42AAC69B84234CB12214031CFD63993CE172E` | `live PCB saved after rerouting /+5V_FUSED and repairing the local /+5V_PROTECTED regulator input feed` |
| `before_batch_03_usb_control_routing` | `2026-05-08 10:33:51 -04:00` | `2349A4D2679F7ACAE1199FC302E42AAC69B84234CB12214031CFD63993CE172E` | `fresh backup created before applying copied-board-proven USB/control copper to the live PCB` |
| `resume_batch_03_usb_control_routing` | `2026-05-08 10:33:51 -04:00` | `2349A4D2679F7ACAE1199FC302E42AAC69B84234CB12214031CFD63993CE172E` | `interrupted batch resumed from the proven copied-board delta; live PCB confirmed unchanged before resume apply` |
| `after_batch_03_usb_control_routing` | `2026-05-08 11:25:47 -04:00` | `22ED35E8FF9CC96F16014B66A2DCF669520D10A7A3C005ACEC3C68F29B9CF3F4` | `live PCB saved after routing /CC1, /CC2, and /SHIELD from the copied-board-proven USB-support candidate` |
| `before_batch_04_control_net_routing` | `2026-05-08 11:25:47 -04:00` | `22ED35E8FF9CC96F16014B66A2DCF669520D10A7A3C005ACEC3C68F29B9CF3F4` | `fresh backup created before copied-board rehearsal and any live apply for /BOOT0, /ESP_EN, and /U0RXD` |
| `after_batch_04_control_net_routing` | `2026-05-08 12:06:26 -04:00` | `7BB955071DCABD9AA6A4B8F71F749AE14DF36F7E041F6C3FE657CDC17C62CF3C` | `live PCB saved after applying the copied-board-proven /U0RXD route only; /BOOT0 and /ESP_EN remained deferred` |
| `before_final_connectivity_cleanup` | `2026-05-08 12:06:26 -04:00` | `7BB955071DCABD9AA6A4B8F71F749AE14DF36F7E041F6C3FE657CDC17C62CF3C` | `fresh backup created before final connectivity cleanup and copied-board local-cluster rehearsal` |
| `after_final_connectivity_cleanup` | `2026-05-08 12:31:56 -04:00` | `38DB921F4A13FFE0C52F2924E2C3E389D404AAF6D4BE1D8D26377D066ECBFC1D` | `live PCB saved after applying only the copied-board-proven BOOT0 and ESP_EN local cluster cleanup` |
| `before_final_trace_by_trace_audit` | `2026-05-08 12:31:56 -04:00` | `38DB921F4A13FFE0C52F2924E2C3E389D404AAF6D4BE1D8D26377D066ECBFC1D` | `fresh backup created before full trace-by-trace routing audit and any live trace-quality repair` |
| `after_final_trace_by_trace_audit` | `2026-05-08 12:56:52 -04:00` | `A90967ABC127674F7008562AAEE46744456F2421550E4B64AD71E91B5D3CF697` | `live PCB saved after the copied-board-proven /+5V_PROTECTED acute-dogleg cleanup` |
