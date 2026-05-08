# Mouser Source Profile

Source confidence level: `DISTRIBUTOR_OFFICIAL`

## Source Purpose

Supplier SKU, MPN, lifecycle/status, stock/pricing summary, datasheet-link, package text, and public product-page evidence.

## Preferred Access Method

Official API first. User-provided CSV export second. Playwright public page capture only when allowed.

## Login/API Key Required

API key required for official API. Public pages may be usable without login.

## Playwright Allowed

Allowed only for public product pages, controlled source-link capture, and screenshots. `--live` required.

## Fields May Be Captured

- product URL
- manufacturer and MPN
- Mouser part number
- public stock and price-break summary
- datasheet URL
- package/case text
- lifecycle/status text

## Must Not Be Captured

- API keys
- logged-in pages
- private account pricing
- carts, quotes, checkout data
- cookies or session data
- page scraping archives

## Rate Limit Guidance

Prefer API terms. Keep Playwright batches small and slow; stop on block, CAPTCHA, or login.

## Redistribution Guidance

Link-only metadata. Do not store copied datasheets unless rights are confirmed.

## Notes For Codex/Claude

Use Mouser package text as a search hint only.

