# AI Uncertainty Disclosure Rules

Uncertainty must be visible and actionable.

## When To Log Uncertainty

Log uncertainty when:

- evidence is incomplete,
- source documents are missing,
- a claim is inferred,
- a KiCad check could not run,
- a footprint or connector is generic,
- exact electrical values are unknown,
- a human decision is required.

## Required Fields

- What is uncertain.
- Why it is uncertain.
- Risk level.
- Required evidence.
- Human review required.
- Where the issue is tracked.

## Wording Rules

Use clear language:

- `UNVERIFIED`
- `PARTIALLY_VERIFIED`
- `REQUIRES_HUMAN_REVIEW`
- `Unknown - requires source verification`
- `NOT_FINAL`

Do not use vague confidence language to hide missing evidence.

