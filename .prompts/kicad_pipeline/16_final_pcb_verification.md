# 16 Final PCB Verification

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: run final PCB verification before any fabrication outputs are generated.

## Mandatory Phase Gate

This is Phase 9. Before doing anything, run:

`python 03_TOOLS/scripts/project_gate/check_phase_allowed.py --project "[ACTIVE_PROJECT_PATH]" --phase 9`

If the result is `BLOCKED`, stop and report the missing earlier phase. Missing DRC evidence or no-unrouted-net proof blocks final PCB verification and every production/export phase.

## Read First

1. `AGENTS.md`
2. `reports/PCB_FULL_ROUTING_REPORT.md`
3. `reports/TRACE_BY_TRACE_AUDIT.md`
4. `09_ACCURACY_ENGINE/pcb_rules/TRACE_ANGLE_ROUTING_RULES.md`
5. `09_ACCURACY_ENGINE/pcb_rules/PCB_ROUTING_QUALITY_RULES.md`
6. `09_ACCURACY_ENGINE/checklists/PCB_ROUTING_QUALITY_CHECKLIST.md`
7. `09_ACCURACY_ENGINE/verification_rules/HUMAN_REVIEW_GATE_RULES.md`
8. `24_FAB_PROFILES/00_INDEX/NOT_FINAL_OUTPUT_RULES.md` if present
9. `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`
10. `24_FAB_PROFILES/UNIVERSAL_PCBA_PACKAGE_RULES.md`
11. `24_FAB_PROFILES/CONNECTOR_ORIENTATION_PRE_UPLOAD_RULES.md`
12. `09_ACCURACY_ENGINE/checklists/PCBA_EXPORT_GATE_CHECKLIST.md`

## Do

Check schematic-to-PCB sync, ERC, DRC, unrouted nets, footprints, connector orientation, polarity, mounting holes, board outline, copper zones, antenna keepout, USB routing, power routing, silkscreen, ref/value fields, 3D model gaps, BOM alignment, PNP risk, human-review list, and routing quality.

Latest connector-orientation and ESP32-antenna orientation audit results must be cited directly; do not replace them with a prose-only summary.

Check routing quality explicitly:

- no obvious 90-degree bends where practical
- no acute-angle bends
- no visually crude or awkward routing accepted just because DRC passes
- clean power-trace transitions
- clean USB pair geometry and stub control
- clean switching-loop geometry around regulators

Before returning `READY_FOR_NOT_FINAL_FAB_EXPORT`, confirm the PCBA export gate requirements:

- DRC and no-unrouted-net proof exist.
- Routing-quality review passed separately from DRC.
- Barrel jack, USB-C, and all connector orientations are proof-audited.
- No required connector remains `NEEDS_HUMAN_REVIEW`.
- IC pin 1, diode/LED polarity, and capacitor polarity are verified.
- Pick-and-place rotation risk is documented as requiring visual review.
- Future JLCPCB/PCBWay packages will remain `NOT_FINAL`.

Create `reports/FINAL_PCB_VERIFICATION_BEFORE_FAB.md`.

## Required Result

Return one result:

- `READY_FOR_NOT_FINAL_FAB_EXPORT`
- `NOT_READY_FOR_FAB_EXPORT`
- `NEEDS_HUMAN_REVIEW`

AI quality closeout is required.
