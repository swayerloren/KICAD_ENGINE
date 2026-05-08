# KiCad Phase Order

Status: `MANDATORY_STARTUP_RULE`

Codex and Claude must follow this phase order for KiCad projects. Later phases are blocked until earlier artifacts and evidence exist.

## Phase Order

0. Project Intake
1. Schematic Gate
2. PCB Creation / Update From Schematic
3. Placement Planning
4. Mechanical Setup
5. Component Placement
6. Placement Audit
7. Zones / Ground Strategy
8. Routing
9. Final PCB Audit
10. JLCPCB / Production Review
11. NOT_FINAL Export
12. JLC Upload Feedback
13. Final Prototype Signoff

## Mandatory Checker

Before starting any PCB phase, run:

`python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project <ACTIVE_PROJECT_PATH> --phase <PHASE>`

For Phase 2 only, if the current user prompt itself is LJ approval to create/update the PCB, include:

`--lj-approval`

If the checker returns `BLOCKED`, stop and report the missing prerequisite. Do not create future-phase blocked review reports unless the task specifically asks for a blocker audit.

## Non-Negotiable Blocks

- Missing `.kicad_pcb` blocks every phase after Phase 2.
- Missing `reports/PCB_SYNC_STATUS.md` blocks placement, routing, JLCPCB, production, export, upload feedback, and signoff.
- Missing DRC evidence blocks JLCPCB, production, export, upload feedback, and signoff.
- Missing no-unrouted-net evidence blocks JLCPCB, production, export, upload feedback, and signoff.
- Missing NOT_FINAL package blocks JLC upload feedback review.
- Reports are evidence only. A report does not replace the actual KiCad artifact or engineering check it claims.

## Redirect Rule

If a requested phase is too early, redirect to the next required phase. Example: if a project has a schematic but no `.kicad_pcb`, the next required phase is Phase 2, PCB Creation / Update From Schematic. JLCPCB review, mechanical production review, BOM production review, export, upload feedback review, and final signoff are not allowed.

