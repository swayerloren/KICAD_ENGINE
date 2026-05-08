# Supplier Ingestion

Status: `ACTIVE_SCAFFOLD_API_SAFE_DRY_RUN_FIRST`

This system must not scrape supplier websites. Use official APIs first, user-provided CSV exports second, and manual source-link records third.

Live API mode is not approved unless the user explicitly enables it for a specific source and credentials are supplied through environment variables or ignored local config. No API keys, tokens, or credentials may be committed.

## PURPOSE

`28_SUPPLIER_INGESTION` defines a safe supplier and vendor data ingestion layer for KiCad Engine. It helps Codex, Claude, and similar agents collect and normalize part numbers, manufacturer part numbers, supplier SKUs, stock/pricing metadata, datasheet links, lifecycle notes, package data, and footprint-risk notes without scraping supplier sites or storing credentials.

## WHAT_BELONGS_HERE

- Supplier connector documentation.
- API and authentication requirements.
- Field-mapping notes.
- User-provided CSV import workflows.
- Normalized supplier part records.
- Supplier gap reports.
- Datasheet-link metadata.
- Stock/pricing metadata snapshots with source dates.
- Footprint-risk notes derived from package and sourcing evidence.

## WHAT_DOES_NOT_BELONG_HERE

- API keys, tokens, passwords, private credentials, or paid-account data.
- Blind web scrapers.
- Cached pages from Mouser, Digi-Key, JLCPCB, LCSC, Octopart, or other suppliers.
- Mass-downloaded datasheets or copyrighted PDFs.
- Final sourcing approvals.
- KiCad design files or manufacturing outputs.

## AI_AGENT_RULES

- Use official supplier APIs first.
- Use user-provided CSV exports second.
- Use manual source-link records third.
- Do not bypass anti-scraping protections.
- Do not make live API calls unless the user explicitly provides the required environment/config and approves the call.
- Treat stock, price, lifecycle, and availability as time-sensitive.
- Mark imported records `UNVERIFIED` until source, date, and mapping are reviewed.
- Do not claim a KiCad footprint is correct based only on supplier package text.
- Use `31_PLAYWRIGHT_RESEARCH_PIPELINE` only for controlled public-page evidence when official APIs, user CSV exports, or manual source-link records are insufficient. Playwright output remains `UNVERIFIED`.

## SAFE_EDIT_RULES

- Scripts must be read-only against source inputs unless an explicit output path is provided.
- Scripts must write generated records under `normalized/` or `reports/`.
- API keys must be read only from environment variables or ignored local config.
- No script may download PDFs by default.
- No script may write into `06_DATASHEETS`, `08_COMPONENT_DATABASE`, `25_VENDOR_DATABASE`, or KiCad project files without a separate explicit task.
- No script may import Playwright evidence as verified supplier data without official-source or human review.

## PUBLIC_RELEASE_NOTES

Public releases should include connector scaffolds, schemas, and safe import scripts only. Do not publish private price quotes, private stock exports, API credentials, restricted supplier responses, or copyrighted documents unless redistribution rights are confirmed.
