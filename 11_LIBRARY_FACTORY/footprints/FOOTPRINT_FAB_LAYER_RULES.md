# Footprint Fab Layer Rules

## Purpose

Fab layer geometry communicates component body size and orientation.

## Rules

- Draw the component body outline on `F.Fab` or `B.Fab`.
- Mark pin 1 orientation when applicable.
- Use dimensions from the package or connector drawing.
- Include polarity/orientation information where useful.
- Keep fab layer distinct from courtyard and silkscreen.

## Connector Notes

For connectors, fab geometry should show:

- Body outline.
- Pin 1 side.
- Mating direction if practical.
- Mounting tabs or shell features.

## Review Gate

A footprint without a fab outline is incomplete unless the footprint type has a documented exception.

