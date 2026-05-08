# Connector Review Checklist

Connector mistakes are high risk.

## Required Evidence

- Exact manufacturer part number or explicit generic placeholder status.
- Datasheet or mechanical drawing.
- Mating connector or cable assembly.
- Pin 1 location.
- Pin numbering direction.
- Mounting style and orientation.
- Footprint and 3D model status.

## Review Steps

- Compare schematic symbol pin numbers to connector drawing.
- Compare footprint pads to connector land pattern.
- Check top/bottom side and mirrored orientation.
- Check shell, shield, mounting tabs, and mechanical pads.
- Check cable exit direction and enclosure clearance.
- Confirm silkscreen pin 1 or orientation marker.

## Stop Conditions

If the exact connector is unknown, mark `UNVERIFIED_PLACEHOLDER` and require human review before PCB approval.

