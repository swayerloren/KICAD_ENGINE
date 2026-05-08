# Schematic Ready For PCB Checklist

## Purpose

Use this checklist before any PCB update, layout, routing, zone work, or manufacturing-style output. Every item must be resolved and evidenced in the project-level `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`.

## Gate Result

- Project:
- Schematic path:
- Gate reviewer:
- Review date:
- Gate result: `NOT_RUN`
- Evidence root:

Allowed final results:

- `PASS`
- `BLOCKED`
- `FAIL`
- `NOT_RUN`

## Required Checks

| # | Required check | Status | Evidence path | Human review required | Notes |
|---|---|---|---|---|---|
| 1 | `check_schematic_annotation.py` report exists and is `PASS`. | NOT_RUN |  | Yes if any `WARN` or `FAIL` remains |  |
| 2 | All references annotated; no `C?`, `R?`, `U?`, `D?`, `SW?`, `J?`, `TP?`, `MH?`, `F?`, or `Q?` remain. | NOT_RUN |  | Yes if any placeholder remains |  |
| 3 | No duplicate physical references, missing reference fields, blank values, or category/reference mismatches remain unresolved. | NOT_RUN |  | Yes if any checker finding remains |  |
| 4 | `check_schematic_completeness.py` report exists and required blocks are `PASS` or explicitly blocked. | NOT_RUN |  | Yes for any missing functional block |  |
| 5 | `check_bom_lock_alignment.py` report exists and expected BOM-lock references are present. | NOT_RUN |  | Yes for any missing or ambiguous BOM item |  |
| 6 | `check_needs_review_markers.py` report exists and no high-risk unresolved marker remains. | NOT_RUN |  | Yes for any marker on high-risk parts |  |
| 7 | ERC pass with report path. | NOT_RUN |  | Yes for any warning, error, waiver, or missing report |  |
| 8 | Full-page visual SVG/PDF evidence exists; PNG exists when a renderer is available. | NOT_RUN |  | Yes if missing or unreadable |  |
| 9 | `run_schematic_visual_check.ps1` or equivalent generated close-up crops from configured visual blocks. | NOT_RUN |  | Yes if crops missing or config incomplete |  |
| 10 | `CLOSE_UP_REVIEW.md` exists with one section per configured crop. | NOT_RUN |  | Yes if missing or incomplete |  |
| 11 | No visible unannotated references were detected in close-up crops. | NOT_RUN |  | Yes for any visible `?` reference |  |
| 12 | No visible footprint, library, or path fields in normal schematic view or close-up crops. | NOT_RUN |  | Yes if fields obscure review |  |
| 13 | Electrical audit pass. | NOT_RUN |  | Yes for any unresolved electrical concern |  |
| 14 | BOM lock audit pass. | NOT_RUN |  | Yes for any unlocked part |  |
| 15 | Component values match BOM lock or are intentionally marked `NEEDS_REVIEW`. | NOT_RUN |  | Yes for any mismatch |  |
| 16 | No unresolved `NEEDS_REVIEW` on high-risk parts. | NOT_RUN |  | Yes for any high-risk item |  |
| 17 | AO3401A symbol/footprint pin mapping resolved or explicitly blocked. | NOT_RUN |  | Yes |  |
| 18 | USB VBUS and shield policy resolved or explicitly blocked. | NOT_RUN |  | Yes |  |
| 19 | Power rail naming matches project standard. | NOT_RUN |  | Yes for mismatch |  |
| 20 | Regulator passives verified. | NOT_RUN |  | Yes for missing datasheet evidence |  |
| 21 | USB-C CC, ESD, and series resistor wiring verified. | NOT_RUN |  | Yes |  |
| 22 | ESP32 EN and BOOT verified. | NOT_RUN |  | Yes |  |
| 23 | All footprints assigned and verified to package drawings. | NOT_RUN |  | Yes for every unverified footprint |  |
| 24 | Connector orientation review complete. | NOT_RUN |  | Yes |  |
| 25 | Polarity-sensitive parts reviewed. | NOT_RUN |  | Yes |  |
| 26 | Human-review-required items listed. | NOT_RUN |  | Yes |  |

## Automatic Blockers

Mark the gate `BLOCKED` if any required check is `NOT_RUN`, `FAIL`, `EVIDENCE_MISSING`, `NEEDS_REVIEW`, or has missing evidence.

Mark the gate `BLOCKED` if any high-risk item requires human review and has not been reviewed.

## Evidence Rules

- Do not use memory as evidence for ERC, annotation, footprint, package drawing, connector orientation, or manufacturing readiness.
- Use file paths, command outputs, reports, screenshots, visual exports, datasheets, package drawings, or user-confirmed facts.
- Exact values, packages, pinouts, and connector drawings require source evidence.

## Approval Statement

Only write this statement when all checks pass:

`SCHEMATIC_TO_PCB_GATE_STATUS is PASS. PCB update from schematic is allowed only within the approved active project, after backup, with command logs and verification plan.`
