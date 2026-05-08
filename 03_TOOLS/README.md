# 03_TOOLS

## PURPOSE
Tooling, scripts, read-only analyzers, external tool notes, and platform control roots.

## WHAT_BELONGS_HERE
- Safe scripts.
- Tool logs.
- External repositories under controlled subfolders.
- Platform roots for common, Windows, and Linux automation.
- Placeholder docs for local-only environments, clones, and logs.

## WHAT_DOES_NOT_BELONG_HERE
- Active KiCad project sources.
- Secrets.
- Final manufacturing packages.

## AI_AGENT_RULES
- Prefer read-only scripts and CLI/API workflows before GUI automation.
- Do not install tools unless explicitly requested.

## SAFE_EDIT_RULES
- Keep scripts non-destructive by default.
- Do not modify third-party repos casually.

## PUBLIC_RELEASE_NOTES
- Exclude large environments, node modules, and private logs from clean payloads.
- `node_envs/`, `python_envs/`, `repos/`, and `tool_logs/` are local-only by default and appear on GitHub via placeholder `README.md` files only.
- A portable clone or ZIP user should be able to use the repo docs, rules, prompts, and included scripts without these local-only folders being populated.
- Extra cloned GitHub repos under `03_TOOLS/repos/` are optional helper sources only. They are not required for basic repo use.
