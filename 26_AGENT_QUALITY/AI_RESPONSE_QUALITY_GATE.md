# AI Response Quality Gate

## Purpose

Define the closeout gate for AI engineering responses in KiCad Engine.

## Required For Engineering Claims

When engineering claims are made, closeout must include:

- AI self-review.
- AI response scorecard.
- Claim/evidence matrix.
- Uncertainty log for unverified or partially verified claims.
- Hallucination-risk log for inferred, guessed, or weakly sourced claims.

## Blocking Conditions

Mark the work `BLOCKED_UNTIL_HUMAN_REVIEW` if:

- exact footprint is not verified,
- connector orientation is not verified,
- datasheet source is missing,
- ERC/DRC was required but not run,
- manufacturing output was generated but not reviewed,
- KiCad design files changed without backup,
- pinout was inferred but not verified,
- source conflicts exist,
- the agent is uncertain about a high-risk electrical/mechanical decision.

## Response Requirements

The final response must not hide blockers. It must state:

- what was verified,
- what was not verified,
- what remains human-review-required,
- where the evidence records were written.

