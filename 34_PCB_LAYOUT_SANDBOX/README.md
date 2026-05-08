# PCB Layout Sandbox

## PURPOSE

`34_PCB_LAYOUT_SANDBOX/` is the pre-layout reasoning layer for real KiCad PCB work. It forces AI agents to think through board shape, connector orientation, keepouts, component clusters, projected routing, and multiple layout variants before editing a real `.kicad_pcb`.

## WHAT_BELONGS_HERE

- Sandbox rules that block premature PCB editing.
- Variant-planning workflow documents.
- Placement, connector, RF, and board-shape rules.
- ESP32-style board placement rules and dev-board shape reasoning rules.
- Routing-feasibility and trace-projection guidance.
- Variant scoring, auto-approval, and conditional human-review rules.
- Templates for project-specific sandbox reports.
- Future sandbox helper scripts and generated sandbox reports.

## WHAT_DOES_NOT_BELONG_HERE

- Real KiCad schematic edits.
- Real KiCad PCB edits.
- Final placement claims without variant comparison.
- Routed boards or fabrication outputs.
- Footprint approvals without mechanical review evidence.

## AI_AGENT_RULES

- Do not edit a real `.kicad_pcb` until an active-project sandbox report set exists.
- Generate at least three layout variants before first real PCB placement work.
- Treat USB-C, barrel jacks, mounting holes, edge connectors, antennas, and other fixed mechanical items as first-order layout constraints.
- Do not assume the board outline is rectangular.
- Do not ask for generic manual sandbox approval when objective evidence can answer the question.
- Do not claim a layout is professional until placement, routing feasibility, DRC, and visual review all pass.

## SAFE_EDIT_RULES

- This folder defines planning and gating rules only.
- Project-specific sandbox outputs belong in the active project's `reports/` folder unless a future workflow says otherwise.
- Preserve existing project evidence and do not backfill fake variant studies.
- Do not store secrets or credentials.

## PUBLIC_RELEASE_NOTES

- This folder is workflow and template source, not proof of implemented auto-layout.
- Review future helper scripts for unsupported claims, secret leakage, and machine-specific paths before public release.

## Standard Project Outputs

Before real PCB edits, an active project should produce at least:

- `reports/PCB_LAYOUT_SANDBOX_VARIANT_01.md`
- `reports/PCB_LAYOUT_SANDBOX_VARIANT_02.md`
- `reports/PCB_LAYOUT_SANDBOX_VARIANT_03.md`
- `reports/PCB_LAYOUT_SANDBOX_SELECTED_VARIANT.md`
- one auto-approval or auto-blocked status report for the selected variant

Equivalent filenames are allowed only if the report set clearly records at least three variants plus one justified selected variant.
