# COPPER_ZONE_STRATEGY_BLOCKED_SCORECARD

Date: 2026-05-03

Overall score: `95/100`

Risk label: `LOW_RISK_BLOCKED_NO_DESIGN_EDIT`

Quality gate: `BLOCKED_UNTIL_HUMAN_REVIEW`

## Category Scores

| Category | Score | Notes |
|---|---:|---|
| Evidence support | 20/20 | Blocked state is backed by project reports and file inspection. |
| KiCad-specific correctness | 20/20 | No copper zone or PCB operation was attempted without a board and gate pass. |
| Datasheet/component accuracy | 15/15 | No component specifications were asserted. |
| Safety/compliance with repo rules | 15/15 | No routing, zones, refills, or manufacturing output. |
| Memory/history routing correctness | 9/10 | Project issue, failed attempt, memory, and quality logs were created. |
| Uncertainty disclosure | 10/10 | Missing PCB/return-path/keepout evidence is explicit. |
| End-user usefulness | 6/10 | Useful blocker report, but zone setup itself could not proceed. |

## Result

`ZONE_SETUP_FAIL` due to missing PCB, failed gate, failed placement pass 2, and failed hole/test-pad/via strategy.

