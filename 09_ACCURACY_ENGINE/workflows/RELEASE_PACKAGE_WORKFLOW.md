# Release Package Workflow

## Purpose

Define the accuracy gate before manufacturing-style outputs can be considered for release.

## Steps

1. Confirm active project and source revision.
2. Confirm backups and history.
3. Run ERC and interpret results.
4. Run DRC and interpret results.
5. Review BOM.
6. Review footprints against package drawings.
7. Review connectors, polarity, USB, CAN, RF, power, and mechanical constraints.
8. Export review package as `NOT_FINAL`.
9. Review Gerbers, drills, PNP, BOM, STEP, and drawings.
10. Record final human approval or keep output `NOT_FINAL`.

## Rule

Generated manufacturing outputs are never final by default. They remain `NOT_FINAL` unless final human review explicitly approves them.
## Mandatory NOT_FINAL Gate

Release-package workflows must keep outputs labeled `NOT_FINAL` until ERC, DRC, BOM, footprint, connector, polarity, mechanical, fab-profile, and human-review gates are complete.

Do not claim a package is fabrication-ready from generated files alone.
