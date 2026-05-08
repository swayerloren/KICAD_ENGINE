# Microcontroller Family Content Generator Claim Evidence Matrix

Date: 2026-05-03

| Claim | Status | Evidence |
| --- | --- | --- |
| Generator script exists. | `VERIFIED_BY_FILE` | `03_TOOLS/scripts/datasheet_tree/create_microcontroller_family_content.py` |
| JSON schema exists. | `VERIFIED_BY_FILE` | `03_TOOLS/scripts/datasheet_tree/family_content_schema.json` |
| All requested templates exist. | `VERIFIED_BY_FILE` | Template directory listing. |
| Script syntax is valid. | `VERIFIED_BY_COMMAND` | `python -m py_compile` passed. |
| Schema JSON parses. | `VERIFIED_BY_COMMAND` | Python `json.load` validation passed. |
| Dry run does not write files. | `VERIFIED_BY_COMMAND` | STM32F0 dry run reported `dry_run: true`, `wrote: 0`. |
| Existing files are skipped without `--force`. | `VERIFIED_BY_COMMAND` | STM32F0 dry run reported existing base files `SKIPPED_EXISTS`. |
| Generator does not download PDFs. | `VERIFIED_BY_FILE` | No network/download implementation exists; script docstring and templates state no downloads. |
| Generator verifies datasheet values. | `UNVERIFIED` | Not claimed; generator creates stubs only. |
| No KiCad files were modified. | `VERIFIED_BY_COMMAND` | Recent-write scan for KiCad design/library extensions returned no files. |
