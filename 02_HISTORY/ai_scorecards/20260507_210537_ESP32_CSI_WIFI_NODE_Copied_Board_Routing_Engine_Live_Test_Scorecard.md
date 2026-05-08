# ESP32_CSI_WIFI_NODE Copied Board Routing Engine Live Test Scorecard

Record kind: `ai_scorecard`
Created: `2026-05-07T21:05:37`
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

The routing engine successfully ingested a copied real board and produced extraction plus audit outputs without touching the active PCB.

## Evidence

Matching source/copy PCB hashes, successful extractor runs, successful copied-board audit run, requested Markdown and JSON outputs, and unchanged source PCB hash after the run.

## Unresolved Issues

Active-project routing remains blocked by both routing-audit hard fails and upstream project gates.
