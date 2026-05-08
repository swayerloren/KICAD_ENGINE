# No Phase Skipping Rules

Status: `MANDATORY`

These rules prevent agents from claiming KiCad PCB, manufacturing, production, or signoff progress before the design has reached the required phase.

## Hard Blocks

1. If `.kicad_pcb` does not exist, block every phase after Phase 2.
2. If `reports/PCB_SYNC_STATUS.md` does not exist, block placement, routing, JLCPCB, mechanical production review, BOM/CPL production review, production signoff, and export tasks.
3. If DRC has not run, block JLCPCB review, production review, NOT_FINAL export, upload feedback review, and production signoff.
4. If no unrouted-net proof exists, block JLCPCB review, production review, NOT_FINAL export, upload feedback review, and production signoff.
5. If no NOT_FINAL package exists, block JLC upload feedback review.
6. If the user asks for a later phase too early, stop and say which earlier phase and evidence are missing.
7. Do not create blocked review reports for future phases unless LJ specifically asks for a blocker audit. Redirect to the next required phase instead.
8. Do not run JLCPCB, mechanical production, BOM production, export, upload feedback, or final signoff prompts before PCB creation/update from schematic is complete.
9. Do not treat documentation or report creation as actual engineering progress.
10. Each phase must have required evidence files before the next phase starts.

## Required Response When Blocked

When a requested phase is blocked, the agent response must include:

- Requested phase.
- Blocking earlier phase.
- Missing evidence files or missing design artifact.
- Next allowed phase.
- A clear statement that no KiCad design files or fabrication outputs were changed.

## Required Script Check

For phase-gated project tasks, agents must run the read-only checker when possible:

`python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project <ACTIVE_PROJECT_PATH> --phase <PHASE>`

The checker is evidence aggregation only. It does not edit KiCad files, run ERC/DRC, or generate outputs.

## Special Production Block

JLCPCB, production, export, upload feedback, and final signoff tasks are forbidden unless the PCB artifact and phase evidence prove the design has completed the earlier PCB phases. A missing `.kicad_pcb` is always a hard block for those tasks.

