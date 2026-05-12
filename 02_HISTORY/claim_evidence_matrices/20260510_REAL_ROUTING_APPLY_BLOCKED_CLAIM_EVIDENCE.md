# Claim Evidence Matrix - Real Routing Apply Blocked

Date: `2026-05-10`

| Claim | Status | Evidence |
| --- | --- | --- |
| Real routing did not start. | VERIFIED_BY_HASH | PCB hash before and after remained identical. |
| The copied-board precondition failed. | VERIFIED_BY_FILE | `reports/COPIED_BOARD_ROUTING_REHEARSAL_REPORT.md` says `COPIED_ROUTING_BLOCKED`. |
| The current live board is still quality-gate failed. | VERIFIED_BY_FILE | `reports/pcb_quality_gate/20260510_quality_gate_creation_v2/pcb_quality_gate_result.json` reports `FAIL_DRC`. |
| Maintenance is now due. | VERIFIED_BY_FILE | `memory/PROMPT_COUNTER.md` now shows `Prompt count: 5` and `Maintenance due: YES`. |
