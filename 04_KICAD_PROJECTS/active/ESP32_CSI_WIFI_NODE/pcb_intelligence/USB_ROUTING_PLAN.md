# USB Routing Plan

## USB Cluster Components

| Ref | Value | Footprint | Cluster | Connected nets | Must be near | Human review |
|---|---|---|---|---|---|---|
| `J2` | `USB-C_NEEDS_REVIEW` | `Connector_USB:USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal` | `USB` | `/CC1`, `/CC2`, `/DM_C`, `/DP_C`, `/SHIELD`, `GND`, `unconnected-(J2-VBUS-PadA4)` | `U3`, `R6`, `R7` | `TRUE` |
| `R5` | `0R_DNI` | `Resistor_SMD:R_0603_1608Metric` | `USB_SHIELD_POLICY` | `/SHIELD`, `GND` | `J2`, `GND` | `FALSE` |
| `R6` | `5.1k_CC1` | `Resistor_SMD:R_0603_1608Metric` | `USB` | `/CC1`, `GND` | `J2` | `FALSE` |
| `R7` | `5.1k_CC2` | `Resistor_SMD:R_0603_1608Metric` | `USB` | `/CC2`, `GND` | `J2` | `FALSE` |
| `R8` | `22R_D-` | `Resistor_SMD:R_0603_1608Metric` | `USB` | `/DM_C`, `/DM_E` | `U3`, `U2` | `FALSE` |
| `R9` | `22R_D+` | `Resistor_SMD:R_0603_1608Metric` | `USB` | `/DP_C`, `/DP_E` | `U3`, `U2` | `FALSE` |
| `U3` | `USB_ESD_REV` | `Package_TO_SOT_SMD:SOT-23-6` | `USB` | `/DM_C`, `/DP_C`, `GND` | `J2`, `R8`, `R9` | `TRUE` |

## USB Nets

| Net | Criticality | Pads | Priority | Width mm | Via policy | Risk |
|---|---|---:|---:|---:|---|---|
| `/DM_C` | `CRITICAL_USB` | 4 | 3 | `0.25` | Avoid vias/stubs; if unavoidable, use symmetric treatment on D+/D- pair. | USB signal integrity/stub risk. |
| `/DM_E` | `CRITICAL_USB` | 3 | 3 | `0.25` | Avoid vias/stubs; if unavoidable, use symmetric treatment on D+/D- pair. | USB signal integrity/stub risk. |
| `/DP_C` | `CRITICAL_USB` | 4 | 3 | `0.25` | Avoid vias/stubs; if unavoidable, use symmetric treatment on D+/D- pair. | USB signal integrity/stub risk. |
| `/DP_E` | `CRITICAL_USB` | 3 | 3 | `0.25` | Avoid vias/stubs; if unavoidable, use symmetric treatment on D+/D- pair. | USB signal integrity/stub risk. |
| `/CC1` | `CRITICAL_USB` | 2 | 4 | `0.25` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | Low to medium; route after critical nets. |
| `/CC2` | `CRITICAL_USB` | 2 | 4 | `0.25` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | Low to medium; route after critical nets. |
| `/SHIELD` | `CRITICAL_USB` | 5 | 4 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | USB shield policy remains human-review required. |

## Routing Rules

- `J2` must be at board edge with mouth off-board.
- `U3` ESD must be close to `J2`.
- `R6/R7` CC resistors must be close to `J2`.
- `R8/R9` series resistors must sit between `U3` and `U2`.
- `/DP_C` and `/DM_C` are connector/ESD-side USB data nets.
- `/DP_E` and `/DM_E` are ESP32-side USB data nets after series resistors.
- USB test pads are stub-risk and need LJ decision before routing.
- `/SHIELD` and `R5` remain USB shield policy review items.
