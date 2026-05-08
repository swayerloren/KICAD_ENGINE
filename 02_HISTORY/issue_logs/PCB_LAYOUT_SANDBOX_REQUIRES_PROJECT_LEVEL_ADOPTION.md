# PCB Layout Sandbox Requires Project-Level Adoption

Date: `2026-05-07`

## Issue

The repo now has a permanent `34_PCB_LAYOUT_SANDBOX/` layer and the main startup/workflow/prompt-pack control points were patched to require it. Existing projects do not automatically gain project-local variant reports from that repo-level change.

## Impact

- Future real `.kicad_pcb` edits should now be blocked until sandbox evidence exists.
- Active boards that already have a PCB file still need project-local sandbox outputs before the next placement or routing edit.

## Required Follow-Up

1. For each active PCB project moving into placement/routing, create at least three sandbox variants and one selected-variant justification report under the project reports area.
2. Treat the selected variant as the basis for connector placement, board shape, keepouts, and routing feasibility before any real PCB edit.

## Status

`OPEN`
