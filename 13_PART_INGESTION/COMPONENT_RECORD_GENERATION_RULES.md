# Component Record Generation Rules

## Purpose

Generate `08_COMPONENT_DATABASE` records from source-backed data without inventing details.

## Required Behavior

- Use `Unknown - requires source verification` for unchecked values.
- Default verification flag is `UNVERIFIED_PLACEHOLDER`.
- Preserve source URL and local path if provided.
- Keep Markdown and JSON records consistent.
- Do not mark pinout or footprint verified from a datasheet stub alone.

## Required Fields

Follow:

- `08_COMPONENT_DATABASE/00_INDEX/PART_SCHEMA.md`
- `08_COMPONENT_DATABASE/00_INDEX/VERIFICATION_LEVELS.md`
- `08_COMPONENT_DATABASE/00_INDEX/KICAD_SYMBOL_FOOTPRINT_LINKING_RULES.md`

## AI Warnings

Every generated placeholder record should warn:

- Do not add to schematic until pinout is verified.
- Do not assign footprint until exact package drawing is verified.
- Do not treat candidate KiCad symbols or footprints as approved.
- Do not create fabrication outputs from placeholder data.

## Output Status

Use:

- `UNVERIFIED_PLACEHOLDER`
- `UNVERIFIED_SYMBOL`
- `UNVERIFIED_FOOTPRINT`
- `Unknown - requires source verification`

until source evidence is reviewed.

