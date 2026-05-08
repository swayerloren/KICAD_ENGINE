# Portability Audit Claim Evidence Matrix

Record kind: `claim_evidence_matrix`
Created: `2026-05-08T18:34:00`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `MEDIUM`
Claim status: `PARTIALLY_VERIFIED`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Matrix

| Claim | Evidence | Claim Status | Confidence | Risk | Human Review Required | Issue |
| --- | --- | --- | --- | --- | --- | --- |
| Local `main` matched GitHub `main` before remediation. | `git rev-parse HEAD`; `git rev-parse origin/main`; `git log --oneline --decorate -n 10` | `VERIFIED_BY_COMMAND` | `HIGH` | `LOW_RISK` | `NO` | None recorded. |
| `03_TOOLS/node_envs`, `python_envs`, `repos`, `tool_logs`, and `99_BACKUPS` are intentionally local-only. | `.gitignore`; `git status --ignored`; `git check-ignore -v ...`; tracked placeholder docs | `VERIFIED_BY_COMMAND` | `HIGH` | `LOW_RISK` | `NO` | None recorded. |
| A new user can start from ZIP or clone without extra helper repos. | Updated `README.md`; `DOWNLOAD_ZIP_START_HERE.md`; `LOCAL_SETUP_REQUIREMENTS.md`; `EXTERNAL_DEPENDENCIES.md` | `VERIFIED_BY_FILE` | `MEDIUM` | `LOW_RISK` | `YES` | Human onboarding review still useful. |
| Passive helper scripts no longer assume a personal checkout path. | Updated `discover_windows.py`; `take_screenshot.py`; `kicad_window_filter.py`; `python -m py_compile ...` | `VERIFIED_BY_FILE` | `MEDIUM` | `LOW_RISK` | `YES` | Runtime behavior not manually exercised in this task. |
| `routing_work` remains a portability gap. | Folder inventory; `git ls-files ...routing_work`; `05_OUTPUTS/release_readiness/PORTABILITY_AUDIT_REPORT.md` | `VERIFIED_BY_COMMAND` | `HIGH` | `MEDIUM_RISK` | `YES` | Existing tracked scratch payload was documented, not removed. |

## Details

This docs-only task intentionally prioritized safe documentation and future-growth controls over destructive cleanup of old tracked scratch artifacts.
