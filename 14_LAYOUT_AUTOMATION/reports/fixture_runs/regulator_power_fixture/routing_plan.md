# Routing Plan

- project: `regulator_power_fixture`
- status: `PASS`
- hard_fail_count: `0`

## Routing Order

| net | stage | priority | critical | power | usb | status |
| --- | --- | --- | --- | --- | --- | --- |
| +VIN | POWER_INPUT_PROTECTION | 100 | True | True | False | ROUTED |
| BUCK_SW | REGULATOR_CRITICAL_LOOP | 90 | True | True | False | ROUTED |
| BUCK_BST | REGULATOR_CRITICAL_LOOP | 88 | True | False | False | ROUTED |
| +3V3 | RAIL_3V3 | 80 | True | True | False | ROUTED |
| FB | DECOUPLING | 50 | True | False | False | ROUTED |
| GND | LOW_RISK_REMAINING | 10 | False | False | False | PLANNED |

## Errors

_none_

## Warnings

_none_

## Hard Fails

_none_
