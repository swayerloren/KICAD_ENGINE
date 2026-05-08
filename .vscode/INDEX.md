# .vscode Index

## PURPOSE
AI-readable index for VS Code workspace files.

## WHAT_BELONGS_HERE
- `settings.json`
- `extensions.json`
- `tasks.json`
- `launch.json`

## WHAT_DOES_NOT_BELONG_HERE
- Secrets.
- Local user authentication state.
- Generated reports.

## AI_AGENT_RULES
- Use tasks for health checks, audits, index builds, validation, and NOT_FINAL exports.
- Do not run destructive commands from tasks.

## SAFE_EDIT_RULES
- Keep commands quoted and cross-platform where feasible.
- Do not assume installed AI credentials.

## PUBLIC_RELEASE_NOTES
- Recommended extensions should be free and relevant to Markdown, Python, PowerShell, JSON/YAML, Git, or KiCad support.
