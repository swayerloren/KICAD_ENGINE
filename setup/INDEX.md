# setup Index

## PURPOSE
AI-readable routing index for setup support.

## WHAT_BELONGS_HERE
- `windows/`
- `macos/`
- `linux/`
- `common/`

## WHAT_DOES_NOT_BELONG_HERE
- Secrets.
- Generated installer binaries.
- KiCad project source files.

## AI_AGENT_RULES
- Use setup scripts for checks and opt-in installs only.
- Do not assume package managers exist.

## SAFE_EDIT_RULES
- Preserve ask-before-install behavior.
- Keep scripts read-only unless the user explicitly chooses installation.

## PUBLIC_RELEASE_NOTES
- Setup scripts must be reviewed before public release on each platform.
