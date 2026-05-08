# Crude 90-Degree Scripted Routing

Date: `2026-05-07`

Status: `ACTIVE_EVIDENCE`

## Mistake

An AI routing pass accepted harsh 90-degree bends, acute-angle risk, awkward pathing, and visually crude scripted-looking copper as if DRC legality were enough.

## Risk

- poor professional routing quality
- copper-geometry and manufacturing risk from acute angles
- higher review churn
- avoidable signal-quality degradation on sensitive nets

## Permanent Avoidance Rule

- Avoid 90-degree corners where practical.
- Never use acute bends sharper than 90 degrees unless there is no reasonable alternative and the exception is documented.
- Use two 45-degree bends for ordinary routing changes.
- Prefer smoother geometry for high-speed, RF, and sensitive nets where practical.
- If local placement causes ugly routing, move the local cluster instead of forcing bad traces.
- Do not approve routing from DRC pass alone.

## Evidence

- `09_ACCURACY_ENGINE/pcb_rules/TRACE_ANGLE_ROUTING_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/PCB_ROUTING_QUALITY_RULES.md`
- `09_ACCURACY_ENGINE/checklists/PCB_ROUTING_QUALITY_CHECKLIST.md`

