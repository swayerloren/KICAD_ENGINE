# AI Closeout Scorecard Rules

Every meaningful AI session must create an AI response scorecard before final response or closeout.

## Required Scorecard Fields

- Overall score: `0-100`
- Evidence support: `0-20`
- KiCad-specific correctness: `0-20`
- Datasheet/component accuracy: `0-15`
- Safety/compliance with repo rules: `0-15`
- Memory/history routing correctness: `0-10`
- Uncertainty disclosure: `0-10`
- End-user usefulness: `0-10`
- Risk label.
- Gate result.
- Human review required.
- Main unsupported claims.
- Main unresolved issues.

## Scoring Discipline

Do not inflate scores because the work was extensive. Score the response based on evidence, correctness, safety, and honesty.

## Low Score Triggers

- Missing evidence for engineering claims.
- Missing ERC/DRC output when required.
- Unverified footprint or connector orientation.
- Missing logs.
- Missing uncertainty disclosure.
- Overconfident fabrication readiness claims.

