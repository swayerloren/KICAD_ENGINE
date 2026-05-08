# PCB Batch 04 Replay Request Commands

Date: `2026-05-08`

## Commands Run

1. Verified the live PCB identity and hash:
   - `Get-FileHash ... ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256`
2. Read the existing Batch 04 report and trace summary:
   - `reports\PCB_BATCH_04_CONTROL_NET_ROUTING_REPORT.md`
   - `reports\PCB_BATCH_04_TRACE_CHANGE_SUMMARY.md`
3. Read the refreshed live project state:
   - `reports\LIVE_PROJECT_STATE.json`
4. Read the routing-work hash log:
   - `routing_work\20260508_091428\BEFORE_AFTER_HASH_LOG.md`
5. Checked helper script usage for closeout index rebuilds:
   - `python 03_TOOLS\scripts\memory_history\build_memory_index.py --help`
   - `python 03_TOOLS\scripts\memory_history\build_history_index.py --help`
   - `python 03_TOOLS\scripts\ai_quality\build_current_known_problems.py --help`
