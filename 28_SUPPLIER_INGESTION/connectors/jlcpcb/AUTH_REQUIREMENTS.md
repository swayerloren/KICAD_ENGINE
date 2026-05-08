# JLCPCB Auth Requirements

Status: `NO_CREDENTIALS_CONFIGURED`

## Expected Credential Source

Environment variables or ignored local config only.

Example variable names:

`JLCPCB_API_KEY_IF_APPROVED`

These are names only. Do not put real values in repo files, Markdown, JSON examples, command logs, or history.

## Missing Credentials Behavior

A future connector must fail gracefully with a clear message and must not attempt fallback scraping.
