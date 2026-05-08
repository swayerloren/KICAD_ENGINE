# ESP32_CSI_WIFI_NODE_COPIED_CRITICAL_ROUTING_REHEARSAL_BLOCKED

Date: `2026-05-07`

Status: `OPEN`

## Blocking Condition

Copied-board critical-net routing rehearsal is blocked by the explicit precondition in the user request:

- `REAL_PCB_ROUTING_PLAN.md` must be `ROUTING_READY`

Current status:

- `REAL_PCB_ROUTING_PLAN.md` is `ROUTING_BLOCKED`

## Impact

Do not create a copied-board routing rehearsal folder and do not route even a copied board until the routing plan and routing-start blockers are cleared.
