# Footprint Package Engine

## Purpose

This engine blocks schematic-to-PCB progression until every physical symbol has:

- a non-blank KiCad footprint
- a footprint lock row
- source or datasheet evidence
- package-drawing proof or an explicitly documented review reason
- risk classification
- required high-risk review evidence

## Scope

This layer is for footprint/package assignment proof, not just footprint text
population.

It is authoritative for:

- `FOOTPRINT_LOCK.csv` expectations
- per-part package evidence rules
- high-risk footprint proof rules
- footprint/package gate results before PCB update

## Canonical Files

- `FOOTPRINT_ASSIGNMENT_WORKFLOW.md`
- `FOOTPRINT_EVIDENCE_RULES.md`
- `HIGH_RISK_FOOTPRINT_RULES.md`
- `FOOTPRINT_LOCK_FILE_RULES.md`
- `PACKAGE_DRAWING_PROOF_RULES.md`
- `README_FOR_CODEX_AND_CLAUDE.md`
- `schemas/`

## Canonical Scripts

- `03_TOOLS/scripts/footprint_package/extract_physical_symbols.py`
- `03_TOOLS/scripts/footprint_package/audit_blank_footprints.py`
- `03_TOOLS/scripts/footprint_package/audit_footprint_lock.py`
- `03_TOOLS/scripts/footprint_package/audit_high_risk_footprints.py`
- `03_TOOLS/scripts/footprint_package/generate_footprint_assignment_plan.py`
- `03_TOOLS/scripts/footprint_package/run_footprint_package_gate.py`

## Required Project Files

Expected active-project support files:

- `FOOTPRINT_LOCK.csv`
- `SCHEMATIC_READY_PARTS_LIST.md`
- `NEEDS_REVIEW_BEFORE_SCHEMATIC.md`

Repo starter templates live under:

- `04_KICAD_PROJECTS/_templates/`

## Gate Rule

Do not move from schematic to PCB unless the latest footprint/package gate is
`PASS`.

Hard-fail examples:

- blank footprint on any physical symbol
- missing lock row for any physical symbol
- missing source link or package evidence
- high-risk footprint without package-drawing proof
- PMOS without symbol-pin to footprint-pad mapping proof
- connector without mechanical orientation proof

## Read-Only Validation

Canonical dry-run:

```powershell
python 03_TOOLS/scripts/footprint_package/run_footprint_package_gate.py --project <ACTIVE_PROJECT_PATH> --no-fail
```

The scripts parse `.kicad_sch` directly and never edit KiCad design files by
default.
