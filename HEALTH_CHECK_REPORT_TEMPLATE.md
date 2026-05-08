# KiCad Engine Health Check Report Template

Generated: `YYYY-MM-DDTHH:MM:SS`

Repo root: `PATH_TO_REPO`

Platform: `OS_VERSION`

This report must be generated locally. It must not install tools, store secrets, or modify KiCad project files.

## Summary

- PASS: `0`
- WARN: `0`
- FAIL: `0`

## Required Checks

| Status | Category | Check | Evidence |
| --- | --- | --- | --- |
| TBD | Tool | KiCad installed |  |
| TBD | Tool | kicad-cli available |  |
| TBD | Tool | Git installed |  |
| TBD | Tool | Python installed |  |
| TBD | Tool | Node installed |  |
| TBD | Tool | VS Code installed |  |
| TBD | Repo Structure | Folder structure valid |  |
| TBD | Datasheets | `06_DATASHEETS` structure valid |  |
| TBD | Component Database | `08_COMPONENT_DATABASE` structure valid |  |
| TBD | Prompt Pack | Prompt packs present |  |
| TBD | Scripts | Setup and validation scripts present |  |
| TBD | Security | No secrets accidentally present |  |
| TBD | Fabrication Outputs | No final fab outputs mislabeled as final |  |

## Warnings

- List environment or maturity warnings here.

## Failures

- List blockers here.

## Safety Notes

- Missing tools should be installed only by the user or by opt-in installer scripts after confirmation.
- Never store API keys, passwords, tokens, private keys, or license keys in this repo.
- Do not treat fabrication-style outputs as final unless the full verification gate has passed.
- Keep generated manufacturing-style outputs labeled `NOT_FINAL` until final approval.
