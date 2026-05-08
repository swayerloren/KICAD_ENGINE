# 17 Export NOT_FINAL Fab Package

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: export a `NOT_FINAL` fabrication review package only if final PCB verification authorizes it.

## Mandatory Phase Gate

This is Phase 11. Before doing anything, run:

`python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project "[ACTIVE_PROJECT_PATH]" --phase 11`

If the result is `BLOCKED`, stop and report the missing earlier phase. A missing `.kicad_pcb`, missing `PCB_SYNC_STATUS.md`, missing DRC/no-unrouted-net proof, or missing production-review evidence blocks export. Do not create future-phase blocked reports unless LJ specifically requested a blocker audit.

## Read First

1. `AGENTS.md`
2. `reports/FINAL_PCB_VERIFICATION_BEFORE_FAB.md`
3. `24_FAB_PROFILES/00_INDEX/GERBER_DRILL_RULES.md` if present
4. `24_FAB_PROFILES/00_INDEX/BOM_CPL_PNP_RULES.md` if present
5. `24_FAB_PROFILES/00_INDEX/NOT_FINAL_OUTPUT_RULES.md` if present
6. `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`
7. `24_FAB_PROFILES/UNIVERSAL_PCBA_PACKAGE_RULES.md`
8. `24_FAB_PROFILES/JLCPCB/README.md`
9. `24_FAB_PROFILES/PCBWAY/README.md`
10. `09_ACCURACY_ENGINE/checklists/PCBA_EXPORT_GATE_CHECKLIST.md`

## Preconditions

If `reports/FINAL_PCB_VERIFICATION_BEFORE_FAB.md` is not exactly `READY_FOR_NOT_FINAL_FAB_EXPORT`, stop.

## Do If Ready

1. Create backup/snapshot.
2. Create separate `jlcpcb` and `pcbway` package folders under a new manufacturing revision folder.
3. Export Gerbers and drill files only if the phase gate and final verification allow export.
4. Create JLCPCB files with exact columns: `BOM_JLCPCB.csv` and `CPL_JLCPCB.csv`.
5. Create PCBWay files with exact columns: `BOM_PCBWay.csv` and `Centroid_PCBWay.csv`.
6. Create `Assembly_Notes.md` for each fab-house folder.
7. Create `review/orientation_checks.md`.
8. Run the fabrication validators under `03_TOOLS/scripts/fabrication`.
9. Copy latest ERC/DRC reports and review evidence.
10. Create `PACKAGE_MANIFEST.md`.
11. Ensure every path and file name is marked `NOT_FINAL`.
12. Run fabrication package audit and create `reports/NOT_FINAL_FAB_PACKAGE_AUDIT.md`.

Block export if DRC, no-unrouted-net, connector orientation, polarity, assembly-note, or package-folder validation gates fail.

## Required Result

Return one result:

- `NOT_FINAL_PACKAGE_CREATED`
- `EXPORT_FAILED`
- `BLOCKED`

AI quality closeout is required.
