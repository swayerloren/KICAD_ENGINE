# Routing Plan

- project: `esp32_usb_power_fixture`
- status: `PASS`
- hard_fail_count: `0`

## Routing Order

| net | stage | priority | critical | power | usb | status |
| --- | --- | --- | --- | --- | --- | --- |
| +5V_IN | POWER_INPUT_PROTECTION | 100 | True | True | False | ROUTED |
| +5V_FUSED | POWER_INPUT_PROTECTION | 95 | True | True | False | ROUTED |
| +5V_PROTECTED | POWER_INPUT_PROTECTION | 90 | True | True | False | ROUTED |
| BUCK_SW | REGULATOR_CRITICAL_LOOP | 88 | True | True | False | ROUTED |
| BUCK_BST | REGULATOR_CRITICAL_LOOP | 87 | True | False | False | ROUTED |
| +3V3 | RAIL_3V3 | 80 | True | True | False | ROUTED |
| USB_D+ | USB_DP_DM | 70 | True | False | True | ROUTED |
| USB_D- | USB_DP_DM | 70 | True | False | True | ROUTED |
| USB_CC1 | ESD_PROTECTION | 60 | True | False | False | ROUTED |
| USB_CC2 | ESD_PROTECTION | 60 | True | False | False | ROUTED |
| EN | ESP32_EN_BOOT | 40 | True | False | False | ROUTED |
| GND | LOW_RISK_REMAINING | 10 | False | False | False | PLANNED |

## Errors

_none_

## Warnings

_none_

## Hard Fails

_none_
