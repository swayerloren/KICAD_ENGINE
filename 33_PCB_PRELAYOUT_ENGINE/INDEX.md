# PCB Prelayout Engine Index

## Files

- `README.md`: folder purpose and boundaries.
- `PCB_PRELAYOUT_ENGINE_WORKFLOW.md`: end-to-end workflow.
- `PCB_VARIANT_PLANNING_RULES.md`: required variant content and variant-count rule.
- `PCB_VARIANT_SCORING_RULES.md`: structured scoring and hard-fail rules.
- `PCB_DIGITAL_TWIN_SCHEMA.md`: board-twin data contract.
- `CONNECTOR_MECHANICAL_TRUTH_SCHEMA.md`: connector truth record contract.
- `TRACE_PROJECTION_RULES.md`: projected 45-degree route rules.
- `PLACEMENT_TO_ROUTING_FEASIBILITY_GATE.md`: final gate logic.
- `README_FOR_CODEX_AND_CLAUDE.md`: short agent-facing usage notes.
- `schemas/`: machine-readable JSON schemas used by the scripts.

## Role In The Repo

`33_PCB_PRELAYOUT_ENGINE/` is the deterministic engine layer.

`34_PCB_LAYOUT_SANDBOX/` remains the broader sandbox and approval workflow layer.

The prelayout engine feeds the sandbox with structured evidence. It does not replace schematic, footprint, live-state, DRC, or human-review gates.

