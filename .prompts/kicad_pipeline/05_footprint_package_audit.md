# 05 Footprint Package Audit

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: perform strict footprint and package verification before PCB update. Do not edit schematic or PCB files.

## Read First

1. `AGENTS.md`
2. `09_ACCURACY_ENGINE/verification_rules/FOOTPRINT_DATASHEET_MATCH_RULES.md`
3. `11_LIBRARY_FACTORY/mapping/DATASHEET_PACKAGE_TO_FOOTPRINT_STANDARD.md`
4. `11_LIBRARY_FACTORY/footprints/FOOTPRINT_QA_CHECKLIST.md`
5. `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`
6. Active project BOM lock, schematic-ready parts, and datasheet decisions.

## Do

1. Parse/export schematic symbol-footprint assignments.
2. Create a table: Ref, Value, MPN, Symbol, Footprint, Package, Datasheet source, Footprint verification, Risk.
3. Flag every unassigned or unverified footprint.
4. Require exact manufacturer drawing for connectors and high-risk mechanical parts.
5. Audit 3D model usefulness without treating 3D as footprint proof.
6. Create or update `reports/FOOTPRINT_PACKAGE_AUDIT.md`.

## Required Result

Return one result:

- `FOOTPRINT_AUDIT_PASS`
- `FOOTPRINT_AUDIT_FAIL`
- `NEEDS_HUMAN_REVIEW`

AI quality closeout is required.

