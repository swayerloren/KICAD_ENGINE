# Real PCB Repair Pass 1 Claim / Evidence Matrix

Created: `2026-05-08T07:13:30-04:00`
Project: `ESP32_CSI_WIFI_NODE`

| Claim | Evidence | Status |
| --- | --- | --- |
| The real PCB file was edited and saved. | `kicad/ESP32_CSI_WIFI_NODE.kicad_pcb` before/after hashes in `REAL_PCB_REPAIR_PASS_1_REPORT.md` | `VERIFIED` |
| The `U2 pad 41` drill-rule blocker is fixed. | `REAL_PCB_REPAIR_PASS_1_DRC.json`; `REAL_PCB_REPAIR_PASS_1_DRC_REPORT.md` | `VERIFIED` |
| GND zones now exist on the live board. | `reports/LIVE_PROJECT_STATE.json`; `_verification/pcb_visual/real_pcb_repair_pass_1_top.png`; `_verification/pcb_visual/real_pcb_repair_pass_1_bottom.png` | `VERIFIED` |
| Detectable unrouted nets dropped from `16` to `15`. | `REAL_PCB_REPAIR_PASS_1_UNROUTED_NETS.md`; `reports/LIVE_PROJECT_STATE.json` | `VERIFIED` |
| Routing continuation is still blocked. | `check_phase_allowed.py --phase 8` output; `REAL_PCB_REPAIR_PASS_1_REPORT.md` | `VERIFIED` |
