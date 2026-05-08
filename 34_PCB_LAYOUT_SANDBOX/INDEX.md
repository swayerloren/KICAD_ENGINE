# PCB Layout Sandbox Index

Status: `ACTIVE_WORKFLOW_LAYER`

## Key Files

- `README.md`
- `PCB_LAYOUT_SANDBOX_RULES.md`
- `PCB_VARIANT_WORKFLOW.md`
- `COMPONENT_PLACEMENT_RULES.md`
- `ESP32_STYLE_BOARD_PLACEMENT_RULES.md`
- `CONNECTOR_ORIENTATION_RULES.md`
- `RF_ANTENNA_KEEP_OUT_RULES.md`
- `BOARD_SHAPE_AND_MECHANICAL_RULES.md`
- `DEV_BOARD_SHAPE_REASONING_RULES.md`
- `ROUTING_FEASIBILITY_RULES.md`
- `FREEROUTING_AS_VARIANT_SCORER.md`
- `VARIANT_SCORING_RULES.md`
- `HUMAN_REVIEW_GATE.md`

## Subfolders

- `variants/`: future reusable example variants or helper assets.
- `reports/`: future global sandbox-layer reports or generated inventories.
- `scripts/`: future helper scripts for sandbox planning support.
- `templates/`: project-facing template files for sandbox report generation.

## Required Use

- Read this folder before any real PCB update, placement, or routing work.
- Use the templates to create project-specific sandbox reports under the active project's `reports/`.
- Use FreeRouting dry-run evidence only as optional support for the `routing_feasibility` score.
- Do not treat this folder as proof of auto-layout capability.

## Standard Project Outputs

- `reports/PCB_LAYOUT_SANDBOX_VARIANT_01.md`
- `reports/PCB_LAYOUT_SANDBOX_VARIANT_02.md`
- `reports/PCB_LAYOUT_SANDBOX_VARIANT_03.md`
- `reports/PCB_LAYOUT_SANDBOX_SELECTED_VARIANT.md`
