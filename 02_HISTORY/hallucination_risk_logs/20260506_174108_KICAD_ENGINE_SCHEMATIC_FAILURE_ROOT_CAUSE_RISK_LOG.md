# Hallucination Risk Log: KiCad Engine Schematic Failure Root-Cause

Date: 2026-05-06

## Risk

Agents may hallucinate that a gate passed because a formal-looking report exists, a command exited successfully, or a generated file uses the word `PASS`.

## Specific Failure Mode

For schematic visual work, generated close-up crops and narrow text screening were over-read as human-readable schematic approval.

## Required Mitigation

- Treat `AUTOMATED_CROP_PASS_ONLY` as evidence generation only.
- Require rendered-image inspection before `VISUAL_PASS`.
- Keep PCB update blocked unless the schematic-to-PCB gate is exactly `PASS`.
- Reject stale reports that say only `Close-up visual review status: PASS` without block-by-block rendered-image inspection.

## Status

OPEN until all visual gate repair plan items are complete and tested.
