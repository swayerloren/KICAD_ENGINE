# Avnet API Notes

Status: `DOCUMENTATION_ONLY`

## Connector Type

`official_api_or_user_exports`

## Live Calls

Live calls are not enabled by this scaffold. Before adding live calls:

- Verify the official API or approved feed path.
- Verify terms of use and rate limits.
- Require user approval for any network call.
- Read credentials only from environment variables or ignored local config.
- Never print, log, or commit credential values.

## Data To Prefer

- Manufacturer part number.
- Supplier SKU.
- Manufacturer name.
- Supplier part URL.
- Datasheet URL.
- Package text.
- Lifecycle status.
- Stock and price snapshot with source date.
