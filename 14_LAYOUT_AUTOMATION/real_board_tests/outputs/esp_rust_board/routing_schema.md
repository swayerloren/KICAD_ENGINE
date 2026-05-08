# KiCad PCB To Routing Schema

- project: `esp-rust-board`
- components: `96`
- pads: `240`
- nets: `63`
- tracks: `543`
- vias: `216`
- zones: `8`
- keepouts: `0`

## Net Sample

| net | role | net_class | routing_status |
| --- | --- | --- | --- |
| +5V | POWER_INPUT | Default | ROUTED |
| +BATT | POWER_INPUT | Default | ROUTED |
| VBUS | POWER_INPUT | Default | ROUTED |
| +3V3 | RAIL_3V3 | Default | ROUTED |
| USB_D+ | USB_D+ | Default | ROUTED |
| USB_D- | USB_D- | Default | ROUTED |
| ENABLE | EN_BOOT | Default | ROUTED |
| IO0 | EN_BOOT | Default | ROUTED |
| IO9_BOOT | EN_BOOT | Default | ROUTED |
| /Buck_Coil | LOW_RISK | Default | ROUTED |
| CHIP_PU | LOW_RISK | Default | ROUTED |
| GND | GROUND | Default | ROUTED |
| IO1 | LOW_RISK | Default | ROUTED |
| IO10_SDA | LOW_RISK | Default | ROUTED |
| IO2 | LOW_RISK | Default | ROUTED |
| IO20_RX | LOW_RISK | Default | ROUTED |
| IO21_TX | LOW_RISK | Default | ROUTED |
| IO3 | LOW_RISK | Default | ROUTED |
| IO4 | LOW_RISK | Default | ROUTED |
| IO5 | LOW_RISK | Default | ROUTED |
| IO6 | LOW_RISK | Default | ROUTED |
| IO7 | LOW_RISK | Default | ROUTED |
| IO8_SCL | LOW_RISK | Default | ROUTED |
| Net-(C6-Pad2) | LOW_RISK | Default | ROUTED |
| Net-(D2-Pad2) | LOW_RISK | Default | ROUTED |
| Net-(D3-Pad1) | LOW_RISK | Default | ROUTED |
| Net-(D6-Pad2) | LOW_RISK | Default | ROUTED |
| Net-(D9-Pad4) | LOW_RISK | Default | ROUTED |
| Net-(J1-PadA5) | LOW_RISK | Default | ROUTED |
| Net-(J1-PadB5) | LOW_RISK | Default | ROUTED |
| Net-(J1-PadS1) | LOW_RISK | Default | ROUTED |
| Net-(R14-Pad1) | LOW_RISK | Default | ROUTED |
| Net-(R7-Pad1) | LOW_RISK | Default | ROUTED |
| Net-(R9-Pad2) | LOW_RISK | Default | ROUTED |
| Net-(TP2-Pad1) | LOW_RISK | Default | ROUTED |
| unconnected-(D9-Pad2) | LOW_RISK | Default | ROUTED |
| unconnected-(J1-PadA8) | LOW_RISK | Default | ROUTED |
| unconnected-(J1-PadB8) | LOW_RISK | Default | ROUTED |
| unconnected-(U2-Pad10) | LOW_RISK | Default | ROUTED |
| unconnected-(U2-Pad11) | LOW_RISK | Default | ROUTED |

## Not Extracted

- ZONE_0_/Buck_Coil exposes keepout-style zone parameters in KiCad API but is not a rule area; extracted as COPPER_ZONE
- ZONE_1_+BATT exposes keepout-style zone parameters in KiCad API but is not a rule area; extracted as COPPER_ZONE
- ZONE_2_+5V exposes keepout-style zone parameters in KiCad API but is not a rule area; extracted as COPPER_ZONE
- ZONE_3_GND exposes keepout-style zone parameters in KiCad API but is not a rule area; extracted as COPPER_ZONE
- ZONE_4_+3V3 exposes keepout-style zone parameters in KiCad API but is not a rule area; extracted as COPPER_ZONE
- ZONE_5_VBUS exposes keepout-style zone parameters in KiCad API but is not a rule area; extracted as COPPER_ZONE
- ZONE_6_GND exposes keepout-style zone parameters in KiCad API but is not a rule area; extracted as COPPER_ZONE
- ZONE_7_+3V3 exposes keepout-style zone parameters in KiCad API but is not a rule area; extracted as COPPER_ZONE
- per-net ratsnest extraction not implemented; only total unconnected count is extracted
