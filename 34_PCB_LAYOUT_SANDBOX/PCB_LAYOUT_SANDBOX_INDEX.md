# PCB Layout Sandbox Index

`34_PCB_LAYOUT_SANDBOX/` is the planning gate before real `.kicad_pcb` edits.

## Start Here

- [README.md](README.md)
- [PCB_LAYOUT_SANDBOX_RULES.md](PCB_LAYOUT_SANDBOX_RULES.md)
- [PCB_VARIANT_WORKFLOW.md](PCB_VARIANT_WORKFLOW.md)
- [AUTO_SANDBOX_APPROVAL_RULES.md](AUTO_SANDBOX_APPROVAL_RULES.md)

## Main Topics

- board shape and mechanical planning
- connector orientation review
- RF antenna keepout planning
- routing feasibility planning
- auto-approval and auto-block rules
- variant scoring and comparison

## Scripts

- `scripts/score_layout_variant.py`
- `scripts/compare_layout_variants.py`
- `scripts/auto_select_best_variant.py`
- `scripts/auto_approve_selected_variant.py`

## Important Constraint

Sandbox approval is a prerequisite to intentional real PCB update, placement, or routing work.
