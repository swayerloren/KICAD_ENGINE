# Power Trace Rules

## Purpose

Define routing rules for power input, protection, regulator, and distribution traces.

## Rules

- Route power input and protection first.
- Keep input protection physically readable from connector to regulator.
- Keep the regulator switching loop short and compact.
- Keep wide power traces wide through most of the path.
- Avoid unnecessary neckdowns and unnecessary vias.
- Separate noisy switching nodes from RF and USB areas.

## Review Triggers

- long detours
- unnecessary vias
- switching-loop sprawl
- power path crossing unrelated areas
