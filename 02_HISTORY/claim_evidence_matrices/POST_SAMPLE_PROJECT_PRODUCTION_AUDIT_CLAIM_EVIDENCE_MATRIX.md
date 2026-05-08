# Claim Evidence Matrix - Post Sample Project Production Audit

Date: `2026-05-06`

| Claim | Status | Evidence |
| --- | --- | --- |
| Sample intake system exists and is documented. | `VERIFIED_BY_FILE` | `32_OPEN_KICAD_SAMPLE_INTAKE/README.md`, source/license/import/review/promotion rules. |
| Candidate records exist. | `VERIFIED_BY_COMMAND` | Candidate folder inventory: 11 files. |
| Imported originals and normalized samples are separate. | `VERIFIED_BY_COMMAND` | Directory inventories show 3 imported original directories and 3 normalized sample directories. |
| Imported samples have attribution/import reports. | `VERIFIED_BY_COMMAND` | Attribution and import report inventories. |
| Golden-path sample exists. | `VERIFIED_BY_FILE` | `19_TEST_PROJECTS/sample_kicad_projects/tomasr8_attiny85_dev_board/`. |
| Gate runner exists and syntax-validates. | `VERIFIED_BY_COMMAND` | Python `py_compile` and PowerShell parser validation. |
| Gate runner was tested on the sample. | `VERIFIED_BY_COMMAND` | `05_OUTPUTS/gate_runs/20260506_145808/PROJECT_GATE_REPORT.md`. |
| Current sample status is blocked. | `VERIFIED_BY_COMMAND` | Fresh gate run final classification `BLOCKED_UNTIL_HUMAN_REVIEW`. |
| Public docs exist. | `VERIFIED_BY_FILE` | README and sample/public docs presence checks. |
| Payload rules exclude unsafe samples. | `VERIFIED_BY_FILE` | `17_RELEASE_BUILD/PAYLOAD_EXCLUDE_RULES.md` and `SAMPLE_PROJECT_PAYLOAD_POLICY.md`. |
| Public payload builder is missing. | `VERIFIED_BY_COMMAND` | `Test-Path 17_RELEASE_BUILD/build_public_payload.py` returned false. |
| No KiCad files were edited during this audit. | `VERIFIED_BY_ACTION_SCOPE` | Audit used read-only commands and only wrote Markdown reports/logs. |
| No credential files found in audited public/sample/release roots. | `VERIFIED_BY_COMMAND` | Targeted credential file scan. |
| Broad repo secret hygiene remains unresolved. | `PARTIALLY_VERIFIED` | Broad scan timed out and reported excluded env/tool paths including a secret-named third-party file. |
