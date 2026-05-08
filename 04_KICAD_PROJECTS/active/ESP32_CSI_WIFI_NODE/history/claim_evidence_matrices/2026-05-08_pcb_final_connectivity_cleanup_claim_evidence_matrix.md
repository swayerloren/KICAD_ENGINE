# Claim Evidence Matrix: PCB Final Connectivity Cleanup

Generated: `2026-05-08T12:34:25-04:00`

| Claim | Evidence |
| --- | --- |
| Live PCB changed | hash `7BB955...CF3C -> 38DB92...FC1D`; live file timestamp `12:31:56 -04:00` |
| Cleanup preserved rule DRC | `reports/PCB_FINAL_CONNECTIVITY_CLEANUP_DRC_POST.json` shows `0` violations |
| Unconnected items dropped from `20` to `17` | precheck JSON and post-edit JSON |
| Accepted live delta was copied-board-proven | `candidate_control_local_drc_rerun.json` shows `0` violations, `17` unconnected items |
| USB-local candidate was unsafe | `candidate_control_usb_local_drc_rerun.json` shows `4` violations |
