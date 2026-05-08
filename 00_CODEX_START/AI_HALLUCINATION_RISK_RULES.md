# AI Hallucination Risk Rules

Hallucination risk is any chance that the agent invented, guessed, overgeneralized, or overstated an engineering fact.

## Risk Labels

- `LOW_RISK`: claims are backed by files, command output, datasheets, or user-provided facts.
- `MEDIUM_RISK`: some claims are inferred but low impact and clearly marked.
- `HIGH_RISK`: high-impact electrical, mechanical, footprint, pinout, or manufacturing claims are weakly sourced.
- `BLOCKED_UNTIL_HUMAN_REVIEW`: work cannot be treated as reliable without human review.

## High-Risk KiCad Claims

Always log hallucination risk when a claim involves:

- footprint correctness,
- connector orientation,
- pinout mapping,
- package selection,
- current/voltage ratings,
- thermal limits,
- RF/USB/CAN/automotive layout,
- ERC/DRC status,
- fabrication output readiness,
- human assembly/mechanical fit.

## Required Action

If any high-risk claim is inferred or weakly sourced:

1. Mark the claim `UNVERIFIED` or `REQUIRES_HUMAN_REVIEW`.
2. Create a hallucination-risk log.
3. Create or update an issue if unresolved.
4. Do not claim fabrication readiness.

