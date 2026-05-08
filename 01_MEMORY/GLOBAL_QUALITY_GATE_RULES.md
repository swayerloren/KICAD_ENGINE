# Global Quality Gate Rules

Status: `ACTIVE_GLOBAL_MEMORY`

Global quality-gate rules for AI-assisted KiCad work.

## Blockers

The agent must mark work `BLOCKED_UNTIL_HUMAN_REVIEW` if:

- exact footprint is not verified,
- connector orientation is not verified,
- datasheet source is missing,
- ERC/DRC was required but not run,
- manufacturing output was generated but not reviewed,
- KiCad design files changed without backup,
- pinout was inferred but not verified,
- source conflicts exist,
- AI is uncertain about a high-risk electrical/mechanical decision.

## Closeout Rule

Every meaningful session must create an AI self-review, response scorecard, claim/evidence matrix, and uncertainty/risk logs as needed.

## Full KiCad Pipeline Rule

Status: `STANDARD_CREATED_NOT_PROJECT_PROVEN`

Future KiCad projects must follow `.prompts/kicad_pipeline/`, `00_CODEX_START/KICAD_PIPELINE_STARTUP_RULES.md`, `09_ACCURACY_ENGINE/workflows/FULL_KICAD_PROJECT_PIPELINE.md`, and `09_ACCURACY_ENGINE/checklists/FULL_PIPELINE_GATE_CHECKLIST.md` from schematic annotation through NOT_FINAL fabrication export unless the user explicitly approves an exception.

Every exception must be logged with affected gate, approval evidence, reason, risk, evidence path, and `HUMAN_REVIEW_REQUIRED`.

## Supplier Ingestion Quality Rule

Status: `ACTIVE_GLOBAL_RULE`

Supplier/distributor stock, pricing, lifecycle, supplier SKU, package text, and availability are time-sensitive metadata. Agents must use official APIs first, user-provided CSV exports second, and manual source-link records third. Blind scraping, credential storage, and footprint approval from supplier package text are forbidden.

All unreviewed supplier records remain `UNVERIFIED` and require source date plus source URL or source file before they can support BOM or purchasing decisions.

## Connector Orientation Quality Rule

Status: `ACTIVE_GLOBAL_RULE`

Connector edge orientation is a mechanical quality gate. Do not approve connector orientation from coordinates alone.

- Horizontal DC barrel jack: female circular opening is the front/mating side; 3-pin solder-leg side is the rear/back side. Edge placement requires the female opening off-board and solder/back side inward.
- Bottom-edge barrel jack: female opening faces down/off-board; 3-pin solder side faces up/inward.
- USB-C receptacle: mouth/opening must face off-board; bottom-edge mouth faces down/off-board; footprint `PCB Edge` indicator must align with board `Edge.Cuts`; pads remain on-board.
- Required evidence: exact 3D model when available, footprint `F.Fab`/`F.SilkS`/`F.CrtYd` geometry, and manufacturer drawing or product image for ambiguous connectors.
- If evidence is missing, mark `BLOCKED_UNTIL_HUMAN_REVIEW` or the connector-specific blocker such as `BLOCKED_BY_BARREL_JACK_ORIENTATION_EVIDENCE`.

## 2026-05-07 Report Status Header Rule

Status: `ACTIVE_EVIDENCE`

Every meaningful report should include a status header with status, generated date/time, project, supersedes, superseded by, evidence files, and current relevance. Missing headers do not invalidate old history, but future current-truth maintenance must classify old files externally.

## 2026-05-07 PCBA Export Quality Gate

Status: `ACTIVE_GLOBAL_RULE`

JLCPCB and PCBWay upload packages remain blocked unless the final PCB/export gates pass. Required evidence includes DRC with schematic parity, no-unrouted-net proof, validated fab-house-specific BOM and placement files, assembly notes, orientation checks, external Gerber-viewer review, connector orientation proof, pin 1 proof, and polarity proof.

Universal BOM/PNP files are internal review aids only. They do not replace JLCPCB BOM/CPL or PCBWay BOM/centroid formats.

Manufacturing outputs remain `NOT_FINAL` until LJ approves.
