# Datasheet Library Index

Status: `ACTIVE_INDEX`

This folder contains the control documents for KiCad Engine's datasheet and reference-document library.

## Purpose

`06_DATASHEETS/00_INDEX` tells Codex, Claude, and other agents how to record datasheet source links, metadata, summaries, missing documents, redistribution status, naming rules, and research workflow outputs.

This folder does not prove that a datasheet database is complete. It is the rules and index layer for building one safely.

## What Belongs Here

- Master datasheet index files.
- Source-list CSV files.
- Naming and metadata schemas.
- Datasheet, dev-board, errata, app-note, and reference-document templates.
- Copyright, redistribution, and link-only policies.
- Missing-datasheet reports.
- Duplicate/revision tracking.
- Research-pipeline rules.

## What Does Not Belong Here

- Downloaded PDFs unless redistribution rights are confirmed.
- Vendor documents copied from websites without license review.
- KiCad design files.
- Fabrication outputs.
- Supplier credentials or API keys.

## Agent Rules

- Prefer official manufacturer source URLs.
- Store source links and metadata before local files.
- Mark exact values `UNKNOWN_REQUIRES_SOURCE` until checked against a cited source.
- Do not infer pinouts, packages, footprints, voltage limits, current limits, or layout rules from folder names.
- Use `REDISTRIBUTION_REVIEW_REQUIRED.md` before including any local PDF in public release material.
- Public releases should be link-only unless redistribution permission is documented.

## Key Files

- `DATASHEET_LIBRARY_README.md`
- `MASTER_DATASHEET_INDEX.md`
- `NAMING_CONVENTIONS.md`
- `METADATA_SCHEMA.md`
- `PUBLIC_RELEASE_DATASHEET_POLICY.md`
- `LINK_ONLY_VS_BUNDLED_POLICY.md`
- `REDISTRIBUTION_REVIEW_REQUIRED.md`
- `source_lists/`
