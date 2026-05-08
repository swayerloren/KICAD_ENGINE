# 04_KICAD_PROJECTS

## PURPOSE
Active KiCad projects, archived samples, and project templates.

## WHAT_BELONGS_HERE
- `active/` project workspaces.
- `templates/` project templates.
- Archived disposable samples when intentionally retained.

## WHAT_DOES_NOT_BELONG_HERE
- Global tools.
- Global command logs.
- Secrets.

## AI_AGENT_RULES
- Do not edit KiCad project files until active project, backup, verification, and rollback gates are confirmed.
- Use project `memory/` and `history/` for project-specific evidence.

## SAFE_EDIT_RULES
- Back up before KiCad source edits.
- Keep generated manufacturing outputs `NOT_FINAL`.

## PUBLIC_RELEASE_NOTES
- Public payloads should include only safe samples or templates, not private user projects.
