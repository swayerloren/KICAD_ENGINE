# Datasheet Link Schema

## Purpose

Track datasheet and document links without downloading PDFs by default.

## Fields

- `manufacturer_part_number`
- `manufacturer`
- `document_title`
- `document_type`
- `source_url`
- `source_supplier`
- `source_date`
- `revision`
- `publication_date`
- `public_redistribution_status`
- `local_copy_status`
- `verification_status`
- `notes`

## Redistribution Status Values

- `LINK_ONLY`
- `REDISTRIBUTION_ALLOWED`
- `REDISTRIBUTION_UNKNOWN`
- `DO_NOT_BUNDLE`

## Rules

- Prefer manufacturer-hosted datasheet links over distributor mirrors.
- Supplier-hosted datasheet mirrors require source and redistribution review.
- Do not download or commit PDFs by default.
