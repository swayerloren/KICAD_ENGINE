# Claim Evidence Matrix - PCB Placement Pass 1

Date: 2026-05-06

| Claim | Evidence | Status |
|---|---|---|
| Selected layout plan is Plan B | `reports/PCB_SELECTED_LAYOUT_PLAN.md` | `VERIFIED_FROM_REPORT` |
| Placement may not begin | `reports/PCB_SELECTED_LAYOUT_PLAN.md` and `reports/PCB_MECHANICAL_SETUP_REPORT.md` | `VERIFIED_FROM_REPORTS` |
| PCB file does not exist | `Test-Path ...ESP32_CSI_WIFI_NODE.kicad_pcb` returned `False` | `VERIFIED_BY_COMMAND` |
| Board outline does not exist | `reports/PCB_MECHANICAL_SETUP_REPORT.md` says `Board outline created: NO` | `VERIFIED_FROM_REPORT` |
| No parts were placed | No PCB file exists; no KiCad design-file edit was performed | `VERIFIED_BY_WORKFLOW` |
| DRC was not run | No PCB file exists | `VERIFIED_BY_WORKFLOW` |
| Orientation risks require human review after placement | PCB rule files under `09_ACCURACY_ENGINE/pcb_rules/` | `VERIFIED_FROM_RULES` |
