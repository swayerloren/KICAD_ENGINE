# Auto Routing Engine

## Purpose

Define the automatic routing-planning and routing-verification intelligence layer used before or alongside controlled PCB routing work.

This layer is for:

- routing-order planning
- critical-net-first sequencing
- trace-rule encoding
- unrouted-net detection
- keepout-violation detection
- trace-by-trace audit
- routing-plan scoring

It is not a claim of complete automatic autorouting.

## Scope

The engine may:

- generate routing plans from normalized net metadata
- split out critical-net routing plans
- score routing intent and routing results
- detect unrouted nets
- detect keepout violations
- audit traces one by one

The engine may not:

- blindly approve autorouter output
- ignore DRC
- ignore keepout crossings
- ignore poor trace geometry
- replace human review for USB, RF, switching loops, or high-current routing

## Routing Order

Use this exact order:

1. power input and protection
2. regulator critical loop
3. 3V3 rail
4. USB D+/D-
5. ESD/protection connections
6. ESP32 EN/BOOT
7. decoupling connections
8. LEDs/buttons
9. test pads
10. low-risk remaining nets

## Core Rules

- Critical nets route first.
- Do not cross antenna keepout.
- Keep USB D+/D- clean and paired where practical.
- Keep regulator switching loop short.
- Avoid unnecessary vias.
- Use vias only with reason.
- Every trace must appear in the trace-by-trace audit.
- DRC must pass after routing.
- No unrouted nets are allowed before final routing pass.
- Autorouting output, if used, is `REVIEW_ONLY` unless fully audited.

## Required Outputs

- routing plan
- critical-net routing plan
- unrouted-net report
- keepout-violation report
- trace-by-trace audit
- routing score
- JSON and Markdown outputs for every stage

## Required Inputs

Use the normalized schema defined in:

- `ROUTING_INPUT_SCHEMA.md`
- `NET_CLASS_SCHEMA.md`

Use the output expectations defined in:

- `ROUTING_OUTPUT_SCHEMA.md`
- `TRACE_AUDIT_SCHEMA.md`
- `ROUTING_SCORECARD_RULES.md`

Test against:

- `test_fixtures/`
- `reports/ROUTING_ENGINE_FIXTURE_TEST_REPORT.md`

## Boundary

This engine is a planning and audit layer. It does not prove professional routing quality by itself. Routing is not complete until DRC, unrouted-net checks, routing-quality review, and critical-net review all pass.
