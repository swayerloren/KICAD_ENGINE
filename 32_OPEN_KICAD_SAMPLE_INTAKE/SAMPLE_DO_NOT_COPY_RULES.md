# Sample Do Not Copy Rules

Status: `ACTIVE_ANTI_COPY_POLICY`

## Purpose

Prevent Codex and Claude from turning open-source samples into blind copy
targets.

## Hard Rules

1. Do not copy an entire schematic or PCB layout into an active project.
2. Do not reuse a sample block verbatim just because it looks familiar.
3. Do not copy connector orientation, pin mapping, or footprint choice without
   independent proof.
4. Do not copy package names or values as footprint verification.
5. Do not copy manufacturing outputs from samples into release payloads.
6. Do not treat a broken but human-made sample as an approval signal.

## Allowed Learning Use

Codex and Claude may extract and compare:

- block grouping patterns
- wire-to-label balance
- connector edge-placement patterns
- board-size ranges
- USB path compactness
- buck-regulator clustering
- general routing-angle tendencies

They must still prove every engineering claim against the active project's own
rules, datasheets, and gate reports.

## Required Warning

Reference samples are evidence of how another human laid out a board, not proof
that the pattern is correct for the current design.
