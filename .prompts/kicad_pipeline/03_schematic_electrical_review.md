# 03 Schematic Electrical Review

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: run a strict schematic electrical review without updating PCB.

## Read First

1. `AGENTS.md`
2. `34_SCHEMATIC_QUALITY_ENGINE/SCHEMATIC_TO_PCB_READY_GATE.md`
3. `34_SCHEMATIC_QUALITY_ENGINE/VISUAL_READABILITY_SCORECARD.md`
4. `09_ACCURACY_ENGINE/schematic_rules/SCHEMATIC_CREATION_STANDARD.md`
5. `09_ACCURACY_ENGINE/schematic_rules/POWER_NET_RULES.md`
6. `09_ACCURACY_ENGINE/schematic_rules/USB_C_SCHEMATIC_RULES.md`
7. `09_ACCURACY_ENGINE/checklists/SCHEMATIC_READY_FOR_PCB_CHECKLIST.md`
8. Active project BOM lock, ready-parts list, and prior audits if present

## Do

1. Locate the target `.kicad_sch`.
2. Run ERC if possible.
3. Review power rails, regulator support parts, reset and boot, connectors,
   USB, ESD, polarity-sensitive parts, and high-risk nets.
4. Review the latest schematic layout score so electrical correctness does not
   get misreported as visual readiness.
5. Do not guess values, pinouts, footprints, or policies.
6. Mark unresolved items `NEEDS_REVIEW` or blocked.

## Required Result

Return one result:

- `SCHEMATIC_ELECTRICAL_PASS`
- `SCHEMATIC_ELECTRICAL_FAIL`
- `NEEDS_HUMAN_REVIEW`
