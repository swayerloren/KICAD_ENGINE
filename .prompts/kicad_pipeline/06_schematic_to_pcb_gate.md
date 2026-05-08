# 06 Schematic To PCB Gate

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: evaluate the schematic-to-PCB gate. Do not update PCB.

## Read First

1. `AGENTS.md`
2. `09_ACCURACY_ENGINE/workflows/SCHEMATIC_TO_PCB_GATE_WORKFLOW.md`
3. `09_ACCURACY_ENGINE/checklists/SCHEMATIC_READY_FOR_PCB_CHECKLIST.md`
4. `09_ACCURACY_ENGINE/verification_rules/SCHEMATIC_TO_PCB_BLOCKERS.md`
5. `09_ACCURACY_ENGINE/verification_rules/NEEDS_REVIEW_BLOCKER_RULES.md`
6. `09_ACCURACY_ENGINE/verification_rules/HUMAN_READABLE_SCHEMATIC_RULES.md`
7. `09_ACCURACY_ENGINE/verification_rules/VISUAL_PASS_IS_NOT_AUTOMATED_PASS.md`
8. `09_ACCURACY_ENGINE/checklists/SCHEMATIC_HUMAN_READABILITY_CHECKLIST.md`
9. `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`
10. `33_KICAD_GUI_AUTOMATION/KICAD_NATIVE_ANNOTATION_WORKFLOW.md`
11. `33_KICAD_GUI_AUTOMATION/KICAD_NATIVE_ANNOTATION_SUCCESS_RECORD.md`
12. All prior project reports from prompts 01 through 05.

## Do

1. Verify annotation/completeness, ERC, visual close-ups, human-readable rendered-image inspection, electrical audit, BOM lock, footprint/package audit, connector orientation, polarity review, and high-risk `NEEDS_REVIEW` closure.
2. Create or update `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`.
3. Gate result must be exactly `PASS` before PCB update, placement, routing, zones, or fab export can proceed.

## Mandatory Annotation Gate Rule

Do not pass this gate from raw `.kicad_sch` text edits, regex scans, or saved-file reference tables alone. The annotation row must be backed by native KiCad annotation evidence:

- GUI/native `Annotate Schematic` applied or LJ-confirmed manual native annotation
- schematic saved from KiCad GUI
- GUI ERC 0 violations when safely automatable
- post-save `kicad-cli` ERC pass
- saved schematic scan 0 unresolved `?` references
- duplicate-reference scan pass

Passing annotation only allows a separate visual cleanup task. It does not authorize PCB update.

## Mandatory Visual Gate Rule

Do not pass this gate from `AUTOMATED_CROP_PASS_ONLY`, `CLOSE_UP_REVIEW.md` existence, ERC pass, annotation pass, footprint field population, or no `?` references. The visual row must be `VISUAL_PASS` with rendered full-page and crop evidence inspected block by block.

## Required Result

Return one result:

- `SCHEMATIC_TO_PCB_GATE_PASS`
- `SCHEMATIC_TO_PCB_GATE_FAIL`
- `BLOCKED_UNTIL_HUMAN_REVIEW`

AI quality closeout is required.
