# Footprint Origin Rules

## Purpose

The footprint origin affects placement, pick-and-place, and review.

## General Rule

Set the origin intentionally and document the convention.

## Common Conventions

- SMD components: origin at component centroid unless a package-specific convention is required.
- Through-hole connectors: origin may be pin 1 or body center, but must be documented.
- Mechanical footprints: origin should support accurate placement relative to board outline or mechanical references.

## Pick-And-Place Review

The origin does not guarantee assembly rotation correctness. PNP outputs require human review against the assembler's convention.

## Review Gate

If origin choice affects assembly, placement, or mechanical alignment, human review is required.

