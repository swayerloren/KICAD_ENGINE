# PCB_PLACEMENT_PASS_2_BLOCKED_SCORECARD

Date: 2026-05-03

Overall score: `94/100`

Risk label: `LOW_RISK_BLOCKED_NO_DESIGN_EDIT`

Quality gate: `BLOCKED_UNTIL_HUMAN_REVIEW`

## Category Scores

| Category | Score | Notes |
|---|---:|---|
| Evidence support | 20/20 | Blocked state is backed by project reports and file inspection. |
| KiCad-specific correctness | 20/20 | No PCB operation was attempted without a board and gate pass. |
| Datasheet/component accuracy | 14/15 | No component specifications were asserted. |
| Safety/compliance with repo rules | 15/15 | No routing, placement, zones, or manufacturing output. |
| Memory/history routing correctness | 9/10 | Project issue, failed attempt, memory, and quality logs were created. |
| Uncertainty disclosure | 10/10 | Missing PCB/outline/gate evidence is explicit. |
| End-user usefulness | 6/10 | Useful blocker report, but placement itself could not proceed. |

## Result

`PLACEMENT_ORIENTATION_FAIL` due to missing PCB and failed upstream gate.

