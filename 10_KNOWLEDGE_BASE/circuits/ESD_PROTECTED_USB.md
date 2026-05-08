# ESD Protected USB Circuit

## Use Case

Use this pattern for any exposed USB connector.

## Required Evidence

- USB connector drawing.
- USB controller or MCU USB datasheet.
- ESD diode array datasheet.
- Layout guidance for the ESD package.

## Typical Schematic Block

- Connector D+ and D- routed through or alongside an ESD array per the protection part guidance.
- VBUS protection considered separately.
- Shield connection documented.
- Optional common-mode choke only when justified by EMI needs and source guidance.

## PCB Review Points

- Place ESD protection as close as possible to the connector.
- Provide a short, low-inductance return path to ground.
- Avoid stubs on D+ and D-.
- Verify the ESD part capacitance is appropriate for USB speed.

## Common Mistakes

- Placing ESD at the controller instead of the connector.
- Using an ESD package footprint with rotated or mirrored pinout.
- Adding high-capacitance protection to data lines.
- Leaving connector shield behavior undefined.

## Verification Gate

Do not approve until ESD pinout, footprint, capacitance suitability, placement, and shield handling are reviewed.

