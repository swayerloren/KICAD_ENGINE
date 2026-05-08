# KiCad GUI Native Annotation ERC Report

Date: `2026-05-06`

Status: `GUI_ERC_AND_CLI_ERC_PASS_AFTER_NATIVE_ANNOTATION`

## Context

KiCad native GUI annotation was run on the currently open `ESP32_CSI_WIFI_NODE` schematic, the schematic was saved from Eeschema, GUI ERC was run, and `kicad-cli` ERC was run after saving.

## GUI ERC

GUI ERC was opened through the Eeschema `Inspect -> Electrical Rules Checker...` menu and run with the `Run ERC` button.

Observed GUI result from UI Automation after `Run ERC`:

```text
Violations (0)
```

GUI ERC screenshot evidence:

`04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\gui_detection\native_annotation_gui_erc_after_run_20260506_210316.bmp`

## CLI ERC Command

```powershell
& 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' sch erc --format report --severity-all --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\KICAD_GUI_NATIVE_ANNOTATION_ERC_REPORT.raw.txt' '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch'
```

Exit code: `0`

## CLI ERC Result

```text
Found 0 violations
Saved ERC Report to 04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\KICAD_GUI_NATIVE_ANNOTATION_ERC_REPORT.raw.txt
ERC_EXIT_CODE=0
```

Raw report excerpt:

```text
ERC report (2026-05-06T21:10:40-0400, Encoding UTF8)

***** Sheet /

 ** ERC messages: 0  Errors 0  Warnings 0
```

## Annotation-Specific ERC Checks

| Check | Result |
|---|---|
| ERC says `Schematic is not fully annotated` | `NO` |
| ERC duplicate reference errors | `NO` |
| ERC total errors | `0` |
| ERC total warnings | `0` |

## Interpretation

This is valid evidence that the saved schematic currently passes ERC after KiCad-native GUI annotation. It does not prove the schematic is visually clean or ready for PCB update; those remain separate gates.

