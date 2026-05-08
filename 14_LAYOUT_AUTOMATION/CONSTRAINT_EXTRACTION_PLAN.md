# Constraint Extraction Plan

## Goal

Extract the constraints AI needs before it can propose placement or routing changes.

## Sources

- `.kicad_pcb` board setup.
- Net classes.
- Custom DRC rules.
- Rule areas and keepouts.
- Footprint properties.
- Board outline.
- Schematic net names.
- Component database records.
- Datasheet layout notes.
- Knowledge-base checklists.
- Reference design records.

## Constraint Types

### Mechanical

- Board outline.
- Mounting holes.
- Connector positions.
- Keepouts.
- Height limits.
- Enclosure edges.

### Electrical

- Net classes.
- Clearance.
- Track width.
- Via sizes.
- Differential pair constraints.
- Power current assumptions.
- Creepage or high-voltage needs.

### Functional

- Power tree.
- Signal groups.
- Programming/debug access.
- User interface.
- Test points.

### Layout Risk

- RF.
- USB.
- CAN/LIN/RS485.
- Crystals.
- Switching regulators.
- Automotive input protection.
- Thermal parts.
- Polarity-sensitive parts.

## Extraction Workflow

1. Parse project files read-only.
2. Identify footprints, nets, net classes, and rules.
3. Classify high-risk nets from names, component records, and datasheet notes.
4. Identify fixed mechanical items.
5. Identify unverified footprints and connectors.
6. Generate a constraint report.
7. Block automation if required constraints are unknown.

## Output Files

Recommended future outputs:

- `placement_constraints.md`
- `routing_constraints.md`
- `high_risk_nets.json`
- `mechanical_constraints.json`
- `drc_baseline.json`

## Stop Conditions

Do not propose automated placement or routing if:

- Board outline is unknown.
- Connector positions are unknown.
- Footprints are unverified.
- Net classes are missing for high-risk nets.
- Power/current assumptions are unknown.
- RF/USB/CAN/automotive requirements are unknown.

