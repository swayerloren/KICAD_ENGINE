# 99_BACKUPS Index

## PURPOSE
AI-readable routing index for backup folders.

## WHAT_BELONGS_HERE
- `pre_codex_edits/`
- `project_snapshots/`
- Recovery records.

## WHAT_DOES_NOT_BELONG_HERE
- Secrets.
- Final release artifacts.
- Canonical current project files.

## AI_AGENT_RULES
- Check for backups before risky project edits.
- Do not treat backups as active design sources.

## SAFE_EDIT_RULES
- Do not delete or overwrite backups.
- Use timestamped folders.

## PUBLIC_RELEASE_NOTES
- Exclude private backups from public installer payloads unless explicitly sanitized.
