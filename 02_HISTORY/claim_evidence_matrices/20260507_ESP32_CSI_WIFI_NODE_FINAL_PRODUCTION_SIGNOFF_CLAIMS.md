# Claim/Evidence Matrix: ESP32_CSI_WIFI_NODE Final Production Signoff

Date: 2026-05-07

| Claim | Evidence | Confidence |
|---|---|---:|
| Final classification is `BLOCKED_HIGH_RISK`. | Production risk register and real-world failure review both classify as blocked high risk; no PCB exists. | `HIGH` |
| ERC is reported pass. | `SCHEMATIC_VERIFICATION_REPORT.md` and gate status record ERC `PASS`. | `MEDIUM_HIGH` |
| DRC has not passed. | `FINAL_PCB_AUDIT_BEFORE_FAB.md` records `NOT_RUN_NO_PCB`. | `HIGH` |
| No unrouted-net proof exists. | `PCB_FULL_ROUTING_REPORT.md` records `UNKNOWN_NO_PCB`. | `HIGH` |
| PCB is not synchronized from schematic. | No `.kicad_pcb` exists; schematic-to-PCB gate blocks update. | `HIGH` |
| BOM/JLC/mechanical/upload signoffs are blocked. | Reviewed reports classify as `BOM_BLOCKED`, `JLCPCB_REVIEW_BLOCKED`, `MECHANICAL_REVIEW_BLOCKED`, and `JLC_FEEDBACK_NEEDS_MORE_INFO`. | `HIGH` |

