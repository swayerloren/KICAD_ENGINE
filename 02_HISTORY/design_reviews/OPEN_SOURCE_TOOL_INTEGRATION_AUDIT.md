# Open-Source Tool Integration Audit

Date: 2026-05-10
Task type: `DOCS_ONLY`
Scope: optional tool integration layer, install-policy docs, startup routing
updates, attribution/security updates, and dry-run verification wrappers.

## Summary

Implemented a first-party open-source integration layer under
`03_TOOLS/open_source_integrations/` so future Codex/Claude sessions can use
documented upstream KiCad-adjacent tools without bundling large repos or
breaking ZIP portability.

## Main Decisions

- Default repo behavior stays ZIP-portable after extraction.
- Optional tools install only into `.tools/` or user-local caches.
- Install wrappers are dry-run by default and do nothing unless explicitly
  applied.
- Upstream heavyweight tools remain `external-only`.
- Route-specific startup docs now point `OPEN_SOURCE_TOOL_USE` into the new
  integration layer before install or attribution claims are made.
- Root attribution, license, security, and memory docs were updated to match
  the new layer.

## Created

- `03_TOOLS/open_source_integrations/`
- `03_TOOLS/open_source_integrations/profiles/`
- `setup/install_optional_kicad_tools_windows.ps1`
- `setup/install_optional_kicad_tools_linux.sh`
- `setup/install_optional_kicad_tools_macos.sh`
- `setup/verify_optional_kicad_tools.py`
- `requirements-kicad-tools.txt`
- `requirements-fab-tools.txt`
- `requirements-visual-tools.txt`

## Validation

- `python -m py_compile setup\verify_optional_kicad_tools.py`
  - `PASS`
- `python setup\verify_optional_kicad_tools.py --dry-run`
  - `PASS`
  - detected `kicad-cli`
  - reported the rest as optional missing, external missing, or manual-check
    required
- `powershell -ExecutionPolicy Bypass -File setup\install_optional_kicad_tools_windows.ps1`
  - `PASS`
  - dry-run only, no installs performed
- `git diff --name-only -- '*.kicad_sch' '*.kicad_pcb'`
  - empty
- `git diff --cached --name-only`
  - empty

## Residual Risks

- Linux and macOS wrapper logic was written but not runtime-tested on this
  Windows machine.
- Tool availability still depends on each user's local environment.
- Copyleft tools remain documented but not bundle-approved.

## Audit Result

`PASS_WITH_FOLLOWUPS`
