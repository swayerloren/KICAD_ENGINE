# How The Component Database Works

`08_COMPONENT_DATABASE/` stores AI-readable component intelligence beyond PDFs.

## Purpose

The database helps agents reason about common electronics parts:

- Part number and vendor.
- Category and family.
- Package candidates.
- KiCad symbol candidates.
- KiCad footprint candidates.
- Datasheet source status.
- Layout warnings.
- Common mistakes.
- Required external parts.
- Verification status.

## Verification Levels

Records use verification flags such as:

- `VERIFIED_FROM_DATASHEET`
- `VERIFIED_FROM_VENDOR_REFERENCE_DESIGN`
- `VERIFIED_FROM_KICAD_LIBRARY`
- `USER_CONFIRMED`
- `UNVERIFIED_PLACEHOLDER`

Do not treat placeholder records as approved.

## KiCad Matching

Symbol and footprint candidates are not final selections. Exact footprint approval requires checking the manufacturer package drawing and land pattern against the KiCad footprint.

## Useful Files

- `08_COMPONENT_DATABASE/00_INDEX/COMPONENT_DATABASE_README.md`
- `08_COMPONENT_DATABASE/00_INDEX/PART_SCHEMA.md`
- `08_COMPONENT_DATABASE/00_INDEX/VERIFICATION_LEVELS.md`
- `08_COMPONENT_DATABASE/00_INDEX/KICAD_SYMBOL_FOOTPRINT_LINKING_RULES.md`
