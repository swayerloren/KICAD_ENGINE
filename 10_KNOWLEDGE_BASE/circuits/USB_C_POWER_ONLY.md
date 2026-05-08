# USB-C Power-Only Receptacle Circuit

## Use Case

Use this pattern when a board only needs power from a USB-C source and does not use USB data.

## Required Evidence

- Exact USB-C connector datasheet and footprint drawing.
- USB Type-C specification reference or trusted design guide.
- Current requirement for the board.
- Protection part datasheets if TVS, fuse, or load switch is used.

## Typical Schematic Block

- USB-C receptacle with VBUS, GND, CC1, and CC2 connected correctly.
- CC pulldown resistors for sink behavior. Exact value requires USB-C spec verification.
- Optional resettable fuse or load switch on VBUS.
- Optional TVS diode on VBUS for exposed connector designs.
- Board power input net named clearly, for example `USB_VBUS` or `VBUS_5V`.

## PCB Review Points

- Connector orientation and pin numbering require human review.
- VBUS trace width must match expected current and copper stackup.
- Place protection close to the connector.
- Avoid routing high-current VBUS through narrow necks.
- Keep connector shell/mechanical pads consistent with the drawing.

## Common Mistakes

- Leaving CC pins floating.
- Shorting CC pins together without checking the connector/pinout.
- Using a USB-C footprint for a different manufacturer part.
- Calling the port compliant without checking current advertisement, protection, and mechanical fit.

## Verification Gate

Do not mark approved until the CC implementation, connector footprint, VBUS current path, and protection strategy are checked against sources.

