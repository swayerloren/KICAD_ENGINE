# Digi-Key Source Profile

Source confidence level: `DISTRIBUTOR_OFFICIAL`

## Source Purpose

Supplier SKU, availability, pricing summary, datasheet-link, manufacturer part, package text, lifecycle/status metadata, and product-page evidence.

## Preferred Access Method

Official API first. User-provided CSV export second. Playwright public page capture only when API/CSV is unavailable and terms allow public browsing.

## Login/API Key Required

API key required for official API. Public product pages may be viewable without login, but browser capture must stop if login, CAPTCHA, or blocking appears.

## Playwright Allowed

Allowed only for public product pages and screenshot/source-link capture. `--live` required.

## Fields May Be Captured

- product URL
- manufacturer and MPN
- Digi-Key SKU
- public stock/availability text with retrieval timestamp
- public price-break summary
- datasheet link URL
- package text
- lifecycle/status text

## Must Not Be Captured

- API keys or client secrets
- logged-in pages
- carts, quotes, order pages
- private price/account data
- cookies or session data
- raw HTML archives

## Rate Limit Guidance

Use API rate limits when using API. For public-page evidence, use low-volume manual-sized batches with delay and stop on block.

## Redistribution Guidance

Store metadata and source links only. Do not bundle Digi-Key pages or downloaded PDFs.

## Notes For Codex/Claude

Supplier package text is not footprint verification. Treat stock and pricing as time-sensitive.

