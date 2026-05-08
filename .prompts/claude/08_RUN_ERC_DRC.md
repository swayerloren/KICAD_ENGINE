# Claude Prompt: Run ERC And DRC

You are Claude working from VS Code in:

your local `KICAD_ENGINE` repo root

## Read First

Read these files before running checks:

1. `AGENTS.md`
2. `00_CODEX_START/START_HERE.md`
3. `00_CODEX_START/CURRENT_PROJECT.md`
4. `00_CODEX_START/KICAD_AGENT_OPERATING_MANUAL.md`
5. `03_TOOLS/kicad_app_intelligence/KICAD_CLI_COMMANDS_REFERENCE.md`
6. `.prompts/shared/SAFETY_GATES.md`
7. `.prompts/shared/KICAD_VERIFICATION_STANDARD.md`

## Goal

Run KiCad ERC and DRC safely from VS Code using the installed KiCad CLI when available.

## Universal Requirements

- Do not modify schematic, PCB, project, symbol, footprint, or fabrication-output files.
- If a check command would write into a project folder, confirm output path and use a report/output folder.
- Require backup before any future project edits.
- Record commands and results in `02_HISTORY/`.
- Produce markdown and/or JSON verification reports when possible.
- Do not fabricate pass status, datasheet coverage, or component verification status; report tool errors and limitations honestly.
- Do not approve footprints without exact verification.
- Label manufacturing-style outputs `NOT_FINAL`; ERC/DRC reports are review artifacts, not fab approval.

## Workflow

1. Confirm active project path and target files.
2. Check `kicad-cli` availability and version.
3. Create a report folder under `02_HISTORY/` or `05_OUTPUTS/NOT_FINAL_*` as appropriate.
4. Run ERC and DRC read-only against the project.
5. Capture exit codes, stdout/stderr, and generated reports.
6. Summarize violations by severity and cite report paths.

## Output

Report:

- KiCad CLI version.
- ERC command, result, and report path.
- DRC command, result, and report path.
- Pass/warn/fail summary.
- Next verification steps.
- History log path.
