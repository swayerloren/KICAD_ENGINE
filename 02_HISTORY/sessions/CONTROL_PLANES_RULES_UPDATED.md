# Control Planes Rules Updated

Date: 2026-04-30

## Scope

Updated Codex startup and control-plane instructions so future agents know when to use common, Windows, and Linux tools.

## Safety Notes

- Did not move tools.
- Did not install anything.
- Did not modify KiCad project files.
- Did not change MCP permissions.

## Files Updated

- `AGENTS.md`
- `00_CODEX_START\START_HERE.md`
- `00_CODEX_START\WORKFLOW_RULES.md`
- `00_CODEX_START\SAFETY_RULES.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`

## Rules Added

- Common / Project Intelligence is the preferred first control plane whenever possible.
- Windows GUI Hands/Eyes is allowed only when common tools are insufficient and must begin with discovery.
- Linux / Headless / CI is for repeatable validation and must use headless checks first.
- Prefer CLI/API/MCP over GUI automation.
- Prefer read-only inspection before edits.
- Prefer copied project workspaces over original projects.
- Prefer `NOT_FINAL` outputs until the verification gate passes.

## Backups Created

- `99_BACKUPS\pre_codex_edits\AGENTS_BACKUP_20260430_183856.md`
- `99_BACKUPS\pre_codex_edits\START_HERE_BACKUP_20260430_183856.md`
- `99_BACKUPS\pre_codex_edits\WORKFLOW_RULES_BACKUP_20260430_183856.md`
- `99_BACKUPS\pre_codex_edits\SAFETY_RULES_BACKUP_20260430_183856.md`
- `99_BACKUPS\pre_codex_edits\README_GPT_BACKUP_20260430_183856.md`
- `99_BACKUPS\pre_codex_edits\FOR CHAT GPT_BACKUP_20260430_183856.MD`

## Conflicts Found

No functional conflicts found. Existing startup rules already required project identification, backups, and verification before KiCad edits. The control-plane rules clarify tool selection without changing tool locations, installs, MCP permissions, or KiCad project state.

## Next Recommended Prompt

Run a documentation-only consistency audit to confirm all startup, tool, and handoff files describe the same common/Windows/Linux control-plane hierarchy.
