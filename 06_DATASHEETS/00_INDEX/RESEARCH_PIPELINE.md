# Datasheet Research Pipeline

Date: 2026-05-02

Status: controlled, metadata-first research workflow. Downloads are disabled by default.

## Purpose

This pipeline lets Codex, Claude, and similar agents collect source links, metadata, missing-document reports, and AI-readable summary stubs without bulk downloading datasheets or ignoring redistribution limits.

## Core Rules

- Do not mass-download datasheets.
- Do not scrape websites aggressively.
- Do not bypass vendor restrictions, login walls, robots controls, paywalls, or license gates.
- Prefer source links, metadata, summaries, and user instructions.
- Do not include copyrighted PDFs in a public GitHub repo unless redistribution is clearly permitted.
- Treat source-list rows as leads, not proof.

## Pipeline Stages

1. **Source List Entry**
   - Add candidate source rows under `06_DATASHEETS/00_INDEX/source_lists`.
   - Use vendor home pages, product pages, documentation portals, or safe search entry points.
   - Avoid direct PDF URLs unless verified.

2. **Link Validation**
   - Run `03_TOOLS/scripts/datasheets/validate_datasheet_links.py`.
   - It checks URL reachability where possible.
   - It does not download PDFs.

3. **Index Building**
   - Run `03_TOOLS/scripts/datasheets/build_datasheet_index.py`.
   - It converts CSV/JSON source lists into a markdown index.
   - It marks redistribution status and missing metadata.

4. **Missing Report**
   - Run `03_TOOLS/scripts/datasheets/create_missing_datasheet_report.py`.
   - It reports rows needing source URLs, local folders, redistribution status, part numbers, titles, or verification.

5. **Summary Stub Generation**
   - Run `03_TOOLS/scripts/datasheets/generate_component_summary_stub.py`.
   - It generates AI-readable summary stub files with all exact values marked unknown until reviewed.

6. **Future Download Review**
   - A future `--download` workflow may be added, but it must remain gated by license and redistribution checks.
   - Downloaded files must not be committed to a public repo unless redistribution is clearly permitted.

## Default Output Locations

- Link validation reports: `05_OUTPUTS/datasheet_research/link_validation_report.md`
- Built index: `05_OUTPUTS/datasheet_research/datasheet_source_index.md`
- Missing report: `05_OUTPUTS/datasheet_research/missing_datasheet_report.md`
- Summary stubs: `05_OUTPUTS/datasheet_research/summary_stubs`

## Public Release Rule

For a public GitHub release, the safe default is:

- Commit source-list CSVs.
- Commit metadata and summaries.
- Commit scripts.
- Do not commit restricted PDFs.
- Include only documents with verified redistribution permission.

## Verification Gate Before Design Use

Before a source-list entry can support a KiCad schematic, footprint, BOM, or layout decision:

1. Confirm official source URL.
2. Confirm document type and revision.
3. Confirm whether local storage is allowed.
4. Review the document manually or with an approved summary workflow.
5. Link the document to the component database record.
6. Verify symbol, footprint, and 3D model separately.
