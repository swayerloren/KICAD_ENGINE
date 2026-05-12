# Footprint Package Engine Scorecard

Record kind: `ai_scorecard`
Created: `2026-05-10T11:56:21`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Scores

- Overall score: `93/100`
- Evidence support: `19/20`
- KiCad-specific correctness: `19/20`
- Datasheet/component accuracy: `13/15`
- Safety/compliance with repo rules: `15/15`
- Memory/history routing correctness: `9/10`
- Uncertainty disclosure: `9/10`
- End-user usefulness: `9/10`

## Summary

Requested footprint/package engine, templates, docs, and dry-run validation completed with no KiCad design edits.

## Evidence

Syntax validation passed, schema parse passed, and the dry-run gate produced a valid failing evidence packet at reports/footprint_package/20260510_115257/.

## Unresolved Issues

The active project still needs a populated FOOTPRINT_LOCK.csv and high-risk proof rows before schematic-to-PCB readiness can pass.
