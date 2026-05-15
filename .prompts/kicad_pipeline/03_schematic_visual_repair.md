# 03 Schematic Visual Repair

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: repair schematic visual issues only after a visual audit identifies fixable problems. Do not change electrical intent unless explicitly required and source-backed.

## Read First

1. `AGENTS.md`
2. `.prompts/shared/HUMAN_DRAFTING_MODE.md`
3. `03_TOOLS/kicad/VISUAL_VERIFICATION_WORKFLOW.md`
4. `09_ACCURACY_ENGINE/verification_rules/HUMAN_READABLE_SCHEMATIC_RULES.md`
5. `09_ACCURACY_ENGINE/verification_rules/VISUAL_PASS_IS_NOT_AUTOMATED_PASS.md`
6. `09_ACCURACY_ENGINE/checklists/SCHEMATIC_HUMAN_READABILITY_CHECKLIST.md`
7. Active project `reports/CLOSE_UP_REVIEW.md`
8. Active project `_verification/schematic_visual/CLOSE_UP_REVIEW.json` if present
9. `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`

## Preconditions

- Active project is confirmed.
- Target files are inside the active project.
- A backup exists under `99_BACKUPS/pre_codex_edits/`.
- The visual issue is specific and repairable without guessing electrical design.

## Do

1. Create a repair plan.
2. Enter `HUMAN_DRAFTING_MODE` before any visual rewrite:
   - rotate, flip, or reposition symbols before reaching for labels
   - replace short avoidable local labels with physical wires
   - keep local MCU support wiring physically readable when near the pins
   - if a dark or emphasized rail is part of the visual fix, verify it is a
     real wire on the intended net
   - keep reset/boot and local control topology visually obvious
3. Fix only visual schematic issues such as hidden clutter, label readability,
   crop framing, note placement, block organization, text ownership, and bad
   local wire-vs-label choices.
4. Do not alter pinouts, footprints, values, power policy, USB policy, or
   connector policy unless source-backed and explicitly in scope.
5. Re-run schematic visual close-up audit.
6. Re-run `03_TOOLS/scripts/schematic_quality/check_schematic_human_drafting_quality.py` when labels, local support wiring, or emphasized return rails changed.
7. Run ERC if any schematic file changed.
8. Do not claim the repair passed unless rendered full-page and crop evidence
   have been inspected and every required block has `VISUAL_PASS`.
9. Report which labels were kept and why, which local labels were replaced with
   wires, and which symbols were rotated/flipped/repositioned.
10. Report any object/net proof for emphasized rails and any reset/boot topology
   sanity checks that were needed before the visual pass claim.
11. Report ERC result, text-overlap result, and unresolved-reference result
    when those checks are available after the repair.

## Forbidden Shortcut

Do not write `SCHEMATIC_VISUAL_REPAIR_PASS` because ERC passed, references are annotated, footprints are populated, or automated crops were generated. Those are separate gates. A visual repair pass requires actual human-readable image inspection.

Do not stop the repair loop only because ERC or text-overlap checks improved if
the sheet still looks like AI shortcut drafting.

## Required Result

Return one result:

- `SCHEMATIC_VISUAL_REPAIR_PASS`
- `SCHEMATIC_VISUAL_REPAIR_FAIL`
- `BLOCKED_NEEDS_REVIEW`

Use `SCHEMATIC_VISUAL_REPAIR_PASS` only when the human-readability checklist is complete. Otherwise use `SCHEMATIC_VISUAL_REPAIR_FAIL` or `BLOCKED_NEEDS_REVIEW`.

AI quality closeout is required.
