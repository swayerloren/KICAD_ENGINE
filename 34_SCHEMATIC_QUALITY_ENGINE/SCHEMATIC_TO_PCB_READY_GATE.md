# Schematic To PCB Ready Gate

## Purpose

Define the exact minimum state required before PCB update from schematic.

## Required Passes

- native annotation gate
- annotation/completeness audit
- footprint assignment gate
- visual/readability gate
- ERC proof
- unresolved high-risk review items closed or explicitly human-blocked

## Hard Rule

`PASS` requires both electrical correctness and drawing readability.

The schematic is not PCB-ready when any of these remain:

- `NEEDS_REVIEW`, `BLOCKED`, or `UNVERIFIED` on visible production symbols
- missing footprints on physical parts
- unresolved placeholder references
- unreadable block flow
- overlap findings
- automated-only crop evidence
- GUI annotation mismatch
