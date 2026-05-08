# Quality Gate Failure - Golden Path Sample Fixture Not Clean Pass

Date: `2026-05-03`

Gate: `GOLDEN_PATH_DEMO_PASS_GATE`

Status: `FAILED`

Risk label: `BLOCKED_UNTIL_HUMAN_REVIEW`

## Result

The promoted sample is a controlled workflow fixture, not a passing golden-path design.

## Evidence

- ERC: `FAIL`, `ERC_MESSAGES_7_ERRORS_1_WARNINGS_6`
- DRC: `FAIL`, `DRC_VIOLATIONS_16; FOOTPRINT_ERRORS_13; UNCONNECTED_0`
- Footprint/library status: unresolved `My footprints:MOLEX_48037-0001`
- Close-up visual review: not generated

## Required Before Pass Claim

- ERC pass or accepted warning review
- DRC pass or accepted warning review
- close-up visual review
- footprint/package and connector orientation review
- final human review for public payload inclusion

