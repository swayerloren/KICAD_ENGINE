# .codex Index

## PURPOSE
AI-readable routing index for workspace-local Codex support files.

## WHAT_BELONGS_HERE
- `.codex/config.toml` when workspace-local Codex settings are needed.
- `.codex/prompts/` for legacy or repo-specific Codex prompts.

## WHAT_DOES_NOT_BELONG_HERE
- Secrets.
- KiCad design files.
- Generated reports or fabrication packages.

## AI_AGENT_RULES
- Treat this as configuration, not durable project memory.
- Use `.prompts/` for the main public prompt pack.

## SAFE_EDIT_RULES
- Back up configuration before editing.
- Do not enable write-capable MCP profiles without explicit approval.

## PUBLIC_RELEASE_NOTES
- Review before payload builds; exclude private machine-local settings.
