# Claim Evidence Matrix - ESP32_CSI_WIFI_NODE Copied Board Routing Rehearsal

Date: `2026-05-10`

| Claim | Status | Evidence |
| --- | --- | --- |
| Only copied boards were edited. | VERIFIED_BY_HASH | Real PCB hash stayed `ACA326C7...`, and candidate hashes changed only under `routing_rehearsals/20260510_143529/`. |
| Four copied candidates were evaluated. | VERIFIED_BY_FILE | `routing_rehearsals/20260510_143529/` contains `candidate_A_baseline`, `candidate_B_grid_planner`, `candidate_C_targeted_local_repair`, and `candidate_D_cluster_rework`. |
| `candidate_C_targeted_local_repair` was the best routed attempt. | VERIFIED_BY_REPORT | `reports/COPIED_BOARD_ROUTING_CANDIDATE_COMPARISON.md` shows it had the lowest DRC damage among routed candidates. |
| No candidate passed the PCB quality gate. | VERIFIED_BY_FILE | Each candidate `reports/pcb_quality_gate/pcb_quality_gate_result.json` reports `FAIL_DRC`. |
| Real-board routing may not begin. | VERIFIED_BY_GATE | `reports/COPIED_BOARD_PCB_QUALITY_GATE_REPORT.md` and the candidate gate outputs remain blocked. |
