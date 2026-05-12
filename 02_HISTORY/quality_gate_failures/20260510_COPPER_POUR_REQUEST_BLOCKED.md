# Copper Pour Request Blocked

Date: `2026-05-10`
Project: `ESP32_CSI_WIFI_NODE`

## Failure Reason

Copper-pour progression was requested, but the upstream real-routing report did
not reach the required ready state.

Required:

- `REAL_ROUTING_READY_FOR_COPPER_POUR`

Actual:

- `REAL_ROUTING_BLOCKED`

## Additional Context

- live PCB quality gate remains `FAIL_DRC`
- live board still has `13` unconnected items and `3` detectable unrouted nets
