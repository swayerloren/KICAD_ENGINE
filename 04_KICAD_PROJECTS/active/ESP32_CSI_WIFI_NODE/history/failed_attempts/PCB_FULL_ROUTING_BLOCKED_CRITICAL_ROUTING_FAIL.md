# PCB_FULL_ROUTING_BLOCKED_CRITICAL_ROUTING_FAIL

Status: `FAILED_BLOCKED`

Date: 2026-05-03

## Attempt

Route remaining nets and perform full trace-by-trace verification.

## Failure/Blocker

Full routing was blocked because critical routing did not pass:

- `reports/PCB_CRITICAL_NETS_ROUTING_REPORT.md`: `CRITICAL_ROUTING_FAIL`
- `reports/PCB_ROUTING_PLAN.md`: `ROUTING_PLAN_BLOCKED`
- `.kicad_pcb` exists: `NO`

## Correct Behavior

Do not route remaining low-risk nets until critical routing has passed or is explicitly accepted with documented non-blocking warnings.

