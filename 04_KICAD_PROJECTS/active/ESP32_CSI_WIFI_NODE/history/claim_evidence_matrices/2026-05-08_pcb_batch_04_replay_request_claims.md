# Claim Evidence Matrix

Session: `PCB_BATCH_04_REPLAY_REQUEST_ALREADY_APPLIED`

Date: `2026-05-08`

| Claim | Evidence |
| --- | --- |
| The live board is already past the Batch 03 baseline. | `kicad_pcb` hash from disk is `7BB955071DCABD9AA6A4B8F71F749AE14DF36F7E041F6C3FE657CDC17C62CF3C`; Batch 03 after-hash in prior report is `22ED35E8FF9CC96F16014B66A2DCF669520D10A7A3C005ACEC3C68F29B9CF3F4`. |
| Batch 04 was already applied earlier on `2026-05-08`. | `reports/PCB_BATCH_04_CONTROL_NET_ROUTING_REPORT.md`; `routing_work/20260508_091428/BEFORE_AFTER_HASH_LOG.md`. |
| Replaying Batch 04 now would be unsafe or meaningless. | Current board already includes the Batch 04 `/U0RXD` delta per `reports/PCB_BATCH_04_TRACE_CHANGE_SUMMARY.md`. |
