# Hallucination Risk Log - Open KiCad Sample Project Import

Date: `2026-05-03`

Status: `RISK_CONTROLLED`

## Risk Areas

| Risk | Severity | Control |
| --- | --- | --- |
| Treating imported projects as verified reference designs. | HIGH | Import reports and indexes mark them `IMPORTED_NEEDS_REVIEW`. |
| Treating upstream Gerbers/BOM/PNP/STEP files as KiCad Engine outputs. | HIGH | Reports explicitly state they are upstream source artifacts. |
| Treating GitHub license metadata as final legal approval. | MEDIUM | Local license files and human review requirement are recorded. |
| Claiming ERC/DRC or benchmark results without running checks. | HIGH | Scorecard and import reports state no checks were run. |

## Agent Rule

Future agents must not infer engineering correctness from the presence of a complete KiCad project. The normalized copy is only a review target until ERC, DRC, visual, BOM, and footprint/package evidence exist.
