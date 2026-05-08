# ESP32_CSI_WIFI_NODE Routing Work Prep Baseline Extraction Retries

Date: `2026-05-08`

Status: `RESOLVED_WITH_FALLBACK`

## Failed Attempts

1. An inline KiCad Python baseline extractor failed with:
   - `SyntaxError: f-string: expecting '}'`

2. A larger multi-output KiCad Python extractor timed out before writing the full prep packet.

3. A trace CSV pipeline attempt timed out and left a zero-byte `CURRENT_TRACE_LIST.csv`.

4. A second direct KiCad Python trace CSV writer also timed out and held the stub file open.

## Resolution

- Kept the authoritative raw trace snapshot as `CURRENT_TRACE_LIST.txt`
- Recorded the timeout behavior honestly instead of fabricating a structured trace CSV
- Stopped only the clearly session-owned orphan KiCad Python processes
- Removed the zero-byte trace CSV stub so the routing-work folder contains only usable evidence
