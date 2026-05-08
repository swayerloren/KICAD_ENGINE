# Portability Audit Scorecard

Record kind: `ai_scorecard`
Created: `2026-05-08T18:33:00`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `MEDIUM`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Scores

- Overall score: `90/100`
- Evidence support: `18/20`
- KiCad-specific correctness: `18/20`
- Datasheet/component accuracy: `11/15`
- Safety/compliance with repo rules: `15/15`
- Memory/history routing correctness: `9/10`
- Uncertainty disclosure: `10/10`
- End-user usefulness: `9/10`

## Summary

The portability pass is strong on repo safety, onboarding clarity, and evidence-backed git/folder conclusions. Score is reduced because some older tracked scratch and generated records remain intentionally unresolved in this docs-only pass.

## Evidence

`git status --ignored`; `git check-ignore -v ...`; folder inventory results; updated startup/onboarding docs; passive helper-script compile check

## Unresolved Issues

`routing_work` tracked payload, legacy machine-specific library-index URIs, and time-sensitive status docs remain follow-up items.
