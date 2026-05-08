# Critical Net Routing Plan

- project: `esp32_usb_power_fixture`
- status: `PASS`

## Critical Nets

| net | stage | priority | status | review_required |
| --- | --- | --- | --- | --- |
| +5V_IN | POWER_INPUT_PROTECTION | 100 | ROUTED | False |
| +5V_FUSED | POWER_INPUT_PROTECTION | 95 | ROUTED | False |
| +5V_PROTECTED | POWER_INPUT_PROTECTION | 90 | ROUTED | False |
| BUCK_SW | REGULATOR_CRITICAL_LOOP | 88 | ROUTED | True |
| BUCK_BST | REGULATOR_CRITICAL_LOOP | 87 | ROUTED | True |
| +3V3 | RAIL_3V3 | 80 | ROUTED | False |
| USB_D+ | USB_DP_DM | 70 | ROUTED | True |
| USB_D- | USB_DP_DM | 70 | ROUTED | True |
| USB_CC1 | ESD_PROTECTION | 60 | ROUTED | False |
| USB_CC2 | ESD_PROTECTION | 60 | ROUTED | False |
| EN | ESP32_EN_BOOT | 40 | ROUTED | False |

## Hard Fails

_none_
