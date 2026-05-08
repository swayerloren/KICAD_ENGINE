# 12 Copper Zones Setup

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: set up copper zones and ground-plane strategy before routing. Do not complete routing.

## Read First

1. `AGENTS.md`
2. `reports/THROUGH_HOLE_TEST_PAD_VIA_STRATEGY.md`
3. `09_ACCURACY_ENGINE/pcb_rules/GROUND_PLANE_RULES.md`
4. `09_ACCURACY_ENGINE/pcb_rules/POWER_LAYOUT_RULES.md`
5. `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`

## Do

1. Create backup.
2. Confirm board outline, placement, hole/via strategy, and route-critical keepouts.
3. Define GND zones, priorities, thermal relief, antenna/USB/mechanical keepouts, and justified power copper areas.
4. Refill zones.
5. Run DRC.
6. Export zone visuals and close-up review.
7. Create `reports/COPPER_ZONE_STRATEGY_REPORT.md`.

## Required Result

Return one result:

- `ZONE_SETUP_PASS`
- `ZONE_SETUP_FAIL`
- `NEEDS_HUMAN_REVIEW`

AI quality closeout is required.

