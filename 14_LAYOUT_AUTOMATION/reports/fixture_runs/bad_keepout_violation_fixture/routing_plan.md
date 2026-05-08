# Routing Plan

- project: `bad_keepout_violation_fixture`
- status: `AUTO_BLOCKED_BAD_LAYOUT`
- hard_fail_count: `3`

## Routing Order

| net | stage | priority | critical | power | usb | status |
| --- | --- | --- | --- | --- | --- | --- |
| +5V_IN | POWER_INPUT_PROTECTION | 100 | True | True | False | UNROUTED |
| USB_D+ | USB_DP_DM | 70 | True | False | True | ROUTED |
| EN | ESP32_EN_BOOT | 40 | True | False | False | ROUTED |

## Errors

_none_

## Warnings

- ground strategy missing

## Hard Fails

- GND strategy missing
- regulator critical loop not planned
- USB D+/D- incomplete
