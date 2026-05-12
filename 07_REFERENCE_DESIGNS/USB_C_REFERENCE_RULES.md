# USB-C Reference Rules

Status: `REFERENCE_RULES_ACTIVE`

## Purpose

Guide comparison of USB-C schematic and PCB treatment against real examples.

## Compare

- mouth/opening faces off-board
- receptacle shell aligns to `Edge.Cuts`
- CC resistors stay close to the connector
- ESD protection stays near the connector/data entry
- D+/D- traces avoid long detours and ugly angle patterns
- schematic wiring reads left-to-right from connector to protection to device

## Do Not Assume

- a sample's footprint is automatically correct
- connector rotation alone proves orientation
- every USB-C board needs the same resistor placements or layer choices

## Hard Rule

Sample comparison is supporting evidence only. Mechanical truth and routing
quality must still be proven against the active project's own rules and audits.
