# Claim Evidence Matrix: PCB Batch 03 USB Control Routing

| Claim | Evidence |
| --- | --- |
| The live PCB changed in batch 03 | `kicad/ESP32_CSI_WIFI_NODE.kicad_pcb` hash `2349A4... -> 22ED35...`; `reports/PCB_BATCH_03_USB_CONTROL_ROUTING_REPORT.md` |
| `/CC1`, `/CC2`, and `/SHIELD` were routed live | `reports/PCB_BATCH_03_USB_CONTROL_ROUTING_APPLY.json`; `reports/PCB_BATCH_03_TRACE_CHANGE_SUMMARY.md` |
| Batch-03 DRC has `0` violations and `21` unconnected items | `reports/PCB_BATCH_03_USB_CONTROL_ROUTING_DRC_FINAL.json`; `reports/LIVE_PROJECT_STATE.json` |
| Detectable unrouted nets dropped to `7` | `reports/LIVE_PROJECT_STATE.json`; `reports/LIVE_PROJECT_STATE.md` |
| Deferred nets were not routed live | `reports/LIVE_PROJECT_STATE.json`; `reports/PCB_BATCH_03_USB_CONTROL_ROUTING_REPORT.md` |
