# Critical Net Routing Plan

- project: `esp-rust-board`
- status: `PASS`

## Critical Nets

| net | stage | priority | status | review_required |
| --- | --- | --- | --- | --- |
| +5V | POWER_INPUT_PROTECTION | 100 | ROUTED | True |
| +BATT | POWER_INPUT_PROTECTION | 100 | ROUTED | True |
| VBUS | POWER_INPUT_PROTECTION | 100 | ROUTED | True |
| +3V3 | RAIL_3V3 | 90 | ROUTED | True |
| USB_D+ | USB_DP_DM | 85 | ROUTED | True |
| USB_D- | USB_DP_DM | 85 | ROUTED | True |
| ENABLE | ESP32_EN_BOOT | 70 | ROUTED | True |
| IO0 | ESP32_EN_BOOT | 70 | ROUTED | True |
| IO9_BOOT | ESP32_EN_BOOT | 70 | ROUTED | True |

## Hard Fails

_none_
