# Claim Evidence Matrix

Session: `PCB_BATCH_05_USB_DATA_ROUTING`

Date: `2026-05-08`

| Claim | Evidence |
| --- | --- |
| Batch 05 did not start on the live board. | `kicad_pcb` hash before and after review are identical: `7BB955071DCABD9AA6A4B8F71F749AE14DF36F7E041F6C3FE657CDC17C62CF3C`. |
| USB data routing is still blocked by live control-net state. | `reports/PCB_BATCH_04_CONTROL_NET_ROUTING_REPORT.md`; `reports/LIVE_PROJECT_STATE.json`. |
| No DRC regression was introduced. | `reports/LIVE_PROJECT_STATE.json` shows `0` violations, `20` unconnected items. |
