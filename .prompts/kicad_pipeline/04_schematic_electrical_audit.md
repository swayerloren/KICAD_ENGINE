# 04 Schematic Electrical Audit

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: run a strict schematic electrical audit. Do not update PCB.

## Read First

1. `AGENTS.md`
2. `09_ACCURACY_ENGINE/schematic_rules/SCHEMATIC_CREATION_STANDARD.md`
3. `09_ACCURACY_ENGINE/schematic_rules/POWER_NET_RULES.md`
4. `09_ACCURACY_ENGINE/schematic_rules/USB_C_SCHEMATIC_RULES.md`
5. `09_ACCURACY_ENGINE/schematic_rules/CONNECTOR_PIN_NUMBERING_RULES.md`
6. `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`
7. Active project BOM lock, ready-parts list, and prior audits if present.

## Do

1. Locate `.kicad_pro` and `.kicad_sch`.
2. Run ERC if possible.
3. Audit power rails, regulators, decoupling, reset/boot, connectors, USB, ESD, polarity-sensitive parts, and high-risk nets.
4. Do not guess values, pinouts, footprints, or policies.
5. Mark unresolved items `NEEDS_REVIEW` or blocked.
6. Create or update `SCHEMATIC_ELECTRICAL_AUDIT.md`.

## Required Result

Return one result:

- `SCHEMATIC_ELECTRICAL_PASS`
- `SCHEMATIC_ELECTRICAL_FAIL`
- `NEEDS_HUMAN_REVIEW`

AI quality closeout is required.

