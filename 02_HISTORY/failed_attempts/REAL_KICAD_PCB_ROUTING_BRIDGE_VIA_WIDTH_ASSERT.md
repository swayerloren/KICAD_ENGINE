# REAL_KICAD_PCB_ROUTING_BRIDGE_VIA_WIDTH_ASSERT

Date: `2026-05-07`

## Failure

The first via extractor used `PCB_VIA.GetWidth()` without a layer argument. KiCad raised an assertion in copied-board extraction.

## Fix

Switched to `GetFrontWidth()` for a stable extracted via diameter value.

## Status

Resolved.
