# Critical Net Routing Rules

## Critical Power Nets

| Net | Criticality | Pads | Priority | Width mm | Via policy | Risk |
|---|---|---:|---:|---:|---|---|
| `/BUCK_BST` | `CRITICAL_POWER` | 2 | 1 | `0.2` | Avoid vias; keep local to U1/L1/C6. | Switching noise and loop-area risk; keep away from USB/RF. |
| `/BUCK_SW` | `CRITICAL_POWER` | 3 | 1 | `0.5` | Avoid vias; keep local to U1/L1/C6. | Switching noise and loop-area risk; keep away from USB/RF. |
| `+3V3` | `CRITICAL_POWER` | 11 | 2 | `0.5` | Vias acceptable only when current path and return path remain low impedance. | Brownout/voltage-drop risk if distribution or return is poor. |
| `/+5V_FUSED` | `CRITICAL_POWER` | 2 | 2 | `0.75` | Vias acceptable only when current path and return path remain low impedance. | Power input/protection path and barrel jack mechanical decision affect route. |
| `/+5V_IN` | `CRITICAL_POWER` | 2 | 2 | `0.75` | Vias acceptable only when current path and return path remain low impedance. | Power input/protection path and barrel jack mechanical decision affect route. |
| `/+5V_PROTECTED` | `CRITICAL_POWER` | 7 | 2 | `0.75` | Vias acceptable only when current path and return path remain low impedance. | Power input/protection path and barrel jack mechanical decision affect route. |

## Critical USB Nets

| Net | Criticality | Pads | Priority | Width mm | Via policy | Risk |
|---|---|---:|---:|---:|---|---|
| `/DM_C` | `CRITICAL_USB` | 4 | 3 | `0.25` | Avoid vias/stubs; if unavoidable, use symmetric treatment on D+/D- pair. | USB signal integrity/stub risk. |
| `/DM_E` | `CRITICAL_USB` | 3 | 3 | `0.25` | Avoid vias/stubs; if unavoidable, use symmetric treatment on D+/D- pair. | USB signal integrity/stub risk. |
| `/DP_C` | `CRITICAL_USB` | 4 | 3 | `0.25` | Avoid vias/stubs; if unavoidable, use symmetric treatment on D+/D- pair. | USB signal integrity/stub risk. |
| `/DP_E` | `CRITICAL_USB` | 3 | 3 | `0.25` | Avoid vias/stubs; if unavoidable, use symmetric treatment on D+/D- pair. | USB signal integrity/stub risk. |
| `/CC1` | `CRITICAL_USB` | 2 | 4 | `0.25` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | Low to medium; route after critical nets. |
| `/CC2` | `CRITICAL_USB` | 2 | 4 | `0.25` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | Low to medium; route after critical nets. |
| `/SHIELD` | `CRITICAL_USB` | 5 | 4 | `0.2` | Vias acceptable when useful; keep away from RF keepout and connector mechanical areas. | USB shield policy remains human-review required. |

## Ground

| Net | Criticality | Pads | Priority | Width mm | Via policy | Risk |
|---|---|---:|---:|---:|---|---|
| `GND` | `GROUND` | 41 | 2 | `None` | Use ground vias for low-impedance returns/stitching; avoid ESP32 RF keepout. | Low to medium; route after critical nets. |

## Rules

- All routing in this file must follow `09_ACCURACY_ENGINE/pcb_rules/TRACE_ANGLE_ROUTING_RULES.md`.
- All routing in this file must follow `09_ACCURACY_ENGINE/pcb_rules/PCB_ROUTING_QUALITY_RULES.md`.
- Route power input and buck regulator loop before low-speed/debug nets.
- Keep `/BUCK_SW` and `/BUCK_BST` very short and local to `U1/C6/L1`.
- Keep power routing clean with 45-degree-style transitions; do not leave crude square turns on wide power nets.
- Keep USB D+/D- short, smooth, and paired as practical; avoid stubs and unnecessary vias.
- Avoid 90-degree corners and acute bends on all critical nets.
- Do not route under ESP32 RF keepout.
- If local placement causes awkward routing, move only the local cluster required to clean the route.
- DRC pass alone does not approve routing quality.
