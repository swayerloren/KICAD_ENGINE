# Schematic Layout Engine Scorecard

Record kind: `ai_scorecard`
Created: `2026-05-10T11:35:04`
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
- Datasheet/component accuracy: `12/15`
- Safety/compliance with repo rules: `15/15`
- Memory/history routing correctness: `9/10`
- Uncertainty disclosure: `9/10`
- End-user usefulness: `10/10`

## Summary

Repo tooling and read-only validation completed; the active schematic was correctly classified as failing readability.

## Evidence

Python syntax passed and the read-only review packet was generated at reports/schematic_layout/20260510_113053/.

## Unresolved Issues

Layout scoring uses heuristics and the active schematic remains blocked on real readability cleanup.
