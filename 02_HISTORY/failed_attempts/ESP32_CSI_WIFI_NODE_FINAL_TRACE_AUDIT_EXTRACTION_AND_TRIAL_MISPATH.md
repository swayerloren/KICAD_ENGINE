# ESP32_CSI_WIFI_NODE Final Trace Audit Extraction And Trial Mismatch

Generated: `2026-05-08T12:59:26-04:00`

## Failure 1

- The first KiCad Python inventory extractor hung for minutes without producing a usable file.
- Workaround:
  - switched to direct `.kicad_pcb` text parsing for the authoritative pre/post inventory files

## Failure 2

- The first copied-board repair script targeted the wrong hardcoded trial folder and failed with `NoneType` because the board path did not exist.
- Workaround:
  - reran the same script against the actual created trial folder `20260508_125541`
  - copied-board DRC then passed cleanly
