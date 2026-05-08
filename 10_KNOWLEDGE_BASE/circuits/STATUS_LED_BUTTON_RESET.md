# Status LED, Button, And Reset Circuit

Status: `GENERAL_PATTERN_NOT_PART_SPECIFIC`

## Use Case

Use this pattern for bring-up and simple user interface functions: a status LED, optional user button, reset button, and test points for debug or production access. This file gives a review structure only; exact resistor values, pin defaults, debounce choices, and footprints require source/project verification.

## Required Evidence

| Item | Evidence Required |
| --- | --- |
| MCU GPIO | GPIO voltage/current limits and boot/reset side effects from MCU datasheet/reference manual. |
| LED | LED color, forward voltage/current target, package, polarity mark, and footprint status. |
| Current-limiting resistor | Target current calculation or project requirement; power rating if relevant. |
| Button | Exact tact switch or connector drawing showing pin shorting pairs and orientation. |
| Reset pin | MCU/module reset requirements, pull-up/down requirements, and external capacitor guidance if any. |
| Boot pins | Required default states and whether the button can disturb boot mode. |

## Typical Schematic Block

- Status LED with current-limiting resistor.
- User button with source-backed pull-up or pull-down strategy.
- Reset button connected only if supported by the target reset pin.
- Optional debounce only when the requirement calls for hardware debounce.
- Test points for reset, boot, UART, SWD/JTAG, ground, and power rails as needed.

## KiCad Review Points

- Symbol pin electrical type for LED, button, reset, and test points is reasonable.
- LED anode/cathode and footprint polarity are visually reviewed.
- Four-pin tact switch footprint orientation and shorted pin pairs are checked against the drawing.
- Boot/reset nets are clearly named and not hidden behind ambiguous GPIO labels.
- Test pads have safe footprints and accessible placement.

## PCB Review Points

- Place reset/programming controls where accessible after assembly.
- Keep boot/reset traces away from noisy switching nodes when practical.
- Label silkscreen clearly without putting text on pads.
- Check button height, actuator direction, enclosure access, and 3D/mechanical fit if relevant.

## Common Mistakes

- Missing LED resistor.
- Reversing LED footprint polarity.
- Assuming a four-pin tact switch has four independent pins.
- Pulling boot/reset pins to the wrong default state.
- Placing a reset button where it cannot be reached after enclosure assembly.

## Verification Gate

Result must be `NEEDS_HUMAN_REVIEW` until button footprint orientation, LED polarity, and boot/reset side effects are reviewed for the exact MCU/module and chosen footprints.
