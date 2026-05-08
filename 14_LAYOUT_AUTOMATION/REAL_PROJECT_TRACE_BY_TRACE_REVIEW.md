# Real Project Trace By Trace Review

## Purpose

Define the minimum per-trace review content required during real PCB routing.

## Required Entry Per Trace

Every routed trace must have an entry containing:

1. net name
2. routing pass
3. whether the net is critical
4. segment count
5. via count
6. via reason
7. width used
8. layer usage
9. whether pair matching is relevant
10. whether RF or antenna keepouts are nearby
11. issue list
12. reroute required: `YES` or `NO`

## Required Issue Types

The review must be able to call out:

- right-angle geometry
- acute or nonstandard bends
- unnecessary detours
- long diagonal shortcuts through unrelated areas
- critical-net via without reason
- power trace too narrow
- USB pair asymmetry that looks suspicious
- keepout proximity concern
- keepout crossing
- ugly pad entry or exit
- likely placement-caused routing problem

## Critical Trace Review

Critical nets require extra notes:

- why the route order is correct
- why any via is justified
- whether the path is short and local enough
- whether the route threatens RF, USB, or switching-noise boundaries

## Completeness Rule

The trace-by-trace review is incomplete when:

- any routed trace is missing an entry
- any critical trace is missing an entry
- issue fields are blank or generic

Incomplete trace-by-trace review is a routing stop condition.

## Review Result States

Use these states per trace:

- `PASS_REVIEW_ONLY`
- `REROUTE_REQUIRED`
- `BLOCKED_BY_PLACEMENT`
- `REQUIRES_HUMAN_REVIEW`
