# Claude Prompt: Create New Project Workspace

You are Claude working from VS Code in:

your local `KICAD_ENGINE` repo root

## Read First

Read these files before creating anything:

1. `AGENTS.md`
2. `00_CODEX_START/START_HERE.md`
3. `00_CODEX_START/WORKFLOW_RULES.md`
4. `00_CODEX_START/SAFETY_RULES.md`
5. `00_CODEX_START/PROJECT_INDEX.md`
6. `00_CODEX_START/CURRENT_PROJECT.md`
7. `00_CODEX_START/KICAD_AGENT_OPERATING_MANUAL.md`
8. `.prompts/shared/SAFETY_GATES.md`
9. `.prompts/shared/KICAD_VERIFICATION_STANDARD.md`

## Goal

Create a safe project workspace for a new KiCad design without touching unrelated project files.

## Universal Requirements

- Do not modify existing KiCad project files unless the active project and target files are confirmed.
- Require a backup before editing any existing schematic, PCB, symbol, footprint, project, or fabrication-output file.
- Record workspace creation and decisions in `02_HISTORY/`; durable project decisions belong in `01_MEMORY/`.
- Produce a verification report or a clear list of checks that remain pending.
- Do not fabricate datasheet claims or component limits.
- Do not select footprints as final without exact package and drawing verification.
- Label future manufacturing-style outputs `NOT_FINAL` until all verification gates pass.

## Workflow

1. Confirm the requested project name and intended folder under `04_KICAD_PROJECTS/active/`.
2. Check whether a project with that name already exists.
3. If using a template, inspect the template read-only before copying.
4. Create a new workspace folder only after confirming it does not overwrite existing work.
5. Update project index or memory only if requested and appropriate.
6. Do not make schematic or PCB design changes unless the user explicitly asks and backup gates are satisfied.

## Output

Report:

- New project workspace path.
- Files created or copied.
- Template source if used.
- Backup status.
- Initial verification checklist.
- History log path.
