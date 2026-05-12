# PCB Layout Style Examples

Status: `REFERENCE_COMPARISON_ONLY`

## Purpose

Define how Codex and Claude should compare placement and routing style against
real human-made KiCad boards.

## Compare These Things

- board size ranges
- connector edge placement
- clustering of USB, power, RF, debug, and user-interface circuits
- routing-angle tendencies
- via pressure
- zone usage strategy
- USB route compactness
- power-path compactness

## Do Not Compare By

- DRC result alone
- board shape alone
- number of vias alone
- whether a board looks "dense"

## Safe Use

Sample comparison may inform routing and placement review language, but it does
not override:

- connector orientation truth
- RF keepout rules
- project-specific mechanical constraints
- prelayout gating
- live DRC and geometry audit results
