# Troubleshooting

Status: `PUBLIC_DRAFT`

## KiCad Not Found

- Confirm KiCad is installed.
- Run the health check.
- Check platform quickstart notes.

## `kicad-cli` Not Found

- Confirm KiCad version includes `kicad-cli`.
- Add KiCad `bin` path to your PATH or use a full path in scripts.

## VS Code Not Found

- Install VS Code from official sources.
- Confirm the `code` command is available if scripts need to open VS Code.

## Python Missing

- Install Python 3 from official platform sources.
- Re-run health check.

## Node/npm Missing

- Needed for installer development, not basic documentation use.
- Install only if you plan to build installer tooling.

## PowerShell Execution Policy

On Windows, scripts may require:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\health_check.ps1
```

## AI Tool Not Authenticated

Log in to Codex, Claude, or your chosen AI tool using your own account. KiCad Engine does not store credentials.

## Missing Datasheets Or Footprints

Treat missing data as a blocker for approval. Add source links or records before relying on parts.

## ERC/DRC Failures

Do not ignore failures. Save reports, review findings, fix intentionally, and rerun checks.

