# REAL_KICAD_PCB_ROUTING_BRIDGE_GETRADIUS_HANG

Date: `2026-05-07`

## Failure

The first extraction pass called `GetRadius()` on non-arc `Edge.Cuts` shapes. On copied-board extraction this stalled the run.

## Fix

Restricted radius extraction to `Arc` and `Circle` shapes only.

## Status

Resolved.
