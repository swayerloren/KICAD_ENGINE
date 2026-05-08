# HOLE_PAD_VIA_STRATEGY_BLOCKED_CLAIM_EVIDENCE_MATRIX

Date: 2026-05-03

## Claims

| Claim | Status | Evidence | Human review required |
|---|---|---|---|
| Placement pass 2 did not run successfully. | `VERIFIED_BY_FILE` | `reports/PCB_PLACEMENT_PASS_2_ORIENTATION_REPORT.md` | No |
| The active project has no `.kicad_pcb`. | `VERIFIED_BY_COMMAND` | Project file inspection command log | No |
| Hole, pad, and via strategy cannot be verified without a PCB. | `VERIFIED_BY_FILE` | No PCB file plus no board outline in reports | Yes for future pass |
| Fab drill/via limits were not verified from a selected fab profile. | `VERIFIED_BY_FILE` | `24_FAB_PROFILES/00_INDEX/FAB_PROFILE_SCHEMA.md` is schema only | Yes |
| No routing was performed. | `VERIFIED_BY_COMMAND` | No PCB file exists and no PCB edit command was run | No |

