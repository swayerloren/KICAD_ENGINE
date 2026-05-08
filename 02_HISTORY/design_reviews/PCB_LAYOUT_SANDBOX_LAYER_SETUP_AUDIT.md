# PCB Layout Sandbox Layer Setup Audit

Date: `2026-05-07`

## Scope

Repo workflow and prompt-pack enforcement only. No KiCad schematic, PCB, or manufacturing files were edited.

## Files Created

- `34_PCB_LAYOUT_SANDBOX/README.md`
- `34_PCB_LAYOUT_SANDBOX/INDEX.md`
- `34_PCB_LAYOUT_SANDBOX/PCB_LAYOUT_SANDBOX_RULES.md`
- `34_PCB_LAYOUT_SANDBOX/PCB_VARIANT_WORKFLOW.md`
- `34_PCB_LAYOUT_SANDBOX/COMPONENT_PLACEMENT_RULES.md`
- `34_PCB_LAYOUT_SANDBOX/CONNECTOR_ORIENTATION_RULES.md`
- `34_PCB_LAYOUT_SANDBOX/RF_ANTENNA_KEEP_OUT_RULES.md`
- `34_PCB_LAYOUT_SANDBOX/BOARD_SHAPE_AND_MECHANICAL_RULES.md`
- `34_PCB_LAYOUT_SANDBOX/ROUTING_FEASIBILITY_RULES.md`
- `34_PCB_LAYOUT_SANDBOX/VARIANT_SCORING_RULES.md`
- `34_PCB_LAYOUT_SANDBOX/HUMAN_REVIEW_GATE.md`
- `34_PCB_LAYOUT_SANDBOX/templates/PCB_VARIANT_PLAN_TEMPLATE.md`
- `34_PCB_LAYOUT_SANDBOX/templates/COMPONENT_PLACEMENT_MAP_TEMPLATE.md`
- `34_PCB_LAYOUT_SANDBOX/templates/CONNECTOR_ORIENTATION_REVIEW_TEMPLATE.md`
- `34_PCB_LAYOUT_SANDBOX/templates/ROUTING_FEASIBILITY_TEMPLATE.md`
- `34_PCB_LAYOUT_SANDBOX/templates/TRACE_PROJECTION_TEMPLATE.md`
- `34_PCB_LAYOUT_SANDBOX/templates/BOARD_SHAPE_DECISION_TEMPLATE.md`
- `34_PCB_LAYOUT_SANDBOX/templates/VARIANT_SCORECARD_TEMPLATE.md`
- `34_PCB_LAYOUT_SANDBOX/templates/HUMAN_LAYOUT_REVIEW_TEMPLATE.md`

## Files Updated

- `01_MEMORY/DESIGN_RULES_MEMORY.md`
- `AGENTS.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`
- `START_HERE_FOR_AI_AGENTS.md`
- `00_CODEX_START/START_HERE.md`
- `00_CODEX_START/FOLDER_ROUTING_RULES.md`
- `00_CODEX_START/REPO_STRUCTURE_INDEX.md`
- `09_ACCURACY_ENGINE/workflows/CREATE_PCB_WORKFLOW.md`
- `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`
- `14_LAYOUT_AUTOMATION/README.md`
- `14_LAYOUT_AUTOMATION/INDEX.md`
- `.prompts/kicad_pipeline/07_update_pcb_from_schematic.md`
- `.prompts/kicad_pipeline/09_pcb_placement_pass_1.md`
- `.prompts/kicad_pipeline/10_pcb_placement_pass_2_orientation.md`

## Rule Patch Summary

- Real `.kicad_pcb` edits now require a project sandbox report set first.
- Each PCB project must produce at least three layout variants before first real placement.
- Each variant must include outline, dimensions, fixed mechanics, connector orientation, antenna keepout, power path, USB/data path, routing projection, and risk score.
- USB-C and barrel-jack style connectors are treated as mechanical edge components unless requirements say otherwise.
- ESP32 antenna keepout planning must happen before surrounding placement.
- Board shape selection must be justified from mechanical, routing, and usability constraints.
- Placement feasibility and routing feasibility now gate the claim that a layout is professional.

## Validation

- `34_PCB_LAYOUT_SANDBOX/` exists with the requested rule, workflow, template, and support files.
- Startup docs, workflow docs, and prompt-pack files now reference the sandbox layer.
- The KiCad project design files stayed untouched during this repo-only task.

## Residual Risk

- Existing projects still need actual sandbox reports created under their project reports before future `.kicad_pcb` edits.
- Legacy documentation with embedded NUL bytes in `14_LAYOUT_AUTOMATION` can complicate text-search visibility, even though the required new rule text was inserted successfully.
