# 03_TOOLS Index

## PURPOSE
AI-readable routing index for tools and scripts.

## WHAT_BELONGS_HERE
- `scripts/`
- `tool_logs/`
- `kicad_app_intelligence/`
- `kicad_library_intelligence/`
- `common/`, `windows/`, and `linux/`
- External tool repos and isolated environments.

## WHAT_DOES_NOT_BELONG_HERE
- Project design files.
- Secrets.
- Final fab outputs.

## AI_AGENT_RULES
- Confirm a tool exists before using it.
- Record important command results in `02_HISTORY/command_logs/`.

## SAFE_EDIT_RULES
- Scripts should fail gracefully and avoid destructive defaults.
- Do not write into installed KiCad folders.

## PUBLIC_RELEASE_NOTES
- Public payloads should not include large dependency folders unless intentionally packaged.
- `node_envs/`, `python_envs/`, `repos/`, and `tool_logs/` are intentionally local-only and should be represented on GitHub by placeholder docs rather than real local contents.
