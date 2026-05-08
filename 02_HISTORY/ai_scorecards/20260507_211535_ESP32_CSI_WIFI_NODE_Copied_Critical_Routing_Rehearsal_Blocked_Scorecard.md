# ESP32_CSI_WIFI_NODE Copied Critical Routing Rehearsal Blocked Scorecard

Record kind: `ai_scorecard`
Created: `2026-05-07T21:15:35`
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

The request was handled by enforcing the user-provided rehearsal precondition and the existing routing blockers rather than creating misleading rehearsal progress.

## Evidence

Routing plan result ROUTING_BLOCKED, scorecard hard fails, blocker report, and no routing or file-copy actions performed.

## Unresolved Issues

The project still has unresolved earlier gate blockers and board-state routing blockers.
