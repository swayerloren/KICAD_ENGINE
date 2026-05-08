# Real KiCad Board Extraction Test Report

Date: `2026-05-07`

Scope: build and validate the read-only `.kicad_pcb` to routing-engine bridge on a copied board, without touching the active project.

## Scripts Created

- `14_LAYOUT_AUTOMATION/scripts/_kicad_pcb_bridge_common.py`
- `14_LAYOUT_AUTOMATION/scripts/_kicad_pcb_bridge_extract.py`
- `14_LAYOUT_AUTOMATION/scripts/extract_kicad_nets_pads.py`
- `14_LAYOUT_AUTOMATION/scripts/extract_kicad_tracks_vias.py`
- `14_LAYOUT_AUTOMATION/scripts/extract_kicad_zones_keepouts.py`
- `14_LAYOUT_AUTOMATION/scripts/extract_kicad_net_classes.py`
- `14_LAYOUT_AUTOMATION/scripts/extract_kicad_pcb_to_routing_schema.py`
- `14_LAYOUT_AUTOMATION/scripts/run_real_board_routing_audit.py`

## Extraction Fields Supported

- board path
- board outline from `Edge.Cuts` geometry
- footprint list
- component placement metadata
- pad list
- net list
- grouped trace records
- raw track segments
- via list
- zone list
- explicit keepout list when KiCad rule-area geometry is present
- net-class extraction from board design settings
- default width / clearance / layer-rule normalization into routing schema
- total unconnected-item count from KiCad connectivity
- copied-board DRC JSON ingestion through `kicad-cli`
- Markdown and JSON outputs for narrow extractors and full-board audit

## Extraction Fields Not Supported Or Still Partial

- per-net ratsnest / unrouted count is `NOT_EXTRACTED`
- via engineering intent / justification is `NOT_EXTRACTED`
- full rule-area semantic extraction beyond explicit rule-area polygons is partial
- blind / buried / microvia-specific strategy extraction is not yet normalized into routing rules
- differential-pair quality metrics are still downstream audit logic, not native PCB extraction facts
- regulator-critical-loop recognition still depends on planning heuristics after extraction

## Copied-Board Test Input

Test board:

- `32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/esp_rs_esp_rust_board/hardware/esp-rust-board/esp-rust-board.kicad_pcb`

Outputs:

- `14_LAYOUT_AUTOMATION/real_board_tests/outputs/esp_rust_board/`
- `14_LAYOUT_AUTOMATION/real_board_tests/reports/esp_rust_board_summary.md`

## Validation Results

- Python syntax check: `PASS`
- Read-only schema extraction on copied board: `PASS`
- Read-only copied-board DRC JSON run: `PASS`
- Copied-board routing audit pipeline: `PASS` as a bridge test

Important distinction:

The bridge test passed because the extractor and audit pipeline ran successfully end to end on a copied board. The copied board itself was not approved for routing quality.

## Copied-Board Audit Summary

- Extracted nets: `63`
- Extracted grouped traces: `34`
- Extracted raw vias: `216`
- Extracted zones: `8`
- Extracted explicit keepouts: `0`
- KiCad connectivity unconnected count: `0`
- DRC violations from copied board: `81`
- DRC unconnected items from copied board: `0`

Audit status:

- `AUTO_BLOCKED_BAD_LAYOUT`

Audit blockers:

- `26 trace audit entries flagged`
- `regulator critical loop not planned`
- `routing plan did not pass`

## Important Extraction Correction

The first bridge pass over-classified ordinary copper zones as keepouts because KiCad zone objects expose keepout-style parameter getters even when the zone is not a rule area.

The bridge now treats only explicit KiCad rule areas as extracted keepouts. Non-rule-area zones that still expose keepout-style API flags are recorded in `not_extracted` notes and remain `COPPER_ZONE`.

## Readiness Decision

- Routing engine ready for copied-board live test: `YES`
- Routing engine ready for active project routing: `NO`

## Exact Remaining Blockers Before Active-Project Routing

- per-net ratsnest / unrouted extraction is still missing
- via-intent extraction is still missing
- richer keepout / rule-area semantics are still partial
- downstream routing-plan logic still blocks boards that lack critical-loop planning evidence
- no active-project-specific copied-board run has been reviewed against the real project gates
- active project `ESP32_CSI_WIFI_NODE` remains blocked by upstream project gates and is not a valid routing target

## KiCad File Safety

No `ESP32_CSI_WIFI_NODE` KiCad design files were modified in this task.
