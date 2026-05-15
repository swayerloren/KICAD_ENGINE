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
8. `.prompts/shared/HUMAN_DRAFTING_MODE.md`
9. `.prompts/shared/KICAD_VERIFICATION_STANDARD.md`
10. `.prompts/shared/COMPONENT_RESEARCH_STANDARD.md`

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
3. Review in `HUMAN_DRAFTING_MODE`:
   - can local nets be physically wired more clearly
   - should symbols be rotated, flipped, or repositioned
   - are any labels hiding bad local layout
   - are any emphasized rails being mistaken for electrical proof without
     object/net verification
   - is reset/boot or local control topology still obvious and sane
   - does every reference/value visibly belong to its part
   - would a human engineer understand the circuit immediately
4. Use `kicad-cli` ERC if available and appropriate.
5. Cross-check symbols, values, references, power pins, unconnected pins,
   interfaces, connectors, programming/debug, reset, clocking, protection, MCU
   local support wiring, connector signal flow, ground/power rail
   presentation, and reset/boot topology sanity.
6. Run or review `03_TOOLS/scripts/schematic_quality/check_schematic_human_drafting_quality.py` when the review includes readability, local wiring, or control-cluster quality.
7. Compare parts against `08_COMPONENT_DATABASE/` and datasheet records.
8. Mark findings by severity and confidence.
9. If rendered-page or crop evidence still shows poor drafting, keep the issue
   open even when ERC or overlap checks are clean.

## Output

Create or report:

- ERC result or reason ERC could not run.
- Schematic review findings.
- Datasheet and component database gaps.
- Footprint verification gaps.
- Required human-review points.
- Net labels that are justified, net labels that should become wires, and any
  required symbol rotations/flips/repositions.
- Graphic-line versus electrical-wire verification result, reset/boot topology
  sanity result, and ERC/text/unresolved results when available.
- Recommended next steps.
- History log path.
