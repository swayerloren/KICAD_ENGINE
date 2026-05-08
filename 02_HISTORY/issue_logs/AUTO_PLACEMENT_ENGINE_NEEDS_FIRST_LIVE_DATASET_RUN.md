# AUTO_PLACEMENT_ENGINE_NEEDS_FIRST_LIVE_DATASET_RUN

Date: `2026-05-07`

Status: `OPEN`

## Issue

The new auto placement engine has documentation and syntax-checked scripts, but it has not yet been exercised on a real project placement dataset in this session.

## Next Step

Create one source-backed placement input JSON for a sandbox-approved project and run:

1. `generate_placement_constraints.py`
2. `place_fixed_mechanical_parts.py`
3. `place_component_groups.py`
4. `detect_placement_collisions.py`
5. `score_component_placement.py`

Then record the first live results and adjust heuristics only if the evidence justifies it.
