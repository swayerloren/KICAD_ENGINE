# JLCPCB API Access Notes

Status: `NO_APPROVED_LIVE_CONNECTOR`

## Policy

The JLCPCB connector may only use official, approved API or data-feed access, user-provided exports, or manual source-link records. It must not scrape JLCPCB pages or bypass access controls.

## Current Implementation

`jlcpcb_connector.py` supports offline `DRY_RUN` normalization only. `--live` exits without a network call.

## Future Credential Handling

If JLCPCB provides or approves an API path for this use case, credentials must be read only from environment variables or ignored local config. No credential values may be committed, printed, cached, or written to command logs.

Reserved future environment variable name:

- `JLCPCB_API_KEY`

## Preferred Inputs Today

- User-provided BOM/assembly CSV exports.
- User-provided parts-library exports.
- Manual source-link records with retrieval date.
