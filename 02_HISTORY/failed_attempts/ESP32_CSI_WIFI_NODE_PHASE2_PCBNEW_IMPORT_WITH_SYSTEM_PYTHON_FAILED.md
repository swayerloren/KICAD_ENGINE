# Failed Attempt - ESP32_CSI_WIFI_NODE Phase 2 pcbnew Import With System Python Failed

Date: `2026-05-07`

## Command Pattern

Attempted to import KiCad `pcbnew` using the system Python with only KiCad `site-packages` added to `sys.path`.

## Result

`ImportError: DLL load failed while importing _pcbnew`

## Resolution

Used KiCad's bundled Python instead:

`C:\Program Files\KiCad\9.0\bin\python.exe`

That successfully imported `pcbnew` version `9.0.7`.

