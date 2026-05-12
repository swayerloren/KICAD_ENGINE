# Schematic Ready For PCB Checklist

## Purpose

Use this checklist before any PCB update, layout, routing, zone work, or
manufacturing-style output. Every item must be resolved and evidenced in the
project-level `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`.

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
| 9 | `03_TOOLS/scripts/schematic_layout/render_schematic_review_pages.py` or equivalent produced a schematic layout review packet. | NOT_RUN |  | Yes if missing |  |
| 10 | `09_ACCURACY_ENGINE/checklists/SCHEMATIC_VISUAL_READABILITY_CHECKLIST.md` was reviewed and does not fail. | NOT_RUN |  | Yes for any fail |  |
| 11 | Schematic readability score exists and is not `FAIL`. | NOT_RUN |  | Yes for any `FAIL` score |  |
| 12 | Visual-flow audit does not fail. | NOT_RUN |  | Yes for any flow failure |  |
| 13 | Local wire usage audit does not fail. | NOT_RUN |  | Yes for label-heavy local blocks |  |
| 14 | `run_schematic_visual_check.ps1` or equivalent generated close-up crops from configured visual blocks. | NOT_RUN |  | Yes if crops missing or config incomplete |  |
| 15 | `CLOSE_UP_REVIEW.md` exists with one section per configured crop. | NOT_RUN |  | Yes if missing or incomplete |  |
| 16 | No visible unannotated references were detected in close-up crops. | NOT_RUN |  | Yes for any visible `?` reference |  |
| 17 | No visible footprint, library, or path fields in normal schematic view or close-up crops. | NOT_RUN |  | Yes if fields obscure review |  |
| 18 | Electrical audit pass. | NOT_RUN |  | Yes for any unresolved electrical concern |  |
| 19 | BOM lock audit pass. | NOT_RUN |  | Yes for any unlocked part |  |
| 20 | Component values match BOM lock or are intentionally marked `NEEDS_REVIEW`. | NOT_RUN |  | Yes for any mismatch |  |
| 21 | No unresolved `NEEDS_REVIEW` on high-risk parts. | NOT_RUN |  | Yes for any high-risk item |  |
| 22 | AO3401A symbol/footprint pin mapping resolved or explicitly blocked. | NOT_RUN |  | Yes |  |
| 23 | USB VBUS and shield policy resolved or explicitly blocked. | NOT_RUN |  | Yes |  |
| 24 | Power rail naming matches project standard. | NOT_RUN |  | Yes for mismatch |  |
| 25 | Regulator passives verified. | NOT_RUN |  | Yes for missing datasheet evidence |  |
| 26 | USB-C CC, ESD, and series resistor wiring verified. | NOT_RUN |  | Yes |  |
| 27 | ESP32 EN and BOOT verified. | NOT_RUN |  | Yes |  |
| 28 | Latest `run_footprint_package_gate.py` report exists and is exactly `PASS`. | NOT_RUN |  | Yes for any non-`PASS` result |  |
| 29 | `FOOTPRINT_LOCK.csv` exists and includes every physical symbol. | NOT_RUN |  | Yes for any missing row |  |
| 30 | No blank footprint on any physical symbol. | NOT_RUN |  | Yes for every blank footprint |  |
| 31 | Every physical symbol has source-backed footprint evidence and package proof recorded. | NOT_RUN |  | Yes for every unverified footprint |  |
| 32 | High-risk parts have package-drawing proof and extra required checks. | NOT_RUN |  | Yes for any unresolved high-risk part |  |
| 33 | PMOS symbol-pin to footprint-pad proof is recorded where applicable. | NOT_RUN |  | Yes |  |
| 34 | Connector mechanical orientation proof is recorded where applicable. | NOT_RUN |  | Yes |  |
| 35 | Connector/mechanical 3D-model or explicit human-review status is recorded. | NOT_RUN |  | Yes |  |
| 36 | Polarity-sensitive parts reviewed. | NOT_RUN |  | Yes |  |
| 37 | Human-review-required items listed. | NOT_RUN |  | Yes |  |

## Automatic Blockers

Mark the gate `BLOCKED` if any required check is `NOT_RUN`, `FAIL`,
`EVIDENCE_MISSING`, `NEEDS_REVIEW`, or has missing evidence.

Mark the gate `BLOCKED` if any high-risk item requires human review and has not
been reviewed.

## Evidence Rules

- Do not use memory as evidence for ERC, annotation, footprint, package
  drawing, connector orientation, or manufacturing readiness.
- Use file paths, command outputs, reports, screenshots, visual exports,
  datasheets, package drawings, or user-confirmed facts.
- Exact values, packages, pinouts, and connector drawings require source evidence.
- Footprint assignment is blocked unless evidence is source-backed per `09_ACCURACY_ENGINE/verification_rules/FOOTPRINT_DATASHEET_MATCH_RULES.md`.

## Approval Statement

Only write this statement when all checks pass:

`SCHEMATIC_TO_PCB_GATE_STATUS is PASS. PCB update from schematic is allowed only within the approved active project, after backup, with command logs and verification plan.`
