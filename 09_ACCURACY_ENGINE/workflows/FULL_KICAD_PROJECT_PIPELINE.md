# Full KiCad Project Pipeline

Status: `ACTIVE_WORKFLOW`

## Purpose

This workflow turns KiCad Engine's schematic-to-PCB-to-routing-to-fabrication process into a permanent gated sequence for future projects. It is designed for Codex, Claude, and similar VS Code-based agents working with the user's installed KiCad app.

## Prime Rule

Future KiCad projects must follow these gates unless the user explicitly approves an exception. Exceptions must be logged with:

- reason
- affected gate
- risk
- human-review-required flag
- evidence path
- user approval source

An exception does not convert unverified engineering work into approved work.

## Pipeline Order

| Step | Prompt | Gate Output |
|---:|---|---|
| 1 | `.prompts/kicad_pipeline/01_schematic_annotation_and_completeness.md` | Annotation/completeness reports |
| 2 | `.prompts/kicad_pipeline/02_schematic_visual_closeup_audit.md` | Close-up visual review |
| 3 | `.prompts/kicad_pipeline/03_schematic_visual_repair.md` | Visual repair report when needed |
| 4 | `.prompts/kicad_pipeline/04_schematic_electrical_audit.md` | `SCHEMATIC_ELECTRICAL_AUDIT.md` |
| 5 | `.prompts/kicad_pipeline/05_footprint_package_audit.md` | `reports/FOOTPRINT_PACKAGE_AUDIT.md` |
| 6 | `.prompts/kicad_pipeline/06_schematic_to_pcb_gate.md` | `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` |
| 7 | `.prompts/kicad_pipeline/07_update_pcb_from_schematic.md` | `reports/PCB_UPDATE_FROM_SCHEMATIC_REPORT.md` |
| 8 | `.prompts/kicad_pipeline/08_pcb_mechanical_setup.md` | `reports/PCB_MECHANICAL_SETUP_REPORT.md` |
| 9 | `.prompts/kicad_pipeline/09_pcb_placement_pass_1.md` | `reports/PCB_PLACEMENT_PASS_1_REPORT.md` |
| 10 | `.prompts/kicad_pipeline/10_pcb_placement_pass_2_orientation.md` | `reports/PCB_PLACEMENT_PASS_2_ORIENTATION_REPORT.md` |
| 11 | `.prompts/kicad_pipeline/11_holes_pads_vias_strategy.md` | `reports/THROUGH_HOLE_TEST_PAD_VIA_STRATEGY.md` |
| 12 | `.prompts/kicad_pipeline/12_copper_zones_setup.md` | `reports/COPPER_ZONE_STRATEGY_REPORT.md` |
| 13 | `.prompts/kicad_pipeline/13_routing_plan_only.md` | `reports/PCB_ROUTING_PLAN.md` |
| 14 | `.prompts/kicad_pipeline/14_route_critical_nets.md` | `reports/PCB_CRITICAL_NETS_ROUTING_REPORT.md` |
| 15 | `.prompts/kicad_pipeline/15_route_remaining_nets.md` | `reports/PCB_FULL_ROUTING_REPORT.md`; `reports/TRACE_BY_TRACE_AUDIT.md` |
| 16 | `.prompts/kicad_pipeline/16_final_pcb_verification.md` | `reports/FINAL_PCB_VERIFICATION_BEFORE_FAB.md` |
| 17 | `.prompts/kicad_pipeline/17_export_not_final_fab_package.md` | `fabrication/NOT_FINAL_<timestamp>/`; `reports/NOT_FINAL_FAB_PACKAGE_AUDIT.md` |

## Hard Stop Gates

- Do not update PCB until `SCHEMATIC_TO_PCB_GATE_STATUS.md` is exactly `PASS`.
- Do not edit a real `.kicad_pcb` until a sandbox report set exists with at least three layout variants and one justified selected variant.
- Do not do mechanical setup until PCB update succeeds and board requirements are known.
- Do not place until PCB exists and mechanical setup is acceptable.
- Do not route until placement, hole/pad/via strategy, zone strategy, and routing plan are ready.
- Do not route remaining nets until critical routing passes or is explicitly accepted with documented non-blocking warnings.
- Do not export `NOT_FINAL` fabrication packages until `FINAL_PCB_VERIFICATION_BEFORE_FAB.md` is exactly `READY_FOR_NOT_FINAL_FAB_EXPORT`.

## Evidence Rules

Each step must write a project report and history record. If a step is blocked, the report must say:

- what was checked
- what failed
- what was not run
- what files were not created
- what remains blocked
- exact next required evidence

## KiCad File Safety

Protected KiCad file edits require active project confirmation, backup, scope, verification plan, and rollback plan.

Protected files include:

- `.kicad_pro`
- `.kicad_sch`
- `.kicad_pcb`
- symbol libraries
- footprint libraries
- manufacturing output files

## Closeout

Every meaningful pipeline step requires AI quality closeout:

- session log
- command log when commands ran
- failed-attempt log when anything failed
- issue log for unresolved blockers
- AI self-review
- response scorecard
- claim/evidence matrix
- uncertainty log
- hallucination-risk log when applicable
- index rebuilds
