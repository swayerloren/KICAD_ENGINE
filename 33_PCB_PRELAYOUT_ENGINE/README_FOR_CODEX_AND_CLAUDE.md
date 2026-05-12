# Readme For Codex And Claude

## Use This Folder When

- the task is pre-placement planning
- the task is placement-versus-routing feasibility
- the task is connector-direction review before routing
- the task must compare multiple PCB variants before touching a real board

## Minimum Agent Sequence

1. Extract the board digital twin.
2. Generate at least three variants.
3. Project 45-degree routes for each variant.
4. Score each variant.
5. Compare variants.
6. Run the prelayout gate.
7. Stop if `placement_gate_status` is blocked before real PCB placement.
8. Stop if `routing_gate_status` is blocked before real PCB routing.

## Do Not Claim

- that the board is routing-ready because one variant looks neat
- that DRC quietness alone makes the board acceptable
- that open nets can be deferred after routing starts
- that connector orientation can be fixed later without variant regeneration
