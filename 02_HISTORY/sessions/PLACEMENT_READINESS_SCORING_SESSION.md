# Placement Readiness Scoring Session

Date: `2026-05-08`

Branch: `hardening/execution-contract`

Task type: `DOCS_ONLY`

## Scope

Implement placement-readiness scoring and wire it into routing preconditions
without editing KiCad design files.

## Completed

- added a real-board placement-readiness rule file
- added a read-only placement readiness scorer
- added connector, power, USB, antenna, and test-pad placement detectors
- extended placement common helpers to extract live board geometry from KiCad
  Python
- updated routing preconditions, routing workflow, and the full pipeline
  checklist to require exact placement-readiness proof before routing
- ran the scorer on a copied `ESP32_CSI_WIFI_NODE` board
- wrote the active-project `PLACEMENT_READINESS_SCORECARD.md`

## Validation Result

- copied board status: `PLACEMENT_READY_FOR_ROUTING`
- copied board score: `98 / 100`
- hard fails: `_none_`
- warning: `regulator -> output_cluster spacing is looser than preferred (13.60 mm).`

## Safety

- no `.kicad_sch` edits
- no `.kicad_pcb` edits
- no routing
- no manufacturing outputs
