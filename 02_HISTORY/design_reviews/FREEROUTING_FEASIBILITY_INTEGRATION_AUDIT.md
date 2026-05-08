# FreeRouting Feasibility Integration Audit

Date: `2026-05-07`

## Scope

Repo workflow, sandbox scoring, routing-feasibility scripts, and startup handoff only. No KiCad schematic, PCB, or manufacturing files were edited.

## Files Created

- `14_LAYOUT_AUTOMATION/FREEROUTING_FEASIBILITY_INTEGRATION.md`
- `34_PCB_LAYOUT_SANDBOX/FREEROUTING_AS_VARIANT_SCORER.md`
- `03_TOOLS/scripts/routing_feasibility/README.md`
- `03_TOOLS/scripts/routing_feasibility/export_dsn_for_feasibility.ps1`
- `03_TOOLS/scripts/routing_feasibility/run_freerouting_dry_run.py`
- `03_TOOLS/scripts/routing_feasibility/import_route_result_for_review.py`
- `03_TOOLS/scripts/routing_feasibility/score_routing_feasibility.py`
- `03_TOOLS/scripts/routing_feasibility/parse_unrouted_and_vias.py`

## Files Updated

- `14_LAYOUT_AUTOMATION/README.md`
- `14_LAYOUT_AUTOMATION/INDEX.md`
- `34_PCB_LAYOUT_SANDBOX/PCB_VARIANT_WORKFLOW.md`
- `34_PCB_LAYOUT_SANDBOX/ROUTING_FEASIBILITY_RULES.md`
- `34_PCB_LAYOUT_SANDBOX/VARIANT_SCORING_RULES.md`
- `34_PCB_LAYOUT_SANDBOX/INDEX.md`
- `34_PCB_LAYOUT_SANDBOX/templates/VARIANT_SCORECARD_TEMPLATE.md`
- `01_MEMORY/DESIGN_RULES_MEMORY.md`
- `README_GPT.md`
- `FOR CHAT GPT.MD`

## Integration Summary

- FreeRouting is now defined as an optional routing-feasibility probe, not a final routing engine.
- The new workflow uses DSN export or staging, optional FreeRouting dry run, coarse metric parsing, feasibility scoring, and review-bundle staging.
- Every output remains `REVIEW_ONLY`.
- The routing-feasibility score may now cite FreeRouting dry-run evidence, but USB, RF, switching-regulator, and high-current nets remain human-review-required.
- The scripts are written to avoid touching the canonical `.kicad_pcb`.

## Validation

- Python syntax check passed for:
  - `run_freerouting_dry_run.py`
  - `import_route_result_for_review.py`
  - `score_routing_feasibility.py`
  - `parse_unrouted_and_vias.py`
- PowerShell parse check passed for:
  - `export_dsn_for_feasibility.ps1`
- Reference scan confirmed the new layer is recorded in sandbox rules, layout-automation docs, startup handoff docs, and durable design memory.
- Final KiCad hash recheck confirmed no changes to:
  - `ESP32_CSI_WIFI_NODE.kicad_pcb`
  - `ESP32_CSI_WIFI_NODE.kicad_sch`
  - `ESP32_CSI_WIFI_NODE.kicad_pro`

## Residual Risk

- The new scripts are syntax-checked but not yet proven by a first live dry run on a copied board candidate.
- DSN export remains partially manual because a universal verified headless KiCad Specctra export path is not assumed here.
- The integration is intentionally conservative and should stay that way unless future evidence proves a safer wider scope.
