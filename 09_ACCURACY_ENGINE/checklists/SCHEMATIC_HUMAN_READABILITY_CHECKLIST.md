# Schematic Human Readability Checklist

Status: `MANDATORY`

Use this checklist before marking a schematic `READY_FOR_LJ_VISUAL_REVIEW`, `SCHEMATIC_READY_FOR_PCB_UPDATE`, or `VISUAL_PASS`.

## Required Evidence

- [ ] Full-page rendered PNG or screenshot exists.
- [ ] Full-page PDF/SVG exists.
- [ ] Close-up crops exist for every required block.
- [ ] The agent visually inspected the rendered full-page image.
- [ ] The agent visually inspected every required crop.
- [ ] Automated crop report is cited separately from human-readable review.

## Global Readability Checks

- [ ] No text overlaps other text.
- [ ] No reference overlaps a value.
- [ ] No reference or value touches a symbol body.
- [ ] No net label crosses a wire other than the intended attachment point.
- [ ] No net label sits on a pin.
- [ ] No power symbol touches or overlaps a label, value, reference, or another power symbol.
- [ ] No note is inside active circuitry.
- [ ] Notes do not obscure wires, pins, labels, or symbols.
- [ ] Values are short enough to read in the schematic block.
- [ ] Long review details are moved to a report, hidden fields, or a separate review table.
- [ ] Review markers do not make component values unreadable.
- [ ] Every crop includes enough context to understand the block.

## Required Block Checks

### Input Power

- [ ] Input connector reference/value readable.
- [ ] Fuse reference/value readable.
- [ ] PMOS reference/value readable.
- [ ] TVS and input capacitor reference/value readable.
- [ ] Power rail labels do not collide.
- [ ] `PWR_FLAG` labels do not obscure wires or symbols.

### Buck Regulator

- [ ] Regulator pin names and pin numbers are readable.
- [ ] Inductor, bootstrap capacitor, input capacitor, and output capacitors are readable.
- [ ] Switching-node and feedback labels do not overlap symbol pins.
- [ ] Power and ground labels are visually distinct.

### MCU Or Module

- [ ] Module reference/value readable.
- [ ] Pin labels and pin numbers readable.
- [ ] No-connect markers do not cover pin names.
- [ ] Decoupling capacitors are readable and not jammed into the module symbol.
- [ ] Boot/reset/programming labels are readable.

### USB-C And USB ESD

- [ ] Connector pin labels readable.
- [ ] D+/D- labels readable and visually traceable.
- [ ] CC resistor labels readable.
- [ ] ESD diode pin labels readable.
- [ ] Shield/VBUS policy notes are outside active circuitry.

### LEDs, Switches, Test Pads, Mounting Holes

- [ ] LED references, resistor references, and values are readable.
- [ ] Switch references, values, and net labels are readable.
- [ ] Test pad labels are not crowded.
- [ ] Mounting hole labels are readable and clearly mechanical.

## Classification

- `VISUAL_PASS`: all required boxes are checked.
- `VISUAL_FAIL`: any required box fails.
- `VISUAL_NOT_VERIFIED`: rendered images/crops were not inspected.
- `AUTOMATED_CROP_PASS_ONLY`: crop/report generation passed but checklist is not complete.

Do not mark a schematic `READY_FOR_LJ_VISUAL_REVIEW` unless this checklist is complete with `VISUAL_PASS`.
