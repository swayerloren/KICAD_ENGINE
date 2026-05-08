# TASK 004: USB-C Power Device

Status: `NOT_RUN`.

## Objective

Ask an AI agent to plan or review a USB-C power-input device using KiCad. The task measures whether the agent handles CC resistors, VBUS protection, connector footprint verification, current claims, and `NOT_FINAL` output discipline.

## Allowed Inputs

- KiCad Engine repo docs and databases.
- USB-C connector datasheet or drawing for the exact connector under review.
- USB Type-C specification summaries only where public and legally usable.
- Regulator, protection, ESD, fuse, and connector source documents.
- Installed KiCad symbol and footprint libraries.

## Expected Outputs

- USB-C power-input schematic plan or review report.
- Connector exact MPN requirement or generic connector flagged `UNVERIFIED_PLACEHOLDER`.
- CC resistor handling.
- VBUS path, fuse/protection, ESD, and regulator plan.
- Symbol/footprint candidates and verification status.
- ERC/DRC evidence if a project is created or supplied.
- Human review flags for connector orientation and current assumptions.

## Required Evidence

- Exact connector drawing for footprint approval.
- CC resistor role and placement.
- VBUS current limit assumptions marked source-backed or unverified.
- ESD/protection part placement notes.
- Regulator input/output capacitor requirements marked source-backed or unverified.
- `NOT_FINAL` labels for any generated outputs.

## Scoring Focus

- USB-C schematic correctness.
- Power design correctness.
- Connector footprint verification.
- BOM completeness.
- Human review flags.
- No overclaimed current capability.

## Failure Modes

- Omitting CC resistors for a sink/device.
- Approving a generic USB-C footprint without exact drawing.
- Claiming high current without source-backed negotiation/current-path design.
- Ignoring connector shell, shield, or ESD review.
