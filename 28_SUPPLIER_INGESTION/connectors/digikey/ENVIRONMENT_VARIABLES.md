# Digi-Key Environment Variables

Status: `DOCUMENTATION_ONLY`

## Required For Future Live Mode

These variable names are reserved for a future official Digi-Key API connector:

- `DIGIKEY_CLIENT_ID`
- `DIGIKEY_CLIENT_SECRET`

## Rules

- Never commit real values.
- Never place values in Markdown, JSON examples, command logs, or history files.
- Read values only from the process environment or an ignored local config.
- Do not print values to stdout or stderr.
- Do not cache values.

## Current Stub Behavior

If `--live` is used and variables are missing, the connector prints only the missing variable names. If variables are present, the stub still refuses to make a live call because the official API implementation has not been added or tested.
