# FreeRouting Feasibility Integration

Status: `OPTIONAL_REVIEW_ONLY_DESIGN`

## Purpose

Define an optional FreeRouting-based dry-run workflow that helps KiCad Engine compare layout variants, routing congestion, and obvious placement traps.

This integration is for feasibility scoring only. It is not final routing, not a replacement for engineering judgment, and not a permission slip to call a board professionally routed.

## Hard Position

- FreeRouting output is never final routing.
- Any autorouted result must be labeled `REVIEW_ONLY`.
- USB, RF, switching-regulator, and high-current paths still require human engineering review.
- Do not use this workflow to auto-approve USB, RF, power, or switching-node routing.
- Never overwrite a real `.kicad_pcb` without backup and explicit approval.

## Allowed Use

Use this integration to compare candidate layouts on:

- unrouted net count
- via count
- reported routed percentage
- congestion indicators
- obvious impossible placements
- coarse trace-length signals when the tool reports them

Use it as one input to the `routing_feasibility` category in sandbox variant scoring.

## Not Allowed

Do not use this integration to:

- declare final routing complete
- skip manual routing review
- skip DRC
- skip the sandbox variant workflow
- import a session into the canonical board by default
- approve USB D+/D-, RF feedlines, buck switch nodes, or high-current paths automatically

## Recommended Workflow

1. Finish sandbox variant reasoning first.
2. Select a candidate for deeper routing-feasibility probing.
3. Work only on a disposable or copied board representation, never the canonical board by default.
4. Export or stage a Specctra `.dsn` file for the candidate.
5. Run FreeRouting as a dry run.
6. Parse:
   - unrouted nets
   - via count
   - routed percentage
   - congestion hints
7. Convert those metrics into a `routing_feasibility` score.
8. Keep the result `REVIEW_ONLY`.
9. Require human review for any high-risk net class even when congestion looks good.

## Integration Modes

### Mode 1: Manual Projection Only

Default when no DSN exists or FreeRouting is unavailable.

Evidence source:

- human routing projection
- sandbox scorecard notes
- routing bottleneck review

### Mode 2: Dry-Run DSN Evaluation

Use a copied or disposable board candidate to export `.dsn`, run FreeRouting, and score congestion.

Evidence source:

- `.dsn`
- FreeRouting stdout/stderr
- generated `.ses`
- parsed metrics JSON
- routing-feasibility score JSON

### Mode 3: Review Bundle Staging

Stage the `.ses` and logs for human comparison without importing them into the real board.

Evidence source:

- staged `.ses`
- review manifest
- human review notes

## Current Script Surface

The first-party scripts for this layer live under:

- `03_TOOLS/scripts/routing_feasibility/export_dsn_for_feasibility.ps1`
- `03_TOOLS/scripts/routing_feasibility/run_freerouting_dry_run.py`
- `03_TOOLS/scripts/routing_feasibility/parse_unrouted_and_vias.py`
- `03_TOOLS/scripts/routing_feasibility/score_routing_feasibility.py`
- `03_TOOLS/scripts/routing_feasibility/import_route_result_for_review.py`

These scripts are designed to:

- stage or copy existing `.dsn` files safely
- run an optional dry-run FreeRouting command when Java or Docker is already available
- parse dry-run metrics
- score feasibility
- stage review artifacts without modifying the canonical board

## DSN Export Reality

KiCad Engine must not pretend that fully wired headless DSN export is already proven for every local KiCad build.

If local `kicad-cli` does not expose a verified Specctra export path, the workflow falls back to:

- a manually exported `.dsn`, or
- an already existing sibling `.dsn`

That fallback is acceptable for feasibility work because the goal is comparison, not final production routing.

## Output Labels

Every generated artifact from this workflow must remain visibly labeled:

- `REVIEW_ONLY`
- `NOT_FINAL`
- `HUMAN_REVIEW_REQUIRED` when high-risk nets or unclear geometry remain

## Variant-Scoring Relationship

FreeRouting dry-run evidence is optional support for the sandbox `routing_feasibility` score.

It should influence questions such as:

- Does this placement force too many vias?
- Does this placement leave many nets unrouted?
- Does the projected channel structure look congested?
- Does the candidate appear mechanically plausible but electrically awkward?

It must not override:

- connector-orientation evidence
- RF keepout evidence
- power-path reasoning
- switching-loop review
- human visual review

## Review Gate

The workflow is only useful when the following statement remains true:

`A good FreeRouting congestion result does not equal acceptable final routing quality.`

If that boundary is removed, this integration becomes a liability rather than a useful review aid.
