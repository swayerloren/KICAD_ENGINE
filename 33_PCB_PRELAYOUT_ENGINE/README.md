# PCB Prelayout Engine

## PURPOSE

`33_PCB_PRELAYOUT_ENGINE/` is the deterministic pre-PCB-planning engine for KiCad Engine.

It turns a read-only KiCad board or project state into:

- a board digital twin
- connector mechanical truth records
- multiple placement variants
- 45-degree route projections
- comparable variant scores
- one explicit prelayout gate result

This layer exists to stop bad real-board work from starting just because a board fits mechanically or a partial DRC snapshot looks quiet.

## WHAT_BELONGS_HERE

- Engine workflow rules
- Digital-twin and connector-truth schemas
- Variant-generation and scoring rules
- Placement-to-routing feasibility gate rules
- Agent-facing usage notes

## WHAT_DOES_NOT_BELONG_HERE

- Real `.kicad_pcb` edits
- Real `.kicad_sch` edits
- Routing passes
- Copper zones
- Fab outputs

## AI_AGENT_RULES

- Do not start real PCB placement until the engine has generated at least three variants and the latest gate result records `placement_gate_status: PASS`.
- Do not start real PCB routing until the latest gate result records both `placement_gate_status: PASS` and `routing_gate_status: PASS`.
- At least one variant must score `PASS` before real PCB work may continue.
- Treat connector direction, edge use, and mating-side proof as first-order facts, not cleanup items.
- Treat projected open nets as blockers even when a current DRC snapshot has zero geometry violations.
- Treat live-board open-net evidence as a routing blocker even if one planning variant passes.
- Treat this engine as an upstream gate that feeds the existing `34_PCB_LAYOUT_SANDBOX/` workflow; it adds a stricter pre-placement/pre-routing stop layer and does not replace existing sandbox, phase, or DRC gates.

## SAFE_EDIT_RULES

- This folder is source and rules only.
- Project-specific outputs belong in the active project's `reports/` folder.
- Scripts using this layer must remain read-only by default.
- Preserve evidence that shows a board is blocked; do not backfill fake passing variants.

## PUBLIC_RELEASE_NOTES

- This layer is planning and gating automation, not proof of full auto-layout.
- Connector truth, keepout reasoning, and projected-route scoring still require human review for high-risk boards.
