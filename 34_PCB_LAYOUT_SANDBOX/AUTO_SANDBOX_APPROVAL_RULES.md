# Auto Sandbox Approval Rules

## Purpose

Replace generic manual approval requests with an evidence-based gate for starting real PCB work.

## Hard Rule

Do not ask LJ for generic sandbox approval when the evidence can answer the question.

The sandbox must either:

- produce `AUTO_APPROVED_FOR_PCB_WORK`, or
- produce an `AUTO_BLOCKED_*` report with exact missing items or failing checks

## Auto-Approval Preconditions

Real PCB update, placement, or other board-edit work may proceed only when all of these are true:

1. schematic gate is `PASS`
2. ERC is `PASS`
3. schematic annotation is KiCad-native verified
4. every physical component has a footprint
5. high-risk footprints have exact part/package evidence or are marked safe candidate with documented source
6. connector orientation is known
7. board shape and dimensions are defined
8. antenna keepout is defined if an RF module exists
9. at least three layout variants were generated
10. a variant scorecard exists
11. the selected variant has no hard fails
12. routing-feasibility check passes
13. no DRC or precheck blocker exists
14. an auto-approval report exists

## Blocking Rule

If any precondition is not satisfied:

- do not ask LJ for generic approval
- do not mark the sandbox gate `PASS`
- do not touch the real `.kicad_pcb`
- create or update an auto-blocked report that lists the exact failing or missing items

## Human Review Rule

Human review is still allowed and often useful, but it is no longer a mandatory generic approval step.

Human review becomes required only when:

- a hard fail cannot be resolved objectively
- a high-risk footprint remains unverified
- connector orientation is still not mechanically defensible
- enclosure or dimensional facts are missing
- RF keepout or service-space evidence remains ambiguous
- routing-feasibility evidence is inconclusive on a high-risk path

