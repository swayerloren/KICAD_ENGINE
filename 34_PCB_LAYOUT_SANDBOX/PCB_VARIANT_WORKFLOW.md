# PCB Variant Workflow

## Purpose

Define the mandatory reasoning workflow that happens before a real KiCad PCB file is edited.

## Workflow

1. Confirm active project, schematic gate status, and footprint-review status.
2. Gather mechanical and usability constraints:
   - enclosure
   - connector access
   - mounting
   - board dimensions
   - edge clearances
   - RF constraints
3. Identify fixed items first:
   - connectors
   - mounting holes
   - antenna keepouts
   - module edge requirements
   - high-current or switching-power clusters
4. Propose at least three layout variants.
5. For each variant, document:
   - board shape and dimensions
   - fixed/mechanical items
   - connector orientation
   - antenna keepout
   - power path projection
   - USB/data path projection
   - routing bottlenecks
   - human-review risks
   - variant score
   - optional FreeRouting dry-run evidence when a copied or sandbox board representation exists
6. Compare variants with the scorecard template.
7. Select one variant and justify why it is better than the others.
8. Run the auto layout decision engine and record either:
   - `AUTO_APPROVED_FOR_PCB_WORK`, or
   - an `AUTO_BLOCKED_*` report with exact missing items
9. Only after the selected variant is justified and auto-approved may real `.kicad_pcb` editing begin.

## Optional FreeRouting Support

FreeRouting may be used only as `REVIEW_ONLY` routing-feasibility evidence.

Allowed contribution:

- congestion comparison
- unrouted-net comparison
- via-pressure comparison
- impossible-placement detection

Not allowed:

- final routing approval
- automatic approval of USB, RF, switching-regulator, or high-current paths

## Standard Project Outputs

- `reports/PCB_LAYOUT_SANDBOX_VARIANT_01.md`
- `reports/PCB_LAYOUT_SANDBOX_VARIANT_02.md`
- `reports/PCB_LAYOUT_SANDBOX_VARIANT_03.md`
- `reports/PCB_LAYOUT_SANDBOX_SELECTED_VARIANT.md`

## Stop Conditions

Stop before real PCB edits if:

- connector orientation is unproven
- board outline is unjustified
- antenna keepout is blocked
- routing projection looks implausible
- footprint mechanics are still candidate-only
- the selected variant has not been justified
- the auto-approval report does not exist
- the auto-approval status is any `AUTO_BLOCKED_*`
