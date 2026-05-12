# Schematic Common Failures

## Frequent Failure Modes

- ERC passes but the page is still hard to read
- local blocks use many labels and too few wires
- symbols are spread out with no clear flow
- passives are detached from the block they support
- values or references overlap wires or pins
- visible `NEEDS_REVIEW` strings remain on symbols
- saved-file scans look annotated but the KiCad GUI still shows unresolved `?`
- footprints exist for some parts but not all physical parts
- crop generation was mistaken for human visual approval

## Response

When these appear, do not proceed to PCB update. Repair readability, annotation,
footprint readiness, or human review evidence first.
