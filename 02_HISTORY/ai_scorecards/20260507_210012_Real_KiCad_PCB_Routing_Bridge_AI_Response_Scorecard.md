# Real KiCad PCB Routing Bridge AI Response Scorecard

Record kind: `ai_scorecard`
Created: `2026-05-07T21:00:12`
Scope: `global`
Project: `N/A`
Severity: `LOW`
Confidence: `HIGH`
Claim status: `VERIFIED_BY_COMMAND`
Risk label: `LOW_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `NO`

## Scores

- Overall score: `96/100`
- Evidence support: `19/20`
- KiCad-specific correctness: `20/20`
- Datasheet/component accuracy: `15/15`
- Safety/compliance with repo rules: `15/15`
- Memory/history routing correctness: `9/10`
- Uncertainty disclosure: `9/10`
- End-user usefulness: `9/10`

## Summary

The routing bridge is now real, read-only, and copied-board tested. It extracts routing-schema JSON from real KiCad boards and couples that with DRC evidence without touching the active project.

## Evidence

Bridge scripts created, copied-board extraction/audit outputs produced, keepout classification bug fixed, py_compile passed, and active-project hashes remained unchanged.

## Unresolved Issues

Active-project routing is still blocked by missing extraction semantics and upstream project gates.
