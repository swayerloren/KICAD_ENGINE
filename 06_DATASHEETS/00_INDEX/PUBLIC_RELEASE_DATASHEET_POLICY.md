# Public Release Datasheet Policy

Date: 2026-05-02

Status: public-release safety policy.

## Policy

Do not publish copyrighted datasheets, application notes, reference manuals, package drawings, or vendor documents in this repo unless redistribution permission is clearly confirmed.

## Safe For Public Release

- Vendor source URLs.
- Product page URLs.
- Documentation portal URLs.
- Metadata records.
- Missing-document reports.
- AI-readable summaries written in original words with citations to document section/page when reviewed.
- Scripts that help users build their own local private library.
- Instructions telling users where to download documents from official sources.

## Not Safe By Default

- Vendor PDF datasheets.
- Full application notes.
- Full reference manuals.
- Package drawing PDFs.
- Dev board schematic PDFs if redistribution is not confirmed.
- Bulk mirrored vendor document folders.
- Files obtained behind account, license, export-control, or click-through terms.

## Redistribution Status Values

Use these values in source lists:

- `UNKNOWN`
- `LINK_ONLY_RECOMMENDED`
- `PRIVATE_LOCAL_COPY_ONLY`
- `PUBLIC_REDISTRIBUTION_PERMITTED`
- `REQUIRES_LICENSE_REVIEW`
- `DO_NOT_BUNDLE`

## Default Decision

When uncertain, use:

```text
LINK_ONLY_RECOMMENDED
```

and leave the file out of the public repo.

## Release Checklist

Before publishing:

1. Search for PDFs and document archives under `06_DATASHEETS`.
2. Confirm each bundled document's redistribution permission.
3. Move restricted documents out of the public release tree.
4. Keep source-list rows and metadata.
5. Document unresolved license questions in `MISSING_DATASHEETS.md` or a release audit.
