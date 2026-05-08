# NOT_FINAL Export Rules

Status: `ACTIVE_RULES`

## Definition

`NOT_FINAL` means generated manufacturing-style files are for review only and must not be uploaded or ordered without LJ approval.

## Required Block Conditions

Block export/package readiness if any of these are missing or failed:

- Phase gate approval.
- ERC evidence.
- Schematic parity evidence.
- DRC pass or exact LJ-approved remaining warnings.
- No-unrouted-net proof.
- Gerber external-viewer review.
- Drill-file review.
- BOM validation.
- CPL/centroid validation.
- Connector orientation proof.
- Pin 1 / diode / LED / capacitor polarity proof.
- Assembly notes.
- Orientation checks.

## Production-Ready Claims

Agents must not call files `production-ready`, `fab-ready`, or `upload-ready` unless the full export gate passes and LJ approves.

