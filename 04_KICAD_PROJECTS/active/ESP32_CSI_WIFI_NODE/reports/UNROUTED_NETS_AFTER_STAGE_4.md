# Unrouted Nets After Stage 4

Status: `NOT_MEASURED_BLOCKED`

Generated: `2026-05-07`

Project: `ESP32_CSI_WIFI_NODE`

## Result

Stage 4 routing was not performed, so there is no valid post-Stage-4 unrouted-net count.

Reason:

`PHASE_GATE_BLOCKED_PRIOR_ROUTING_STAGES_NOT_COMPLETE`

## Latest Available Context

The latest reviewed pre-routing/post-orientation DRC reported:

- Unconnected pads: `78`
- DRC violations: `12 x U2 pad 41 drill_out_of_range`
- Footprint errors: `0`

This is not a Stage 4 result because no Stage 4 traces were added.

## Required Future Measurement

When routing is allowed and Stage 4 is actually completed, rerun DRC with schematic parity and record:

- remaining unrouted count
- remaining unrouted nets by name
- DRC errors/warnings by category
- whether remaining GND connections are expected to be resolved by copper pour

GND copper pour may begin: `NO`

