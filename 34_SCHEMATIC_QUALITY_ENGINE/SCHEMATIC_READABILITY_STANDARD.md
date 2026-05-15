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
3. Before using a local label, decide whether rotating, flipping, mirroring, or
   repositioning symbols would allow cleaner physical wiring.
4. Use short local wires for local connections inside a block when the wire can
   stay short, orthogonal, and readable.
5. Use net labels only when wires would make the drawing less readable.
6. MCU local support circuits should usually be physically wired when they are
   close to the MCU or module pins:
   - `EN`, `RESET`, `ESP_EN`
   - `BOOT0`, `IO0`, and strap pins
   - local reset/boot switches
   - pullups/pulldowns
   - local LEDs
   - local decoupling
7. Ground and power rails must read like intentional rails or local return
   paths. Any emphasized common return must be a real wire on the intended net,
   not a graphic line.
8. Reset/boot and other local control topology must remain visually obvious.
   Labels, wires, or notes must not hide switch behavior or capacitor return
   intent.
9. References, values, notes, and labels must not overlap wires, pins, symbol
   bodies, or other text, and every visible reference/value must clearly belong
   to its own symbol.
10. Visible schematic notes must support readability instead of crowding active
    circuitry.
11. ERC pass is required but is not enough by itself. The sheet must also pass
    human presentation review.

## Recommended Automated Evidence

- Run `03_TOOLS/scripts/schematic_quality/check_schematic_human_drafting_quality.py`
  before closing schematic create, repair, or readability-cleanup work.
- Treat its output as an early warning layer for:
  - graphic-line versus electrical-wire mistakes
  - local label shortcuts in MCU support circuits
  - reset/boot topology risks
  - local return clusters that are not actually on `GND`
  - text-ownership drift
  - suspicious local loopback wire paths
- Do not treat the checker as a visual-pass replacement. Human rendered-page
  review remains mandatory.

## Fail Conditions

- random symbol scatter
- dense unlabeled wire tangles
- label-heavy local blocks with little actual wiring
- labels used as a shortcut for avoidable bad symbol orientation
- local MCU support circuits reduced to label shortcuts or detached parts
- graphic lines or unverified visual rails used as electrical proof
- reset/boot topology that is ambiguous, misleading, or visually obscured
- detached values in blank space or values closer to the wrong symbol
- confusing power, ground, or return presentation
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
- `09_ACCURACY_ENGINE/schematic_rules/REFERENCE_VALUE_TEXT_PLACEMENT_RULES.md`
- `09_ACCURACY_ENGINE/schematic_rules/ESP32_BOOT_RESET_RULES.md`
- `09_ACCURACY_ENGINE/schematic_rules/FUNCTIONAL_BLOCK_SPACING_RULES.md`
- `09_ACCURACY_ENGINE/checklists/SCHEMATIC_HUMAN_READABILITY_CHECKLIST.md`
