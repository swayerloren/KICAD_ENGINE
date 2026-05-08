# 11 Holes Pads Vias Strategy

You are working in:

`[REPO_ROOT]`

ACTIVE PROJECT:

`[ACTIVE_PROJECT_PATH]`

Task: build and verify the mounting-hole, test-pad, and via strategy before routing. Do not route traces.

## Read First

1. `AGENTS.md`
2. `reports/PCB_PLACEMENT_PASS_2_ORIENTATION_REPORT.md`
3. `09_ACCURACY_ENGINE/pcb_rules/PCB_CREATION_STANDARD.md`
4. `24_FAB_PROFILES/00_INDEX/FAB_PROFILE_SCHEMA.md` if present
5. `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`

## Do

1. Create backup.
2. Verify mounting-hole count, diameter, plated status, clearance, positions, and GND/isolation policy.
3. Verify test-pad count, size, spacing, accessibility, and side.
4. Define signal, power, stitching, and thermal via rules from fab constraints and design evidence.
5. Define ground stitching strategy.
6. Run DRC and visual close-up review.
7. Create `reports/THROUGH_HOLE_TEST_PAD_VIA_STRATEGY.md`.

## Required Result

Return one result:

- `HOLE_PAD_VIA_PASS`
- `HOLE_PAD_VIA_FAIL`
- `NEEDS_HUMAN_REVIEW`

AI quality closeout is required.

