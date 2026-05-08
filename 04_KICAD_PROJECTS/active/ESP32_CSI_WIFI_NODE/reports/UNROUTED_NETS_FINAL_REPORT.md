# Unrouted Nets Final Report

Generated: 2026-05-07

Source DRC: `reports/FULL_ROUTING_SAFE_PARTIAL_DRC4.rpt`

Final unrouted status: `67_UNCONNECTED_ITEMS_REMAIN`

## Net Summary From DRC

| net | DRC unconnected references |
|---|---:|
| `GND` | 52 |
| `+3V3` | 16 |
| `/ESP_EN` | 10 |
| `/BOOT0` | 8 |
| `/SHIELD` | 8 |
| `/DM_C` | 6 |
| `/DP_C` | 6 |
| `/DM_E` | 4 |
| `/DP_E` | 4 |
| `/+5V_FUSED` | 2 |
| `/+5V_PROTECTED` | 2 |
| `/CC1` | 2 |
| `/CC2` | 2 |
| `/PLED` | 2 |
| `/SLED` | 2 |
| `/STATUS_LED` | 2 |
| `/U0RXD` | 2 |
| `/U0TXD` | 2 |

Counts above are net mentions parsed from the DRC unconnected-item blocks; one unconnected item can mention two endpoints.

## Important Remaining Routing Work

- `/+5V_FUSED`: F1-to-Q1 local route remains unresolved. Direct scripted attempts caused Q1-area crossing/clearance risk, so it was left unrouted.
- USB: CC1/CC2, D+/D- through U3/R8/R9, shield policy route remain unrouted.
- Low-speed/control: ESP_EN, BOOT0, UART, LED, and test-pad routes remain unrouted.
- `+3V3`: local buck segment exists, but distribution to U2, passives, LEDs, and test pads remains incomplete.
- `GND`: many GND connections remain for a future valid GND pour after routing completion.

## Classification

`ROUTING_PARTIAL_NEEDS_REPAIR`

