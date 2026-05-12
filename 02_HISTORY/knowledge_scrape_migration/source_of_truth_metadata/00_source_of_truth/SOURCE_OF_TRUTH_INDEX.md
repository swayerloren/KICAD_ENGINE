# SOURCE_OF_TRUTH_INDEX

Generated at: `2026-05-11T14:40:36`

## Priority Order

1. Original manufacturer PDFs in `../14_datasheets_pdf_markdown/original_pdf/`
2. Official manufacturer app notes and layout guides
3. Official KiCad docs, dev docs, and KLC/library sources
4. Fabricator rules
5. Forums, blogs, and videos only for corroboration or failure-mode examples

## Source Buckets

- `official_datasheets/`: use for pinouts, package drawings, electrical limits, and tables.
- `official_app_notes/`: use for vendor layout guidance and implementation details.
- `kicad_official_docs/`: use for KiCad behavior, file formats, APIs, and KLC guidance.
- `fabricator_rules/`: use for manufacturing constraints that must match the chosen board house.

## Top Official Domains

- `ww1.microchip.com`: `1254`
- `www.st.com`: `1115`
- `docs.kicad.org`: `979`
- `www.microchip.com`: `911`
- `gitlab.com`: `595`
- `www.ti.com`: `390`
- `forum.microchip.com`: `200`
- `www.silabs.com`: `108`
- `www.renesas.com`: `104`
- `docs.espressif.com`: `51`
- `www.espressif.com`: `41`
- `www.analog.com`: `33`
- `jlcpcb.com`: `29`
- `ti.com`: `23`
- `espressif.com`: `16`
- `dev-docs.kicad.org`: `13`
- `docs.oshpark.com`: `12`
- `www.infineon.com`: `10`
- `www.pcbway.com`: `10`
- `monolithicpower.com`: `9`

## Retrieval Rule

- Use `URL_INDEX.csv` before trusting a local file.
- Treat extracted PDF Markdown as secondary only.
- Cite local file path plus `url_index_id` when making engineering decisions.

