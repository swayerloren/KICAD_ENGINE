# Uncertainty Log: ESP32 CSI GUI Annotation Diagnosis

Date: `2026-05-06`

## Uncertainty

Codex did not extract a GUI object-level symbol table from the live KiCad window. LJ's report that the GUI shows `R?`, `D?`, `SW?`, `C?`, and `MH?` is treated as user-verified evidence.

Status: `REQUIRES_HUMAN_REVIEW`

Severity: `HIGH`

## Known Evidence

- `eeschema.exe` command line points to the exact active schematic path.
- The Eeschema window title starts with `*`, indicating modified/unsaved GUI state.
- The saved disk file parses with 0 bad placed-symbol references.
- Local CLI ERC against the saved disk file reports 0 errors and 0 warnings.

## Unresolved

- The live GUI state has not been saved or annotated.
- The live GUI question-mark references have not been enumerated by automation.
- KiCad-native annotation has not been run by Codex.

## Required Resolution

LJ must manually run KiCad-native annotation and save the schematic, then Codex can re-run saved-file checks.
