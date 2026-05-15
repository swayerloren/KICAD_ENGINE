# Claude Prompt: Plan Schematic

You are Claude working from VS Code in:

your local `KICAD_ENGINE` repo root

## Read First

Read these files before planning schematic work:

1. `AGENTS.md`
2. `00_CODEX_START/START_HERE.md`
3. `00_CODEX_START/CURRENT_PROJECT.md`
4. `00_CODEX_START/PROJECT_INDEX.md`
5. `00_CODEX_START/KICAD_AGENT_OPERATING_MANUAL.md`
6. `00_CODEX_START/KICAD_SAFE_AUTOMATION_RULES.md`
7. `08_COMPONENT_DATABASE/00_INDEX/AI_USAGE_RULES.md`
8. `.prompts/shared/SAFETY_GATES.md`
9. `.prompts/shared/HUMAN_DRAFTING_MODE.md`
10. `.prompts/shared/KICAD_VERIFICATION_STANDARD.md`
11. `.prompts/shared/COMPONENT_RESEARCH_STANDARD.md`

## Goal

Create a schematic plan that can be reviewed before any KiCad source file edits are made.

## Universal Requirements

- Do not modify schematic, PCB, project, symbol, or footprint files during planning.
- Require active project confirmation, backup, target file list, rollback plan, and verification plan before future edits.
- Record planning decisions or open questions in `02_HISTORY/`; durable approved decisions belong in `01_MEMORY/`.
- Define the verification reports that will be required after implementation.
- Do not fabricate component specs, datasheet claims, pinouts, power limits, or package data.
- Do not select footprints as final without exact package drawing verification.
- Label any future fabrication-style output `NOT_FINAL` until the full verification gate passes.

## Planning Checklist

1. Identify functional blocks.
2. Enter `HUMAN_DRAFTING_MODE` before planning labels:
   - ask whether symbols should be rotated, flipped, or repositioned first
   - ask whether each local net can be drawn with a clean short wire first
   - use labels only after the local layout is sensible
3. List candidate parts and their verification status.
4. List required datasheets, reference designs, and app notes.
5. Define power rails, interfaces, connectors, protection, debug, boot, and
   programming paths with human-readable signal flow.
6. Plan MCU support circuits so EN, RESET, BOOT0/strap pins, local LEDs, and
   decoupling are physically wired when close to the MCU or module pins.
7. Choose connector orientation from clean signal flow before label use,
   especially for USB and connector-protection blocks.
8. Plan any emphasized power, ground, or common-return rails so they can later
   be proven as real wires on the intended nets.
9. Plan reset/boot and other local control topology so no label shortcut can
   hide unsafe switch behavior.
10. Identify risk areas: connectors, polarity, RF, USB, CAN, automotive, power
   thermals, footprint ambiguity, local label abuse, and detached text
   ownership.
11. Define ERC, DRC, BOM, datasheet, footprint, visual, and human-drafting
   checks required after edits.
12. Plan the future report content so it explicitly records symbols
    rotated/flipped/repositioned, labels replaced with wires, labels kept and
    why, graphic-line versus electrical-wire verification, reset/boot topology
    sanity result, and ERC/text/unresolved-reference results.

## Output

Provide a schematic implementation plan with:

- Block diagram in text form.
- Candidate component table.
- Datasheet and source requirements.
- KiCad symbols and footprints as candidates only.
- Risks and human-review points.
- Expected label exceptions, local wires, symbol reorientation decisions,
  emphasized-rail verification expectations, and reset/boot topology sanity
  proof expectations.
- Required backup and verification gates before edits.
