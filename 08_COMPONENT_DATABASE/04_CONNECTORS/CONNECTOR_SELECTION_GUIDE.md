# Connector Selection Guide

Date: 2026-05-02

Status: AI-readable connector selection guide. Generic connector records are placeholders only and are not approved for schematic or PCB use.

## Core Rule

Connector selection is mechanical, electrical, sourcing, assembly, and layout work. KiCad can help place a footprint, but it cannot prove that a cable fits, pin 1 is correct, the mating part exists, or the connector survives the environment.

## Required Selection Workflow

1. Define what crosses the board boundary: power, signal, RF, USB, battery, sensor harness, debug, field wiring, or antenna.
2. Define voltage, current, signal speed, impedance, environmental exposure, mating cycles, cable strain, and enclosure constraints.
3. Select an exact manufacturer part number.
4. Record the exact datasheet or drawing source.
5. Record the mating connector, terminals, seals, crimp tool, cable assembly, or panel part.
6. Match the KiCad footprint to the manufacturer land pattern.
7. Verify pin numbering against the drawing and mating connector view.
8. Verify mechanical orientation with a 3D model or drawing overlay.
9. Check silkscreen labels, polarity marks, pin 1 marks, board edge clearance, and cable bend clearance.
10. Run DRC and perform visual/mechanical review before any fabrication-style output.

## Family Guidance

| Connector Family | Use When | Avoid When | Verification Focus |
| --- | --- | --- | --- |
| USB-C | Reversible USB power/data connector is required. | Only a simple two-wire power jack is needed and CC behavior is not understood. | CC pins, shell pads, orientation, ESD, VBUS current, footprint. |
| micro USB B | Legacy USB 2.0 device interface is acceptable. | New product should use USB-C or needs higher durability. | Shield tabs, D+/D-, ID pin, VBUS, mechanical retention. |
| Barrel jack | Simple DC input from wall adapter. | Polarity, center pin size, switched pin, or enclosure fit is unknown. | Center diameter, switched contact, panel fit, polarity. |
| JST PH/XH/GH | Low-current board harnesses with known mating cables. | Current, crimp, latch, or pin numbering is unknown. | Exact series, pitch, top/side entry, mating housing and crimp. |
| Pin header | Debug, internal jumpers, or low-cost board interconnects. | Field wiring needs keyed/latching/polarized connector. | Orientation, shrouding, pin 1, mating cable, strain relief. |
| Terminal block | Field screw/spring wiring. | Vibration, wrong wire gauge, or enclosure access is unresolved. | Wire entry direction, pitch, current, torque, pin numbering. |
| U.FL/IPEX | Internal RF coax to module/antenna. | User-accessible antenna connector or frequent mating cycles are needed. | Exact U.FL/MHF compatibility, height, keepout, cable bend. |
| SMA edge launch | Board-edge RF connection is needed. | Stackup/board thickness and controlled impedance are unknown. | Launch geometry, ground vias, board thickness, RF simulation/review. |
| RP-SMA pigtail | Panel antenna connection via cable assembly. | Direct board RF launch is needed. | Cable assembly, bulkhead mounting, board-end connector, strain relief. |
| Automotive sealed | Harness must survive vibration, moisture, and service handling. | Housing/terminal/seal system is unknown. | Housing, terminals, seals, latch, wire gauge, cavity plugs, keying. |

## KiCad Rules

- Treat KiCad connector symbols and footprints as starting points.
- Never use a connector footprint only because the pitch and pin count match.
- Connector footprints from the same family can differ by locking posts, shell tabs, pad sizes, entry direction, or courtyard.
- Always check the manufacturer drawing view: top view, bottom view, mating face, or PCB footprint view can invert pin numbering.
- Add pin 1, polarity, voltage, and orientation silkscreen when possible.
- Keep mechanical courtyard and cable keepouts clear.
- Use 3D models for mechanical review, but do not trust them as electrical pinout proof.

## Generic Connector Records

Records are stored in:

- `08_COMPONENT_DATABASE/04_CONNECTORS/CONNECTOR_RECORDS.md`
- `08_COMPONENT_DATABASE/04_CONNECTORS/connector_records.json`

Every current record is `UNVERIFIED_PLACEHOLDER`.

## Blockers For AI Agents

Stop and mark the connector unready if any of these are missing:

- Exact manufacturer part number.
- Manufacturer drawing or datasheet.
- KiCad footprint matched to drawing.
- Mating connector or cable part.
- Pin numbering view confirmed.
- Mechanical orientation confirmed.
- 3D/mechanical clearance confirmed for enclosure and cable path.
- Current/voltage/environment rating confirmed.
- Polarity and pin 1 markings reviewed.
