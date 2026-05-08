# Secret Handling Rules

Status: `ACTIVE_POLICY`

## Never Store

- API keys.
- Passwords.
- OAuth tokens.
- Private keys.
- Signing certificates.
- Distributor credentials.
- Fab-house credentials.
- AI-provider credentials.

## Logs

Logs must not include secrets. If a secret appears in a log, stop and escalate for human review.

## Examples

Use placeholders such as `YOUR_API_KEY_HERE` only when clearly marked as examples. Do not include real values.

