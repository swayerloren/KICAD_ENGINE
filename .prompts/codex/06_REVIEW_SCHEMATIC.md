# Codex Prompt: Review Schematic

You are working in your local `KICAD_ENGINE` repo root from VS Code.

## Read First

Read `AGENTS.md`, `.prompts/shared/SAFETY_GATES.md`, `.prompts/shared/HUMAN_DRAFTING_MODE.md`, `.prompts/shared/KICAD_VERIFICATION_STANDARD.md`, `00_CODEX_START/CURRENT_PROJECT.md`, `00_CODEX_START/KICAD_SAFE_AUTOMATION_RULES.md`, and relevant project memory/history.

## Goal

Review schematic for:

- Project path: `[PROJECT_PATH]`
- Review focus: `[POWER/MCU/USB/CAN/CONNECTORS/ALL]`

## Restrictions

- Read-only review unless user separately approves fixes.
- Do not edit schematic, project, libraries, or PCB.
- Do not assert datasheet compliance without source evidence.
- Do not assert footprints are correct from schematic fields alone.

## Required Workflow

1. Confirm active project and project path.
2. Parse schematic and library references read-only.
3. Review the sheet in `HUMAN_DRAFTING_MODE`:
   - can local nets be physically wired more clearly
   - should any symbol be rotated, flipped, or repositioned
   - are any net labels compensating for bad layout
   - are any emphasized rails being over-read as electrical proof without
     object/net verification
   - is reset/boot or local control topology still obvious and sane
   - would a human engineer understand the circuit immediately
   - does every visible reference and value clearly belong to its own part
4. Run project validation and ERC availability checks where safe.
5. Check power, connectors, polarity, datasheet coverage, symbol candidates,
   MCU support circuits, USB path readability, local wire-vs-label balance,
   ground/power rail presentation, and reset/boot topology sanity.
6. Run or review `03_TOOLS/scripts/schematic_quality/check_schematic_human_drafting_quality.py` when the review includes readability, local wiring, or control-cluster quality.
7. Run ERC if the project gate allows read-only verification.
8. If screenshot, rendered-page, or crop evidence shows bad orientation,
   awkward local wiring, label spray, detached text, or ambiguous rail/topology
   presentation, do not soften that finding just because ERC passes.
9. Write a review report and history log.

## Output

Provide findings ordered by severity with file references, ERC/report paths if
run, unresolved risks, recommended next steps, net labels that should be kept,
local labels that should become wires, and any required symbol
rotation/flip/reposition work. Also report graphic-line versus electrical-wire
verification, reset/boot topology sanity result, and ERC/text/unresolved
results when available.

## Universal Safety Requirements

- Do not modify schematic, PCB, symbol, footprint, project, or fabrication-output files during review unless explicitly requested and backup gates pass.
- Require backup, rollback plan, verification plan, and history log before any future KiCad source edit.
- Produce a verification report or explain why ERC/checks could not run.
- Do not fabricate datasheet claims, pinouts, electrical limits, package data, or verification status.
- Do not approve a footprint unless the exact part package and manufacturer drawing have been verified.
- Label every generated manufacturing-style output `NOT_FINAL` until ERC, DRC, BOM, footprint, datasheet, and visual review gates pass.
