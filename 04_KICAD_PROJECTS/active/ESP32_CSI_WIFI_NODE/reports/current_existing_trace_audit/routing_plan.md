# Routing Plan

- project: `ESP32_CSI_WIFI_NODE`
- status: `AUTO_BLOCKED_BAD_LAYOUT`
- hard_fail_count: `1`

## Routing Order

| net | stage | priority | critical | power | usb | status |
| --- | --- | --- | --- | --- | --- | --- |
| /+5V_FUSED | POWER_INPUT_PROTECTION | 100 | True | True | False | ROUTED |
| /+5V_IN | POWER_INPUT_PROTECTION | 100 | True | True | False | ROUTED |
| /+5V_PROTECTED | POWER_INPUT_PROTECTION | 100 | True | True | False | ROUTED |
| unconnected-(J2-VBUS-PadA4) | POWER_INPUT_PROTECTION | 100 | True | True | False | UNROUTED |
| /BUCK_BST | REGULATOR_CRITICAL_LOOP | 95 | True | True | False | ROUTED |
| /BUCK_SW | REGULATOR_CRITICAL_LOOP | 95 | True | True | False | ROUTED |
| +3V3 | RAIL_3V3 | 90 | True | True | False | ROUTED |
| /BOOT0 | ESP32_EN_BOOT | 70 | True | False | False | UNROUTED |
| /ESP_EN | ESP32_EN_BOOT | 70 | True | False | False | UNROUTED |
| /PLED | LEDS_BUTTONS | 15 | False | False | False | UNROUTED |
| /SLED | LEDS_BUTTONS | 15 | False | False | False | UNROUTED |
| /STATUS_LED | LEDS_BUTTONS | 15 | False | False | False | UNROUTED |
| /CC1 | LOW_RISK_REMAINING | 10 | False | False | False | UNROUTED |
| /CC2 | LOW_RISK_REMAINING | 10 | False | False | False | UNROUTED |
| /DM_C | LOW_RISK_REMAINING | 10 | False | False | False | UNROUTED |
| /DM_E | LOW_RISK_REMAINING | 10 | False | False | False | UNROUTED |
| /DP_C | LOW_RISK_REMAINING | 10 | False | False | False | UNROUTED |
| /DP_E | LOW_RISK_REMAINING | 10 | False | False | False | UNROUTED |
| /SHIELD | LOW_RISK_REMAINING | 10 | False | False | False | UNROUTED |
| /U0RXD | LOW_RISK_REMAINING | 10 | False | False | False | UNROUTED |
| /U0TXD | LOW_RISK_REMAINING | 10 | False | False | False | UNROUTED |
| GND | LOW_RISK_REMAINING | 10 | False | False | False | UNROUTED |
| unconnected-(U2-IO1-Pad39) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO10-Pad18) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO11-Pad19) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO12-Pad20) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO13-Pad21) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO14-Pad22) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO15-Pad8) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO16-Pad9) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO17-Pad10) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO18-Pad11) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO21-Pad23) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO3-Pad15) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO35-Pad28) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO36-Pad29) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO37-Pad30) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO38-Pad31) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO39-Pad32) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO4-Pad4) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO40-Pad33) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO41-Pad34) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO42-Pad35) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO45-Pad26) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO46-Pad16) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO47-Pad24) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO48-Pad25) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO5-Pad5) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO6-Pad6) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO7-Pad7) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO8-Pad12) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-IO9-Pad17) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |

## Errors

_none_

## Warnings

- ground strategy missing

## Hard Fails

- GND strategy missing
