# Placement To Routing Feasibility Gate

## Purpose

Turn digital-twin evidence, variants, and route projections into one explicit go/no-go result.

## Placement Start Gate

`placement_gate_status` is `PASS` only when all are true:

1. variant count is at least `3`
2. passing variant count is at least `1`
3. selected variant status is `PASS`
4. selected variant projected open-net count is `0`
5. selected variant connector truth records contain no `FAIL` or `UNKNOWN`
6. selected variant route projections contain no RF keepout crossing

## Routing Continuation Gate

`routing_gate_status` is `PASS` only when:

1. `placement_gate_status` is already `PASS`
2. live board context does not report open-net evidence that still blocks continuation

## Blocking Codes

- `BLOCKED_NEEDS_THREE_VARIANTS`
- `BLOCKED_NO_PASSING_VARIANT`
- `BLOCKED_CONNECTOR_DIRECTION`
- `BLOCKED_PROJECTED_OPEN_NETS`
- `BLOCKED_PROJECTED_KEEP_OUT_CROSSING`
- `BLOCKED_LIVE_OPEN_NETS`
- `BLOCKED_MISSING_EVIDENCE`

## Rule For Real PCB Work

No real PCB placement may begin until the latest prelayout result records:

- at least `3` generated variants
- at least `1` passing variant
- `placement_gate_status: PASS`

No real PCB routing may begin until the latest prelayout result also records:

- `routing_gate_status: PASS`

This gate does not replace:

- schematic-to-PCB rules
- footprint verification
- live-state gating
- DRC
- human review for high-risk mechanical facts

It adds an earlier deterministic stop layer.
