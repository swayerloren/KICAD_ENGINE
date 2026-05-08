# ESP32_CSI_WIFI_NODE GUI Annotation Diagnosis Session

Date: `2026-05-06`

Task: forensic diagnosis and KiCad-native annotation workflow only.

## Scope

No schematic edits, no visual cleanup, no value changes, no footprint changes, no PCB edits, no routing, and no manufacturing outputs were performed.

## Key Finding

Windows process inspection confirmed `eeschema.exe` is opened on:

`C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`

But the window title is:

`*ESP32_CSI_WIFI_NODE [ESP32_CSI_WIFI_NODE] - Schematic Editor`

The leading `*` indicates the GUI document is modified/unsaved in memory. This explains why saved-disk CLI checks can pass while LJ still sees question-mark references in the GUI.

## Saved Disk Checks

- Active disk file SHA256: `D0706DEDE551179DB96BF3CC5AE2F0072DF8CE15AE577EDADED4A7B0EB4DA15C`
- Structured placed-symbol parse found 79 placed symbols.
- Bad refs in saved placed-symbol blocks: `0`.
- Duplicate refs in saved placed-symbol blocks: `0`.
- KiCad CLI ERC from repo root: `0 errors, 0 warnings`.
- KiCad CLI ERC from project schematic directory: `0 errors, 0 warnings`.

## KiCad-Native Annotation

Codex did not run GUI annotation.

Reason: GUI automation would have to act on an unsaved modified KiCad window, which is unsafe and could overwrite the current saved disk file with stale in-memory data.

## Required LJ Action

Manually run:

`Tools -> Annotate Schematic -> Re-annotate all symbols -> Save -> Run ERC`

Then tell Codex when it is complete.

## Evidence

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/GUI_ANNOTATION_MISMATCH_DIAGNOSIS.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/KICAD_NATIVE_ANNOTATION_RESULT.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/ANNOTATION_REFERENCE_TABLE_GUI_VERIFIED.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/GUI_MISMATCH_DIAGNOSIS_ERC_FROM_REPO_ROOT.rpt`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/GUI_MISMATCH_DIAGNOSIS_ERC_FROM_PROJECT_DIR.rpt`

## Final Status

`BLOCKED_PENDING_MANUAL_KICAD_NATIVE_ANNOTATION`
