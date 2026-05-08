# Failed Attempt - Routing Geometry Integration Fixture Context Miss

Date: `2026-05-08`

## What Failed

The first end-to-end integration run used a minimal `good_45_degree_route`
fixture that passed the geometry checker but failed the routing-plan stage for
an unrelated reason: `regulator critical loop not planned`.

## Why It Failed

The existing routing-plan workflow requires a regulator-loop role to avoid an
upstream blocked state. The initial geometry-only fixture did not include that
minimum plan context.

## Fix Applied

Added a clean `BUCK_SW` net and straight routed trace to the geometry fixtures
so the integration path could isolate geometry acceptance instead of failing on
missing-plan context.

## Result After Fix

The good fixture then passed the full routing-plan -> trace-audit -> scorecard
path, while the bad 90-degree fixture failed on `RIGHT_ANGLE_FOUND` as
intended.
