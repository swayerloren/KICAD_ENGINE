# Routing Current State Report

Date: `2026-05-07`

Result: `PARTIAL_ROUTING_AUDITED_NOT_VERIFIED_FOR_NEW_ROUTING`

Board hash in this audit: `0CFE639213D3B0A111F5D06E728A3F7F34B55674DC27312B00D39F80235B2844`

## Current Routing Inventory

| Item | Result |
| --- | --- |
| Track segments | `24` |
| Grouped traces | `6` |
| Vias | `2` |
| Zones | `0` |
| Bottom-copper routed content | `YES - one +3V3 path segment through the via pair` |

## Routed Nets Present

- `/+5V_IN`
- `/+5V_FUSED`
- `/+5V_PROTECTED`
- `/BUCK_SW`
- `/BUCK_BST`
- `+3V3`

These match the live board and the earlier Stage 1/2 power cleanup report.

## Detectable Unrouted Nets

Count: `16`

- `unconnected-(J2-VBUS-PadA4)`
- `/BOOT0`
- `/ESP_EN`
- `/PLED`
- `/SLED`
- `/STATUS_LED`
- `/CC1`
- `/CC2`
- `/DM_C`
- `/DM_E`
- `/DP_C`
- `/DP_E`
- `/SHIELD`
- `/U0RXD`
- `/U0TXD`
- `GND`

## DRC / Audit State

| Item | Result |
| --- | --- |
| DRC violations | `12` |
| Unconnected items | `65` |
| Trace-audit flagged entries | `3` |
| Trace-audit issue nets | `+3V3`, `/+5V_IN`, `/+5V_PROTECTED` |
| Zones / GND strategy | `MISSING` |

Trace-audit geometry findings:

- `+3V3`: `acute_or_nonstandard_angle`, `right_angle_turn`
- `/+5V_IN`: `right_angle_turn`
- `/+5V_PROTECTED`: `right_angle_turn`

## Decision

Routing exists on the live board.

Current existing traces were audited in this session.

Further routing may not continue yet because:

- the current routed geometry is not fully verified for continuation
- `16` unrouted nets remain
- `65` unconnected items remain
- `12` DRC drill-rule violations remain
- no accepted GND strategy exists

No new traces were added in this session.
