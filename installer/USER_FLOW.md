# User Flow

Status: planning only.

## First Install

1. User downloads installer from the official GitHub release.
2. User verifies publisher/signature/checksum if desired.
3. User runs installer.
4. Installer explains:
   - KiCad Engine is local-first.
   - It uses the user's installed KiCad app.
   - It does not bundle KiCad in v1.
   - It does not store AI credentials.
   - It does not require paid APIs.
5. User selects install folder.
6. Installer checks for existing files.
7. Installer creates `KICAD_ENGINE` workspace.
8. Installer checks requirements.
9. Installer offers optional installs for missing free tools.
10. Installer configures VS Code workspace files.
11. Installer installs prompt pack files into `.prompts`.
12. Installer creates datasheet and component database scaffolding.
13. Installer runs health check.
14. Installer shows health summary and report path.
15. Installer opens VS Code at the workspace.

## First AI Agent Session

1. User logs in to Codex, Claude, or another AI tool using their own account.
2. User opens `.prompts/README.md`.
3. User copies the appropriate start prompt:
   - `.prompts/codex/00_START_SESSION.md`
   - `.prompts/claude/00_START_SESSION.md`
4. Agent reads `AGENTS.md` and startup files.
5. Agent reports active project status and safety gates.

## Missing KiCad Flow

If KiCad is missing:

1. Installer reports KiCad missing.
2. Installer explains KiCad is not bundled in v1.
3. Installer offers official package-manager install when available.
4. User confirms or skips.
5. Installer continues with repo setup but health check remains warning/fail until KiCad is installed.

## Missing VS Code Flow

If VS Code is missing:

1. Installer reports VS Code missing.
2. Installer offers official package-manager install when available.
3. User confirms or skips.
4. Installer still creates the repo and writes setup reports.

## Repair Flow

1. User points installer at existing workspace.
2. Installer runs health check.
3. Installer identifies missing repo scaffolding.
4. Installer offers repair.
5. Installer backs up files before overwriting repo-controlled files.
6. Installer writes repair report.

## Uninstall Flow

Uninstall must be conservative:

- Remove only installer registration/launcher files if present.
- Do not delete user workspace by default.
- Offer to open workspace folder so user can archive or delete it manually.
- Never delete KiCad projects, memory, history, outputs, datasheets, component records, or backups without explicit user selection.

## Success Message

Success message should say:

`KiCad Engine is ready for local review and AI-assisted KiCad workflows. It is not fabrication approval. Use KiCad, ERC, DRC, BOM review, footprint verification, datasheet review, and human visual review before manufacturing.`
