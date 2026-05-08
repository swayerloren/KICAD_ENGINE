# Maintenance Layer Investigation And Repair Claim Evidence Matrix

Record kind: `claim_evidence_matrix`
Created: `2026-05-07T22:39:00-04:00`
Scope: `project`
Project: `ESP32_CSI_WIFI_NODE`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Matrix

| Claim | Evidence | Claim Status | Confidence | Risk | Human Review Required | Issue |
| --- | --- | --- | --- | --- | --- | --- |
| The every-5-prompts layer existed only partially before repair. | `memory/PROMPT_COUNTER.md`, legacy `03_TOOLS/scripts/memory_maintenance/*`, absence of a canonical live-state supervisor before this task. | `VERIFIED_BY_FILE` | `HIGH` | `MEDIUM_RISK` | `NO` | None recorded. |
| The old maintenance path did not rebuild live project truth from `.kicad_pro`, `.kicad_sch`, and `.kicad_pcb`. | Legacy maintenance scripts and their README contents; no live-state JSON/markdown outputs before repair. | `VERIFIED_BY_FILE` | `HIGH` | `MEDIUM_RISK` | `NO` | None recorded. |
| `check_phase_allowed.py` previously trusted stale markdown and could block real PCB work incorrectly. | Pre-repair script audit, stale report audit, and the existence of a live board alongside old `NO_PCB` style blockers. | `VERIFIED_BY_FILE` | `HIGH` | `HIGH_RISK` | `NO` | `STALE_GATE_REPORTS_BLOCKED_REAL_PCB_WORK.md` |
| The repaired phase checker now allows phases 2 and 3 from live evidence and blocks phase 8 for real board reasons. | Final outputs from `check_phase_allowed.py --phase 2`, `--phase 3`, `--phase 8`; `GATE_RECONCILIATION_REPORT.md`. | `VERIFIED_BY_COMMAND` | `HIGH` | `LOW_RISK` | `YES` | Routing continuation still requires human review. |
| The live PCB currently exists with partial routing and is not ready for routing continuation. | `LIVE_PROJECT_STATE.json`, DRC results, stale report audit, existing trace audit. | `VERIFIED_BY_COMMAND` | `HIGH` | `HIGH_RISK` | `YES` | Existing routed geometry, GND strategy, and unrouted nets remain open. |

## Notes

This matrix separates repaired maintenance-layer claims from unresolved physical board-state claims so the maintenance fix is not confused with fabrication readiness.
