# 02 Schematic Visual Cleanup

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: reorganize the schematic into readable functional blocks and cleaner
local wiring without changing electrical intent.

## Read First

1. `AGENTS.md`
2. `34_SCHEMATIC_QUALITY_ENGINE/README.md`
3. `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_LAYOUT_ALGORITHM.md`
4. `34_SCHEMATIC_QUALITY_ENGINE/FUNCTIONAL_BLOCK_TEMPLATES.md`
5. `34_SCHEMATIC_QUALITY_ENGINE/LOCAL_WIRING_STYLE_GUIDE.md`
6. `34_SCHEMATIC_QUALITY_ENGINE/VISUAL_READABILITY_SCORECARD.md`
7. `09_ACCURACY_ENGINE/schematic_rules/READABLE_SCHEMATIC_FLOW_RULES.md`
8. `09_ACCURACY_ENGINE/schematic_rules/WIRE_VS_NET_LABEL_RULES.md`
9. `09_ACCURACY_ENGINE/checklists/SCHEMATIC_READY_FOR_PCB_CHECKLIST.md`
10. Active project `reports/CLOSE_UP_REVIEW.md` when present

## Do

1. Extract the current schematic layout.
2. Score readability.
3. Audit visual flow and local wire usage.
4. Create a block-layout cleanup plan before any rewrite.
5. Prefer real wires inside local blocks instead of label spray.
6. Keep power flow readable.
7. Keep USB-C support parts visually grouped.
8. Do not write the schematic unless an explicit cleanup step later uses
   `--apply`.

## Required Evidence

- `03_TOOLS/scripts/schematic_layout/render_schematic_review_pages.py`
- `03_TOOLS/scripts/schematic_layout/score_schematic_readability.py`
- `03_TOOLS/scripts/schematic_layout/plan_schematic_block_layout.py`

## Required Result

Return one result:

- `SCHEMATIC_VISUAL_CLEANUP_PASS`
- `SCHEMATIC_VISUAL_CLEANUP_FAIL`
- `BLOCKED_NEEDS_REVIEW`
