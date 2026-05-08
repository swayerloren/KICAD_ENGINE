# Placement DRC Precheck Rules

## Purpose

Define the minimum precheck rules that a proposed automatic placement must satisfy before real KiCad placement work continues.

## Required Checks

- no courtyard overlap
- no body overlap
- no board-edge clearance violation
- no antenna-keepout intrusion
- no mounting-hole clearance intrusion
- fixed mechanical connectors remain edge-facing
- test pads remain accessible
- obvious routing impossibility is flagged

## Status Rule

Use:

- `PASS`
- `AUTO_BLOCKED_BAD_LAYOUT`
- `AUTO_BLOCKED_MISSING_DATA`

## Important Boundary

Passing this precheck does not mean the board is ready for routing or fabrication. It means the placement concept is coherent enough to continue into controlled KiCad work.
