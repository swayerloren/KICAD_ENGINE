# Hallucination Risk Log - Golden Path Sample Promotion

Date: `2026-05-03`

Risk label: `MEDIUM_RISK`

## Risk Controls

- Did not claim the sample passes ERC or DRC.
- Did not claim the custom footprint is correct.
- Did not claim public payload inclusion is approved.
- Excluded upstream generated outputs from the controlled copy.
- Marked the fixture as a workflow demo with known failures.

## Remaining Risk Patterns

Future agents may accidentally overstate this fixture as:

- a clean golden-path pass
- a verified reference design
- a scored benchmark result
- fabrication-ready
- public-payload-approved

## Required Rule

Before using this fixture, read `GOLDEN_PATH_DEMO_STATUS.md`. Treat it as blocked from pass claims until repair, rerun, and human review evidence exists.

