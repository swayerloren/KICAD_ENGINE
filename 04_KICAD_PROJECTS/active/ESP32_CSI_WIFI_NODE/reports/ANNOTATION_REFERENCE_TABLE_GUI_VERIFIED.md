# Annotation Reference Table - GUI Verification Status

Generated: `2026-05-06 18:55:00 -04:00`

Status: `NOT_GUI_VERIFIED`

Reason: LJ reports the KiCad GUI still shows `R?`, `D?`, `SW?`, `C?`, and `MH?`. Windows process inspection confirms the GUI has the exact active schematic open, but the window title begins with `*`, indicating unsaved/modified in-memory state. Codex did not run GUI annotation or save the GUI state.

## Exact Active Schematic

`C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`

## Saved-Disk Parse Summary

| Check | Result |
| --- | --- |
| Placed symbols | `79` |
| Bad refs in saved placed-symbol blocks | `0` |
| Duplicate refs in saved placed-symbol blocks | `0` |
| Local CLI ERC on saved file | `0 errors, 0 warnings` |
| GUI verified | `NO` |

## Saved-Disk Reference Table

The current saved-disk reference table is:

`04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/ANNOTATION_REFERENCE_TABLE_FINAL.md`

Do not treat that saved-disk table as GUI-verified until LJ runs KiCad-native annotation in the GUI, saves, and confirms the GUI no longer shows question-mark references.

## Bad References Reported By GUI

Codex did not enumerate GUI symbol objects directly. LJ reported that the GUI still shows actual unannotated references including:

- `R?`
- `D?`
- `SW?`
- `C?`
- `MH?`

## Required Next Verification

After LJ manually runs KiCad-native annotation and saves:

1. Codex should re-parse the saved schematic.
2. Codex should run KiCad CLI ERC.
3. Codex should create a new GUI-verified reference table only if LJ confirms the GUI itself no longer shows `?` references.
