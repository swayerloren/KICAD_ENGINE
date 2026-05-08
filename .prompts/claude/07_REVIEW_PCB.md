# Claude Prompt: Review PCB

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

Review a KiCad PCB layout for manufacturability, electrical risks, footprint risks, and missing verification.

## Universal Requirements

- Do not modify PCB, schematic, project, footprint, symbol, or manufacturing-output files unless explicitly requested and backup gates pass.
- Require backup before any future edits.
- Record review findings and commands in `02_HISTORY/`.
- Produce a verification report with pass/warn/fail status.
- Do not fabricate datasheet, package, or layout-rule claims.
- Do not approve footprints without exact part-number drawing verification.
- Label any generated manufacturing-style outputs `NOT_FINAL`.

## Review Workflow

1. Confirm active project and PCB path.
2. Parse `.kicad_pcb` read-only where possible.
3. Run DRC with `kicad-cli` if available and appropriate.
4. Check board outline, design rules, stackup assumptions, footprints, 3D models, connectors, polarity, RF, USB, CAN, power routing, thermal issues, mounting holes, clearances, and silkscreen.
5. Cross-check footprint names against component records and known high-risk categories.
6. Use GUI screenshots only for visual discovery when CLI/file inspection is insufficient.

## Output

Create or report:

- DRC result or reason DRC could not run.
- PCB review findings by severity.
- Footprint and mechanical-risk list.
- Datasheet/layout verification gaps.
- Required human-review points.
- Recommended next steps.
- History log path.
