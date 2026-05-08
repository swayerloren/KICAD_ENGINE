# Automotive Connector Rules

Date: 2026-05-02

Status: mandatory automotive connector guidance. Generic automotive connector records are placeholders only.

## Core Rule

Automotive connectors are connector systems, not isolated PCB parts. Housing, terminals, seals, cavity plugs, wire gauge, keying, latch, CPA/TPA, and harness routing must be verified together.

## Required Checks

- Exact manufacturer and series.
- Housing part number.
- Header or receptacle part number.
- Terminal/contact part number.
- Wire gauge range.
- Seal, cavity plug, wedge lock, CPA, TPA, or secondary lock part numbers.
- Mating connector and service part availability.
- Cavity numbering view.
- Keying and color coding.
- Current, voltage, temperature, ingress, vibration, and chemical exposure ratings.
- Harness exit direction and strain relief.

## PCB/Header Checks

- Verify through-hole or press-fit pin geometry.
- Verify board thickness range.
- Verify mounting holes, latches, and keepouts.
- Verify connector body overhang and enclosure opening.
- Verify potting, gasket, or waterproofing clearance.
- Verify current-carrying copper from each terminal.

## Honda-Style Sub-Harness Placeholder

- Treat any Honda-style connector request as an OEM-specific research task.
- Do not infer pinout from forum images, marketplace listings, or similar harnesses.
- Require exact vehicle/model/year/service-manual context or exact connector manufacturer data.
- Keep the record as `UNVERIFIED_PLACEHOLDER` until source evidence is available.

## Common Mistakes

- Using a generic sealed connector footprint for a different housing.
- Ignoring terminal crimp/contact part numbers.
- Reversing cavity numbering from mating face versus wire side.
- Forgetting blanking plugs for unused sealed cavities.
- Assuming waterproof connector means waterproof PCB assembly.
- Ignoring harness bend radius and enclosure strain relief.

## AI Release Rule

An automotive connector cannot be promoted from `UNVERIFIED_PLACEHOLDER` until exact connector-system part numbers, mating parts, pin numbering view, and mechanical fit are documented.
