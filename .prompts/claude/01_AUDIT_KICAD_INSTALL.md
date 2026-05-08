# Claude Prompt: Audit KiCad Install

You are Claude working from VS Code in:

`C:\Users\LJ\GitHub\KICAD_ENGINE`

## Read First

Read these files before auditing:

1. `AGENTS.md`
2. `00_CODEX_START/START_HERE.md`
3. `00_CODEX_START/SAFETY_RULES.md`
4. `00_CODEX_START/CONTROL_PLANES.md`
5. `00_CODEX_START/KICAD_AGENT_OPERATING_MANUAL.md`
6. `03_TOOLS/kicad_app_intelligence/KICAD_9_WINDOWS_PATH_MAP.md`
7. `03_TOOLS/kicad_app_intelligence/KICAD_DO_NOT_TOUCH_RULES.md`
8. `.prompts/shared/SAFETY_GATES.md`
9. `.prompts/shared/KICAD_VERIFICATION_STANDARD.md`

## Goal

Audit the user's installed KiCad app with read-only inspection so agents can understand what KiCad provides from VS Code.

## Universal Requirements

- Do not modify KiCad project files or KiCad install files.
- If the task changes from read-only inspection to edits, stop and require active project confirmation, backup, verification plan, rollback plan, and history log.
- Record findings and command outputs in `02_HISTORY/`.
- Produce a verification or audit report.
- Do not fabricate datasheet, symbol, footprint, command, or environment-variable claims.
- Do not approve footprints without exact source verification.
- Label any manufacturing-style output `NOT_FINAL`; this prompt should not generate fab outputs.

## Audit Targets

Inspect likely KiCad install paths read-only:

- `C:\Program Files\KiCad\9.0\bin`
- `C:\Program Files\KiCad\9.0\etc`
- `C:\Program Files\KiCad\9.0\lib`
- `C:\Program Files\KiCad\9.0\share`

Also inspect known user/global KiCad config paths read-only if accessible.

## Required Checks

1. Confirm KiCad install paths exist.
2. Inventory executables in `bin`.
3. Run only safe version checks such as `kicad-cli version`.
4. Inventory default symbol libraries.
5. Inventory default footprint libraries.
6. Inventory 3D model folders.
7. Identify templates, demos, examples, plugins, scripts, and environment path assumptions.
8. Identify user global library table locations on Windows.
9. Document what agents may read and must never modify.

## Output

Create or update audit notes under `02_HISTORY/` and/or `03_TOOLS/kicad_app_intelligence/` with:

- Install path summary.
- CLI availability summary.
- Library and model inventory.
- Environment/path assumptions.
- Read-only and do-not-touch guidance.
- Commands run and results.
