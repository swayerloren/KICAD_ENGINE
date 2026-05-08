# PCB Layout Sandbox Rules

## Purpose

Prevent agents from jumping directly into live PCB edits without reasoning through mechanical constraints, orientation, keepouts, and projected routing.

## Hard Rules

1. Do not edit a real `.kicad_pcb` until an active-project PCB Layout Sandbox report set exists.
2. Every PCB project must generate at least three layout variants before first real placement work.
3. Every variant must include:
   - board outline
   - dimensions
   - fixed mechanical components
   - connector orientation
   - antenna keepout
   - power path
   - USB or data path
   - routing projection
   - risk score
4. Connector placement must be reasoned before routing.
5. USB-C and barrel jack footprints must be treated as fixed mechanical and edge-facing components unless project requirements explicitly justify another approach.
6. ESP32 and similar module antenna keepouts must be defined before placing surrounding components.
7. Do not assume every PCB is rectangular.
8. Board shape must be chosen from mechanical, connector, enclosure, routing, and usability requirements.
9. Do not claim a layout is professional until placement, routing feasibility, DRC, and visual review all pass.
10. The selected variant must be justified before real KiCad PCB work starts.
11. Do not treat footprints as mechanically verified without exact package, edge, and orientation review.
12. Do not route first and hope the placement works later.

## Minimum Project Evidence

An active project must have at least:

- three variant plan reports
- one selected-variant justification report
- connector orientation review evidence
- routing-feasibility evidence
- human-review gate status

## Standard Status Labels

- `SANDBOX_NOT_STARTED`
- `VARIANTS_IN_PROGRESS`
- `SANDBOX_VARIANTS_READY_FOR_REVIEW`
- `SANDBOX_SELECTED_VARIANT_JUSTIFIED`
- `SANDBOX_BLOCKED_BY_MECHANICAL_OR_FOOTPRINT_RISK`
- `SANDBOX_APPROVED_FOR_REAL_PCB_EDIT`

