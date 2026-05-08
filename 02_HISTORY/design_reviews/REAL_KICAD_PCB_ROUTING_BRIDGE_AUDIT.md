# Real KiCad PCB Routing Bridge Audit

Date: `2026-05-07`

## Objective

Add the missing read-only bridge from a real copied `.kicad_pcb` into the routing-engine schema so the routing engine can be tested on actual KiCad boards without touching the active project.

## What Was Added

- real-board extraction helpers under `14_LAYOUT_AUTOMATION/scripts/`
- narrow extractors for nets/pads, tracks/vias, zones/keepouts, and net classes
- full-schema extractor for `ROUTING_INPUT_SCHEMA.md`
- copied-board audit runner that couples extraction with `kicad-cli pcb drc --format json`
- copied-board test workspace under `14_LAYOUT_AUTOMATION/real_board_tests/`

## Evidence

- `14_LAYOUT_AUTOMATION/reports/REAL_KICAD_BOARD_EXTRACTION_TEST_REPORT.md`
- `14_LAYOUT_AUTOMATION/real_board_tests/reports/esp_rust_board_summary.md`
- `14_LAYOUT_AUTOMATION/real_board_tests/outputs/esp_rust_board/`

## Findings

1. The bridge is real and useful.
   It reads copied `.kicad_pcb` boards, enters KiCad Python when needed, extracts routing-schema JSON, runs copied-board DRC, and feeds the existing routing audit stack.

2. The first zone/keepout classification rule was too broad.
   `HasKeepoutParametersSet()` is not a safe proxy for a real keepout. On copied sample boards it returned truthy on ordinary copper zones. This was corrected by restricting extracted keepouts to explicit KiCad rule areas and recording the ambiguous API behavior as `NOT_EXTRACTED`.

3. The copied-board audit now fails for meaningful reasons instead of bridge noise.
   After the keepout correction, the sample copied board blocks on routing-plan and trace-audit criteria, not fake keepout crossings.

4. The bridge does not make the engine ready for active-project routing by itself.
   Important extraction gaps remain, especially per-net ratsnest status, via intent, and richer planning semantics on real boards.

## Decision

- Bridge implementation quality: `PASS`
- Copied-board live-test readiness: `PASS`
- Active-project routing readiness: `FAIL`

## Required Next Steps

- add per-net ratsnest / unrouted extraction if KiCad API support can be made reliable
- add richer keepout semantics for rule areas and special restrictions
- improve downstream real-board planning heuristics for regulator-loop recognition and trace-audit triage
- run the bridge on an approved copied project that is closer to the eventual target board
- keep active-project routing blocked until all real-project routing preconditions are exact `PASS`
