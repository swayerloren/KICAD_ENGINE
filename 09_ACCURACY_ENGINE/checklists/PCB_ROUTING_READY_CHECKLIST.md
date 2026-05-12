# PCB Routing Ready Checklist

Use with:

- `09_ACCURACY_ENGINE/pcb_rules/TRACE_ANGLE_ROUTING_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/PCB_ROUTING_QUALITY_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/GROUNDING_AND_RETURN_PATH_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/TEST_POINT_LAYOUT_RULES.md`

## Checks

- Placement review is complete.
- USB route plan is compact and paired.
- `BUCK_SW` route plan is short and isolated.
- Power-net width constraints are defined.
- RF keepout route exclusions are defined.
- Test-point access plan uses short leaf stubs.
- The copied-board or projected-route plan does not rely on rectangular perimeter detours.
- Routing quality gate scripts are ready to run after each stage.
