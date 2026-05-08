# AI Self-Review Rules

## Purpose

Require Codex, Claude, and similar agents to inspect their own KiCad engineering claims before closing a session.

## When Required

Create an AI self-review when a session includes any engineering claim about:

- components,
- datasheets,
- symbols,
- pinouts,
- footprints,
- 3D models,
- schematic correctness,
- PCB layout correctness,
- ERC or DRC status,
- BOM completeness,
- fab output readiness,
- connector orientation,
- polarity,
- RF, USB, CAN, power, automotive, or manufacturing rules.

## Required Questions

1. What claims did I make?
2. Which claims are verified by files, commands, datasheets, KiCad evidence, or user-provided facts?
3. Which claims are partially verified?
4. Which claims are unverified?
5. Did I infer or guess any value, pinout, footprint, package, orientation, or rule?
6. Did I say ERC/DRC passed without command output?
7. Did I imply fabrication readiness without human review?
8. Did I clearly mark uncertainty?
9. Did I create the required scorecard, uncertainty log, and claim/evidence matrix?
10. Did I route memory/history records correctly?

## Required Output Location

Global records:

- `02_HISTORY/ai_self_reviews/`

Project-specific records:

- `04_KICAD_PROJECTS/active/<PROJECT>/history/ai_self_reviews/`

