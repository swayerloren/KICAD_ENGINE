# Uncertainty Log - Project Gate Runner

Date: `2026-05-06`

| Item | Confidence | Human Review Required | Notes |
| --- | --- | --- | --- |
| Full repository diff status | `MEDIUM` | `NO` | `git status` failed because this checkout has no `.git` metadata. Scope was controlled by file paths patched in this session. |
| Gate runner report naming coverage beyond current KiCad Engine reports | `MEDIUM` | `NO` | Runner supports current report names and fallback missing-evidence behavior; future projects may need config-driven report path aliases. |
| ATtiny85 electrical correctness | `LOW` | `YES` | The runner only reports existing blockers; it does not certify the sample design. |
| Fabrication readiness | `LOW` | `YES` | Explicitly blocked until final PCB verification permits `READY_FOR_NOT_FINAL_FAB_EXPORT`. |
