# MCU Common Mistakes

## High-Risk Mistakes

- Missing power or ground pins because the symbol hides units or uses split power units.
- Missing analog supply pins such as VDDA/VSSA where present.
- Leaving boot mode pins floating.
- Forgetting reset pullup or required reset circuit.
- Assuming debug pins are optional before first bring-up.
- Choosing a footprint by pin count instead of exact package drawing.
- Copying oscillator circuits without checking load capacitance and drive requirements.

## Agent Checks

- Compare symbol pins to the datasheet pin table.
- Check every power unit in a multi-unit KiCad symbol.
- Confirm boot, reset, clock, and programming pins.
- Mark every unknown package suffix as `Unknown - requires source verification`.

## Required Human Review

Human review is required before approving first-revision MCU pinout, boot mode, clocking, and programming/debug access.

