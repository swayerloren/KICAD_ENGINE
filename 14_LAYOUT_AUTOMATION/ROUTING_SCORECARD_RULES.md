# Routing Scorecard Rules

## Purpose

Define strict routing-plan scoring for the automatic routing engine.

This scorecard is for planning and audit readiness, not fabrication approval.

## Status Values

- `PASS`
- `AUTO_BLOCKED_MISSING_DATA`
- `AUTO_BLOCKED_BAD_LAYOUT`

## Score Categories

The routing score must include all of these:

1. `critical_net_completeness`
2. `power_path_quality`
3. `usb_path_quality`
4. `rf_keepout_compliance`
5. `via_count_reasonableness`
6. `unrouted_net_count`
7. `drc_risk`
8. `trace_audit_completeness`
9. `human_review_risk`

## Hard Fail Rules

Hard fail if any of these are true:

1. critical power net missing
2. USB D+/D- incomplete
3. trace crosses RF keepout
4. trace crosses antenna keepout
5. unrouted critical net
6. GND strategy missing
7. regulator critical loop not planned
8. via used without reason on critical net
9. trace-by-trace audit missing or incomplete

## Scoring Intent

- Critical-net completeness should dominate the score.
- Power-path quality should reward correct current-flow planning, appropriate width, and compact critical-loop intent.
- USB-path quality should reward complete D+/D- planning, pairing awareness, and local ESD/series/CC routing intent.
- RF-keepout compliance should drop to zero when any RF/antenna keepout crossing exists.
- Via-count reasonableness should penalize unnecessary vias and undefined via reasons on critical nets.
- Unrouted-net count should penalize all unrouted nets, with stronger penalty for critical nets.
- DRC risk should reflect keepout crossings, malformed data, missing layer/clearance information, and geometric issues found in the audit.
- Trace-audit completeness should require one audit entry per routed trace.
- Human-review risk should remain visible even on a passing plan when USB, RF, switching-loop, or high-current nets exist.

## Readiness Rule

The routing engine is ready for a real copied-KiCad PCB test only when:

- fixture tests pass,
- hard-fail handling works,
- JSON and Markdown outputs are generated,
- trace-by-trace audit completeness is proven, and
- the engine still labels routed results `REVIEW_ONLY` rather than fabrication-ready.
