# API Key Handling

## Rule

No API keys, tokens, passwords, client secrets, private config, paid-account credentials, or commercial quote data may be committed to this repo.

## Allowed Credential Sources

- Environment variables.
- A local ignored config file such as `private_config.local.json`.
- A password manager or OS credential store outside this repo.

## Disallowed Credential Sources

- Markdown files.
- JSON examples committed to the repo.
- Python source files.
- PowerShell scripts.
- `.env` files committed to source control.
- Command logs or history records.

## Connector Behavior

Connector scripts must:

- Fail gracefully when credentials are missing.
- Explain which environment variables are expected.
- Avoid printing secret values.
- Avoid writing credentials to logs.
- Support dry-run and offline normalization where possible.

## Example Environment Variable Names

These names are examples only. They are not configured and must not contain real values in repo files:

- `DIGIKEY_CLIENT_ID`
- `DIGIKEY_CLIENT_SECRET`
- `MOUSER_API_KEY`
- `OCTOPART_API_KEY`
- `SUPPLIER_INGESTION_CONFIG`

## Local Ignored Files

`28_SUPPLIER_INGESTION/.gitignore` excludes local credential and config file patterns.
