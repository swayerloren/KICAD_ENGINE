# Layout Automation Index

`14_LAYOUT_AUTOMATION/` documents realistic routing and placement assistance, not magic autorouting claims.

## Start Here

- [README.md](README.md)
- [ROADMAP.md](ROADMAP.md)
- [REAL_PROJECT_ROUTING_WORKFLOW.md](REAL_PROJECT_ROUTING_WORKFLOW.md)
- [REAL_PROJECT_ROUTING_STOP_CONDITIONS.md](REAL_PROJECT_ROUTING_STOP_CONDITIONS.md)

## Key Rule Sets

- USB: [USB_TRACE_RULES.md](USB_TRACE_RULES.md)
- Power: [POWER_TRACE_RULES.md](POWER_TRACE_RULES.md)
- Critical nets: [CRITICAL_NET_ROUTING_RULES.md](CRITICAL_NET_ROUTING_RULES.md)
- RF keepout: [RF_KEEP_OUT_TRACE_RULES.md](RF_KEEP_OUT_TRACE_RULES.md)
- Trace audit: [TRACE_BY_TRACE_VERIFICATION_RULES.md](TRACE_BY_TRACE_VERIFICATION_RULES.md)
- Scorecards: [ROUTING_SCORECARD_RULES.md](ROUTING_SCORECARD_RULES.md)

## Scripts

- `scripts/generate_routing_plan.py`
- `scripts/route_critical_nets_plan.py`
- `scripts/trace_by_trace_audit.py`
- `scripts/run_real_board_routing_audit.py`
- extraction helpers under `scripts/`

## Important Constraint

Real live-board edits must preserve DRC cleanliness and should be rehearsed on copied boards first.
