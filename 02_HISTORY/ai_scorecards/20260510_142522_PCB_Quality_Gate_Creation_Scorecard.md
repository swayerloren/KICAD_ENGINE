# PCB Quality Gate Creation Scorecard

Record kind: `ai_scorecard`
Created: `2026-05-10T14:25:22`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `VERIFIED_BY_FILE`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Scores

- Overall score: `95/100`
- Evidence support: `20/20`
- KiCad-specific correctness: `20/20`
- Datasheet/component accuracy: `12/15`
- Safety/compliance with repo rules: `15/15`
- Memory/history routing correctness: `9/10`
- Uncertainty disclosure: `9/10`
- End-user usefulness: `10/10`

## Summary

Requested PCB quality-gate layer, CI hook, constraints template, and live dry-run validation completed with no KiCad design-file edits.

## Evidence

03_TOOLS/scripts/pcb_quality/; .github/workflows/pcb-quality-gate.yml; 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/pcb_quality_gate/20260510_quality_gate_creation_v2/pcb_quality_gate_result.json

## Unresolved Issues

The active board still fails the authoritative gate and cannot be treated as acceptable routing.
