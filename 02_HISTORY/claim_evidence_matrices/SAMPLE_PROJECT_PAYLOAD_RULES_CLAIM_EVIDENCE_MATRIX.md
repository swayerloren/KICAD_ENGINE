# Claim Evidence Matrix - Sample Project Payload Rules

Date: `2026-05-06`

| Claim | Status | Evidence |
| --- | --- | --- |
| `17_RELEASE_BUILD/build_public_payload.py` is missing. | `VERIFIED_BY_COMMAND` | `Test-Path` validation in `02_HISTORY/command_logs/SAMPLE_PROJECT_PAYLOAD_RULES_COMMANDS.md`. |
| The ATtiny85 fixture has MIT license evidence. | `VERIFIED_BY_FILE` | `ORIGINAL_SOURCE_ATTRIBUTION.md`, `GOLDEN_PATH_DEMO_STATUS.md`. |
| The ATtiny85 fixture public bundle status is pending final human review. | `VERIFIED_BY_FILE` | `ORIGINAL_SOURCE_ATTRIBUTION.md`, `GOLDEN_PATH_DEMO_STATUS.md`, `SAMPLE_PROJECTS_INDEX.md`. |
| The latest gate status is `BLOCKED_UNTIL_HUMAN_REVIEW`. | `VERIFIED_BY_FILE` | `05_OUTPUTS/gate_runs/20260506_142924/PROJECT_GATE_REPORT.md`. |
| No KiCad design files were edited for this task. | `VERIFIED_BY_ACTION_SCOPE` | Only Markdown files were patched; KiCad sample source inventory was read-only. |
| No dry-run public payload build was executed. | `VERIFIED_BY_COMMAND` | Builder missing check in command log. |
| Public sample source files should remain excluded until status is `PUBLIC_BUNDLE_ALLOWED`. | `PARTIALLY_VERIFIED_POLICY_DECISION` | Derived from sample intake rules, attribution status, license audit status, and user payload rules. Human review still required. |
