# Failed Attempt: ERC Invoked With Project Path

Date: `2026-05-06`

Project: `ESP32_CSI_WIFI_NODE`

Severity: `LOW`

## What Failed

During the emergency annotation repair, an initial ERC command was invoked with the `.kicad_pro` path instead of the `.kicad_sch` path.

## Command Pattern

```powershell
kicad-cli sch erc --output <report> <project>.kicad_pro
```

## Result

KiCad reported `Failed to load schematic`.

## Fix

The command was corrected to use:

```powershell
kicad-cli sch erc --output <report> <schematic>.kicad_sch
```

The corrected ERC command passed with 0 violations.

## Lesson

For KiCad 9 `kicad-cli sch erc`, pass the schematic file path, not the project file path.
