# Component Database

## PURPOSE

Store structured part intelligence for AI-assisted KiCad design beyond raw PDFs.

## WHAT_BELONGS_HERE

- Component records in Markdown and JSON.
- KiCad symbol, footprint, and 3D model candidates.
- Verification levels and source-confidence notes.
- Design-rule snippets and part-selection guides.

## WHAT_DOES_NOT_BELONG_HERE

- Datasheet PDFs.
- Active KiCad project source files.
- Fabrication outputs.
- Fabricated electrical claims.
- Secrets or distributor credentials.

## AI_AGENT_RULES

- Do not treat placeholder records as verified.
- Mark exact specs `Unknown - requires source verification` until sourced.
- Do not approve footprints without exact package or connector drawing review.
- Keep records link-first when document redistribution is unclear.

## SAFE_EDIT_RULES

- Add new records as `UNVERIFIED_PLACEHOLDER` unless verified.
- Preserve existing records.
- Do not delete old component decisions.

## PUBLIC_RELEASE_NOTES

Public release records must avoid unsupported claims and must not bundle restricted datasheets.

## CORE COMPONENT INTELLIGENCE UPDATE

The strict core component-intelligence layer adds:

- `00_INDEX/DO_NOT_GUESS_RULES.md`
- `00_INDEX/templates/`
- `15_PACKAGE_FOOTPRINT_DATABASE/`
- `16_VERIFICATION_RECORDS/`
- `99_UNVERIFIED_INBOX/core_starter_records/`

Starter records in `99_UNVERIFIED_INBOX/core_starter_records/` are placeholders only. They must not be used as approved schematic, footprint, BOM, purchase, or manufacturing data.
