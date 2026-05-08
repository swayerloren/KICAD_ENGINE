# AI Response Quality Gate

This gate determines whether an AI response can be considered usable or must be blocked until human review.

## Claim Statuses

- `VERIFIED_BY_FILE`
- `VERIFIED_BY_COMMAND`
- `VERIFIED_BY_DATASHEET`
- `VERIFIED_BY_USER`
- `PARTIALLY_VERIFIED`
- `UNVERIFIED`
- `CONTRADICTED`
- `REQUIRES_HUMAN_REVIEW`

## Mandatory Blockers

Mark the work `BLOCKED_UNTIL_HUMAN_REVIEW` if any of these are true:

- exact footprint is not verified,
- connector orientation is not verified,
- datasheet source is missing,
- ERC/DRC was required but not run,
- manufacturing output was generated but not reviewed,
- KiCad design files changed without backup,
- pinout was inferred but not verified,
- source conflicts exist,
- AI is uncertain about a high-risk electrical/mechanical decision.

## Gate Result Values

- `PASS`: all major claims are supported and no blocker exists.
- `PASS_WITH_WARNINGS`: usable, but explicit lower-risk uncertainty remains.
- `BLOCKED_UNTIL_HUMAN_REVIEW`: high-risk unresolved issue exists.
- `FAIL`: repo safety rules were violated or critical evidence contradicts the response.

## Required Outputs

If the gate is blocked or fails, create:

- quality gate failure record,
- issue record,
- uncertainty log,
- hallucination-risk log if applicable.

