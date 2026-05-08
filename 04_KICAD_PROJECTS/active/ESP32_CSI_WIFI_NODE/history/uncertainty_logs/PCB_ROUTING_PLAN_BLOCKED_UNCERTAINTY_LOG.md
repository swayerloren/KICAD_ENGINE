# PCB Routing Plan Uncertainty Log

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

## Status

`UNVERIFIED_ROUTING_CONSTRAINTS`

## Uncertainties

| Item | Severity | Confidence | Human review required | Notes |
|---|---|---|---|---|
| Trace widths | `HIGH` | `LOW` | Yes | No board stackup, fab profile, current budget, or placement exists. |
| Clearances | `HIGH` | `LOW` | Yes | No selected verified fab constraints or board rules exist. |
| Via sizes and via policy | `HIGH` | `LOW` | Yes | Hole/test-pad/via strategy is blocked. |
| USB D+/D- geometry | `HIGH` | `LOW` | Yes | No stackup, connector placement, or impedance target exists. |
| ESP32 antenna keepout | `HIGH` | `LOW` | Yes | No PCB placement or exact keepout geometry exists. |
| Regulator switcher layout | `HIGH` | `LOW` | Yes | No placement or source-backed component layout evidence exists. |
| CAN routing applicability | `MEDIUM` | `LOW` | Yes | CAN rules were read, but CAN presence/applicability for this project was not established in this task. |

## Resolution

Keep routing blocked until prior PCB gates pass and exact constraints are source-backed or user-confirmed.

