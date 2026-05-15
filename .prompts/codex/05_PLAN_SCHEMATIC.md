# Codex Prompt: Plan Schematic

You are working in your local `KICAD_ENGINE` repo root from VS Code.

## Read First

Read `AGENTS.md`, `.prompts/shared/SAFETY_GATES.md`, `.prompts/shared/HUMAN_DRAFTING_MODE.md`, `.prompts/shared/KICAD_VERIFICATION_STANDARD.md`, `00_CODEX_START/CURRENT_PROJECT.md`, `00_CODEX_START/KICAD_AGENT_OPERATING_MANUAL.md`, `03_TOOLS/kicad_app_intelligence/KICAD_AGENT_TASK_MAP.md`, and relevant `01_MEMORY`/`02_HISTORY`.

## Goal

Plan schematic for:

- Project ID: `[project-id]`
- Feature/block: `[SCHEMATIC_BLOCK]`

## Restrictions

- Planning only unless user explicitly approves source edits.
- Do not edit `.kicad_sch`, `.kicad_pro`, libraries, or PCB files.
- Do not choose final footprints without package drawing verification.
- Do not invent datasheet facts.

## Required Workflow

1. Confirm active project and requirements.
2. Enter `HUMAN_DRAFTING_MODE` before proposing any labels:
   - ask whether symbols should be rotated, flipped, or repositioned first
   - ask whether a clean short local wire is possible first
   - use labels only after the block flow and local geometry are sensible
3. Identify parts, datasheets, power rails, connectors, interfaces,
   protection, and programming/debug needs.
4. Plan MCU support blocks so EN, RESET, BOOT0/strap pins, local LEDs, local
   pullups/pulldowns, and decoupling will be physically wired when close to the
   MCU or module pins.
5. Plan connector orientation from signal flow first, especially for USB,
   connector-protection, ESD, and series-resistor chains.
6. Plan any emphasized power, ground, or common-return rails so they can later
   be proven as real wires on the intended nets, not just pretty graphics.
7. Plan reset/boot and other local control topology so switch behavior remains
   obvious and no label shortcut can hide an unsafe short path.
8. Define text ownership expectations so references and values visibly belong
   to the correct parts and no wire path is allowed to cross text.
9. List ERC/DRC/BOM checks needed after future edits, plus the human-drafting
   checks that must pass before the schematic is called readable or gate-ready.
10. Plan the future report content so it will explicitly list symbols
    rotated/flipped/repositioned, labels replaced with wires, labels kept and
    why, graphic-line versus electrical-wire verification, reset/boot topology
    sanity result, and ERC/text/unresolved-reference results.
11. Identify backup requirements before any future schematic edit.
12. Identify symbol and footprint candidates as candidates only.

## Output

Create a schematic plan/review note in `02_HISTORY/design_reviews` or project
history. Include risks, unknowns, verification plan, next steps, expected label
exceptions, expected local wires, any planned symbol rotations/flips or
repositions, planned graphic-line versus electrical-wire proof, planned
reset/boot topology proof, and planned ERC/text/unresolved checks.

## Universal Safety Requirements

- Do not modify schematic, PCB, symbol, footprint, project, or fabrication-output files during planning.
- Require active project confirmation, backup, rollback plan, verification plan, and history log before future KiCad source edits.
- Do not fabricate datasheet claims, part limits, pinouts, package data, or lifecycle status.
- Do not select or approve a footprint unless the exact part package and manufacturer drawing have been verified.
- Label every generated manufacturing-style output `NOT_FINAL` until ERC, DRC, BOM, footprint, datasheet, and visual review gates pass.
