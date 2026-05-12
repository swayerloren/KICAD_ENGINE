# 01 Schematic Annotation And Completeness

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: run the schematic annotation and completeness gate. Do not edit KiCad design files.

## Read First

1. `AGENTS.md`
2. `README_GPT.md`
3. `FOR CHAT GPT.MD`
4. `00_CODEX_START/KICAD_PIPELINE_STARTUP_RULES.md`
5. `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`
6. `09_ACCURACY_ENGINE/verification_rules/SCHEMATIC_ANNOTATION_RULES.md`
7. `09_ACCURACY_ENGINE/verification_rules/SCHEMATIC_COMPLETENESS_RULES.md`
8. `33_KICAD_GUI_AUTOMATION/KICAD_NATIVE_ANNOTATION_WORKFLOW.md`
9. `33_KICAD_GUI_AUTOMATION/KICAD_ANNOTATION_DO_AND_DO_NOT.md`
10. `33_KICAD_GUI_AUTOMATION/KICAD_AUTO_OPEN_PROJECT_WORKFLOW.md`
11. `33_KICAD_GUI_AUTOMATION/KICAD_GUI_ACTION_MATRIX.md`
10. `34_SCHEMATIC_QUALITY_ENGINE/README.md`
11. `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_ANNOTATION_GATE.md`
12. `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_TO_PCB_READY_GATE.md`
13. `34_SCHEMATIC_QUALITY_ENGINE/README_FOR_CODEX_AND_CLAUDE.md`
10. Active project memory and prior reports.

## Mandatory Native Annotation Rule

If annotation repair or annotation proof is needed, use KiCad native annotation through the GUI automation gate when available. Raw `.kicad_sch` text edits are not accepted as annotation proof.

The authoritative annotation evidence is:

- native KiCad `Annotate Schematic` applied
- schematic saved from KiCad GUI
- GUI ERC 0 violations when safely automatable
- post-save `kicad-cli` ERC pass
- saved schematic scan 0 unresolved `?` references
- duplicate-reference scan pass

If Eeschema is not open, attempt to open the target `.kicad_pro` only when the task explicitly allows it and safety gates can be met. If Eeschema is open with a different project, stop.

Exact future live command:

```powershell
.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe .\33_KICAD_GUI_AUTOMATION\scripts\windows\run_native_annotation_workflow.py `
  --project "<ACTIVE .kicad_pro>" `
  --schematic "<ACTIVE .kicad_sch>" `
  --live `
  --allow-annotation `
  --allow-save `
  --allow-gui-erc
```

## Do

1. Locate the active `.kicad_pro` and `.kicad_sch`.
2. For annotation proof or repair, run or review the KiCad native annotation workflow evidence.
3. Run or review:
   - `03_TOOLS/scripts/kicad_schematic_checks/check_schematic_annotation.py`
   - `03_TOOLS/scripts/kicad_schematic_checks/check_schematic_completeness.py`
   - `03_TOOLS/scripts/kicad_schematic_checks/check_bom_lock_alignment.py`
   - `03_TOOLS/scripts/kicad_schematic_checks/check_needs_review_markers.py`
   - `03_TOOLS/scripts/schematic_quality/run_schematic_quality_gate.py --project <ACTIVE_PROJECT_PATH> --no-fail`
4. Create or update project reports for annotation, completeness, BOM-lock alignment, and `NEEDS_REVIEW` markers.
5. Mark missing scripts, missing BOM lock, missing schematic-ready list, parser failures, missing native annotation evidence, or failing schematic-quality evidence as blockers.

## Required Result

Return one result:

- `ANNOTATION_COMPLETENESS_PASS`
- `ANNOTATION_COMPLETENESS_FAIL`
- `NEEDS_HUMAN_REVIEW`

AI quality closeout is required.
