# Hallucination Risk Log: ESP32_CSI_WIFI_NODE Strict Visual Readability Re-Audit

Date: 2026-05-06  
Risk: confusing automated visual artifact generation with human-readable schematic approval

## Risk Description

The visual automation can successfully generate SVG/PDF/PNG files and close-up crops while the schematic remains visually unacceptable to a human reviewer. Treating crop generation as `VISUAL_PASS` would be an overconfident and unsafe claim.

## Current Evidence

The re-audit found multiple crop-level visual failures:
- text touching or crossing wires
- labels too close to pins and symbol bodies
- crowded values and references
- clipped crop context
- review notes not cleanly framed

## Required Agent Behavior

- Do not mark visual status as pass from crop existence alone.
- Inspect rendered images or classify visual status as `NOT_VERIFIED`.
- Keep PCB update blocked while any strict visual block fails.

## Status

OPEN
