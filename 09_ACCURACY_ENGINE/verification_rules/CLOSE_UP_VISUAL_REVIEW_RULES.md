# Close-Up Visual Review Rules

## Purpose

These rules define the close-up visual evidence required before a schematic can move toward PCB update or layout.

## Required Evidence

The active project must have:

- Full-page schematic SVG export.
- Full-page schematic PDF export.
- Full-page PNG export when a renderer is available.
- Close-up crop folder.
- `CLOSE_UP_REVIEW.md`.
- Visual block config at `_verification/schematic_visual/visual_blocks.json`.

## Required Tooling

Preferred command:

```powershell
.\03_TOOLS\kicad\run_schematic_visual_check.ps1 -ProjectRoot "<active-project-root>" -CreateDefaultConfig
```

The wrapper must not edit KiCad project files. It may write only generated verification outputs and reports.

## Required Review Blocks

- `input_power`
- `reverse_polarity`
- `tvs_input_cap`
- `buck_regulator`
- `esp32_module`
- `usb_c_connector`
- `usb_esd`
- `cc_resistors`
- `reset_boot`
- `leds`
- `test_pads`
- `mounting_holes`
- `mechanical_notes`

## Blocking Conditions

Mark the schematic-to-PCB gate blocked with `VISUAL_REVIEW_INCOMPLETE` when:

- full-page export is missing
- crop folder is missing
- no crops were generated
- `CLOSE_UP_REVIEW.md` is missing
- a required block crop is missing
- a crop misses the intended circuit block
- visible unannotated references remain
- visible footprint, library, or path fields are present in normal schematic view
- the review has not been checked by a human or explicitly logged visual reviewer
- the rendered full-page image or any required crop has overlapping text, values, references, net labels, wires, pins, symbol bodies, or power symbols
- notes are placed inside active circuitry or obscure circuit elements
- long review notes or component values make the block unreadable
- net labels, power symbols, references, or values are stacked or visually touching
- rendered PNG/crops cannot be inspected by the agent
- KiCad GUI or rendered output visibly shows question-mark references, even if file parsing reports annotation pass

## Automated Pass Is Not Visual Pass

The close-up generator may report `PASS` when crops are created and limited text screening succeeds. That status must be treated as `AUTOMATED_CROP_PASS_ONLY` unless the rendered full-page image and every relevant crop were visually inspected for human readability.

Do not use automated crop `PASS`, ERC pass, annotation pass, populated footprint fields, hidden footprint fields, or no `?` token detection as a substitute for human-readable layout review.

To claim `VISUAL_PASS`, the report must cite the rendered image paths and state that:

- no text overlaps another text item
- no value/reference/net label touches wires, pins, power symbols, or symbol bodies
- notes are outside active circuitry
- values are short and readable
- each required crop contains the intended block and enough context
- any review markers are visible only where useful and are otherwise moved to hidden fields or review tables

## Detection Rules

The visual crop generator must attempt to detect:

- visible unannotated references such as `R?`, `C?`, `U?`, `J?`, `D?`, `Q?`, `F?`, `TP?`, or `MH?`
- visible fields that indicate hidden metadata may be showing, such as footprint names, library names, datasheet fields, or file paths

Detection based on SVG text is a screening aid. If text extraction is incomplete, the review remains human-review required.

Rendered PNG/crop evidence overrides SVG text extraction. If a rendered image visibly fails but SVG text extraction reports no issue, classify the visual result as `VISUAL_FAIL`.

## Limits

Close-up visual review does not prove:

- ERC pass
- DRC pass
- footprint correctness
- connector orientation
- MOSFET pin mapping
- datasheet accuracy
- BOM lock accuracy
- fabrication readiness
