# Coding And Scripting Rules

Durable rules for scripts and automation used in this KiCad workspace.

## Safety
- Scripts must be safe to run repeatedly.
- Scripts must not delete source project files.
- Scripts must fail safely if KiCad CLI is missing.
- Scripts must not hardcode secrets.
- Do not store passwords, API keys, license keys, private tokens, or credentials in scripts, memory, history, or generated reports.

## File Placement
- General scripts belong in `03_TOOLS/scripts/`.
- Project-specific scripts belong inside the relevant project only when the project intentionally owns them.
- Generated files go to outputs, reports, or fabrication folders.
- Do not write generated files over source `.kicad_sch`, `.kicad_pcb`, `.kicad_pro`, symbol libraries, footprint libraries, or manufacturing packages unless explicitly requested and backed up.

## PowerShell Rules
- PowerShell scripts must use quoted paths.
- Prefer `-LiteralPath` for filesystem operations.
- Avoid path assumptions; resolve workspace-relative paths before acting.

## Logging
- Log commands and results.
- Command logs belong in `02_HISTORY/command_logs/`.
- Verification outputs belong in `02_HISTORY/erc_drc_reports/` or project-specific history.
- Session summaries belong in `02_HISTORY/sessions/`.

## KiCad CLI Behavior
- Check for `kicad-cli` before running ERC, DRC, export, or render commands.
- If `kicad-cli` is missing, report the missing dependency and stop without pretending checks passed.
- Record failed or blocked checks in history when they affect release readiness.

## Repeatability
- Prefer deterministic command arguments and explicit output paths.
- Prefer dated or versioned output directories for generated release artifacts.
- Do not silently overwrite previous verification or fabrication outputs.
