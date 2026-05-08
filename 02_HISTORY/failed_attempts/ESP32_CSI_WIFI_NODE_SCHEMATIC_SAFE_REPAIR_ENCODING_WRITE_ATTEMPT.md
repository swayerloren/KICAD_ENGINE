# Failed Attempt: PowerShell Encoding Write Attempt

Date: 2026-05-06
Task: `ESP32_CSI_WIFI_NODE` schematic safe repair

## What Failed

A first PowerShell write attempt used `Set-Content -Encoding utf8NoBOM`, but this host does not support the `utf8NoBOM` encoding enum.

## Impact

The command failed before writing the schematic file. The cleanup was rerun with `.NET` UTF-8 no-BOM file writing.

## Lesson

Use `[System.IO.File]::WriteAllText(..., [System.Text.UTF8Encoding]::new($false))` on this PowerShell host when a no-BOM UTF-8 write is required.
