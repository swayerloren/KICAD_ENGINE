# 14 Route Critical Nets

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: route only critical nets first. Do not route all remaining low-risk nets.

## Read First

1. `AGENTS.md`
2. `reports/PCB_ROUTING_PLAN.md`
3. `09_ACCURACY_ENGINE/pcb_rules/TRACE_ANGLE_ROUTING_RULES.md`
4. `09_ACCURACY_ENGINE/pcb_rules/PCB_ROUTING_QUALITY_RULES.md`
5. `09_ACCURACY_ENGINE/checklists/PCB_ROUTING_QUALITY_CHECKLIST.md`
6. `09_ACCURACY_ENGINE/pcb_rules/USB_LAYOUT_RULES.md`
7. `09_ACCURACY_ENGINE/pcb_rules/POWER_LAYOUT_RULES.md`
8. `09_ACCURACY_ENGINE/pcb_rules/RF_LAYOUT_RULES.md`
9. `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`

## Preconditions

- Routing plan is `ROUTING_PLAN_READY`.
- Placement and zone setup pass.
- Backup is created.
- Connector-orientation audit is `PASS`.
- ESP32 antenna-orientation audit is `PASS` when applicable.

## Do

1. Route main power path, regulator critical loops, USB D+/D-, EN/BOOT if needed, decoupling, and ESD/protection nets only.
2. Use 45-degree bends for normal routing and avoid crude 90-degree or acute-angle geometry.
3. If local placement causes ugly routing, move only the local cluster needed to clean the route.
4. Refill zones only if the phase and user scope explicitly allow it.
5. Run DRC.
6. Export PCB visuals and close-up crops.
7. Inspect every routed critical trace, including angle quality and unnecessary via count.
8. Create `reports/PCB_CRITICAL_NETS_ROUTING_REPORT.md`.

## Required Result

Return one result:

- `CRITICAL_ROUTING_PASS`
- `CRITICAL_ROUTING_FAIL`
- `NEEDS_HUMAN_REVIEW`

AI quality closeout is required.
