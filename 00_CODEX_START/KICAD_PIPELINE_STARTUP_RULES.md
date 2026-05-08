# KiCad Pipeline Startup Rules

Status: `ACTIVE_STARTUP_RULES`

## Purpose

These startup rules make the schematic-to-PCB-to-routing-to-fabrication pipeline mandatory for future KiCad project work.

## Required Read

Before schematic review, PCB update, PCB setup, placement, routing, or fabrication-style export, agents must read:

1. `AGENTS.md`
2. `README_GPT.md`
3. `FOR CHAT GPT.MD`
4. `00_CODEX_START/START_HERE.md`
5. `00_CODEX_START/SESSION_START_CHECKLIST.md`
6. `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`
7. `09_ACCURACY_ENGINE/checklists/FULL_PIPELINE_GATE_CHECKLIST.md`
8. The relevant `.prompts/kicad_pipeline/NN_*.md`
9. Active project memory/history

## Mandatory Pipeline Rule

Future KiCad projects must follow the pipeline gates unless the user explicitly approves an exception.

Pipeline prompt pack:

- `.prompts/kicad_pipeline/01_schematic_annotation_and_completeness.md`
- `.prompts/kicad_pipeline/02_schematic_visual_closeup_audit.md`
- `.prompts/kicad_pipeline/03_schematic_visual_repair.md`
- `.prompts/kicad_pipeline/04_schematic_electrical_audit.md`
- `.prompts/kicad_pipeline/05_footprint_package_audit.md`
- `.prompts/kicad_pipeline/06_schematic_to_pcb_gate.md`
- `.prompts/kicad_pipeline/07_update_pcb_from_schematic.md`
- `.prompts/kicad_pipeline/08_pcb_mechanical_setup.md`
- `.prompts/kicad_pipeline/09_pcb_placement_pass_1.md`
- `.prompts/kicad_pipeline/10_pcb_placement_pass_2_orientation.md`
- `.prompts/kicad_pipeline/11_holes_pads_vias_strategy.md`
- `.prompts/kicad_pipeline/12_copper_zones_setup.md`
- `.prompts/kicad_pipeline/13_routing_plan_only.md`
- `.prompts/kicad_pipeline/14_route_critical_nets.md`
- `.prompts/kicad_pipeline/15_route_remaining_nets.md`
- `.prompts/kicad_pipeline/16_final_pcb_verification.md`
- `.prompts/kicad_pipeline/17_export_not_final_fab_package.md`

## Exception Logging

Exceptions must be logged with:

- reason
- gate affected
- risk
- human-review-required flag
- user approval source
- evidence path

If an exception affects PCB update, routing, or fabrication output, create a quality-gate failure or exception record in project history.

## Stop Conditions

Stop rather than proceed when:

- required reports are missing
- required report status is not pass/ready
- footprints are unverified
- connector orientation is unverified
- DRC was required but not run
- no `.kicad_pcb` exists for PCB tasks
- manufacturing output was requested before final PCB verification allows it

