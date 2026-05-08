# AUTO_ROUTING_ENGINE_AUDIT

Date: `2026-05-07`

Classification: `PLANNING_LAYER_CREATED`

## Summary

This patch adds the first deterministic routing-planning and routing-audit layer to KiCad Engine.

The new layer is for:

- staged routing plans
- critical-net-first routing plans
- unrouted-net detection
- keepout-violation detection
- trace-by-trace audit
- routing-plan scoring

It is not a claim of complete automatic routing or fabrication-ready routing quality.

## Files Created

- `14_LAYOUT_AUTOMATION/AUTO_ROUTING_ENGINE.md`
- `14_LAYOUT_AUTOMATION/TRACE_PLANNING_RULES.md`
- `14_LAYOUT_AUTOMATION/CRITICAL_NET_ROUTING_RULES.md`
- `14_LAYOUT_AUTOMATION/POWER_TRACE_RULES.md`
- `14_LAYOUT_AUTOMATION/USB_TRACE_RULES.md`
- `14_LAYOUT_AUTOMATION/RF_KEEP_OUT_TRACE_RULES.md`
- `14_LAYOUT_AUTOMATION/VIA_STRATEGY_RULES.md`
- `14_LAYOUT_AUTOMATION/GROUND_STITCHING_RULES.md`
- `14_LAYOUT_AUTOMATION/TRACE_BY_TRACE_VERIFICATION_RULES.md`
- `14_LAYOUT_AUTOMATION/scripts/_routing_common.py`
- `14_LAYOUT_AUTOMATION/scripts/generate_routing_plan.py`
- `14_LAYOUT_AUTOMATION/scripts/route_critical_nets_plan.py`
- `14_LAYOUT_AUTOMATION/scripts/score_routing_plan.py`
- `14_LAYOUT_AUTOMATION/scripts/detect_unrouted_nets.py`
- `14_LAYOUT_AUTOMATION/scripts/detect_trace_keepout_violations.py`
- `14_LAYOUT_AUTOMATION/scripts/trace_by_trace_audit.py`

## Files Updated

- `14_LAYOUT_AUTOMATION/README.md`
- `14_LAYOUT_AUTOMATION/INDEX.md`
- `14_LAYOUT_AUTOMATION/scripts/README.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `01_MEMORY/DESIGN_RULES_MEMORY.md`

## Rule Coverage

The routing engine now encodes:

- critical nets first
- power/protection before low-risk nets
- regulator-loop priority
- 3V3 before cosmetic nets
- USB pair priority and cleanliness expectations
- no trace crossing RF antenna keepout
- via minimization and via-reason expectations
- trace-by-trace audit requirement
- autorouting remains `REVIEW_ONLY` unless fully audited

## Validation

- `python -m py_compile` passed for all new routing scripts.
- No KiCad design files were edited.
- Active project hashes remained unchanged for:
  - `.kicad_pcb`
  - `.kicad_sch`
  - `.kicad_pro`

## Residual Risk

This layer has syntax-checked scripts and documented behavior, but it has not yet been exercised on a full routing-plan input dataset in this session.
