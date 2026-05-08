# Playwright Research Pipeline

Status: `ACTIVE_SCAFFOLD_DRY_RUN_FIRST`

Playwright research output is evidence, not truth. Any data captured from browser pages must remain `UNVERIFIED` until checked against an official datasheet, official vendor source, package drawing, KiCad library evidence, or human review.

Do not run live browser capture unless the user explicitly approves it for a specific target/source and the source profile allows Playwright on public pages.

## PURPOSE

`31_PLAYWRIGHT_RESEARCH_PIPELINE` defines a controlled Playwright-assisted research workflow for supplier, datasheet, part-number, vendor, and KiCad-footprint evidence.

It helps grow:

- `06_DATASHEETS`
- `08_COMPONENT_DATABASE`
- `25_VENDOR_DATABASE`
- `28_SUPPLIER_INGESTION`
- `29_FOOTPRINT_GAP_ANALYSIS`
- `30_SUPPLIER_FOOTPRINT_MATCHES`

This system is not a scraper. It is a browser-assisted evidence capture layer for public pages, controlled searches, source-link capture, metadata normalization, screenshots, and human-review workflows.

## WHAT_BELONGS_HERE

- Playwright usage rules.
- Source profiles and rate-limit notes.
- Research target CSV files.
- Dry-run planning scripts.
- Public-page capture scripts that require explicit `--live`.
- Normalized research output schemas.
- Screenshot and source-evidence templates.
- Integration docs for downstream KiCad Engine systems.

## WHAT_DOES_NOT_BELONG_HERE

- API keys, tokens, passwords, cookies, session data, or private account exports.
- Scraped supplier HTML archives.
- CAPTCHA bypasses or login automation.
- Mass-downloaded datasheets.
- Copyrighted PDFs unless redistribution rights are confirmed.
- KiCad design files or global KiCad library edits.
- Final footprint, sourcing, lifecycle, or design approvals.

## AI_AGENT_RULES

- Default to `DRY_RUN`.
- Use official APIs first, official manufacturer pages second, distributor pages third, public KiCad library sources fourth, user CSV fifth, and Playwright public-page extraction only when allowed and useful.
- Do not bypass login, paywalls, anti-bot protections, access controls, or site terms.
- Do not store credentials or browser profiles.
- Stop if a page requests login, shows CAPTCHA, blocks automation, or has unclear terms.
- Treat browser-captured data as evidence, not truth.
- Mark all captured part data `UNVERIFIED` until checked against an official datasheet, official vendor source, or human review.

## SAFE_EDIT_RULES

- Scripts may write timestamped research artifacts under this folder's `output/`, `evidence/`, and `reports/` folders.
- Scripts must not write into `06_DATASHEETS`, `08_COMPONENT_DATABASE`, `25_VENDOR_DATABASE`, `28_SUPPLIER_INGESTION`, `29_FOOTPRINT_GAP_ANALYSIS`, or `30_SUPPLIER_FOOTPRINT_MATCHES` unless a future task explicitly enables a reviewed `--apply` mode.
- Scripts must not edit KiCad project files.
- Scripts must not download PDFs by default.
- `--download-pdf` requires `--confirm-redistribution-risk` and should still prefer link-only records.

## PUBLIC_RELEASE_NOTES

Public releases may include these policies, target templates, dry-run scripts, and normalized schema templates. Do not publish private supplier captures, screenshots from logged-in sessions, restricted raw API responses, cookies, credentials, or copyrighted PDFs without redistribution review.
