# Claude Prompt: Review Fab Package

You are Claude working from VS Code in:

your local `KICAD_ENGINE` repo root

## Read First

Read these files before reviewing a fabrication package:

1. `AGENTS.md`
2. `00_CODEX_START/START_HERE.md`
3. `00_CODEX_START/CURRENT_PROJECT.md`
4. `00_CODEX_START/KICAD_AGENT_OPERATING_MANUAL.md`
5. `00_CODEX_START/KICAD_SAFE_AUTOMATION_RULES.md`
6. `.prompts/shared/SAFETY_GATES.md`
7. `.prompts/shared/KICAD_VERIFICATION_STANDARD.md`
8. `.prompts/shared/GITHUB_RELEASE_STANDARD.md`

## Goal

Review generated Gerber, drill, BOM, position, drawing, and archive outputs before manufacturing submission.

## Universal Requirements

- Do not modify KiCad source files or generated fab files unless explicitly requested and backup/working-copy gates pass.
- Require backup before any source edits.
- Record review findings and commands in `02_HISTORY/`.
- Produce a verification report with pass/warn/fail status.
- Do not fabricate ERC, DRC, BOM, datasheet, footprint, visual, or manufacturer-rule pass status.
- Do not approve footprints without exact source verification.
- Treat packages as `NOT_FINAL` unless the full verification gate is complete and the user explicitly authorizes final labeling.

## Review Workflow

1. Identify the package path and source project.
2. Confirm whether the package is labeled `NOT_FINAL`.
3. Inspect Gerber/drill layer presence and naming.
4. Check BOM, position files, board outline, drill files, solder mask/paste layers, and fabrication notes.
5. Compare outputs to current source project timestamps where possible.
6. Verify there are current ERC/DRC reports and human visual-review notes.
7. Flag missing manufacturer-specific requirements for JLCPCB, PCBWay, or other fabs.

## Output

Report:

- Package path.
- File inventory.
- Missing or suspicious outputs.
- Verification gates passed and missing.
- Manufacturer-specific warnings.
- Final/not-final status.
- History log path.
