# Schematic Footprint Gate

## Rule

Every physical component must have a footprint before PCB update.

Footprint presence alone is not enough. Footprint/package proof is
authoritatively enforced by `35_FOOTPRINT_PACKAGE_ENGINE/`.

## Required

- footprint field exists on every physical symbol
- footprint field is not blank
- `FOOTPRINT_LOCK.csv` exists and covers every physical symbol
- source evidence exists for every physical symbol
- high-risk footprints have exact package-drawing verification
- connectors have mechanical orientation proof
- PMOS / reverse-polarity FETs have explicit pin-mapping proof

## Fail Conditions

- blank footprint on a physical symbol
- missing footprint property
- missing `FOOTPRINT_LOCK.csv`
- missing lock row for any physical symbol
- assigned footprint without source evidence
- high-risk footprint without required proof
- visible placeholder or review-marker value left on a production symbol

## Note

Use `python 03_TOOLS/scripts/footprint_package/run_footprint_package_gate.py --project <ACTIVE_PROJECT_PATH> --no-fail`
for the authoritative read-only gate.
