# ESP32_CSI_WIFI_NODE PCB Batch 05 USB Data Routing Commands

Date: `2026-05-08`

## Commands Run

1. Read the required Batch 04 reports:
   - `reports\PCB_BATCH_04_CONTROL_NET_ROUTING_REPORT.md`
   - `reports\PCB_BATCH_04_TRACE_CHANGE_SUMMARY.md`
2. Read the required routing rules:
   - `14_LAYOUT_AUTOMATION\USB_TRACE_RULES.md`
   - `14_LAYOUT_AUTOMATION\TRACE_PLANNING_RULES.md`
   - `14_LAYOUT_AUTOMATION\REAL_PROJECT_ROUTING_STOP_CONDITIONS.md`
3. Verified the live PCB identity and current hash:
   - `Get-FileHash ... ESP32_CSI_WIFI_NODE.kicad_pcb -Algorithm SHA256`
4. Read the refreshed live project state:
   - `reports\LIVE_PROJECT_STATE.json`
5. Checked maintenance status:
   - `python 03_TOOLS\scripts\memory_maintenance\check_maintenance_due.py --project ...`
6. Created a guarded Batch 05 script scaffold and syntax-checked it:
   - `python -m py_compile 03_TOOLS\scripts\pcb_routing\esp32_csi_usb_data_batch_05.py`
7. Rebuilt indexes and `CURRENT_KNOWN_PROBLEMS.md` during closeout:
   - `python 03_TOOLS\scripts\memory_history\build_memory_index.py --repo-root ...`
   - `python 03_TOOLS\scripts\memory_history\build_history_index.py --repo-root ...`
   - `python 03_TOOLS\scripts\ai_quality\build_current_known_problems.py --repo-root ...`
