# Trace Audit Schema

## Purpose

Define the minimum per-trace audit fields required by the routing engine.

## Required Per-Trace Fields

Each trace audit entry must include:

- `net`
- `critical`
- `routing_status`
- `segment_count`
- `via_count`
- `via_reason`
- `widths_mm`
- `angles_deg`
- `issues`
- `review_required`

## Required Issue Detection

The audit must be able to flag:

- `no_segments`
- `right_angle_turn`
- `acute_or_nonstandard_angle`
- `vias_without_reason`
- `trace_crosses_rf_keepout`
- `trace_crosses_antenna_keepout`
- `critical_trace_unrouted`
- `usb_pair_incomplete`
- `power_trace_too_narrow`
- `trace_missing_from_audit`

## Required Summary Fields

The audit output must include:

- `trace_count`
- `flagged_count`
- `critical_trace_count`
- `audit_complete`
- `missing_trace_nets`
- `hard_fails`

## Completeness Rule

The trace-by-trace audit is incomplete when:

- a routed trace exists but has no audit entry
- a critical routed net has no trace audit entry
- the audit output does not contain per-trace issue lists

Incomplete trace audit is a hard fail for readiness.
