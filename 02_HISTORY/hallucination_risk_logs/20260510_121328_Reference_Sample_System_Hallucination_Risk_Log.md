# Reference Sample System Hallucination Risk Log

Timestamp: `2026-05-10T12:13:28-04:00`

## Main Risk

An agent could over-read human-made sample projects as proof that a generated
design is correct.

## Mitigations Added

- sample anti-copy rules
- explicit "comparison evidence only" language in startup and handoff docs
- quality scorecard separating good references from failure fixtures
- public payload policy update that stays link-first by default

## Residual Risk

Agents still need human judgment and project-local proof when using sample
comparisons.
