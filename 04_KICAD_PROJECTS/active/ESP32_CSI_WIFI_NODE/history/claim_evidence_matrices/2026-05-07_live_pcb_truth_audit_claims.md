# Claim Evidence Matrix - Live PCB Truth Audit

Date: `2026-05-07`

| Claim | Evidence | Status |
|---|---|---|
| The live PCB file exists and is the audited artifact | `kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`, SHA256 `0CFE639213D3B0A111F5D06E728A3F7F34B55674DC27312B00D39F80235B2844` | `VERIFIED_BY_FILE` |
| The live board outline is present and measures `60.0 mm x 95.0 mm` | `reports/PCB_FILE_CURRENT_STATE.md`, `reports/live_pcb_truth_audit/real_board_routing_audit_summary.md` | `VERIFIED_BY_COMMAND` |
| The live board contains `43` footprints and `4` mounting-hole footprints | `reports/PCB_FILE_CURRENT_STATE.md` | `VERIFIED_BY_COMMAND` |
| Placement exists on the live board | `reports/PCB_PLACEMENT_CURRENT_STATE_REPORT.md`, `_verification/pcb_visual/live_pcb_truth_audit/top.png` | `VERIFIED_BY_BOARD_STATE` |
| Partial routing exists on the live board | `reports/ROUTING_CURRENT_STATE_REPORT.md`, `_verification/pcb_visual/live_pcb_truth_audit/crop_existing_routed_traces_top.png`, `_verification/pcb_visual/live_pcb_truth_audit/crop_existing_routed_traces_bottom.png` | `VERIFIED_BY_BOARD_STATE` |
| The live board currently has `24` tracks, `2` vias, and `0` zones | `reports/PCB_FILE_CURRENT_STATE.md` | `VERIFIED_BY_COMMAND` |
| The current DRC is not clean | `reports/live_pcb_truth_audit/LIVE_PCB_TRUTH_AUDIT_DRC.json` | `VERIFIED_BY_DRC` |
| Routing may not continue yet | `reports/LIVE_PCB_TRUTH_AUDIT.md`, `reports/ROUTING_START_BLOCKERS.md`, phase-check output for phases `2`, `3`, `5`, and `8` | `VERIFIED_BY_EVIDENCE` |
