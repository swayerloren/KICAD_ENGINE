# Library QA

Status: `AI_GUIDANCE_ONLY`

## Purpose

This folder defines cross-cutting quality checks for symbols, footprints, mappings, 3D model references, and project-local library use. QA records should make it clear what was checked, what evidence was used, and what remains blocked.

## Required QA Result Fields

| Field | Required | Guidance |
| --- | --- | --- |
| `item_type` | Yes | `symbol`, `footprint`, `symbol_footprint_mapping`, `3d_model`, or `library_table`. |
| `item_path` | Yes | Repo-relative or KiCad library identifier. |
| `part_number` | Yes when exact | Use `generic_placeholder` only for true generic parts. |
| `source_evidence` | Yes | Datasheet, package drawing, KiCad file inspection, command output, or user confirmation. |
| `checks_performed` | Yes | Pinout, pad numbers, courtyard, fab outline, fields, model path, etc. |
| `result` | Yes | `PASS`, `FAIL`, `NEEDS_REVIEW`, or `UNVERIFIED`. |
| `human_review_required` | Yes | True for high-risk categories until reviewed. |
| `next_action` | Yes | Concrete fix or verification step. |

## What Belongs Here

- QA workflow rules.
- Review status definitions.
- Evidence requirements.
- Script-use guidance.
- Templates for manual QA summaries.

## What Does Not Belong Here

- Active KiCad source files.
- Installed KiCad global libraries.
- User-global library tables.
- Fabrication outputs.
- Raw generated script output without a review summary.

## Agent Rules

- Treat script results as warnings and evidence, not approval.
- Keep symbol, footprint, mapping, package drawing, and 3D model statuses separate.
- Require human review for connectors, polarity, RF, USB, CAN, high-current parts, and mechanical fit.
- Do not edit project-local libraries without active project confirmation, backup, rollback plan, and verification plan.
- Do not modify installed KiCad global libraries or user global library tables.

## Approval Rule

No library item is production-approved until the QA record links to evidence and the exact unresolved risks are closed or explicitly accepted by a human.
