# 13 Routing Plan Only

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: create a routing plan before any traces are routed. Do not edit PCB.

## Read First

1. `AGENTS.md`
2. `reports/PCB_PLACEMENT_PASS_2_ORIENTATION_REPORT.md`
3. `reports/COPPER_ZONE_STRATEGY_REPORT.md`
4. `09_ACCURACY_ENGINE/pcb_rules/USB_LAYOUT_RULES.md`
5. `09_ACCURACY_ENGINE/pcb_rules/POWER_LAYOUT_RULES.md`
6. `09_ACCURACY_ENGINE/pcb_rules/RF_LAYOUT_RULES.md`
7. `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`
8. Latest connector-orientation audit result
9. Latest ESP32 antenna-orientation audit result when an ESP32 RF module is present

## Preconditions

- Placement orientation audit passed.
- No required connector remains `NEEDS_HUMAN_REVIEW`.
- ESP32 antenna orientation is proven or the project is blocked.

## Do

1. Define net classes, trace width, clearance, via strategy, power priority, GND return strategy, USB routing, RF keepout, switch-node constraints, decoupling loops, no-go areas, route order, DRC checks, and visual checks.
2. Mark unknown values as blocked instead of guessing.
3. Create `reports/PCB_ROUTING_PLAN.md`.

## Required Result

Return one result:

- `ROUTING_PLAN_READY`
- `ROUTING_PLAN_BLOCKED`

AI quality closeout is required.
