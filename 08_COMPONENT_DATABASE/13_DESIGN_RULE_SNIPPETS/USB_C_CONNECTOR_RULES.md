# USB-C Connector Rules

Date: 2026-05-02

Status: mandatory USB-C connector guidance. Generic USB-C connector records are placeholders only.

## Core Rule

USB-C connector footprints are not interchangeable. A USB-C receptacle must be selected by exact manufacturer part number and land pattern.

## Required Checks

- USB-C role: sink, source, dual-role, charge-only, data-only, or debug.
- Pin count: 16-pin USB2-only or 24-pin full-feature.
- Mount type: mid-mount, top-mount, through-hole shell, hybrid, vertical, or edge.
- USB speed and routing requirements.
- CC resistor or controller requirements.
- VBUS current and protection.
- Shell grounding and shield strategy.
- ESD protection for D+/D-, CC, SBU, high-speed pairs if used, and VBUS as required.
- Cable insertion direction and enclosure opening.

## 16-Pin USB2-Only Receptacles

- Do not assume every 16-pin USB-C receptacle has the same pad layout.
- Verify duplicated D+/D- pins and orientation behavior.
- Verify CC1/CC2 pins and required pull-downs for sink-only designs.
- Verify whether SBU pins exist or are omitted.
- Verify shell pad geometry and mechanical peg holes.

## 24-Pin Full-Feature Receptacles

- Full-feature receptacles add high-speed pairs and more routing constraints.
- Do not use a 24-pin connector footprint for USB2-only unless the unused high-speed pins, pads, and DRC implications are intentional.
- Verify superspeed pair orientation, escape routing, and impedance before layout.
- USB PD requires a suitable PD controller; the connector alone does not provide PD behavior.

## Footprint And Mechanical Review

- Check board edge location.
- Check connector height and insertion depth.
- Check shell tab hole size, plating, and mechanical strength.
- Check courtyard for plug shell and cable strain.
- Check 3D model alignment to enclosure.
- Confirm pin numbering using the manufacturer drawing, not a distributor image.

## Common Mistakes

- Omitting CC pull-downs on a sink.
- Mirroring D+ and D- through the receptacle.
- Using the wrong shell-tab footprint.
- Backfeeding VBUS.
- Treating TUSB320 as a full USB PD controller.
- Using a 16-pin symbol with a 24-pin footprint or the reverse.
- Ignoring shield grounding and ESD return path.

## AI Release Rule

A USB-C connector stays `UNVERIFIED_PLACEHOLDER` until exact part, drawing, footprint, mating cable/enclosure access, CC behavior, ESD, and VBUS behavior are all documented.
