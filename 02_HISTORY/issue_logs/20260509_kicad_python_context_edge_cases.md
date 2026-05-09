# KiCad Python Context Edge Cases

Record kind: `issue_log`
Status: `OPEN`
Created: `2026-05-09T08:43:20`
Scope: `global`
Project: `N/A`

## Summary

The repo now handles the common Windows KiCad-Python mismatch safely, but some non-default KiCad packaging layouts may still require an explicit `--kicad-root` override or future probe expansion.

## Details

1. The new context helper is verified on the current Windows KiCad 9 install, where KiCad bundles `bin\python.exe` and `python311.dll`.
2. Future KiCad packaging variants may ship different Python layouts or omit a directly callable bundled interpreter.
3. When those variants appear, the first step should be to extend `03_TOOLS/scripts/kicad_api/kicad_python_context.py` rather than falling back to hardcoded user-local assumptions.

## Source Or Evidence

- `05_OUTPUTS/release_readiness/KICAD_PYTHON_CONTEXT_FIX_REPORT.md`
- `python 03_TOOLS/scripts/kicad_api/kicad_python_context.py`
- `python 03_TOOLS/scripts/kicad_api/pcbnew_import_check.py`

## Verification Status

Current behavior is `VERIFIED_WORKFLOW` on this machine only. Treat broader packaging support as `UNVERIFIED` until tested on additional KiCad installs.

## Secret Check

No secrets should be stored in this record.
