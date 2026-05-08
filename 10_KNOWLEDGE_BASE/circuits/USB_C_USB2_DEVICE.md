# USB-C USB2 Device Circuit

## Use Case

Use this pattern for a USB-C receptacle connected to a USB 2.0 device controller, MCU, bridge, or interface IC.

## Required Evidence

- Exact connector drawing.
- USB device IC or MCU datasheet.
- USB-C CC requirements from a trusted specification or vendor reference.
- ESD protection datasheet and layout guidance.

## Typical Schematic Block

- USB-C receptacle.
- CC1 and CC2 configured for device/sink behavior.
- D+ and D- connected to the USB device pins.
- ESD protection on D+ and D- near the connector.
- Optional VBUS sense into the MCU if required by the USB controller.
- Shield connection strategy documented.

## PCB Review Points

- Route D+ and D- as a matched USB2 differential pair using the board stackup.
- Keep stubs short and avoid test pads that create excessive discontinuity.
- Place ESD protection close to the connector, before long internal routing.
- Verify connector pin mirroring and orientation in 3D/mechanical view.

## Common Mistakes

- Swapping D+ and D-.
- Missing VBUS sense where the controller requires it.
- Treating all USB-C connectors as pin-compatible.
- Placing ESD far from the connector.
- Using differential-pair dimensions from a random board instead of the actual stackup.

## Verification Gate

Do not mark approved until the connector, CC resistors, USB pins, ESD part, and footprint are source-verified.

