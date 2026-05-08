# Hallucination Risk Log - Supplier Footprint Match System

Date: 2026-05-03

## Risk

Supplier package names can look precise enough to select a KiCad footprint, but they often omit land pattern, pin numbering, mechanical orientation, and variant-specific details.

## Mitigation

- Confidence levels separate package-name matches from drawing-backed verification.
- High-risk categories require human review.
- Example records are marked `EXAMPLE_ONLY`.
- Confidence checker blocks unsafe connector approval when orientation is missing.

## Remaining Risk

Future agents must not treat JLC/LCSC/Mouser/Digi-Key package labels as footprint approval without exact drawing evidence.

