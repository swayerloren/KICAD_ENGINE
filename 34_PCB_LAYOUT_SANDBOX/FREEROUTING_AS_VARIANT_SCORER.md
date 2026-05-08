# FreeRouting As Variant Scorer

Status: `OPTIONAL_SUPPORTING_EVIDENCE`

## Purpose

Show how FreeRouting dry-run output can support sandbox variant comparison without becoming the primary routing decision-maker.

## Core Rule

FreeRouting is a feasibility probe, not a final routing engine for KiCad Engine.

Use it to help score:

- routing congestion
- unrouted-net pressure
- via pressure
- coarse trace-length pressure
- placement plausibility

Do not use it to approve:

- USB D+/D-
- RF paths
- buck switch-node routing
- high-current routes
- production routing quality

## When To Use It

Use FreeRouting scoring only after a variant has enough placement definition that a `.dsn` meaningfully represents the candidate.

That means the candidate already has:

- board outline assumption
- connector edge plan
- module orientation
- major component clusters
- keepouts
- projected critical paths

If those conditions are missing, use manual routing-feasibility scoring only.

## Scoring Role

The sandbox `routing_feasibility` category remains `0-10`.

FreeRouting dry-run output can inform that number with evidence such as:

- `0` if the run exposes obvious impossible routing
- `3-5` if many nets remain unrouted or via pressure is high
- `6-7` if the board is mostly routable but still crowded
- `8-10` if congestion looks manageable and the major channels remain plausible

Even with a high `routing_feasibility` score:

- overall variant status may still be `NEEDS_HUMAN_REVIEW`
- high-risk nets still require explicit engineering review
- selected-variant approval is still blocked until LJ review when required

## Evidence Levels

### Level 0: Manual Projection Only

Use when:

- no DSN exists
- FreeRouting is unavailable
- the candidate is too rough for a meaningful dry run

Allowed result:

- manual `routing_feasibility` score with explanation

### Level 1: Dry-Run Congestion Evidence

Use when:

- a sandbox or copied board candidate exists
- a `.dsn` exists
- FreeRouting can run locally

Allowed result:

- `routing_feasibility` score supported by unrouted-net, via, and congestion evidence

### Level 2: Review Bundle

Use when:

- the team wants side-by-side review artifacts
- a `.ses` file and run logs exist

Allowed result:

- stronger human comparison evidence
- still `REVIEW_ONLY`

## Required Warnings In Variant Reports

When FreeRouting evidence is used, the variant report must say:

- `FreeRouting dry-run result is REVIEW_ONLY.`
- `USB, RF, switching regulator, and high-current routing still require human review.`
- `This evidence supports routing-feasibility scoring only; it does not approve final routing quality.`

## Suggested Scorecard Fields

Add the following optional fields to the machine-readable scorecard when FreeRouting evidence exists:

```json
{
  "routing_feasibility_evidence_mode": "MANUAL_ONLY | FREEROUTING_DRY_RUN",
  "freerouting_review_only": true,
  "freerouting_run_status": "UNAVAILABLE | COMPLETED | ERROR | TIMEOUT",
  "freerouting_routed_pct": 0.0,
  "freerouting_unrouted_net_count": 0,
  "freerouting_via_count": 0,
  "freerouting_congestion_mentions": 0
}
```

These fields inform the `routing_feasibility` score. They do not replace the existing sandbox hard-fail checks.
