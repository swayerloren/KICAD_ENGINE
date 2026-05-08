# Connector Footprint Verification Rules

Date: 2026-05-02

Status: mandatory connector review guidance for AI-assisted KiCad work.

## Core Rule

Connector footprints must be treated as high-risk until matched to an exact manufacturer drawing. Pitch and pin count are not enough.

## Required Evidence

Before a connector footprint can be considered verified, record:

- Manufacturer.
- Exact part number.
- Datasheet or mechanical drawing source.
- Drawing revision or access date.
- KiCad symbol name.
- KiCad footprint name.
- Mating connector, cable, contact, crimp, seal, or panel part.
- Pin numbering view used for verification.
- 3D model source and status.
- Reviewer and date.

## Footprint Checklist

- Pad count matches the exact connector.
- Pad pitch matches the drawing.
- Pad sizes match the recommended land pattern or are intentionally adjusted for fabrication.
- Mechanical pegs, shield tabs, shell pads, mounting holes, and edge cutouts match the drawing.
- Hole sizes and plating match the connector pins.
- Board-edge distance matches the drawing.
- Courtyard covers connector body, latch, shield, cable exit, and hand-soldering needs.
- Silkscreen does not interfere with pads or shell.
- Pin 1 marker is visible after assembly if possible.
- Orientation matches the cable and enclosure.
- 3D model aligns with pads and board edge.

## Pin Numbering Checklist

- Identify whether the drawing uses mating face, PCB top view, PCB bottom view, or connector rear view.
- Check pin 1 and last pin against the symbol.
- Check odd/even numbering for dual-row connectors.
- Check shield pins and mounting tabs are not confused with electrical pins.
- Check keyed or polarized housings against the cable assembly.
- For terminal blocks, verify wire entry direction versus board orientation.
- For automotive connectors, verify cavity numbering from the service manual or manufacturer drawing.

## AI Warnings

- Do not mirror a footprint to fix a suspected orientation issue without drawing evidence.
- Do not assume JST-compatible parts use identical footprints.
- Do not assume Molex, TE, JST, and generic clones are footprint-compatible.
- Do not assume a 3D model from a different vendor proves fit.
- Do not trust marketplace or distributor images for pin numbering.
- Do not route a board until connector placement and cable exit are reviewed.

## Release Gate

Connector footprint verification is incomplete until ERC/DRC, visual review, and mechanical review agree with the exact connector drawing and mating part.
