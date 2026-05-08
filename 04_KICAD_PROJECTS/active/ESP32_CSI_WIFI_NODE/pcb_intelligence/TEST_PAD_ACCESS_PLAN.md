# Test Pad Access Plan

## Test Pad Components

| Ref | Value | Footprint | Cluster | Connected nets | Must be near | Human review |
|---|---|---|---|---|---|---|
| `TP1` | `TP_5V` | `TestPoint:TestPoint_Pad_D1.5mm` | `TEST_PAD` | `/+5V_PROTECTED` |  | `FALSE` |
| `TP2` | `TP_EN` | `TestPoint:TestPoint_Pad_D1.5mm` | `TEST_PAD` | `/ESP_EN` |  | `FALSE` |
| `TP3` | `TP_3V3` | `TestPoint:TestPoint_Pad_D1.5mm` | `TEST_PAD` | `+3V3` |  | `FALSE` |
| `TP4` | `TP_BOOT` | `TestPoint:TestPoint_Pad_D1.5mm` | `TEST_PAD` | `/BOOT0` |  | `FALSE` |
| `TP5` | `TP_GND` | `TestPoint:TestPoint_Pad_D1.5mm` | `TEST_PAD` | `GND` |  | `FALSE` |
| `TP6` | `TP_U0TXD` | `TestPoint:TestPoint_Pad_D1.5mm` | `TEST_PAD` | `/U0TXD` |  | `FALSE` |
| `TP7` | `TP_U0RXD` | `TestPoint:TestPoint_Pad_D1.5mm` | `TEST_PAD` | `/U0RXD` |  | `FALSE` |
| `TP8` | `TP_D+_REV` | `TestPoint:TestPoint_Pad_D1.5mm` | `TEST_PAD` | `/DP_E` |  | `FALSE` |
| `TP9` | `TP_D-_REV` | `TestPoint:TestPoint_Pad_D1.5mm` | `TEST_PAD` | `/DM_E` |  | `FALSE` |

## Rules

- Move `TP1-TP9` into a clean accessible row before routing.
- Do not crowd test pads behind USB-C shell or cable path.
- Do not mix test pads with `R6/R7/R8/R9`, LEDs, LED resistors, ESD, or switches.
- USB data test pads (`TP8/TP9` on `/DP_E` and `/DM_E`) are `USB_TEST_PAD_STUB_RISK`.
- Test pads must not block routing corridors from `J2` to `U3/R8/R9/U2`.
