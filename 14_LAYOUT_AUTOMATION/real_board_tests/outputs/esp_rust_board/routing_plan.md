# Routing Plan

- project: `esp-rust-board`
- status: `AUTO_BLOCKED_BAD_LAYOUT`
- hard_fail_count: `1`

## Routing Order

| net | stage | priority | critical | power | usb | status |
| --- | --- | --- | --- | --- | --- | --- |
| +5V | POWER_INPUT_PROTECTION | 100 | True | True | False | ROUTED |
| +BATT | POWER_INPUT_PROTECTION | 100 | True | True | False | ROUTED |
| VBUS | POWER_INPUT_PROTECTION | 100 | True | True | False | ROUTED |
| +3V3 | RAIL_3V3 | 90 | True | True | False | ROUTED |
| USB_D+ | USB_DP_DM | 85 | True | False | True | ROUTED |
| USB_D- | USB_DP_DM | 85 | True | False | True | ROUTED |
| ENABLE | ESP32_EN_BOOT | 70 | True | False | False | ROUTED |
| IO0 | ESP32_EN_BOOT | 70 | True | False | False | ROUTED |
| IO9_BOOT | ESP32_EN_BOOT | 70 | True | False | False | ROUTED |
| /Buck_Coil | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| CHIP_PU | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| GND | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| IO1 | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| IO10_SDA | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| IO2 | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| IO20_RX | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| IO21_TX | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| IO3 | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| IO4 | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| IO5 | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| IO6 | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| IO7 | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| IO8_SCL | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| Net-(C6-Pad2) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| Net-(D2-Pad2) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| Net-(D3-Pad1) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| Net-(D6-Pad2) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| Net-(D9-Pad4) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| Net-(J1-PadA5) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| Net-(J1-PadB5) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| Net-(J1-PadS1) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| Net-(R14-Pad1) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| Net-(R7-Pad1) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| Net-(R9-Pad2) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| Net-(TP2-Pad1) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(D9-Pad2) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(J1-PadA8) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(J1-PadB8) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-Pad10) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-Pad11) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-Pad2) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-Pad3) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U2-Pad4) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U3-Pad10) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U3-Pad15) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U3-Pad17) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U3-Pad24) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U3-Pad25) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U3-Pad28) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U3-Pad29) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U3-Pad32) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U3-Pad33) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U3-Pad34) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U3-Pad35) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U3-Pad4) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U3-Pad7) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U3-Pad9) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U4-Pad21) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U4-Pad22) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U4-Pad23) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U4-Pad24) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U4-Pad25) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |
| unconnected-(U4-Pad3) | LOW_RISK_REMAINING | 10 | False | False | False | ROUTED |

## Errors

_none_

## Warnings

_none_

## Hard Fails

- regulator critical loop not planned
