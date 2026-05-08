# RF Antenna U.FL Module Circuit

## Use Case

Use this pattern for modules that expose an RF pin or U.FL/IPEX antenna connector.

## Required Evidence

- Module hardware design guide.
- RF connector exact datasheet and footprint.
- Antenna or pigtail datasheet.
- Stackup and impedance target.

## Typical Schematic Block

- Module RF output connected to U.FL or matching network.
- Optional pi matching network populated or DNP per reference design.
- RF ground stitching near connector and feedline.
- Antenna keepout documented.

## PCB Review Points

- Use controlled-impedance RF feedline based on the actual stackup.
- Keep feedline short and free of stubs.
- Keep copper/ground clearances and antenna keepout per source.
- Verify connector orientation and keepout in 3D.

## Common Mistakes

- Treating RF trace width as universal.
- Using generic U.FL footprint without exact connector drawing.
- Routing under antenna keepout.
- Ignoring enclosure, cable, and nearby metal effects.

## Verification Gate

RF layout requires human review. Do not approve without exact RF connector, feedline, stackup, and antenna evidence.

