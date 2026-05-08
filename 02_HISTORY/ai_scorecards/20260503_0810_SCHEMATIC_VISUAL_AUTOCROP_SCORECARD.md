# AI Response Scorecard: Schematic Visual Autocrop Setup

Record kind: `ai_scorecard`
Created: `2026-05-03T08:10:00`
Scope: `global`
Severity: `LOW`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Scores

- Overall score: `91/100`
- Evidence support: `19/20`
- KiCad-specific correctness: `18/20`
- Datasheet/component accuracy: `15/15`
- Safety/compliance with repo rules: `15/15`
- Memory/history routing correctness: `9/10`
- Uncertainty disclosure: `9/10`
- End-user usefulness: `6/10`

## Evidence

- PowerShell parser validation passed.
- Python syntax validation passed.
- Active project run generated full-page SVG/PDF/PNG, 13 SVG crops, 13 PNG crops, config, review Markdown, and JSON summary.
- Health check passed.

## Deductions

- First wrapper smoke test failed due a path bug and was fixed.
- Default crop blocks are starter coordinates, not human-confirmed exact crop windows.
- Active project visual review status remains `FAIL`.
