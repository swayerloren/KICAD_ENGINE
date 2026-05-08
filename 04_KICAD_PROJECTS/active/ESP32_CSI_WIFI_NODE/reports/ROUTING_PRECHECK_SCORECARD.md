# ESP32_CSI_WIFI_NODE Routing Precheck Scorecard

Date: `2026-05-07`

Final result: `ROUTING_BLOCKED`

Source score JSON:

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/real_board_routing_audit/score.json`

## Status

- score status: `AUTO_BLOCKED_BAD_LAYOUT`
- total score: `62`
- hard fail count: `3`

## Category Scores

| Category | Score |
| --- | ---: |
| critical_net_completeness | `13` |
| power_path_quality | `15` |
| usb_path_quality | `10` |
| rf_keepout_compliance | `15` |
| via_count_reasonableness | `10` |
| unrouted_net_count | `0` |
| drc_risk | `4` |
| trace_audit_completeness | `0` |
| human_review_risk | `5` |

## Hard Fails

- `GND strategy missing`
- `critical power net missing`
- `unrouted critical net`

## Blocking Reasons

- `16 unrouted nets remain`
- `3 trace audit entries flagged`
- `GND strategy missing`
- `critical power net missing`
- `routing plan did not pass`
- `unrouted critical net`

## Trace Audit Findings

Flagged trace count: `3`

Flagged routed nets:

- `+3V3`
  - `acute_or_nonstandard_angle`
  - `right_angle_turn`
- `/+5V_IN`
  - `right_angle_turn`
- `/+5V_PROTECTED`
  - `right_angle_turn`

## DRC Context

Live-board audit DRC summary:

- risk: `HIGH`
- violations: `12`
- errors: `12`
- warnings: `0`
- unconnected: `65`

## Interpretation

This scorecard is sufficient to block routing start.

The board can be analyzed by the routing engine, but it is not ready for routing execution.
