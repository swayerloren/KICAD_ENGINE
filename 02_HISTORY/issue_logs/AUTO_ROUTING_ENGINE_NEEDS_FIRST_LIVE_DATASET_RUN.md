# AUTO_ROUTING_ENGINE_NEEDS_FIRST_LIVE_DATASET_RUN

Date: `2026-05-07`

Status: `OPEN`

## Issue

The new auto routing engine has documentation and syntax-checked scripts, but it has not yet been exercised on a real routing-plan or routing-state dataset in this session.

## Next Step

Create one source-backed routing input JSON for a sandbox-approved project and run:

1. `generate_routing_plan.py`
2. `route_critical_nets_plan.py`
3. `detect_unrouted_nets.py`
4. `detect_trace_keepout_violations.py`
5. `trace_by_trace_audit.py`
6. `score_routing_plan.py`

Then record the first live results and refine heuristics only if the evidence justifies it.
