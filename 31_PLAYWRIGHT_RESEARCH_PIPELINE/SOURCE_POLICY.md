# Source Policy

Status: `MANDATORY`

## Preferred Source Order

1. Official APIs where available.
2. Official manufacturer/vendor pages.
3. Official distributor product pages.
4. Public KiCad library repositories.
5. User-provided CSV exports.
6. Playwright browser extraction only when allowed and useful.

## Allowed Inputs

- Official API responses when credentials are supplied through environment variables or ignored local config and the user explicitly approves live mode.
- Public manufacturer pages.
- Public distributor product pages that can be viewed without login and without bypassing access controls.
- Public KiCad library repository pages.
- User-provided CSV exports.
- Manual source-link records.

## Prohibited Inputs

- Credentials, cookies, browser sessions, paid-account pages, private quotes, and private stock data.
- CAPTCHA-protected pages.
- Pages requiring login or account acceptance.
- Pages whose terms prohibit automated access.
- Scraped HTML archives.
- Copyrighted PDFs without redistribution review.

## Output Status Rules

Every captured item must include:

- source URL
- source type
- retrieval timestamp
- source confidence
- redistribution status
- verification status
- human-review-required flag

Default verification status is `UNVERIFIED`.

## Datasheet Rule

Prefer link-only datasheet records. Do not download PDFs by default. PDF download, if ever enabled, requires explicit flags and redistribution-risk confirmation.

