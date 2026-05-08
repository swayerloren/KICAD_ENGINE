# Real Project Routing Stop Conditions

## Purpose

Define exactly when Codex/Claude must stop routing a real PCB instead of pushing through bad conditions.

## Immediate Stop Conditions

Stop routing immediately if any of these occur:

1. schematic gate is no longer exact `PASS`
2. PCB sync becomes invalid or stale
3. placement changes make the routing plan obsolete
4. DRC precheck fails in a way that blocks current routing
5. trace crosses RF keepout
6. trace crosses antenna keepout
7. critical power net is missing or broken
8. USB D+/D- becomes incomplete
9. regulator critical loop becomes long, awkward, or placement-blocked
10. via appears on a critical net without reason
11. any 90-degree bend appears in routed work without explicit justification
12. any non-45 acute jog appears
13. critical-net pad entry geometry becomes poor
14. unnecessary zigzags or critical detours appear
15. trace width drops below the assigned target without explicit justification
16. trace-by-trace review becomes incomplete
17. routing quality is visually crude even if DRC does not flag it

## Stop And Re-Plan Conditions

Stop the current pass and re-plan if:

- a route can only be finished with awkward geometry
- local placement is forcing ugly routing
- repeated keepout pressure suggests the board shape or placement is wrong
- USB path quality degrades
- power path quality degrades
- geometry hard-fail status appears in the trace audit
- routing scorecard drops to blocked state
- staged routing runner reports `STAGE_BLOCKED`
- no-progress detector reports `BLOCKED_REPAIR_MODE`

## Stop And Escalate Conditions

Stop and require human review if:

- connector orientation is still uncertain
- RF boundary impact is unclear
- USB pair quality cannot be judged confidently
- real DRC and routing-engine output disagree and the reason is unclear
- a high-current or switching-node compromise is required
- geometry checker flags a route but the recommended fix is not obvious

## Required Output On Stop

When routing stops, create or update evidence showing:

- exact stop reason
- current routing pass
- affected nets
- blocker source
- recommended targeted repair stage when `BLOCKED_REPAIR_MODE` applies
- whether reroute, placement repair, or human review is required

## Rule

Do not keep routing just because some progress was made. Once a stop condition is hit, routing is blocked until the exact problem is resolved.
