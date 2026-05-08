# Issue Log: KiCad Engine Visual Gate Repair Remaining

Date: 2026-05-06  
Status: OPEN

## Issue

The root-cause patch fixed the worst pass-like script wording and updated prompt rules, but the visual gate is not fully repaired across every possible workflow.

## Remaining Work

- Update `09_ACCURACY_ENGINE/checklists/SCHEMATIC_READY_FOR_PCB_CHECKLIST.md`.
- Update `09_ACCURACY_ENGINE/workflows/SCHEMATIC_TO_PCB_GATE_WORKFLOW.md`.
- Check and update the project gate runner schematic visual gate if it consumes old `PASS` wording.
- Extend `03_TOOLS/scripts/visual/generate_schematic_closeups.py` JSON output with separate automated and human visual statuses.
- Run a controlled dry-run to prove automated-only output is classified as `AUTOMATED_CROP_PASS_ONLY`, not `VISUAL_PASS`.

## Evidence

- `02_HISTORY/design_reviews/KICAD_ENGINE_SCHEMATIC_FAILURE_ROOT_CAUSE_AUDIT.md`
- `05_OUTPUTS/release_readiness/KICAD_ENGINE_VISUAL_GATE_REPAIR_PLAN.md`

## Risk

If these remaining paths are not repaired, future agents may still encounter stale reports or alternate gates that over-read automated visual evidence.
