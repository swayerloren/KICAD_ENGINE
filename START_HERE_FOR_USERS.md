# Start Here For Users

KiCad Engine is a local-first AI-assisted KiCad engineering workspace. It helps Codex, Claude, and similar VS Code-based agents work around your installed KiCad app with more context and safer verification habits.

It does not replace KiCad, certify designs, store AI credentials, or submit boards for fabrication.

## What You Need

- KiCad installed locally.
- VS Code.
- Python for the repo scripts.
- Git if you cloned the repo.
- PowerShell on Windows, or a POSIX shell on macOS/Linux.
- Your own Codex, Claude, or other AI coding agent account.

Node/npm are only needed if you are building the Electron installer or working on JavaScript tooling.

## Open The Workspace

1. Download, clone, or install KiCad Engine.
2. Open the `KICAD_ENGINE` folder in VS Code.
3. Review workspace trust before trusting the folder.
4. Review optional recommended extensions in `.vscode/extensions.json`.
5. Log in to Codex, Claude, or your chosen AI tool yourself. This repo does not configure or store authentication.

Platform guides:

- `QUICKSTART_WINDOWS.md`
- `QUICKSTART_MACOS.md`
- `QUICKSTART_LINUX.md`

## First Files To Read

Read these before asking an AI agent to work here:

1. `README.md`
2. `DISCLAIMER.md`
3. `SECURITY.md`
4. `.prompts/README.md`
5. `START_HERE_FOR_AI_AGENTS.md`
6. `docs/SAFETY_AND_LIMITATIONS.md`

`AGENTS.md` is written for AI agents, but users should skim it so the safety model is clear.

## Run The Health Check

From VS Code, run `Tasks: Run Task` and choose:

```text
KiCad Engine: Run Health Check
```

Or run from a terminal:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\health_check.ps1
```

or:

```bash
python health_check.py
```

The health check reports missing tools and structure problems. It does not install tools or edit KiCad project files.

## Use The Prompt Pack

Use `.prompts/` when asking an AI agent to work in this repo:

- `.prompts/codex/` for Codex.
- `.prompts/claude/` for Claude.
- `.prompts/shared/` for common safety and verification standards.

Good first prompts:

- `.prompts/codex/00_START_SESSION.md`
- `.prompts/claude/00_START_SESSION.md`

## Common VS Code Tasks

Open the Command Palette and run `Tasks: Run Task`.

Useful tasks:

- `KiCad Engine: Run Health Check`
- `KiCad Engine: Audit Installed KiCad App`
- `KiCad Engine: Build Datasheet Index`
- `KiCad Engine: Build Component Database Index`
- `KiCad Engine: Validate a KiCad Project`
- `KiCad Engine: Run ERC`
- `KiCad Engine: Run DRC`
- `KiCad Engine: Export NOT_FINAL Review Package`

Project validation, ERC, DRC, and export tasks ask for a KiCad project folder or `.kicad_pro` file.

## Safety Rules

- Do not let an AI edit KiCad project files until the active project, target files, backup plan, verification plan, and rollback plan are confirmed.
- Do not trust generated component specs without source verification.
- Do not trust selected footprints without exact manufacturer package drawing verification.
- Do not treat ERC or DRC as full design approval.
- Keep generated manufacturing-style outputs labeled `NOT_FINAL` until final human approval.

## More Help

- `USER_MANUAL.md`
- `INSTALLER_USER_GUIDE.md`
- `FAQ.md`
- `TROUBLESHOOTING.md`
- `docs/HOW_TO_CREATE_A_PROJECT.md`
- `docs/HOW_TO_REVIEW_A_PROJECT.md`
- `docs/HOW_TO_RUN_ERC_DRC.md`
