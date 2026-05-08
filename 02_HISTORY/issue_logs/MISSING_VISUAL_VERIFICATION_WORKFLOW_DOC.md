# Issue: Missing Visual Verification Workflow Document

Date opened: `2026-05-03`
Status: `CLOSED`
Severity: `MEDIUM`
Scope: repo workflow documentation.

## Issue

The task required reading `03_TOOLS/kicad/VISUAL_VERIFICATION_WORKFLOW.md`, but that file does not exist.

## Risk

Agents may follow stale startup or prompt references and miss the intended visual verification workflow before schematic-to-PCB gate review.

## Recommended Fix

Create the missing document or update all references to the actual visual verification workflow path.

## Resolution

Resolved on `2026-05-03` by creating:

- `03_TOOLS/kicad/VISUAL_VERIFICATION_WORKFLOW.md`
- `03_TOOLS/kicad/run_schematic_visual_check.ps1`
- `03_TOOLS/kicad/VISUAL_BLOCK_CONFIG_STANDARD.md`

## Evidence

Startup read attempt returned:

`MISSING: 03_TOOLS\kicad\VISUAL_VERIFICATION_WORKFLOW.md`
