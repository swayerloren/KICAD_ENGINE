# Uncertainty Log - Open KiCad Sample Projects Audit

Date: `2026-05-03`

Severity: `MEDIUM`

## Uncertainties

| uncertainty | impact | required follow-up |
| --- | --- | --- |
| The audit did not perform datasheet-level design-intent verification. | A sample might be electrically intentional despite ERC/DRC warnings, or might contain real design faults not captured by KiCad. | Human engineering review before any reference or benchmark promotion. |
| Close-up visual crop review was not generated because visual block definitions were absent. | Full-page SVG export is not equivalent to detailed visual verification. | Create sample-specific visual block configs in normalized copies if a future task approves enrichment. |
| Some missing library or footprint mismatch reports may reflect upstream project age or local KiCad 9 library drift. | Failures may be useful compatibility signals rather than design defects. | Preserve as regression fixtures, then separately test repaired/migrated copies. |
| Existing upstream Gerbers/BOMs/placement files were not audited as manufacturing outputs. | Imported artifacts must not be treated as KiCad Engine-generated or approved outputs. | Keep imported artifacts source-only unless separately reviewed. |

## Closeout Status

Uncertainties are documented and do not block the read-only audit result. They block promotion of the samples to clean demos, references, benchmarks, or public payload content.

