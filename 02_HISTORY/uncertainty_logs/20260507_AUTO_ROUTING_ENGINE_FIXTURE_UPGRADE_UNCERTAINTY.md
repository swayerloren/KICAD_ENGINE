# Uncertainty Log

Session: `AUTO_ROUTING_ENGINE_FIXTURE_UPGRADE`

Date: `2026-05-07`

## Uncertainties

1. The routing engine has not yet processed a copied real KiCad board.
2. The scorecard still estimates USB pair quality and DRC risk from fixture data rather than from KiCad board geometry and DRC output.

## Risk Level

`MEDIUM`

## Required Evidence

- copied-board routing exporter
- real-board DRC-coupled scoring
- first copied-board live routing-engine run

## Human Review Required

`YES`

## Issue Tracking

- `02_HISTORY/issue_logs/AUTO_ROUTING_ENGINE_REAL_KICAD_BOARD_TEST_BLOCKERS.md`
