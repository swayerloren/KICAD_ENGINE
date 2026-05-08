# KiCad Native Annotation Success Record

Status: `VERIFIED_SINGLE_PROJECT_SUCCESS`

Date: `2026-05-06`

Project: `ESP32_CSI_WIFI_NODE`

## What Was Verified

Codex successfully used safety-gated KiCad GUI automation to run KiCad's native `Annotate Schematic` workflow on:

`C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`

Verified actions:

1. Detected `eeschema.exe`.
2. Confirmed the Eeschema title included `ESP32_CSI_WIFI_NODE`.
3. Confirmed the Eeschema command line opened the exact target schematic path.
4. Created a backup before GUI action.
5. Captured a screenshot before annotation.
6. Opened KiCad's native `Tools -> Annotate Schematic...` dialog.
7. Applied annotation through the native dialog.
8. Saved the schematic from KiCad GUI.
9. Ran GUI ERC.
10. Ran `kicad-cli` ERC after GUI save.
11. Parsed the saved schematic into a placed-symbol reference table.

## Evidence

Project reports:

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/KICAD_GUI_NATIVE_ANNOTATION_RUN_REPORT.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/KICAD_GUI_NATIVE_ANNOTATION_ERC_REPORT.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/KICAD_GUI_NATIVE_ANNOTATION_REFERENCE_TABLE.md`

Backup:

- `99_BACKUPS/pre_codex_edits/20260506_210316_ESP32_CSI_WIFI_NODE_before_native_gui_annotation`

Screenshot evidence:

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/_verification/gui_detection/native_annotation_before_20260506_210316.bmp`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/_verification/gui_detection/native_annotation_tools_dropdown_primary_20260506_210316.png`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/_verification/gui_detection/native_annotation_dialog_after_apply_20260506_210316.bmp`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/_verification/gui_detection/native_annotation_after_save_20260506_210316.bmp`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/_verification/gui_detection/native_annotation_gui_erc_after_run_20260506_210316.bmp`

## Pass Results

| Check | Result |
|---|---|
| Native annotation dialog opened | `PASS` |
| Annotation applied | `PASS` |
| Schematic saved from KiCad GUI | `PASS` |
| GUI ERC | `PASS`, `Violations (0)` |
| `kicad-cli` ERC after GUI save | `PASS`, 0 errors, 0 warnings |
| Saved schematic unresolved `?` references | `0` |
| Duplicate references | `0` |
| Placed symbols parsed | `79` |
| Physical symbols parsed | `43` |
| `#PWR` symbols parsed | `33` |
| `#FLG` symbols parsed | `3` |

## Mandatory Reuse Rule

Future schematic annotation tasks must use this native KiCad workflow when available. Raw `.kicad_sch` text edits, regex scans, and saved-file-only reference tables are not accepted as proof of annotation success.

The authoritative annotation gate is:

1. GUI/native `Annotate Schematic` applied, or LJ-confirmed manual native annotation.
2. Schematic saved from KiCad GUI.
3. GUI ERC shows 0 violations when safely automatable.
4. `kicad-cli` ERC passes after GUI save.
5. Saved schematic scan shows 0 unresolved `?` references.
6. Duplicate-reference scan passes.

## Limits

This success proves annotation/save/ERC automation for one active schematic under safety gates. It does not approve:

- raw text annotation repair as primary workflow
- visual readability pass
- footprint/package verification
- schematic-to-PCB transition
- PCB update from schematic
- PCB placement, routing, zones, or manufacturing outputs

After annotation passes, visual cleanup may resume only as a separate task. PCB update remains blocked until the full schematic-to-PCB gate is exactly `PASS`.

