# Uncertainty Log: Schematic Visual Autocrop Setup

Record kind: `uncertainty_log`
Created: `2026-05-03T08:10:00`
Scope: `global`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Uncertainties

- Default normalized visual block positions may not perfectly match the intended schematic blocks.
- SVG text parsing may miss text converted to paths or graphical labels.
- Visible field-risk detection is conservative and may flag notes that mention footprint or datasheet review.
- Browser PNG rendering depends on installed Edge/Chrome behavior.

## Required Follow-Up

- Human-review crop alignment before using the visual report as gate evidence.
- Tune `_verification/schematic_visual/visual_blocks.json` for the active project.
- Keep visual findings as blockers until reviewed or resolved.
