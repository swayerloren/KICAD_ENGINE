# 02 Schematic Visual Cleanup

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: reorganize the schematic into readable functional blocks and cleaner
local wiring without changing electrical intent.

## Read First

1. `AGENTS.md`
2. `.prompts/shared/HUMAN_DRAFTING_MODE.md`
3. `34_SCHEMATIC_QUALITY_ENGINE/README.md`
4. `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_LAYOUT_ALGORITHM.md`
5. `34_SCHEMATIC_QUALITY_ENGINE/FUNCTIONAL_BLOCK_TEMPLATES.md`
6. `34_SCHEMATIC_QUALITY_ENGINE/LOCAL_WIRING_STYLE_GUIDE.md`
7. `34_SCHEMATIC_QUALITY_ENGINE/VISUAL_READABILITY_SCORECARD.md`
8. `09_ACCURACY_ENGINE/schematic_rules/READABLE_SCHEMATIC_FLOW_RULES.md`
9. `09_ACCURACY_ENGINE/schematic_rules/WIRE_VS_NET_LABEL_RULES.md`
10. `09_ACCURACY_ENGINE/checklists/SCHEMATIC_READY_FOR_PCB_CHECKLIST.md`
11. Active project `reports/CLOSE_UP_REVIEW.md` when present

## HUMAN_DRAFTING_MODE

Before proposing labels or rewiring:

1. Ask whether symbols should be rotated, flipped, or repositioned first.
2. Ask whether each local net can be shown with a clean short orthogonal wire.
3. Treat labels as the fallback after the block geometry is sensible, not as a
   shortcut for poor local layout.
4. Default MCU support circuits such as EN, RESET, BOOT0, local LED drive,
   pullups/pulldowns, and decoupling to physical wiring when they are near the
   MCU or module pins.
5. If a dark or emphasized power/ground/return rail is kept or introduced, plan
   separate proof that it is a real wire on the intended net.
6. Keep reset/boot and other local control topology visually obvious; do not
   let labels or loopback wiring hide switch behavior.
7. Fail the cleanup if text ownership is still weak even when ERC remains
   clean.

## Do

1. Extract the current schematic layout.
2. Score readability.
3. Audit visual flow and local wire usage.
4. Create a block-layout cleanup plan before any rewrite.
5. List the blocks that need symbol rotation, flipping, or repositioning before
   any label decision.
6. Prefer real wires inside local blocks instead of label spray.
7. Keep MCU support circuits physically wired when they are local.
8. Keep power flow readable.
9. Keep USB-C support parts visually grouped and oriented for clean D+/D- flow.
10. Keep ground and return presentation intentional, and reject avoidable short
    loopback/S-shaped local wire paths.
11. Record which labels can stay, which labels should become wires, and which
    symbol moves are required.
12. Record any local MCU-support labels kept and why a physical wire would be
    worse.
13. Record any separate object/net proof needed for dark or emphasized rails,
    plus any reset/boot topology sanity review still required before gate
    claims.
14. Record the symbols that must be rotated/flipped/repositioned, the labels
    that should become wires, the labels that can stay and why, and the
    ERC/text/unresolved checks that must still be run after edits.
15. If rendered-page or crop evidence already shows an avoidable drafting
    problem, do not keep it in the plan just because ERC is likely to stay
    clean.
16. Do not write the schematic unless an explicit cleanup step later uses
   `--apply`.

## Required Evidence

- `03_TOOLS/scripts/schematic_layout/render_schematic_review_pages.py`
- `03_TOOLS/scripts/schematic_layout/score_schematic_readability.py`
- `03_TOOLS/scripts/schematic_layout/plan_schematic_block_layout.py`
- `03_TOOLS/scripts/schematic_quality/check_schematic_human_drafting_quality.py`

## Required Result

Return one result:

- `SCHEMATIC_VISUAL_CLEANUP_PASS`
- `SCHEMATIC_VISUAL_CLEANUP_FAIL`
- `BLOCKED_NEEDS_REVIEW`
