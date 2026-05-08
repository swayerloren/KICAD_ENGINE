# Claim/Evidence Matrix: ESP32_CSI_WIFI_NODE NOT_FINAL JLCPCB Export

Date: 2026-05-07

| Claim | Evidence | Confidence |
|---|---|---:|
| Export is blocked. | Failed preconditions in export report; no PCB file; JLCPCB and BOM reviews blocked. | `HIGH` |
| No PCB file exists. | `Test-Path kicad/ESP32_CSI_WIFI_NODE.kicad_pcb` returned `False`. | `HIGH` |
| DRC cannot pass for this export. | `FINAL_PCB_AUDIT_BEFORE_FAB.md` records DRC `NOT_RUN_NO_PCB`. | `HIGH` |
| Unrouted net count is not confirmed zero. | `PCB_FULL_ROUTING_REPORT.md` records `UNKNOWN_NO_PCB`. | `HIGH` |
| JLCPCB review is blocked. | `JLCPCB_DFM_DFA_REVIEW.md` final classification `JLCPCB_REVIEW_BLOCKED`. | `HIGH` |
| BOM review is blocked. | `PRODUCTION_BOM_REVIEW.md` final classification `BOM_BLOCKED`. | `HIGH` |
| ERC is reported pass. | `SCHEMATIC_VERIFICATION_REPORT.md` and `SCHEMATIC_TO_PCB_GATE_STATUS.md` record ERC `PASS`. | `MEDIUM_HIGH` |

