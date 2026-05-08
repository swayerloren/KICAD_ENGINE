# Routing Feasibility Rules

## Purpose

Require projected routing thought before actual routing begins.

## Core Rules

- Every layout variant must include projected routing, not just component positions.
- Project the power path before accepting a connector or regulator placement.
- Project the USB or other critical data path before accepting connector orientation.
- Identify likely congestion, forced via escapes, blocked channels, and keepout collisions.
- Reject placements that make clean routing unlikely even if the parts seem to fit physically.
- Do not defer all routing thought until after placement.

## Minimum Projected Paths

- power input path
- switching-regulator cluster path
- local power-distribution path
- USB/data path when present
- debug/test accessibility path when relevant

## Optional FreeRouting Evidence

- FreeRouting dry-run output may be used as optional congestion evidence.
- FreeRouting output remains `REVIEW_ONLY`.
- Use it to compare unrouted nets, via pressure, congestion hints, and impossible placements.
- Do not use it to auto-approve USB, RF, switching-regulator, or high-current routing.
- If FreeRouting is unavailable, fall back to manual routing-feasibility reasoning.

## Variant Failure Conditions

- obvious crossing dependencies
- blocked USB or power channel
- forced routing through RF keepout
- connector placement that implies long awkward detours
- switching cluster that cannot stay compact
