# Supplier Footprint Matches

Status: source-backed supplier-to-KiCad footprint matching scaffold.

## PURPOSE

`30_SUPPLIER_FOOTPRINT_MATCHES/` tracks whether supplier parts from Mouser, Digi-Key, JLCPCB, LCSC, or manual records have reliable KiCad symbol, footprint, and 3D model candidates.

This layer connects supplier metadata to KiCad library evidence without pretending that supplier package text is footprint verification.

## WHAT_BELONGS_HERE

- Supplier-to-KiCad match schemas.
- Confidence and human-review rules.
- Supplier CAD model source indexes and distrust rules.
- Match records keyed by supplier or manual verification workflow.
- Reports for unmatched supplier parts and low-confidence footprint mappings.
- Scripts that create, check, index, and report match records.

## WHAT_DOES_NOT_BELONG_HERE

- API keys, tokens, supplier credentials, or private quotes.
- Cached supplier pages or scraped supplier HTML.
- Downloaded datasheet PDFs or package drawings unless redistribution is confirmed.
- KiCad global library edits.
- Project-local production library files.
- Final footprint approvals without drawing-level evidence.

## AI_AGENT_RULES

- Use official supplier APIs, user CSV exports, or manual source-link records as input.
- Treat supplier package names as candidate metadata, not proof.
- Treat supplier CAD models as candidate geometry only until exact package proof exists.
- Do not mark connector, PMOS, ESD array, MCU module, or regulator footprints verified from package name only.
- Keep `human_review_required` set to `true` for high-risk parts until exact drawing, pad numbering, orientation, and mechanical review are complete.
- Route exact footprint verification evidence to `08_COMPONENT_DATABASE/16_VERIFICATION_RECORDS/` when appropriate.
- Playwright evidence from `31_PLAYWRIGHT_RESEARCH_PIPELINE` may provide source URLs, screenshots, and candidate package text, but it cannot verify a footprint by itself.

## Canonical Files

- [SUPPLIER_CAD_MODEL_RULES.md](SUPPLIER_CAD_MODEL_RULES.md)
- [CAD_MODEL_SOURCE_INDEX.md](CAD_MODEL_SOURCE_INDEX.md)
- [cad_model_index.json](cad_model_index.json)

## SAFE_EDIT_RULES

- Scripts must be non-destructive and write only to requested output paths.
- Do not modify KiCad installation folders, user global KiCad library tables, or KiCad design files.
- Do not store credentials.
- Do not make live supplier API calls from this folder.

## PUBLIC_RELEASE_NOTES

Public release can include schemas, scripts, and example-only records. Do not publish private supplier data, credentials, restricted API responses, or unlicensed datasheet/package drawing copies.
