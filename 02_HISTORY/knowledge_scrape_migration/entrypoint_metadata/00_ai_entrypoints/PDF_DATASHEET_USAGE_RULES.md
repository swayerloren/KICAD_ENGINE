# PDF Datasheet Usage Rules

Extracted PDF Markdown is useful for search, indexing, and rough synthesis. It is not the source of truth for detailed engineering decisions.

## What The Extracted Markdown Is Good For

- finding where a concept appears in a long datasheet
- searching register names, feature names, and text descriptions
- quickly locating possible sections before opening the original PDF

## What Requires The Original PDF

Always go back to `14_datasheets_pdf_markdown/original_pdf/` for:
- pinouts
- package dimensions
- recommended land patterns
- recommended layout examples
- tables
- figures
- timing diagrams
- package drawings
- thermal pad details
- ordering tables

## Hard Rules

- Do not infer a footprint solely from extracted text.
- Do not trust extracted text alone for package size, pad geometry, or pin numbering.
- Do not assume figure captions, tables, or diagram labels survived extraction cleanly.
- If the extracted Markdown and the original PDF disagree, the original PDF wins.

## Practical Usage Pattern

1. Search the extracted Markdown to find the relevant section quickly.
2. Open the corresponding original PDF for final verification.
3. Cite the local extracted file for search context if useful.
4. Cite the original PDF as the engineering source of truth when details matter.

## Registry Linkage

Use these `URL_INDEX` fields when working with PDF material:
- `original_pdf_path`
- `extracted_markdown_path`
- `extraction_status`
- `extraction_tool`
- `extraction_warning`

If a PDF extraction failed or looks incomplete, check `14_datasheets_pdf_markdown/extraction_logs/` and keep the original PDF as the only authoritative reference.
