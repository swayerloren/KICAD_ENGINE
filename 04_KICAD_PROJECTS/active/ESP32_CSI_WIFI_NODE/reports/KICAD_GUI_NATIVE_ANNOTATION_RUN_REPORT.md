# KiCad GUI Native Annotation Run Report

Date: `2026-05-06`

Task: run KiCad native GUI annotation on the currently open `ESP32_CSI_WIFI_NODE` schematic.

Final status: `NATIVE_GUI_ANNOTATION_APPLIED_AND_ERC_PASS`

## Scope And Safety

- Active project: `C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE`
- Target project: `C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro`
- Target schematic: `C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`
- KiCad process: `C:\Program Files\KiCad\9.0\bin\eeschema.exe`
- Hand-edited schematic references: `NO`
- PCB edited: `NO`
- PCB updated from schematic: `NO`
- Routing or manufacturing outputs generated: `NO`

## Backup

Backup path:

`C:\Users\LJ\GitHub\KICAD_ENGINE\99_BACKUPS\pre_codex_edits\20260506_210316_ESP32_CSI_WIFI_NODE_before_native_gui_annotation`

Backup contents:

- `ESP32_CSI_WIFI_NODE.kicad_sch`
- `ESP32_CSI_WIFI_NODE.kicad_pro`

Pre-annotation schematic SHA256:

`D0706DEDE551179DB96BF3CC5AE2F0072DF8CE15AE577EDADED4A7B0EB4DA15C`

Backup schematic SHA256:

`D0706DEDE551179DB96BF3CC5AE2F0072DF8CE15AE577EDADED4A7B0EB4DA15C`

## GUI Detection

Initial detection at `2026-05-06T21:03:16`:

| Check | Result |
|---|---|
| `eeschema.exe` running | `PASS` |
| Process ID | `5408` |
| Process path | `C:\Program Files\KiCad\9.0\bin\eeschema.exe` |
| Window title includes `ESP32_CSI_WIFI_NODE` | `PASS` |
| Open schematic path matches target | `PASS` |
| Initial unsaved GUI state | `NO` |

The detected command line was:

```text
"C:\Program Files\KiCad\9.0\bin\eeschema.exe" "C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch"
```

## Screenshots

| Evidence | Path |
|---|---|
| Before annotation screenshot | `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\gui_detection\native_annotation_before_20260506_210316.bmp` |
| Tools menu showing `Annotate Schematic...` | `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\gui_detection\native_annotation_tools_dropdown_primary_20260506_210316.png` |
| Annotation dialog after applying annotation | `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\gui_detection\native_annotation_dialog_after_apply_20260506_210316.bmp` |
| Schematic after GUI save | `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\gui_detection\native_annotation_after_save_20260506_210316.bmp` |
| GUI ERC after run | `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\gui_detection\native_annotation_gui_erc_after_run_20260506_210316.bmp` |

## GUI Actions Performed

| Action | Result |
|---|---|
| Opened KiCad native `Annotate Schematic` dialog | `YES` |
| Selected entire schematic scope | `YES` |
| Selected reset/re-annotate existing annotations | `YES` |
| Applied native annotation with the dialog `Annotate` button | `YES` |
| Closed annotation dialog | `YES` |
| Saved schematic from Eeschema GUI with `Ctrl+S` | `YES` |
| Opened GUI Electrical Rules Checker | `YES` |
| Ran GUI ERC | `YES` |
| Closed GUI ERC dialog | `YES` |

The Eeschema title after save was `ESP32_CSI_WIFI_NODE - Schematic Editor` and did not begin with `*`.

## ERC Results

GUI ERC result: `PASS`

Evidence: UI Automation reported the GUI ERC dialog tab as `Violations (0)` after clicking `Run ERC`.

CLI ERC result after GUI save: `PASS`

Raw report:

`04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\KICAD_GUI_NATIVE_ANNOTATION_ERC_REPORT.raw.txt`

Markdown summary:

`04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\KICAD_GUI_NATIVE_ANNOTATION_ERC_REPORT.md`

## Reference Validation

Reference table:

`04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\KICAD_GUI_NATIVE_ANNOTATION_REFERENCE_TABLE.md`

Parsed placed-symbol summary:

| Check | Result |
|---|---|
| Placed symbols parsed | `79` |
| Physical symbols parsed | `43` |
| Power symbols parsed | `33` |
| PWR_FLAG symbols parsed | `3` |
| Reference properties ending in `?` | `0` |
| Instance references ending in `?` | `0` |
| Duplicate references | `0` |
| Direct unresolved-token scan hits | `{}` |

## Visible Question-Mark Reference Check

The post-save GUI screenshot did not show unresolved schematic references in the visible viewport. The screenshot does show the KiCad toolbar icon text `R??`; that is UI chrome, not a schematic symbol reference.

This run did not perform a full human-readability cleanup or full-sheet visual quality gate. It only addressed native annotation and ERC.

## Final Decision

| Item | Result |
|---|---|
| Native annotation dialog opened | `YES` |
| Annotation applied | `YES` |
| Schematic saved from GUI | `YES` |
| GUI ERC run | `YES_PASS_VIOLATIONS_0` |
| CLI ERC after GUI save | `PASS_0_ERRORS_0_WARNINGS` |
| `Schematic is not fully annotated` remains | `NO` |
| Duplicate reference errors remain | `NO` |
| Stored unresolved `?` references remain | `NO` |
| Visual cleanup may resume | `YES_FOR_LAYOUT_ONLY` |
| PCB update remains blocked | `YES` |

