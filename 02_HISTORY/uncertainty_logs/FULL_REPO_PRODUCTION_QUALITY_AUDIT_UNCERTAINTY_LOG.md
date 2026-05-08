# Uncertainty Log - Full Repo Production Quality Audit

Date: `2026-05-03`

| Uncertainty | Impact | Required follow-up |
|---|---|---|
| Broken-reference scan is heuristic and includes path-portability/template findings. | CSV rows require triage; not every row is a confirmed broken production link. | Run stricter markdown-link-only validation after path normalization. |
| Secret-like scan includes false positives from code, GitHub examples, and vendored files. | Public release could be blocked if any are real secrets, but this audit did not confirm active credentials. | Manual review and payload exclusion. |
| Legal redistribution status of the two Espressif PDFs was not determined. | Public release risk. | Human legal/source review or remove PDFs and keep source links only. |
| Heavy/generated trees were excluded from deep text scans. | Additional weak files may exist inside excluded areas. | Treat excluded trees as release-exclusion candidates, then audit intended payload only. |
| Bash syntax validation was not run. | Linux/macOS scripts may have syntax issues not visible on Windows. | Run `bash -n` in Linux/macOS CI. |
| Scores are audit judgments, not benchmark measurements. | Scores should not be used as public claims. | Add benchmark runs and formal release criteria. |
