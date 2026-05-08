# PCB_PLACEMENT_PASS_1_BLOCKED_CLAIM_EVIDENCE_MATRIX

Status: `COMPLETED`

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

| Claim | Status | Evidence | Human review required |
| --- | --- | --- | --- |
| No `.kicad_pcb` file exists. | `VERIFIED_BY_COMMAND` | Active project KiCad folder scan found `.kicad_pro` and `.kicad_sch` only. | No |
| PCB update from schematic has not run. | `VERIFIED_BY_FILE` | `reports/PCB_UPDATE_FROM_SCHEMATIC_REPORT.md` status `NOT_RUN_GATE_FAIL`. | No |
| Mechanical setup has not run. | `VERIFIED_BY_FILE` | `reports/PCB_MECHANICAL_SETUP_REPORT.md` status `NOT_RUN_BLOCKED`. | No |
| Board outline does not exist. | `VERIFIED_BY_COMMAND` | No board file exists to contain an outline. | No |
| Placement pass 1 was not run. | `VERIFIED_BY_FILE` | `reports/PCB_PLACEMENT_PASS_1_REPORT.md` status `PLACEMENT_FAIL_NOT_RUN`. | No |
| DRC and PCB visuals were not run. | `VERIFIED_BY_FILE` | `reports/PCB_PLACEMENT_PASS_1_REPORT.md` marks both `NOT_RUN`. | No |

