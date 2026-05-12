# Schematic Readability Standard

## Standard

KiCad schematics must read like intentional engineering drawings, not raw data
containers.

## Mandatory Requirements

1. Functional blocks must be grouped:
   - input power/protection
   - buck regulator
   - ESP32 module
   - USB-C/ESD/CC/data resistors
   - reset/boot
   - LEDs
   - test pads/debug
   - mounting/mechanical notes
2. Blocks must show readable left-to-right or top-to-bottom power and signal
   flow.
3. Use short local wires for local connections inside a block.
4. Use net labels only when wires would make the drawing less readable.
5. References, values, notes, and labels must not overlap wires, pins, symbol
   bodies, or other text.
6. Visible schematic notes must support readability instead of crowding active
   circuitry.
7. ERC pass is required but is not enough by itself.

## Fail Conditions

- random symbol scatter
- dense unlabeled wire tangles
- label-heavy local blocks with little actual wiring
- visible overlaps
- unreadable long values
- unresolved placeholder references
- unresolved high-risk review markers on visible symbol values

## Reference Sample Comparison

Reviewed open-source sample metrics may be used as supporting comparison
evidence for readability, block grouping, and wire-vs-label balance.

They do not override the direct readability rules above. A schematic that
matches a sample but still violates overlap, annotation, or local-wiring rules
still fails.

## Canonical Rule Links

- `09_ACCURACY_ENGINE/schematic_rules/READABLE_SCHEMATIC_FLOW_RULES.md`
- `09_ACCURACY_ENGINE/schematic_rules/WIRE_VS_NET_LABEL_RULES.md`
- `09_ACCURACY_ENGINE/schematic_rules/FUNCTIONAL_BLOCK_SPACING_RULES.md`
- `09_ACCURACY_ENGINE/checklists/SCHEMATIC_VISUAL_READABILITY_CHECKLIST.md`
