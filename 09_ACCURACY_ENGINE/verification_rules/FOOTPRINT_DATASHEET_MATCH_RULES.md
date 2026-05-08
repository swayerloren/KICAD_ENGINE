# Footprint Datasheet Match Rules

## Purpose

Define what counts as a verified footprint.

## Required Match Evidence

- Exact manufacturer part number.
- Exact package code.
- Package drawing or land pattern.
- KiCad footprint file path.
- Pad count and numbering match.
- Mechanical orientation match.
- Pin 1 marking match.

## Not Enough

- Footprint name looks similar.
- 3D model appears to fit.
- Another project used it.
- DRC is clean.
- Symbol default footprint field points to it.

## Status

Use `FOOTPRINT_VERIFIED_AGAINST_DRAWING` only when the evidence above is recorded.
## Mandatory Evidence Gate

Footprint-to-datasheet match claims require exact package drawing evidence. A footprint name match, 3D model match, or clean DRC result does not prove package correctness.

Connector, RF, USB-C, and board-to-board footprints remain `BLOCKED_UNTIL_HUMAN_REVIEW` until exact drawing and orientation are reviewed.
