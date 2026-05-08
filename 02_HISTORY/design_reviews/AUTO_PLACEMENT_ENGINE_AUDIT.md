# AUTO_PLACEMENT_ENGINE_AUDIT

Date: `2026-05-07`

Classification: `PLANNING_LAYER_CREATED`

## Summary

This patch adds the first deterministic automatic PCB placement-planning layer to KiCad Engine.

The new layer is for:

- placement constraints
- fixed mechanical placement
- grouped placement
- overlap / keepout / edge-clearance detection
- precheck scoring

It is not a claim of complete automatic placement or fabrication-ready placement quality.

## Files Created

- `14_LAYOUT_AUTOMATION/AUTO_PLACEMENT_ENGINE.md`
- `14_LAYOUT_AUTOMATION/PLACEMENT_CONSTRAINTS_SCHEMA.md`
- `14_LAYOUT_AUTOMATION/PLACEMENT_GROUPING_RULES.md`
- `14_LAYOUT_AUTOMATION/FIXED_MECHANICAL_PLACEMENT_RULES.md`
- `14_LAYOUT_AUTOMATION/POWER_PATH_PLACEMENT_RULES.md`
- `14_LAYOUT_AUTOMATION/USB_PLACEMENT_RULES.md`
- `14_LAYOUT_AUTOMATION/RF_ANTENNA_PLACEMENT_RULES.md`
- `14_LAYOUT_AUTOMATION/TEST_PAD_PLACEMENT_RULES.md`
- `14_LAYOUT_AUTOMATION/PLACEMENT_DRC_PRECHECK_RULES.md`
- `14_LAYOUT_AUTOMATION/scripts/_placement_common.py`
- `14_LAYOUT_AUTOMATION/scripts/generate_placement_constraints.py`
- `14_LAYOUT_AUTOMATION/scripts/place_fixed_mechanical_parts.py`
- `14_LAYOUT_AUTOMATION/scripts/place_component_groups.py`
- `14_LAYOUT_AUTOMATION/scripts/detect_placement_collisions.py`
- `14_LAYOUT_AUTOMATION/scripts/score_component_placement.py`
- `14_LAYOUT_AUTOMATION/scripts/README.md`

## Files Updated

- `14_LAYOUT_AUTOMATION/README.md`
- `14_LAYOUT_AUTOMATION/INDEX.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `01_MEMORY/DESIGN_RULES_MEMORY.md`

## Rule Coverage

The placement engine now encodes:

- board outline first
- mounting holes before nearby placement
- USB-C and barrel jack or input connector as fixed mechanical parts
- RF module and antenna keepout before nearby placement
- power path in physical current-flow order
- USB ESD local to the connector
- test pad accessibility requirements
- courtyard-overlap failure
- board-edge-clearance checks
- placement rejection when routing is obviously impossible

## Validation

- `python -m py_compile` passed for all new placement scripts.
- No KiCad design files were edited.
- Active project hashes remained unchanged for:
  - `.kicad_pcb`
  - `.kicad_sch`
  - `.kicad_pro`

## Residual Risk

This layer has syntax-checked scripts and documented behavior, but it has not yet been run on a full project placement-input dataset in this session.
