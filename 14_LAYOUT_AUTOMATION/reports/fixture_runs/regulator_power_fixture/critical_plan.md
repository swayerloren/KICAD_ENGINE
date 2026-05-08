# Critical Net Routing Plan

- project: `regulator_power_fixture`
- status: `PASS`

## Critical Nets

| net | stage | priority | status | review_required |
| --- | --- | --- | --- | --- |
| +VIN | POWER_INPUT_PROTECTION | 100 | ROUTED | False |
| BUCK_SW | REGULATOR_CRITICAL_LOOP | 90 | ROUTED | True |
| BUCK_BST | REGULATOR_CRITICAL_LOOP | 88 | ROUTED | True |
| +3V3 | RAIL_3V3 | 80 | ROUTED | False |
| FB | DECOUPLING | 50 | ROUTED | False |

## Hard Fails

_none_
