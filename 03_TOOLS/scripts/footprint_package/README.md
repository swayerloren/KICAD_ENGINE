# Footprint Package Scripts

## Purpose

These scripts provide a read-only footprint/package proof layer for saved
KiCad schematics.

They detect:

- blank or missing footprints
- missing or incomplete `FOOTPRINT_LOCK.csv` rows
- missing source or package evidence
- high-risk footprint proof gaps
- connector and PMOS proof gaps

## Scripts

- `extract_physical_symbols.py`
- `audit_blank_footprints.py`
- `audit_footprint_lock.py`
- `audit_high_risk_footprints.py`
- `generate_footprint_assignment_plan.py`
- `run_footprint_package_gate.py`

## Canonical Commands

```powershell
python 03_TOOLS/scripts/footprint_package/extract_physical_symbols.py --project <ACTIVE_PROJECT_PATH> --no-fail
python 03_TOOLS/scripts/footprint_package/audit_blank_footprints.py --project <ACTIVE_PROJECT_PATH> --no-fail
python 03_TOOLS/scripts/footprint_package/audit_footprint_lock.py --project <ACTIVE_PROJECT_PATH> --no-fail
python 03_TOOLS/scripts/footprint_package/audit_high_risk_footprints.py --project <ACTIVE_PROJECT_PATH> --no-fail
python 03_TOOLS/scripts/footprint_package/generate_footprint_assignment_plan.py --project <ACTIVE_PROJECT_PATH> --no-fail
python 03_TOOLS/scripts/footprint_package/run_footprint_package_gate.py --project <ACTIVE_PROJECT_PATH> --no-fail
```

## Safety

- These scripts never edit `.kicad_sch` or `.kicad_pcb` by default.
- They parse saved schematic text directly.
- They are designed to fail closed when lock-file evidence is missing.
