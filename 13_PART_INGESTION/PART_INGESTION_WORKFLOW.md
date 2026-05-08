# Part Ingestion Workflow

Use this workflow when a user asks to add or research a new component.

## Inputs

- Part number.
- Vendor/manufacturer.
- Category.
- Datasheet URL or user-provided local datasheet path.
- Package or module variant if known.
- Intended use in the design.

## Steps

1. Create a source record from the user-provided URL or local path.
2. Do not download or redistribute the PDF unless permission is clear.
3. Generate a datasheet summary stub.
4. Generate component database Markdown and JSON stubs.
5. Generate symbol requirements checklist.
6. Generate footprint requirements checklist.
7. Extract or mark unknown:
   - Pinout.
   - Electrical limits.
   - Absolute maximum ratings.
   - Recommended operating conditions.
   - Package and land-pattern requirements.
   - Layout notes.
   - Required external parts.
   - Common mistakes.
8. Add source links and verification status.
9. Mark missing evidence explicitly.
10. Store generated outputs in the selected output folder.

## Required Cross-Checks

- `06_DATASHEETS/00_INDEX/METADATA_SCHEMA.md`
- `06_DATASHEETS/00_INDEX/DATASHEET_SUMMARY_TEMPLATE.md`
- `08_COMPONENT_DATABASE/00_INDEX/PART_SCHEMA.md`
- `08_COMPONENT_DATABASE/00_INDEX/AI_USAGE_RULES.md`
- `11_LIBRARY_FACTORY/symbols/SYMBOL_QA_CHECKLIST.md`
- `11_LIBRARY_FACTORY/footprints/FOOTPRINT_QA_CHECKLIST.md`

## Exit Criteria

The workflow is complete when the part has:

- Datasheet summary stub.
- Component record Markdown.
- Component record JSON.
- Symbol checklist.
- Footprint checklist.
- Layout warnings.
- Common mistakes.
- Source links.
- Verification status.

Default status is `UNVERIFIED_PLACEHOLDER` until exact source review is complete.

