# Quality Gate Failure: Codex Text-Edit Annotation Did Not Resolve GUI State

Date: `2026-05-06`

Project: `ESP32_CSI_WIFI_NODE`

Severity: `HIGH`

Status: `BLOCKED_PENDING_MANUAL_KICAD_NATIVE_ANNOTATION`

## Failure

LJ opened the exact active schematic in KiCad and still saw actual question-mark references such as `R?`, `D?`, `SW?`, `C?`, and `MH?`.

This means previous command-line and saved-file reports claiming annotation pass did not verify the live GUI-loaded schematic state.

## Forensic Evidence

Windows process inspection confirmed:

```text
eeschema.exe "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch"
```

The window title was:

```text
*ESP32_CSI_WIFI_NODE [ESP32_CSI_WIFI_NODE] - Schematic Editor
```

The leading `*` means the GUI document is modified/unsaved in memory. This is the likely root cause of the discrepancy: CLI checks were reading the saved disk file, while LJ was looking at a live unsaved GUI state.

## Saved File Evidence

The saved active `.kicad_sch` currently parses with:

- 79 placed symbols
- 0 bad refs ending in `?`
- 0 duplicate refs
- local KiCad CLI ERC: 0 errors, 0 warnings

This is not enough to clear the GUI gate.

## Required Corrective Action

Codex must not continue text-edit annotation repair.

LJ must manually run KiCad-native annotation in the GUI:

`Tools -> Annotate Schematic -> Re-annotate all symbols -> Save -> Run ERC`

Only after LJ confirms the GUI no longer shows `?` references may Codex re-run saved-file checks and continue to visual cleanup.

## Gate Result

Annotation GUI gate: `FAIL_NOT_GUI_VERIFIED`

Visual cleanup may resume: `NO`

PCB update allowed: `NO`
