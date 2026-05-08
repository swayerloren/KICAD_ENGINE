# Claim Evidence Matrix

Session: `PCB_BATCH_04_CONTROL_NET_ROUTING`

Date: `2026-05-08`

| Claim | Evidence |
| --- | --- |
| The live PCB changed in Batch 04. | `kicad_pcb` hash before `22ED35E8FF9CC96F16014B66A2DCF669520D10A7A3C005ACEC3C68F29B9CF3F4`; hash after `7BB955071DCABD9AA6A4B8F71F749AE14DF36F7E041F6C3FE657CDC17C62CF3C`. |
| `/U0RXD` was routed live. | `reports/PCB_BATCH_04_TRACE_CHANGE_SUMMARY.md`; script output from `esp32_csi_control_batch_04.py`; top visual packet. |
| No DRC violations were introduced. | `reports/PCB_BATCH_04_CONTROL_NET_ROUTING_DRC.json`; `reports/LIVE_PROJECT_STATE.json`. |
| Unconnected items dropped from `21` to `20`. | Pre-batch state in `reports/PCB_BATCH_03_USB_CONTROL_ROUTING_REPORT.md`; post-batch DRC and live state. |
| `/BOOT0` and `/ESP_EN` were deferred for real board safety reasons. | Copied-board trial folders under `routing_work/20260508_091428/batch04_control_trials/20260508_114318/`; `reports/PCB_BATCH_04_CONTROL_NET_ROUTING_REPORT.md`. |
