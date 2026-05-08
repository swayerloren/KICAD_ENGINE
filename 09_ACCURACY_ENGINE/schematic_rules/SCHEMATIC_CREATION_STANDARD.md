# Schematic Creation Standard

## Purpose

Define the minimum evidence needed before an AI agent creates or edits a KiCad schematic.

## Required Inputs

- Project requirements.
- Power domains and expected voltage/current ranges.
- Component sources or source links.
- Datasheets, reference manuals, package drawings, or explicit missing-source notes.
- Component database records where available.
- KiCad symbol candidates.

## Creation Rules

1. Do not place a component from memory alone.
2. Do not invent pin numbers, pin names, electrical types, voltage limits, or required external parts.
3. Do not use a symbol until its pinout has been compared to the source package/device.
4. Add required support circuitry from the datasheet or vendor reference design, not generic expectation.
5. Keep connector orientation and pin numbering as `HUMAN_REVIEW_REQUIRED` until exact drawing evidence is reviewed.
6. Flag polarity-sensitive parts, RF parts, USB parts, CAN parts, and power-path parts.
7. Mark all unknown specs as `Unknown - requires source verification`.
8. Keep visible schematic values short enough to read; move long review detail into hidden fields, review tables, or separate notes zones.
9. Do not place review notes inside active circuitry blocks.
10. Do not allow references, values, net labels, power symbols, pin labels, or notes to overlap or visually touch wires, pins, symbol bodies, or other text.
11. Split or space dense regulator, connector, module, MCU, and power-path blocks until they are readable in rendered full-page and close-up views.

## Required Schematic Review Flags

- Missing datasheet or source.
- Generic symbol used.
- Unverified pinout.
- Unverified power pins.
- Missing decoupling.
- Missing reset, boot, programming, oscillator, or strap circuit.
- Connector pin numbering or orientation risk.
- Interface-specific rule review needed.

## Exit Criteria

A schematic plan may proceed only when each component has a source status, symbol status, pinout status, support-circuit status, and review flag status. A clean ERC does not override missing source evidence.

A schematic drawing may not be marked ready for visual review or PCB update unless it also passes `09_ACCURACY_ENGINE/checklists/SCHEMATIC_HUMAN_READABILITY_CHECKLIST.md`. Automated crop generation, ERC pass, annotation pass, and populated footprints do not prove human readability.

## Required AI Quality Gate

If the agent makes schematic correctness claims, it must create a claim/evidence matrix and uncertainty log before closeout. If the agent creates or modifies schematic files, ERC is required or must be explicitly recorded as not run with the reason.
