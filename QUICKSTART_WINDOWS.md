# Quickstart Windows

Windows is the primary first-platform workflow for KiCad Engine.

KiCad Engine uses your installed KiCad app. It does not replace KiCad, store AI credentials, or write into `C:\Program Files\KiCad`.

## Prerequisites

- Windows 10 or newer.
- KiCad installed locally.
- VS Code.
- Python on `PATH`.
- PowerShell.
- Codex, Claude, or another AI coding agent installed separately and logged in by you.
- Node/npm only if building the Electron installer.

## Open In VS Code

1. Open VS Code.
2. Open your `KICAD_ENGINE` folder.
3. Review workspace trust before trusting the folder.
4. Review optional extensions from `.vscode/extensions.json`.
5. Open `.prompts/README.md`.
6. Use the Codex or Claude start-session prompt.

## Run The Health Check

From VS Code:

1. Open Command Palette.
2. Run `Tasks: Run Task`.
3. Select `KiCad Engine: Run Health Check`.

Or run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\health_check.ps1
```

Expected report:

```text
05_OUTPUTS/health_checks/
```

No KiCad design files should be edited.

## Audit Installed KiCad

Run this VS Code task:

```text
KiCad Engine: Audit Installed KiCad App
```

The audit searches for the installed KiCad app, inventories local KiCad assets, and writes reports under:

```text
05_OUTPUTS/kicad_app_audit/
```

It must not modify `C:\Program Files\KiCad` or user-global KiCad config.

## Validate A KiCad Project

For validation, ERC, DRC, and exports, VS Code asks for a project path.

Use a project folder or `.kicad_pro` file, for example:

```text
C:\Users\<you>\Documents\MyBoard\MyBoard.kicad_pro
```

Useful tasks:

- `KiCad Engine: Validate a KiCad Project`
- `KiCad Engine: Run ERC`
- `KiCad Engine: Run DRC`
- `KiCad Engine: Export NOT_FINAL Review Package`

Review reports are written under `05_OUTPUTS/` unless the script documents another output folder.

## AI Agent Workflow

1. Log in to your own Codex or Claude environment.
2. Paste `.prompts/codex/00_START_SESSION.md` or `.prompts/claude/00_START_SESSION.md`.
3. For a specific task, paste the matching prompt from `.prompts/codex` or `.prompts/claude`.
4. Require the agent to read `AGENTS.md` and startup files first.
5. Do not approve KiCad source edits until backup, rollback, and verification plans are clear.

## PowerShell Execution Policy

If PowerShell blocks scripts, use the repo command form:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\health_check.ps1
```

This bypass applies to that process only. Do not weaken system policy globally unless you understand the tradeoff.

## Fabrication Safety

Generated manufacturing-style outputs must remain `NOT_FINAL` until ERC, DRC, BOM, footprint, datasheet, connector, polarity, mechanical, and visual reviews pass.
