# ESP32 CSI WiFi Node KiCad GUI Native Annotation Commands

Date: `2026-05-06`

## Summary

This command log records the commands and GUI automation used to run KiCad-native schematic annotation and validate the result.

## Commands And Actions

1. Ran GUI state detection:

```powershell
.\33_KICAD_GUI_AUTOMATION\scripts\windows\detect_unsaved_kicad_state.ps1 -ExpectedSchematicPath 'C:\Users\LJ\GitHub\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch' -Json
```

Result: `eeschema.exe` detected, title included `ESP32_CSI_WIFI_NODE`, open schematic path matched target, initial unsaved state was `false`.

2. Created backup:

```powershell
Copy-Item ESP32_CSI_WIFI_NODE.kicad_sch, ESP32_CSI_WIFI_NODE.kicad_pro -> 99_BACKUPS\pre_codex_edits\20260506_210316_ESP32_CSI_WIFI_NODE_before_native_gui_annotation
```

Result: backup created; active and backup schematic SHA256 matched before GUI annotation.

3. Captured before screenshot with handle-based `PrintWindow`.

Result:

`04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\_verification\gui_detection\native_annotation_before_20260506_210316.bmp`

4. Opened `Tools -> Annotate Schematic...` through GUI automation.

Result: native `Annotate Schematic` dialog opened.

5. Configured and applied native annotation.

Result: clicked `Annotate` in KiCad's native dialog.

6. Saved schematic from Eeschema GUI.

Result: Eeschema title no longer started with `*`, and KiCad status text reported the schematic file was saved.

7. Ran GUI ERC:

Result: GUI ERC dialog reported `Violations (0)`.

8. Ran CLI ERC after GUI save:

```powershell
& 'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe' sch erc --format report --severity-all --output '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\KICAD_GUI_NATIVE_ANNOTATION_ERC_REPORT.raw.txt' '04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch'
```

Result: exit code `0`; report showed `0 Errors 0 Warnings`.

9. Parsed saved schematic into a placed-symbol reference table.

Result: `79` placed symbols, `0` unresolved references, `0` duplicates.

## Safety Notes

- No `.kicad_pcb` file was edited.
- No PCB update from schematic was run.
- No routing, zones, or manufacturing outputs were generated.
- Annotation was performed through KiCad GUI/native workflow, not by text-editing schematic references.

