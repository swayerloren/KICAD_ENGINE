# Claim Evidence Matrix - PCB Placement Strict Audit

Date: 2026-05-06

| Claim | Evidence | Status |
|---|---|---|
| No PCB file exists | `Test-Path ...ESP32_CSI_WIFI_NODE.kicad_pcb` returned `False` | `VERIFIED_BY_COMMAND` |
| Placement pass 1 did not run | `reports/PCB_PLACEMENT_PASS_1_REPORT.md` | `VERIFIED_FROM_REPORT` |
| No parts were placed | `reports/PCB_PLACEMENT_PASS_1_REPORT.md` says `Parts placed: 0` | `VERIFIED_FROM_REPORT` |
| Orientation risks remain unresolved | `reports/PCB_PLACEMENT_ORIENTATION_RISK_REPORT.md` | `VERIFIED_FROM_REPORT` |
| Routing is not allowed | Placement strict audit result and prior placement report | `VERIFIED_BY_GATE_LOGIC` |
