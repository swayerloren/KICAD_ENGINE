# Real Routing Apply Blocked

Date: `2026-05-10`
Project: `ESP32_CSI_WIFI_NODE`

## Failure Reason

Real routing application was requested, but the upstream copied-board rehearsal
never reached the required ready state.

Required:

- `COPIED_ROUTING_READY_FOR_REAL_BOARD`

Actual:

- `COPIED_ROUTING_BLOCKED`

## Additional Blocking State

- live PCB quality gate remains `FAIL_DRC`
- prompt-counter maintenance is now due
