# Critical Net Routing Plan

- project: `ESP32_CSI_WIFI_NODE`
- status: `PASS`

## Critical Nets

| net | stage | priority | status | review_required |
| --- | --- | --- | --- | --- |
| /+5V_FUSED | POWER_INPUT_PROTECTION | 100 | ROUTED | True |
| /+5V_IN | POWER_INPUT_PROTECTION | 100 | ROUTED | True |
| /+5V_PROTECTED | POWER_INPUT_PROTECTION | 100 | ROUTED | True |
| unconnected-(J2-VBUS-PadA4) | POWER_INPUT_PROTECTION | 100 | UNROUTED | True |
| /BUCK_BST | REGULATOR_CRITICAL_LOOP | 95 | ROUTED | True |
| /BUCK_SW | REGULATOR_CRITICAL_LOOP | 95 | ROUTED | True |
| +3V3 | RAIL_3V3 | 90 | ROUTED | True |
| /BOOT0 | ESP32_EN_BOOT | 70 | UNROUTED | True |
| /ESP_EN | ESP32_EN_BOOT | 70 | UNROUTED | True |

## Hard Fails

_none_
