# NOT_FINAL Output Rules

Status: `ACTIVE_RULES`

## Prime Rule

All generated manufacturing-style outputs are `NOT_FINAL` until the full verification and human review gate passes.

## Applies To

- Gerbers.
- Drill files.
- BOM.
- CPL / PNP.
- Assembly notes.
- STEP files.
- Fab drawings.
- Stencil files.
- Zipped manufacturing packages.

## Required Labeling

Use `NOT_FINAL` in output folder names, package names, reports, and review notes until final human approval.

## Blockers

Do not remove `NOT_FINAL` if:

- ERC/DRC was not run when required.
- Footprints are unverified.
- Connector orientation is unverified.
- Polarity orientation is unverified.
- BOM lacks source/datasheet review.
- Mechanical fit is unreviewed.
- Fab-house requirements are not sourced.

