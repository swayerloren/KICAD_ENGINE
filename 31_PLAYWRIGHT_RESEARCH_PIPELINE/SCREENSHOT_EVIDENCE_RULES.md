# Screenshot Evidence Rules

Status: `MANDATORY`

## Allowed Screenshot Evidence

- Public manufacturer product pages.
- Public distributor product pages when terms allow viewing.
- Public KiCad library repository pages.
- Public search result pages only when capturing source-discovery context.

## Prohibited Screenshot Evidence

- Logged-in pages.
- Private account dashboards.
- Quotes, carts, order pages, checkout pages, or user-specific pricing.
- Pages showing API keys, tokens, usernames, cookies, or account identifiers.
- CAPTCHA pages except a small report note that capture stopped because CAPTCHA appeared.

## Storage Rules

- Store screenshots under `evidence/<timestamp>/`.
- Record source URL and retrieval timestamp.
- Do not crop out context in a way that hides the source identity.
- Do not treat screenshots as verified engineering proof.

