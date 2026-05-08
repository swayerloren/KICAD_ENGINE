# Human Readable Schematic Rules

Status: `MANDATORY`

## Purpose

These rules prevent an agent from marking a schematic visually ready when the rendered schematic is not actually readable by a human reviewer.

This file exists because automated checks can pass while the KiCad schematic still has overlapping text, crowded values, labels crossing wires, notes inside circuitry, or component references that are hard to inspect.

## Core Rule

A schematic is not visually ready until the rendered full-page image and required close-up crops are human-readable.

The following statuses do not prove human readability:

- `ERC_PASS`
- annotation checker `PASS`
- all footprints populated
- automated crop generation `PASS`
- no visible footprint/library/path field strings
- no `?` reference tokens found by file parsing

## Visual Fail Conditions

Mark visual status `VISUAL_FAIL` when any rendered full-page image or close-up crop shows:

- text, values, references, or net labels overlapping each other
- text, values, references, or net labels touching or crossing wires
- text, values, references, or net labels touching symbol bodies
- text, values, references, or net labels touching power symbols
- net labels stacked on top of pins, wires, or other labels
- power symbols visually stacked or touching unrelated labels
- component values too long to read clearly in their block
- review notes placed inside active circuitry
- review notes, block notes, or design comments hiding circuit content
- pin names, pin numbers, or no-connect markers crowding each other so the symbol cannot be reviewed
- labels clipped by crop boundaries
- a crop that does not include enough surrounding context to review the block

Any one of these conditions blocks `READY_FOR_LJ_VISUAL_REVIEW`, `SCHEMATIC_READY_FOR_PCB_UPDATE`, and PCB update.

## Notes And Review Markers

Review markers such as `NEEDS_REVIEW`, `BLOCKED`, `HUMAN_REVIEW_REQUIRED`, or long package notes should not clutter component values when they make the schematic unreadable.

Preferred handling:

1. Keep visible component values short.
2. Store detailed review status in hidden schematic fields when appropriate.
3. Record detailed open issues in a review table or report.
4. Put block notes in a separate notes zone outside active circuitry.
5. Keep short visible markers only where the reviewer must see them directly.

## Required Human-Readable Layout Standards

Every schematic block must satisfy these standards before visual signoff:

- Symbols have enough whitespace around references, values, and pin labels.
- Net labels attach clearly to intended wires and do not cover pins.
- Power symbols are separated from references, values, net labels, and each other.
- Text reads left-to-right or in the intentional KiCad symbol orientation without crowding.
- Notes are outside active circuitry and do not overlap wires, symbols, labels, or component fields.
- Long decisions are moved to review reports rather than forced into visible values.
- Dense connector, module, regulator, and MCU blocks are split or spaced until pin labels are readable.

## Required Evidence

To claim `VISUAL_PASS`, the agent must cite:

- full-page rendered PNG or screenshot path
- close-up crop folder path
- close-up review report path
- explicit statement that the rendered full-page image and each relevant crop were visually inspected
- result table for each required block
- any remaining human review items

If the agent cannot visually inspect the rendered PNG/crops, visual status must be `NOT_VERIFIED`, not `PASS`.

## File-Level Annotation Is Not Enough

File parsing can miss what KiCad displays. If the KiCad GUI or rendered schematic still visibly shows `?` references, placeholder references, or question-mark reference artifacts, visual status is `VISUAL_FAIL` even when a parser reports annotation pass.

## Native KiCad Annotation Requirement

For annotation tasks, raw `.kicad_sch` text edits are not sufficient evidence. If LJ reports GUI-visible question-mark references, agents must use verified KiCad-native annotation through the GUI automation gate or stop and provide manual KiCad instructions.

Required manual fallback:

`Tools -> Annotate Schematic -> Re-annotate all symbols -> Save -> Run ERC`

If Eeschema has an unsaved `*` title, saved-file parsing and CLI ERC may not describe the GUI state LJ is seeing. Treat GUI annotation as `NOT_VERIFIED` until the GUI itself has been annotated, saved, and checked.

## Output Statuses

Use these statuses:

- `VISUAL_PASS`: rendered full-page image and required crops are human-readable and no visual fail conditions remain.
- `VISUAL_FAIL`: visible overlap/crowding/notes-in-circuitry/crop problems remain.
- `VISUAL_NOT_VERIFIED`: rendered image or crops were not inspected.
- `AUTOMATED_CROP_PASS_ONLY`: crop generation and basic automated screening passed, but human-readable layout was not verified.
- `READY_FOR_LJ_VISUAL_REVIEW`: allowed only when visual status is `VISUAL_PASS` and unresolved high-risk items are clearly listed for LJ.

## ESP32_CSI_WIFI_NODE Precedent

The ESP32_CSI_WIFI_NODE schematic had ERC, annotation, footprint-population, and automated crop checks pass while the rendered schematic remained unreadable. Future agents must treat that as a known failure mode and must not repeat it.
