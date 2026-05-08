# Terms And Rate Limit Rules

Status: `MANDATORY`

## Access Rules

- Use official APIs before browser automation.
- Do not bypass paywalls, login prompts, CAPTCHA, rate limits, anti-bot protections, robots guidance, or site terms.
- Do not use personal browser profiles or saved sessions.
- Do not store cookies, local storage, browser profiles, auth headers, or session screenshots.

## Rate Rules

- Default live browser runs must use a low request rate.
- Wait between pages.
- Keep batches small.
- Stop when blocked.
- Stop when a page displays CAPTCHA, login, account-wall, or "access denied" language.
- Record a `BLOCKED_OR_LOGIN_REQUIRED` status instead of trying again aggressively.

## Human Review Rules

Human review is required when:

- terms are unclear,
- the source requires login,
- data conflicts across sources,
- a package/footprint decision is high risk,
- a connector orientation or pin numbering decision is involved,
- stock/price/lifecycle data affects a purchasing decision.

