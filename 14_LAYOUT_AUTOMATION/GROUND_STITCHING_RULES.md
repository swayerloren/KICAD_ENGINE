# Ground Stitching Rules

## Purpose

Define how the routing engine should think about local ground stitching and ground-support review.

## Rules

- Ground stitching is not a replacement for good signal or power routing.
- Use ground-stitching guidance mainly near RF boundaries, connector entry points, and return-path-sensitive regions.
- Ground stitching should not distract from unfinished critical nets.
- If no copper zones exist yet, record local ground-return needs explicitly rather than pretending they are solved.

## Boundary

This is a planning and review rule set. It does not auto-create copper zones in setup-only tasks.
