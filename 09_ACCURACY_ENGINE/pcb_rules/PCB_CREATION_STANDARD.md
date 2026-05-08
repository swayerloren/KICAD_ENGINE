# PCB Creation Standard

## Purpose

Define minimum evidence before an AI agent creates or edits a KiCad PCB.

## Required Inputs

- Approved or review-ready schematic.
- Netlist/update-from-schematic status.
- Footprint assignments and verification status.
- Board constraints and fab assumptions.
- Interface-specific layout rules.
- Mechanical constraints and connector orientation notes.

## Rules

1. Do not place an unverified footprint without marking it `UNVERIFIED_FOOTPRINT`.
2. Do not approve connector orientation without exact drawing and human review.
3. Do not route RF, USB, CAN, power, crystal, or high-current paths without layout-specific review.
4. Do not treat DRC as full manufacturability approval.
5. Keep generated manufacturing outputs `NOT_FINAL`.

## Exit Criteria

PCB creation may proceed only when every footprint has a status and every high-risk component has a layout-review flag.
## Mandatory Evidence Gate

PCB creation must not begin from unverified schematic assumptions. Before PCB edits, confirm source status, footprint status, package drawing status, connector orientation status, polarity status, and interface-specific layout review status.

If PCB files are created or changed, DRC is required or must be explicitly recorded as not run with the reason.
