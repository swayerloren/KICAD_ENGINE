# Critical Net Routing Plan

- project: `can_node_fixture`
- status: `PASS`

## Critical Nets

| net | stage | priority | status | review_required |
| --- | --- | --- | --- | --- |
| +12V_IN | POWER_INPUT_PROTECTION | 100 | ROUTED | False |
| REG_SW | REGULATOR_CRITICAL_LOOP | 90 | ROUTED | True |
| +3V3 | RAIL_3V3 | 80 | ROUTED | False |
| EN | ESP32_EN_BOOT | 40 | ROUTED | False |

## Hard Fails

_none_
