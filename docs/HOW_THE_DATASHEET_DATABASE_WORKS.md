# How The Datasheet Database Works

`06_DATASHEETS/` is a structured datasheet and reference-document library scaffold.

## Purpose

The database helps AI agents find source material without inventing component facts.

It stores:

- Source links.
- Metadata.
- Missing-document lists.
- Naming rules.
- Summary templates.
- Redistribution policy notes.
- Link-only versus bundled-document decisions.

## Public Release Rule

Do not include copyrighted PDFs in a public repo unless redistribution is clearly permitted.

Prefer:

- Vendor source links.
- Metadata.
- Human-written summaries.
- Notes about missing or unverified documents.

## Verification Status

Exact specs should come from verified source documents. If a value has not been checked, use:

```text
Unknown - requires source verification
```

## Useful Files

- `06_DATASHEETS/00_INDEX/DATASHEET_LIBRARY_README.md`
- `06_DATASHEETS/00_INDEX/NAMING_CONVENTIONS.md`
- `06_DATASHEETS/00_INDEX/METADATA_SCHEMA.md`
- `06_DATASHEETS/00_INDEX/PUBLIC_RELEASE_DATASHEET_POLICY.md`
- `06_DATASHEETS/00_INDEX/RESEARCH_PIPELINE.md`
