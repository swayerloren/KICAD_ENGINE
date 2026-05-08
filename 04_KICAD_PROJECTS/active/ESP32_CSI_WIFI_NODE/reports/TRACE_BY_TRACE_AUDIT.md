# ESP32_CSI_WIFI_NODE Trace-By-Trace Audit

Date: 2026-05-06

Status: `NO_TRACES_TO_AUDIT`

Final classification: `BLOCKED`

## Scope

Audit routed traces after full remaining-net routing.

## Audit Result

No traces were routed during this session. There is no `.kicad_pcb` file and no critical routing pass.

## Trace Groups

| Trace group | Audit result |
|---|---:|
| Critical power traces | `NOT_PRESENT_CRITICAL_ROUTING_BLOCKED` |
| Buck regulator loop traces | `NOT_PRESENT_CRITICAL_ROUTING_BLOCKED` |
| USB D+/D- traces | `NOT_PRESENT_CRITICAL_ROUTING_BLOCKED` |
| LED traces | `NOT_PRESENT_FULL_ROUTING_BLOCKED` |
| Test pad traces | `NOT_PRESENT_FULL_ROUTING_BLOCKED` |
| UART/debug traces | `NOT_PRESENT_FULL_ROUTING_BLOCKED` |
| Miscellaneous low-speed traces | `NOT_PRESENT_FULL_ROUTING_BLOCKED` |

## DRC And Unrouted State

DRC result: `NOT_RUN_NO_PCB`

Unrouted net count: `UNKNOWN_NO_PCB`

## Disposition

Routing remains blocked until critical routing passes on an actual PCB.
