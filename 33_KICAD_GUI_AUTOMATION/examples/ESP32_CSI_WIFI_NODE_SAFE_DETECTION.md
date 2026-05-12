# Example: ESP32_CSI_WIFI_NODE Safe GUI Detection

Status: `EXAMPLE_ONLY`

```powershell
$repo = (Resolve-Path ".").Path
$schematic = Join-Path $repo "04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch"

.\33_KICAD_GUI_AUTOMATION\scripts\windows\detect_kicad_windows.ps1 -ExpectedSchematicPath $schematic -Json

.\33_KICAD_GUI_AUTOMATION\scripts\windows\detect_unsaved_kicad_state.ps1 -ExpectedSchematicPath $schematic -Json

.\03_TOOLS\python_envs\windows_gui\Scripts\python.exe `
  .\33_KICAD_GUI_AUTOMATION\scripts\windows\annotate_schematic_gui.py `
  --expected-schematic $schematic
```

If the dry-run annotation helper returns `UNSAVED_GUI_STATE` or `BLOCKED_LIVE_GUI_ANNOTATION_NOT_VERIFIED`, LJ must use the manual workflow:

`Tools -> Annotate Schematic -> Re-annotate all symbols -> Save -> Run ERC`
