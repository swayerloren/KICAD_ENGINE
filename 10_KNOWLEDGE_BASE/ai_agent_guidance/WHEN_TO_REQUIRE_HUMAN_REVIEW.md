# When To Require Human Review

Human review is required for:

- Connector orientation and pin numbering.
- Footprint approval for exact package fit.
- Polarity-sensitive parts.
- RF layout and antenna keepouts.
- USB-C role, CC wiring, and connector footprint.
- CAN/LIN/RS485 connector pinout and termination.
- Automotive input protection.
- High-current power paths.
- Thermal decisions.
- PNP rotations.
- Gerber/drill package approval.
- Any manufacturing order decision.

## AI Agent Responsibility

The agent should prepare the evidence and highlight risks. It should not act as the final manufacturing authority.

## Output Language

Use:

- `Human review required before fabrication.`
- `This is NOT_FINAL.`
- `Evidence is incomplete.`
- `Footprint is candidate-only until package drawing is checked.`

