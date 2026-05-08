# Issue Tracking Rules

KiCad Engine uses markdown issue records for unresolved problems that must not be forgotten across sessions.

## When To Create An Issue

Create an issue record when:

- A user correction leaves unresolved work.
- A project has an open design risk.
- A component, datasheet, footprint, connector, or 3D model is unverified.
- A script or workflow is unsafe, failing, or incomplete.
- A release blocker remains open.

## Routing

- Global issue: `02_HISTORY/issue_logs/`
- Project issue: `04_KICAD_PROJECTS/active/PROJECT/history/issue_logs/`
- Durable project risk summary: `04_KICAD_PROJECTS/active/PROJECT/memory/OPEN_DESIGN_RISKS.md`

## Close Criteria

An issue can be closed only when the record names:

- The fix or human decision.
- The evidence.
- The verification run if applicable.
- Any memory update needed.

