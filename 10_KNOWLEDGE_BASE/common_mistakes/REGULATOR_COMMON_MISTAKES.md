# Regulator Common Mistakes

## High-Risk Mistakes

- Missing required input or output capacitors.
- Using capacitors with incorrect voltage rating or ESR.
- Ignoring thermal dissipation.
- Choosing an inductor without checking saturation current.
- Placing feedback traces near switching nodes.
- Routing high-current switching loops large and noisy.
- Assuming pin-compatible regulators have the same requirements.

## Agent Checks

- Verify regulator datasheet and package.
- Verify load current and thermal dissipation.
- Verify capacitor values, ESR, voltage rating, and placement.
- Verify inductor and diode ratings for switching regulators.
- Check layout recommendations before PCB placement.

## Required Human Review

Human review is required for thermal margin, switching-loop layout, input protection, and any high-current power path.

