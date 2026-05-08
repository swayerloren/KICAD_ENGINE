# setup

## PURPOSE
Cross-platform setup and requirements-check scripts.

## WHAT_BELONGS_HERE
- Windows setup scripts.
- macOS setup scripts.
- Linux setup scripts.
- Common setup helpers.

## WHAT_DOES_NOT_BELONG_HERE
- Secrets.
- Silent credential capture.
- KiCad project source files.

## AI_AGENT_RULES
- Setup scripts must ask before installing anything.
- Prefer official package managers and manual fallback instructions.

## SAFE_EDIT_RULES
- Do not use destructive commands.
- Do not silently install paid tools.
- Do not modify installed KiCad app folders or global libraries.

## PUBLIC_RELEASE_NOTES
- Public setup should be transparent, opt-in, and safe for local-first users.
