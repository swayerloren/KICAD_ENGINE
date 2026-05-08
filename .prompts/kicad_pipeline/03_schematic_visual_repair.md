# 03 Schematic Visual Repair

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: repair schematic visual issues only after a visual audit identifies fixable problems. Do not change electrical intent unless explicitly required and source-backed.

## Read First

1. `AGENTS.md`
2. `03_TOOLS/kicad/VISUAL_VERIFICATION_WORKFLOW.md`
3. `09_ACCURACY_ENGINE/verification_rules/HUMAN_READABLE_SCHEMATIC_RULES.md`
4. `09_ACCURACY_ENGINE/verification_rules/VISUAL_PASS_IS_NOT_AUTOMATED_PASS.md`
5. `09_ACCURACY_ENGINE/checklists/SCHEMATIC_HUMAN_READABILITY_CHECKLIST.md`
6. Active project `reports/CLOSE_UP_REVIEW.md`
7. Active project `_verification/schematic_visual/CLOSE_UP_REVIEW.json` if present
8. `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`

## Preconditions

- Active project is confirmed.
- Target files are inside the active project.
- A backup exists under `99_BACKUPS/pre_codex_edits/`.
- The visual issue is specific and repairable without guessing electrical design.

## Do

1. Create a repair plan.
2. Fix only visual schematic issues such as hidden clutter, label readability, crop framing, note placement, or block organization.
3. Do not alter pinouts, footprints, values, power policy, USB policy, or connector policy unless source-backed and explicitly in scope.
4. Re-run schematic visual close-up audit.
5. Run ERC if any schematic file changed.
6. Do not claim the repair passed unless rendered full-page and crop evidence has been inspected and every required block has `VISUAL_PASS`.

## Forbidden Shortcut

Do not write `SCHEMATIC_VISUAL_REPAIR_PASS` because ERC passed, references are annotated, footprints are populated, or automated crops were generated. Those are separate gates. A visual repair pass requires actual human-readable image inspection.

## Required Result

Return one result:

- `SCHEMATIC_VISUAL_REPAIR_PASS`
- `SCHEMATIC_VISUAL_REPAIR_FAIL`
- `BLOCKED_NEEDS_REVIEW`

Use `SCHEMATIC_VISUAL_REPAIR_PASS` only when the human-readability checklist is complete. Otherwise use `SCHEMATIC_VISUAL_REPAIR_FAIL` or `BLOCKED_NEEDS_REVIEW`.

AI quality closeout is required.
