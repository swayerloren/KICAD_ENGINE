# Mouser Environment Variables

Status: `DOCUMENTATION_ONLY`

## Required For Future Live Mode

This variable name is reserved for a future official Mouser API connector:

- `MOUSER_API_KEY`

## Rules

- Never commit real values.
- Never place values in Markdown, JSON examples, command logs, or history files.
- Read values only from the process environment or an ignored local config.
- Do not print values to stdout or stderr.
- Do not cache values.

## Current Stub Behavior

If `--live` is used and `MOUSER_API_KEY` is missing, the connector prints only the missing variable name. If the variable is present, the stub still refuses to make a live call because the official API implementation has not been added or tested.
