# Routing Plan

- project: `can_node_fixture`
- status: `PASS`
- hard_fail_count: `0`

## Routing Order

| net | stage | priority | critical | power | usb | status |
| --- | --- | --- | --- | --- | --- | --- |
| +12V_IN | POWER_INPUT_PROTECTION | 100 | True | True | False | ROUTED |
| REG_SW | REGULATOR_CRITICAL_LOOP | 90 | True | True | False | ROUTED |
| +3V3 | RAIL_3V3 | 80 | True | True | False | ROUTED |
| EN | ESP32_EN_BOOT | 40 | True | False | False | ROUTED |
| CANH | LOW_RISK_REMAINING | 60 | False | False | False | ROUTED |
| CANL | LOW_RISK_REMAINING | 60 | False | False | False | ROUTED |
| GND | LOW_RISK_REMAINING | 10 | False | False | False | PLANNED |

## Errors

_none_

## Warnings

_none_

## Hard Fails

_none_
