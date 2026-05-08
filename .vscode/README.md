# .vscode

## PURPOSE
VS Code workspace support for users and AI agents.

## WHAT_BELONGS_HERE
- Workspace settings.
- Recommended extensions.
- Tasks.
- Launch configuration.

## WHAT_DOES_NOT_BELONG_HERE
- Secrets, tokens, or AI credentials.
- User-private machine settings.
- KiCad design files.

## AI_AGENT_RULES
- Do not assume Codex, Claude, or other AI tools are authenticated.
- Tasks should be safe, local, and explicit.

## SAFE_EDIT_RULES
- Do not add paid-tool requirements.
- Do not silently install dependencies through tasks.

## PUBLIC_RELEASE_NOTES
- VS Code support should work as a local-first helper layer, not a credential store.
