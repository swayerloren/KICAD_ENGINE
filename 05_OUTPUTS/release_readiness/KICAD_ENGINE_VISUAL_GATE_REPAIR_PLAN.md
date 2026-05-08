# KiCad Engine Visual Gate Repair Plan

Date: 2026-05-06  
Status: ACTIVE_REPAIR_PLAN

## Goal

Prevent any future Codex/Claude session from confusing exported visual artifacts with a human-readable schematic.

## Priority 0 Fixes

1. Replace bare automated visual `PASS` wording.
   - Done for `03_TOOLS/scripts/visual/generate_schematic_closeups.py`.
   - Expected automated-only status: `AUTOMATED_CROP_PASS_ONLY`.

2. Ban automated-only visual pass in prompt pack.
   - Done for `.prompts/kicad_pipeline/02_schematic_visual_closeup_audit.md`.
   - Done for `.prompts/kicad_pipeline/03_schematic_visual_repair.md`.
   - Done for `.prompts/kicad_pipeline/06_schematic_to_pcb_gate.md`.

3. Make current known problem visible at startup.
   - Done in `00_CODEX_START/CURRENT_KNOWN_PROBLEMS.md`.

## Priority 1 Fixes Still Needed

1. Update `09_ACCURACY_ENGINE/checklists/SCHEMATIC_READY_FOR_PCB_CHECKLIST.md`.
   - Add separate rows for automated crop generation and human-readable visual inspection.
   - Block PCB update unless human-readable visual inspection is `VISUAL_PASS`.

2. Update `09_ACCURACY_ENGINE/workflows/SCHEMATIC_TO_PCB_GATE_WORKFLOW.md`.
   - Require `VISUAL_PASS`, not `AUTOMATED_CROP_PASS_ONLY`.

3. Update project gate runner visual gate.
   - Locate `03_TOOLS/scripts/project_gate/gates/schematic_visual_gate.py`.
   - Ensure automated-only visual evidence returns `FAIL` or `BLOCKED_UNTIL_HUMAN_REVIEW`.

4. Extend `generate_schematic_closeups.py` output schema.
   - Add `automated_status`.
   - Add `human_visual_status`.
   - Add `manual_review_required: true`.
   - Add `cannot_claim_visual_pass: true` unless a separate inspection file is supplied.

## Priority 2 Improvements

1. Add optional image-screening heuristics:
   - crop boundary clipping warnings
   - dense text cluster warnings
   - text near symbol/wire warnings
   - notes/circuit overlap warnings

2. Add a dedicated strict visual audit command:
   - input: project root and crops folder
   - output: block table requiring manual result entry
   - default result: `VISUAL_NOT_VERIFIED`

3. Add a visual review packet template:
   - full-page paths
   - crop paths
   - per-block LJ inspection checklist
   - explicit `PCB_UPDATE_ALLOWED: NO` until visual pass.

## Acceptance Criteria

The visual gate repair is complete only when:

- No visual script emits bare `PASS` for human readability without rendered-image inspection.
- Prompt 02 cannot complete with `SCHEMATIC_VISUAL_PASS` from automated crop output alone.
- Prompt 06 cannot pass the schematic-to-PCB gate unless human-readable visual status is `VISUAL_PASS`.
- The ESP32 failure mode is recorded in global memory and current known problems.
- A future dry-run demonstrates that automated-only crops classify as `AUTOMATED_CROP_PASS_ONLY` or blocked, not `VISUAL_PASS`.

## Current Production Status

KiCad Engine visual gate status: `REPAIR_IN_PROGRESS`

Do not claim production-ready schematic visual approval until the remaining checklist/workflow/gate-runner updates are complete and tested.
