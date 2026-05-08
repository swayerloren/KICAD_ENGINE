# Claude Prompt: Review Schematic

You are Claude working from VS Code in:

your local `KICAD_ENGINE` repo root

## Read First

Read these files before reviewing:

1. `AGENTS.md`
2. `00_CODEX_START/START_HERE.md`
3. `00_CODEX_START/CURRENT_PROJECT.md`
4. `00_CODEX_START/KICAD_AGENT_OPERATING_MANUAL.md`
5. `00_CODEX_START/KICAD_SAFE_AUTOMATION_RULES.md`
6. `03_TOOLS/kicad_app_intelligence/KICAD_AGENT_TASK_MAP.md`
7. `.prompts/shared/SAFETY_GATES.md`
8. `.prompts/shared/KICAD_VERIFICATION_STANDARD.md`
9. `.prompts/shared/COMPONENT_RESEARCH_STANDARD.md`

## Goal

Review a KiCad schematic for correctness, missing context, and verification gaps without making automatic design edits.

## Universal Requirements

- Do not modify schematic, PCB, project, symbol, footprint, or manufacturing-output files unless explicitly requested and backup gates pass.
- Require backup before any future edits.
- Record review findings and commands in `02_HISTORY/`.
- Produce a verification report with pass/warn/fail status.
- Do not fabricate datasheet claims, pinouts, electrical limits, or component recommendations.
- Do not approve footprints without exact package and footprint verification.
- Label any generated output `NOT_FINAL` if it resembles a manufacturing deliverable.

## Review Workflow

1. Confirm the active project and schematic path.
2. Parse schematic files read-only where possible.
3. Use `kicad-cli` ERC if available and appropriate.
4. Cross-check symbols, values, references, power pins, unconnected pins, interfaces, connectors, programming/debug, reset, clocking, and protection.
5. Compare parts against `08_COMPONENT_DATABASE/` and datasheet records.
6. Mark findings by severity and confidence.

## Output

Create or report:

- ERC result or reason ERC could not run.
- Schematic review findings.
- Datasheet and component database gaps.
- Footprint verification gaps.
- Required human-review points.
- Recommended next steps.
- History log path.
