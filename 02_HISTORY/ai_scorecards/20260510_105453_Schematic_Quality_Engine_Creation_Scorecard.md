# Schematic Quality Engine Creation Scorecard

Record kind: `ai_scorecard`
Created: `2026-05-10T10:54:53`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Scores

- Overall score: `92/100`
- Evidence support: `19/20`
- KiCad-specific correctness: `19/20`
- Datasheet/component accuracy: `12/15`
- Safety/compliance with repo rules: `15/15`
- Memory/history routing correctness: `9/10`
- Uncertainty disclosure: `9/10`
- End-user usefulness: `9/10`

## Summary

Requested repo tooling, rules, and validation work completed with a successful dry-run gate and no KiCad design edits.

## Evidence

Syntax validation passed, schema parse passed, and the dry-run gate produced a failing-but-valid project audit packet at reports/schematic_quality/20260510_104847/.

## Unresolved Issues

Overlap detection uses estimated geometry and the active project remains blocked for real schematic-to-PCB progression.
