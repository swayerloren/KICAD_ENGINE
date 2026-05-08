# FreeRouting Feasibility Integration Needs First Live Dry Run

Date: `2026-05-07`

Status: `OPEN`

## Issue

The new FreeRouting routing-feasibility layer is documented and syntax-checked, but it has not yet been exercised on a real copied or sandbox board candidate.

## Why It Matters

- DSN export ergonomics may still need refinement.
- FreeRouting stdout/stderr formats may vary by version.
- SES via counting and congestion parsing may need small adjustments after first live evidence.

## Required Follow-Up

1. Use a copied or sandbox board candidate.
2. Stage or manually export a `.dsn`.
3. Run `run_freerouting_dry_run.py`.
4. Run `score_routing_feasibility.py`.
5. Record whether the metrics are stable enough for repeated variant scoring.

## Rule

Do not upgrade this layer from `REVIEW_ONLY` scope based on theory alone.
