# Reference Designs Index

Status: `LINK_FIRST_RESERVED_LAYER`

## Purpose

This top-level folder is reserved for lightweight reference-design notes and public-source pointers. Structured reusable reference records belong in `12_REFERENCE_DESIGN_LIBRARY/`.

## Current Contents

- `README.md`: folder routing, safety, and public-release rules.
- `SCHEMATIC_STYLE_EXAMPLES.md`: comparison rules for schematic readability.
- `PCB_LAYOUT_STYLE_EXAMPLES.md`: comparison rules for PCB layout quality.
- `ESP32_DEV_BOARD_REFERENCE_RULES.md`: ESP32-style board comparison notes.
- `USB_C_REFERENCE_RULES.md`: USB-C comparison notes.
- `BUCK_REGULATOR_LAYOUT_REFERENCE_RULES.md`: buck-layout comparison notes.

## Use This Folder For

- Short link-first notes before a reference design is promoted into `12_REFERENCE_DESIGN_LIBRARY/`.
- Public-source candidate lists.
- License/attribution triage notes.
- Human-review notes about what can be learned from a design.

## Do Not Store

- Proprietary design files without permission.
- Downloaded vendor archives without redistribution review.
- Active KiCad project source files.
- Final fabrication outputs.
- Secrets or credentials.

## Agent Rules

- Reference designs are evidence, not approval.
- Do not copy schematic or layout blocks unless source license and design context permit it.
- Mark all unsourced electrical, footprint, and layout claims as `UNVERIFIED`.
- Promote durable records to `12_REFERENCE_DESIGN_LIBRARY/00_INDEX/REFERENCE_RECORD_TEMPLATE.md` format.

## Current Gap

This folder now contains comparison rules, not a fully curated gold-standard
sample corpus. Future promoted sample summaries still need license review,
quality scoring, and human curation.
