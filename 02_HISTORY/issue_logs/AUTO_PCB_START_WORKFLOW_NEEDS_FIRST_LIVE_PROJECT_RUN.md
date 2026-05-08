# AUTO_PCB_START_WORKFLOW_NEEDS_FIRST_LIVE_PROJECT_RUN

Date: `2026-05-07`

Status: `OPEN`

## Issue

The auto PCB start workflow is documented and integrated, but it has not yet been exercised on a real project that satisfies every precondition.

## Impact

Low for documentation integrity.

Medium for first-use confidence, because the exact project-local reporting flow still needs one real pass.

## Recommended Next Step

Run the workflow on the first project that has:

- `SCHEMATIC_TO_PCB_GATE_STATUS.md` exact `PASS`
- footprint/package gate `PASS` or `SAFE_CANDIDATE_WITH_EVIDENCE`
- sandbox gate exact `PASS`
- selected layout plan
- auto-approval report with `AUTO_APPROVED_FOR_PCB_WORK`

Then capture the first live evidence report and close this issue if the workflow behaves as documented.
