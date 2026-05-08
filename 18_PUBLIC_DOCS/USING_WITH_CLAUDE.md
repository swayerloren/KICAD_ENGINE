# Using With Claude

Status: `PUBLIC_DRAFT`

## Setup

1. Open KiCad Engine in VS Code.
2. Log in to Claude with your own account.
3. Use `.prompts/claude/00_START_SESSION.md`.
4. Keep project edits gated by backup and verification rules.

## Required Safety Gates

- No fake datasheet values.
- No unverified footprint approval.
- No connector orientation assumptions.
- No final fab outputs without review.
- Logs and reports go to history/output folders.

## Prompt Pack

Use task prompts in `.prompts/claude/` and shared standards in `.prompts/shared/`.

