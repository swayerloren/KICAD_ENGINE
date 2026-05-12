# Schematic Visual Audit Rules

## Rule

Human-readable visual review is a separate gate from ERC, annotation, and crop
generation.

## Required Visual Evidence

- full-page render
- close-up block crops
- block-by-block review record
- no unresolved `NOT_REVIEWED` sections

## Automatic Fail Conditions

- visible reference/value/label/text overlaps
- visible footprint/library/path fields in normal view
- visible unresolved placeholder references
- review notes crowding active circuitry
- crop report status only `AUTOMATED_CROP_PASS_ONLY`

## Pass Condition

Use `VISUAL_PASS` only when rendered images were actually reviewed and every
block is readable.
