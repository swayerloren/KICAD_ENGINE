# Codex Prompt: Audit Installed KiCad

You are working in your local `KICAD_ENGINE` repo root from VS Code.

## Read First

Read `AGENTS.md`, `.prompts/shared/SAFETY_GATES.md`, `00_CODEX_START/START_HERE.md`, `00_CODEX_START/PATH_PORTABILITY_RULES.md`, `00_CODEX_START/CONTROL_PLANES.md`, `00_CODEX_START/KICAD_SAFE_AUTOMATION_RULES.md`, and `03_TOOLS/kicad_app_intelligence/KICAD_DO_NOT_TOUCH_RULES.md`.

## Goal

Audit the installed KiCad app read-only so agents know what the current user's local KiCad provides.

Run live discovery first:

- `python health_check.py --no-write`
- `python 03_TOOLS/scripts/kicad_discovery/find_kicad.py`

Inspect only:

- the detected KiCad install root and its `bin`, `etc`, `lib`, and `share` subfolders when present
- common Windows KiCad 9/8/7 paths under `C:\Program Files\KiCad` only as fallback examples if discovery needs confirmation
- accessible user-global KiCad config paths, read-only

## Restrictions

- Do not modify `C:\Program Files\KiCad`.
- Do not modify `%APPDATA%\kicad`.
- Do not edit KiCad project files.
- Do not install tools.
- Do not assume `C:\Users\LJ` or any other maintainer-machine path.

## Expected Work

- Inventory executables, `kicad-cli`, stock symbols, stock footprints, 3D models, templates, demos, scripts/plugins, and library tables.
- Run only safe version checks such as `kicad-cli version`.
- Record exact paths and counts.
- Generate reports under `02_HISTORY` or `05_OUTPUTS`.

## Output

Create or update appropriate audit docs. End with a history/session log and a clear statement of what was read, what was not modified, and what future agents should use.

## Universal Safety Requirements

- If the task changes from read-only audit to any edit, stop and require active project confirmation, backup, rollback plan, verification plan, and history log.
- Produce an audit or verification report with commands run and limitations.
- Do not fabricate datasheet claims, KiCad path behavior, environment assumptions, or library contents.
- Do not select or approve a footprint unless the exact part package and manufacturer drawing have been verified.
- Label every generated manufacturing-style output `NOT_FINAL`; this audit prompt should not create fabrication outputs.
