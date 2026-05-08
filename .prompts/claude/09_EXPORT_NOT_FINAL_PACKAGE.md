# Claude Prompt: Export NOT_FINAL Package

You are Claude working from VS Code in:

your local `KICAD_ENGINE` repo root

## Read First

Read these files before exporting:

1. `AGENTS.md`
2. `00_CODEX_START/START_HERE.md`
3. `00_CODEX_START/CURRENT_PROJECT.md`
4. `00_CODEX_START/KICAD_AGENT_OPERATING_MANUAL.md`
5. `00_CODEX_START/KICAD_SAFE_AUTOMATION_RULES.md`
6. `03_TOOLS/kicad_app_intelligence/KICAD_CLI_COMMANDS_REFERENCE.md`
7. `.prompts/shared/SAFETY_GATES.md`
8. `.prompts/shared/KICAD_VERIFICATION_STANDARD.md`

## Goal

Export review-only manufacturing-style files that are clearly labeled `NOT_FINAL`.

## Universal Requirements

- Do not modify source KiCad project files.
- Confirm active project, output folder, and exact export commands before generating outputs.
- Require backup before project edits; export commands should not edit source files.
- Record commands and results in `02_HISTORY/`.
- Produce a verification report and list unverified gates.
- Do not fabricate ERC, DRC, BOM, footprint, datasheet, or visual-review status.
- Do not approve footprints without exact package drawing verification.
- Every generated fab-style output folder and archive must include `NOT_FINAL` in its name.

## Export Rules

1. Run or locate current ERC, DRC, BOM, footprint, datasheet, and visual-review status first.
2. Export only to `05_OUTPUTS/NOT_FINAL_*` or another clearly labeled review folder.
3. Include a `NOT_FINAL_README.md` describing missing gates.
4. Do not claim the package is manufacturing-ready unless all verification gates passed and the user explicitly approved finalization.

## Output

Report:

- Output folder path.
- Exported file list.
- Commands run.
- Verification gates passed and not passed.
- Warnings and human-review requirements.
- History log path.
