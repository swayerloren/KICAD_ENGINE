# Gerber Review Rules

## Purpose

Keep fabrication output review explicit.

## Required Checks

- Layer set complete.
- Board outline present.
- Drill files present.
- Solder mask and paste layers reviewed.
- Silkscreen readability reviewed.
- Copper polarity and zones reviewed.
- Fab notes and stackup assumptions reviewed.
- Board-house requirements checked.

## Rule

Gerbers are `NOT_FINAL` until checked in a viewer and matched against the source PCB, drill files, BOM, PNP, and fab-house requirements.
