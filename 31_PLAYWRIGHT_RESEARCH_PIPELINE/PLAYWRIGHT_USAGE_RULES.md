# Playwright Usage Rules

Status: `MANDATORY`

## Default Mode

All scripts default to `DRY_RUN`. In dry-run mode scripts may:

- read local target CSV files,
- create research plans,
- create normalized placeholder JSON,
- create Markdown reports,
- validate arguments,
- state what would be captured.

Dry-run mode must not:

- open a browser,
- make network requests,
- download PDFs,
- write credentials,
- modify downstream databases.

## Live Mode

Live browser execution requires `--live`.

Live mode may only be used for:

- public pages,
- source-link capture,
- controlled metadata extraction,
- public-page screenshot evidence,
- official/public source verification.

Live mode must stop when:

- login is required,
- CAPTCHA appears,
- access is denied,
- terms are unclear,
- the site blocks automation,
- the user requested dry-run only.

## PDF Rule

`--download-pdf` is disabled by default. If a future task enables it, it must also require `--confirm-redistribution-risk`, write a risk note, and prefer link-only storage.

## Evidence Rule

Screenshots and extracted data are evidence, not truth. They must not promote a part, datasheet, stock value, lifecycle state, symbol, footprint, package, or 3D model to verified status without official source review or human review.

## Allowed Live Capture Scope

Live Playwright use is limited to one clearly scoped public page at a time unless the user explicitly approves a batch. Acceptable live tasks:

- capture a product/source page screenshot,
- record page title, URL, retrieval timestamp, and short visible-text excerpt,
- detect whether a page requires login, CAPTCHA, or blocks automation,
- extract obvious public metadata fields when terms allow it,
- create `UNVERIFIED` normalized JSON and Markdown evidence.

Unacceptable live tasks:

- bulk scraping inventory or pricing tables,
- crawling supplier categories,
- bypassing anti-bot systems,
- using personal browser profiles or saved cookies,
- logging in to supplier accounts,
- downloading PDFs without explicit risk confirmation,
- storing raw restricted HTML or API payloads.

## Required Live Run Checklist

Before `--live`, the agent must record:

1. source profile read,
2. exact URL,
3. reason public-page capture is allowed,
4. output folder,
5. confirmation that no login, credentials, or PDF download will be used,
6. stop condition for CAPTCHA, blocking, or unclear terms.

After `--live`, the report must list source URLs, screenshot paths, normalized output paths, blocked sources, and every field that remains `UNVERIFIED`.
