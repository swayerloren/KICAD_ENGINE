# AI Placement Review Rules

## Purpose

Define what AI can review or suggest during placement without overstepping into final layout approval.

## AI May Suggest

- Placement groups.
- Relative placement priorities.
- Fixed connector and mounting-hole assumptions.
- High-risk net route order.
- Keepout candidates.
- Decoupling proximity warnings.
- Power path layout warnings.
- RF/USB/CAN/clock/thermal review flags.

## AI Must Not Approve

- Connector orientation.
- RF antenna placement.
- USB-C connector footprint and CC implementation.
- CAN/LIN/RS485 connector pinout and termination.
- High-current trace adequacy.
- Thermal performance.
- PNP rotation.
- Final manufacturability.

## Required Placement Report Sections

- Fixed mechanical items.
- Connector review list.
- Power input and regulator placement.
- MCU/module placement.
- Decoupling placement risks.
- High-risk nets.
- Keepouts and rule areas.
- Items blocked by missing information.
- Recommended human review sequence.

## Stop Conditions

Stop before suggesting placement if:

- Board outline is missing.
- Connector direction is unknown.
- Footprint verification is incomplete.
- RF/USB/CAN/high-current requirements are unknown.
- Mechanical enclosure constraints are unknown.

## Before/After Checks

After any placement change:

- Run DRC if a PCB exists.
- Export position file if useful.
- Generate visual review artifacts if useful.
- Compare footprint positions and locks.
- Record changed footprints.
- Keep outputs `NOT_FINAL`.

