# PCB_PLACEMENT_PASS_2_BLOCKED_CLAIM_EVIDENCE_MATRIX

Date: 2026-05-03

## Claims

| Claim | Status | Evidence | Human review required |
|---|---|---|---|
| Placement pass 1 did not run successfully. | `VERIFIED_BY_FILE` | `reports/PCB_PLACEMENT_PASS_1_REPORT.md` | No |
| The active project has no `.kicad_pcb`. | `VERIFIED_BY_COMMAND` | Project file inspection command log | No |
| Schematic-to-PCB gate is `FAIL`. | `VERIFIED_BY_FILE` | `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` | Yes for closure |
| Placement pass 2 cannot inspect orientation/courtyards. | `VERIFIED_BY_FILE` | No PCB file and pass-1 failure | Yes for future pass |
| No routing was performed. | `VERIFIED_BY_COMMAND` | No PCB file exists and no PCB edit command was run | No |

