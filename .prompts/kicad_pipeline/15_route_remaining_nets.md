# 15 Route Remaining Nets

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: route remaining nets only after critical routing is acceptable, then perform trace-by-trace verification.

## Read First

1. `AGENTS.md`
2. `reports/PCB_CRITICAL_NETS_ROUTING_REPORT.md`
3. `reports/PCB_ROUTING_PLAN.md`
4. `09_ACCURACY_ENGINE/pcb_rules/TRACE_ANGLE_ROUTING_RULES.md`
5. `09_ACCURACY_ENGINE/pcb_rules/PCB_ROUTING_QUALITY_RULES.md`
6. `09_ACCURACY_ENGINE/checklists/PCB_ROUTING_QUALITY_CHECKLIST.md`
7. `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`

## Preconditions

If critical routing is not `CRITICAL_ROUTING_PASS` or explicitly acceptable with documented non-blocking warnings, stop.

## Do

1. Create backup.
2. Route remaining signals, LED/button nets, test pad nets, and low-speed misc nets.
3. Use 45-degree bends for normal routing and avoid crude 90-degree or acute-angle geometry.
4. If local placement causes ugly routing, move only the local cluster needed to clean the route.
5. Refill zones only when the scope explicitly allows it.
6. Run DRC.
7. Run ratsnest/unrouted check and confirm no unrouted nets.
8. Export top/bottom visuals and close-ups.
9. Create trace-by-trace audit table with routing-quality findings, not DRC only.
10. Create `reports/PCB_FULL_ROUTING_REPORT.md` and `reports/TRACE_BY_TRACE_AUDIT.md`.

## Required Result

Return one result:

- `FULL_ROUTING_PASS`
- `FULL_ROUTING_FAIL`
- `NEEDS_HUMAN_REVIEW`

AI quality closeout is required.
