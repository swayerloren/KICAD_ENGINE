# Accuracy Engine Checklists

Status: `MANDATORY_GATE_CHECKLISTS`

This folder contains the checklists that keep KiCad Engine from moving too quickly from idea to schematic, PCB, routing, or fabrication output. A checklist is not a substitute for ERC, DRC, source review, or human review; it is the control surface that makes those checks explicit.

## Required Use By Workflow

| Workflow Stage | Required Checklist | Blocks If |
| --- | --- | --- |
| Requirements and block planning | `PRE_SCHEMATIC_CHECKLIST.md` | Required function, power input, external connector, source document, or risk class is unknown. |
| Schematic edits | `ACCURACY_GATE_CHECKLIST.md` and schematic-specific checklists | Symbols, pinouts, rails, connector pin numbering, or high-risk parts lack evidence. |
| Schematic-to-PCB transition | `SCHEMATIC_READY_FOR_PCB_CHECKLIST.md` | Annotation, ERC, visual review, electrical audit, BOM lock, footprint audit, or `NEEDS_REVIEW` blockers remain open. |
| PCB update | `PCB_UPDATE_FROM_SCHEMATIC_CHECKLIST.md` | Gate status is not `PASS` or stale footprints are unresolved. |
| PCB placement/routing | Placement, routing, and review checklists | Connector orientation, polarity, keepouts, net classes, or DRC evidence is missing. |
| Fabrication review exports | `FULL_PIPELINE_GATE_CHECKLIST.md` plus fab rules | Outputs would be unlabeled, unreviewed, or treated as final. |

## Checklist Entry Format

Use this structure for new checklist rows:

| Field | Required | Example |
| --- | --- | --- |
| `check_id` | Yes | `SCH-USB-CC-001` |
| `check` | Yes | Verify USB-C CC resistor role and value from design requirement/source. |
| `evidence_required` | Yes | Datasheet/source link, schematic net, command output, or visual crop. |
| `status` | Yes | `PASS`, `FAIL`, `NEEDS_REVIEW`, `NOT_APPLICABLE`, or `TODO_SOURCE_REQUIRED`. |
| `blocks_next_stage` | Yes | `true` for any high-risk or required item. |
| `notes` | Yes | Include report path or unresolved decision. |

## What Belongs Here

- Reusable checklists for agent workflows.
- Stage gates for schematic, PCB, routing, and fab review.
- Evidence requirements and pass/fail criteria.
- Human-review triggers.

## What Does Not Belong Here

- KiCad project files, screenshots, raw ERC/DRC output, generated fab packages, or datasheet PDFs.
- Project-specific checklist results. Store those under the project `reports/` or `history/verification_runs/` folder.
- Generic advice that does not block or permit a next action.

## Agent Rule

If a checklist says an item blocks the next stage, the agent must stop, record the blocker, and report it. Do not bypass a checklist by calling the work "draft" unless the user explicitly approves a documented exception.
