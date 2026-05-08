# 07 Update PCB From Schematic

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: update PCB from schematic only if the schematic-to-PCB gate is `PASS`.

## Mandatory Phase Gate

This is Phase 2. Before doing anything, run:

`python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project "[ACTIVE_PROJECT_PATH]" --phase 2`

If the current LJ prompt explicitly approves PCB creation/update from schematic, include `--lj-approval`.

If the result is `BLOCKED`, stop and report the missing Phase 1 evidence. Do not create later-phase blocked reports.

## Read First

1. `AGENTS.md`
2. `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`
3. `reports/FOOTPRINT_PACKAGE_AUDIT.md`
4. `34_PCB_LAYOUT_SANDBOX/README.md`
5. `34_PCB_LAYOUT_SANDBOX/PCB_LAYOUT_SANDBOX_RULES.md`
6. `34_PCB_LAYOUT_SANDBOX/PCB_VARIANT_WORKFLOW.md`
7. `34_PCB_LAYOUT_SANDBOX/PCB_WORK_AUTO_START_RULES.md`
8. `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md`
9. `layout_sandbox/SELECTED_LAYOUT_PLAN.md`
10. `09_ACCURACY_ENGINE/workflows/AUTO_PCB_START_WORKFLOW.md`
11. `09_ACCURACY_ENGINE/checklists/AUTO_PCB_START_CHECKLIST.md`
12. `09_ACCURACY_ENGINE/checklists/PCB_UPDATE_FROM_SCHEMATIC_CHECKLIST.md`
13. `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`

## Preconditions

If `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` is not exactly `PASS`, stop with `AUTO_PCB_START_BLOCKED`.

If `reports/PCB_LAYOUT_SANDBOX_GATE_STATUS.md` is not exactly `PASS`, stop with `AUTO_PCB_START_BLOCKED`.

If the project does not have at least three sandbox variants, one justified selected variant, one auto-approval report with `AUTO_APPROVED_FOR_PCB_WORK`, defined board dimensions, connector-orientation planning, antenna-keepout planning when required, and routing-feasibility evidence, stop with `AUTO_PCB_START_BLOCKED`.

## Do If PASS

1. Locate `.kicad_pro`, `.kicad_sch`, and `.kicad_pcb`.
2. Create backup under `99_BACKUPS/pre_codex_edits/`.
3. Confirm the selected sandbox variant is the basis for the real PCB work.
4. Confirm the project satisfies `AUTO_PCB_START_WORKFLOW.md`.
5. Update PCB from schematic using a KiCad-safe method.
6. Do not route traces.
7. Run DRC.
8. Create `reports/PCB_UPDATE_FROM_SCHEMATIC_REPORT.md`.
9. Create or update the auto PCB start report from the template.

## Required Result

Return one result:

- `PCB_UPDATE_PASS`
- `PCB_UPDATE_FAIL`
- `AUTO_PCB_START_BLOCKED`

AI quality closeout is required.
