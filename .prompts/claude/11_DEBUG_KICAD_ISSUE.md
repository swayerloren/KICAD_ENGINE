# Claude Prompt: Debug KiCad Issue

You are Claude working from VS Code in:

`C:\Users\LJ\GitHub\KICAD_ENGINE`

## Read First

Read these files before debugging:

1. `AGENTS.md`
2. `00_CODEX_START/START_HERE.md`
3. `00_CODEX_START/SAFETY_RULES.md`
4. `00_CODEX_START/CONTROL_PLANES.md`
5. `00_CODEX_START/KICAD_AGENT_OPERATING_MANUAL.md`
6. `03_TOOLS/kicad_app_intelligence/KICAD_CLI_COMMANDS_REFERENCE.md`
7. `03_TOOLS/kicad_app_intelligence/KICAD_DO_NOT_TOUCH_RULES.md`
8. `.prompts/shared/SAFETY_GATES.md`
9. `.prompts/shared/KICAD_VERIFICATION_STANDARD.md`

## Goal

Diagnose KiCad CLI, library, project, export, ERC, DRC, or GUI issues without unsafe changes.

## Universal Requirements

- Start with read-only inspection.
- Do not modify KiCad project files, user global library tables, or KiCad install folders unless the user explicitly approves a safe edit path.
- Require backup before any source or config edit.
- Record commands, errors, and findings in `02_HISTORY/`.
- Produce a diagnosis report and verification status.
- Do not fabricate tool behavior, datasheet claims, or footprint verification.
- Do not label generated manufacturing outputs as final; use `NOT_FINAL`.

## Debug Workflow

1. Reproduce the issue with the smallest safe command or file inspection.
2. Capture exact command, working directory, environment assumptions, and error output.
3. Check KiCad version and relevant paths.
4. Inspect project-local library tables before user-global settings.
5. Prefer CLI/API/file inspection over GUI automation.
6. Use GUI screenshots for discovery only when CLI and file inspection are insufficient.
7. Propose fixes separately from diagnosis; do not apply risky fixes without explicit approval and backup.

## Output

Report:

- Issue summary.
- Reproduction steps.
- Evidence and logs.
- Likely cause.
- Safe fix options.
- Required backup and verification plan before edits.
- History log path.
