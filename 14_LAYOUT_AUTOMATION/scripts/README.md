# Placement And Routing Automation Scripts

## Purpose

These scripts support deterministic PCB placement and routing planning before real KiCad board edits.

They work on normalized JSON constraints, placement proposals, routing fixtures, routing plans, and routing audit models. They do not edit KiCad files.

## Scripts

- `generate_placement_constraints.py`
  - Normalizes component metadata into staged placement constraints.
- `place_fixed_mechanical_parts.py`
  - Places mounting holes, edge connectors, and RF modules first.
- `place_component_groups.py`
  - Places functional groups around the fixed placements.
- `detect_placement_collisions.py`
  - Detects overlap, keepout intrusion, and edge-clearance violations.
- `score_component_placement.py`
  - Scores the resulting placement plan.
- `_routing_common.py`
  - Shared helpers for routing-plan and trace-audit scripts.
- `generate_routing_plan.py`
  - Builds a staged routing plan from a schema-aware routing fixture.
- `route_critical_nets_plan.py`
  - Extracts the critical-net-first route sequence from the routing plan.
- `detect_unrouted_nets.py`
  - Detects unrouted nets from a routing fixture.
- `detect_trace_keepout_violations.py`
  - Detects trace segments that cross keepouts, with RF/antenna hard-fail awareness.
- `trace_by_trace_audit.py`
  - Produces one audit entry per trace and flags geometry / via / keepout issues.
- `route_quality_common.py`
  - Shared geometry hard-fail helpers used by routing-audit and detector scripts.
- `routing_geometry_quality.py`
  - Runs the aggregate geometry hard-fail checker for right angles, acute jogs, poor pad entry, zigzags, detours, keepout crossings, unjustified vias, and width mismatches.
- `detect_right_angle_traces.py`
  - Detects right-angle trace geometry failures.
- `detect_acute_jogs.py`
  - Detects acute non-45 routing jogs.
- `detect_bad_pad_entry.py`
  - Detects poor critical-net pad-entry runout.
- `detect_unnecessary_zigzags.py`
  - Detects unnecessary zigzags and critical detours.
- `score_routing_plan.py`
  - Scores routing intent and routing audit outputs with hard-fail rules.
- `_kicad_pcb_bridge_common.py`
  - Shared read-only helpers for re-entering KiCad Python and normalizing board extraction output.
- `_kicad_pcb_bridge_extract.py`
  - Shared read-only extraction logic for board outline, footprints, pads, tracks, vias, zones, keepouts, nets, and net classes.
- `extract_kicad_nets_pads.py`
  - Extracts read-only footprint, pad, and net data from a real `.kicad_pcb`.
- `extract_kicad_tracks_vias.py`
  - Extracts read-only tracks, vias, and grouped trace records from a real `.kicad_pcb`.
- `extract_kicad_zones_keepouts.py`
  - Extracts read-only board outline, zones, and keepouts from a real `.kicad_pcb`.
- `extract_kicad_net_classes.py`
  - Extracts read-only net classes and default routing-rule values from a real `.kicad_pcb`.
- `extract_kicad_pcb_to_routing_schema.py`
  - Builds the full routing-engine input schema from a real `.kicad_pcb`.
- `run_real_board_routing_audit.py`
  - Runs extraction, optional DRC precheck, and the existing routing-plan/audit scripts on a copied real board.

## Typical Flow

1. Create project placement input JSON.
2. Run `generate_placement_constraints.py`.
3. Run `place_fixed_mechanical_parts.py`.
4. Run `place_component_groups.py`.
5. Run `detect_placement_collisions.py`.
6. Run `score_component_placement.py`.

Routing flow:

1. Create project routing input JSON using `ROUTING_INPUT_SCHEMA.md`.
2. Run `generate_routing_plan.py <fixture.json> <routing_plan.json> --markdown <routing_plan.md>`.
3. Run `route_critical_nets_plan.py <routing_plan.json> <critical_plan.json> --markdown <critical_plan.md>`.
4. Run `detect_unrouted_nets.py <fixture.json> <unrouted.json> --markdown <unrouted.md>`.
5. Run `detect_trace_keepout_violations.py <fixture.json> <keepouts.json> --markdown <keepouts.md>`.
6. Run `trace_by_trace_audit.py <fixture.json> <trace_audit.json> --markdown <trace_audit.md>`.
7. Run `routing_geometry_quality.py <fixture.json> <geometry.json> --markdown <geometry.md>`.
8. Run `score_routing_plan.py <fixture.json> <routing_plan.json> <critical_plan.json> <unrouted.json> <keepouts.json> <trace_audit.json> <score.json> --markdown <score.md>`.

Real-board bridge flow:

1. Use a copied `.kicad_pcb`, not an active production board.
2. Run `extract_kicad_pcb_to_routing_schema.py <board.kicad_pcb> <routing_schema.json> --markdown <routing_schema.md>`.
3. Optionally run the narrower extractors for targeted audits.
4. Run `run_real_board_routing_audit.py <board.kicad_pcb> <output_dir> --report-json <summary.json> --report-markdown <summary.md>`.
5. Treat all outputs as `REVIEW_ONLY`.

## Output Statuses

- `PASS`
- `AUTO_BLOCKED_MISSING_DATA`
- `AUTO_BLOCKED_BAD_LAYOUT`

## Hard Fail Coverage

The routing scorecard hard-fails when any of these are true:

- critical power net missing
- USB D+/D- incomplete
- trace crosses RF keepout
- trace crosses antenna keepout
- unrouted critical net
- GND strategy missing
- regulator critical loop not planned
- via used without reason on critical net
- trace-by-trace audit missing or incomplete
- right-angle geometry found
- acute non-45 jog found
- poor critical-net pad entry found
- unnecessary zigzag or critical detour found
- trace width mismatch found

## Boundary

These scripts are planning and precheck tools only. They do not prove final placement quality, routing quality, or fabrication readiness.
