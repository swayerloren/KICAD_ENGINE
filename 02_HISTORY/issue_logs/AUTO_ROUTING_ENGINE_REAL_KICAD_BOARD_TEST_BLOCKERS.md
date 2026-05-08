# AUTO_ROUTING_ENGINE_REAL_KICAD_BOARD_TEST_BLOCKERS

Status: `OPEN`

Date: `2026-05-07`

## Summary

The routing engine is now fixture-tested and materially more useful, but it is still blocked from a real KiCad board test.

## Exact Blockers

1. No exporter currently converts a real `.kicad_pcb` into `14_LAYOUT_AUTOMATION/ROUTING_INPUT_SCHEMA.md`.
2. No copied-board routing-state extractor currently populates trace, keepout, and net-class data automatically from KiCad.
3. `score_routing_plan.py` does not yet consume real-board DRC output.
4. Differential-pair quality is still approximated from fixture geometry rather than measured from KiCad board geometry.
5. The engine has not yet been run on a copied KiCad board with human review evidence.
6. Active project `ESP32_CSI_WIFI_NODE` remains blocked by upstream schematic/sandbox gates and is not a valid routing target.

## Next Step

Build a copied-board routing exporter for `.kicad_pcb` and run the routing engine on a non-production copied KiCad board with DRC evidence.
