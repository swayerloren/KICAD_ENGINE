# README For Codex And Claude

## Use This Engine When

- the user asks to assign footprints
- the user asks whether a schematic is ready for PCB update
- the user asks for package or footprint verification
- the user asks for a footprint lock file or footprint proof

## First Reads

- `35_FOOTPRINT_PACKAGE_ENGINE/README.md`
- `FOOTPRINT_ASSIGNMENT_WORKFLOW.md`
- `FOOTPRINT_EVIDENCE_RULES.md`
- `HIGH_RISK_FOOTPRINT_RULES.md`
- `FOOTPRINT_LOCK_FILE_RULES.md`
- `PACKAGE_DRAWING_PROOF_RULES.md`
- `09_ACCURACY_ENGINE/verification_rules/FOOTPRINT_DATASHEET_MATCH_RULES.md`

## Canonical Commands

Dry-run extract:

```powershell
python 03_TOOLS/scripts/footprint_package/extract_physical_symbols.py --project <ACTIVE_PROJECT_PATH> --no-fail
```

Dry-run plan:

```powershell
python 03_TOOLS/scripts/footprint_package/generate_footprint_assignment_plan.py --project <ACTIVE_PROJECT_PATH> --no-fail
```

Dry-run gate:

```powershell
python 03_TOOLS/scripts/footprint_package/run_footprint_package_gate.py --project <ACTIVE_PROJECT_PATH> --no-fail
```

## Hard Rules

- Blank footprint is a hard fail.
- Name similarity is not verification.
- High-risk parts require extra proof.
- Connectors require mechanical orientation proof.
- Missing 3D model on connectors/mechanical parts requires human review.
- Do not claim schematic-to-PCB readiness unless the footprint/package gate is
  `PASS`.
