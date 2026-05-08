# Automotive 12 V Input Protection Circuit

## Use Case

Use this pattern when a board connects to an automotive 12 V harness or similar harsh supply.

## Required Evidence

- Required automotive transient standard or user requirement.
- Fuse/polyfuse rating source.
- TVS diode datasheet.
- Reverse-polarity protection device datasheet.
- Downstream regulator absolute maximum ratings.

## Typical Schematic Block

- Connector with clearly labeled battery, switched power, ground, and signals.
- Fuse or resettable protection.
- Reverse-polarity protection.
- TVS/transient clamp.
- Input filtering and bulk capacitance.
- Downstream buck or protected regulator.

## PCB Review Points

- Put protection near the connector.
- Size traces for fault and operating current.
- Keep high-energy transient paths short and direct.
- Separate dirty input area from sensitive logic.
- Check creepage/clearance if high transients are expected.

## Common Mistakes

- Treating automotive 12 V as a clean 12 V bench supply.
- Omitting reverse polarity.
- Choosing a TVS without checking standoff, clamp, surge, and package power.
- Letting transient current return through sensitive ground.

## Verification Gate

Human review is required. Do not approve without explicit transient, fuse, protection, and thermal requirements.

