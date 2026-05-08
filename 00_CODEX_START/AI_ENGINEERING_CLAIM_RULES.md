# AI Engineering Claim Rules

KiCad Engine treats engineering claims as evidence-bound assertions.

## Engineering Claims Include

- A component is suitable.
- A pinout is correct.
- A symbol is correct.
- A footprint is correct.
- A connector orientation is correct.
- A regulator, protection, RF, USB, CAN, or automotive circuit is acceptable.
- ERC or DRC passed.
- A package is ready for fabrication.

## Required Behavior

- Cite evidence for every major claim.
- Use claim statuses.
- Create an issue for unresolved high-risk claims.
- Mark manufacturing-style outputs `NOT_FINAL`.
- Require human review for connector orientation, mechanical fit, polarity, footprint verification, and fabrication readiness.

## Forbidden Behavior

- Do not guess datasheet values.
- Do not infer pinouts from similar parts.
- Do not approve generic footprints for exact parts.
- Do not claim ERC/DRC pass without command output.
- Do not claim fabrication readiness without human review.

