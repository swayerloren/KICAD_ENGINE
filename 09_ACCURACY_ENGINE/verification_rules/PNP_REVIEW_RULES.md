# Pick And Place Review Rules

## Purpose

Prevent assembly errors from generated position files.

## Required Checks

- Reference designator present.
- X/Y coordinates plausible.
- Rotation reviewed for polarized and asymmetric parts.
- Side/top-bottom correct.
- Footprint origin appropriate.
- DNP parts excluded or marked.
- Connector orientation reviewed.
- Pin 1 marker visible in assembly output.

## Rule

PNP outputs are `NOT_FINAL` until assembly orientation review is complete.
