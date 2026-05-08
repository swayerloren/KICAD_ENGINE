# {family} Common Mistakes

Date: {date}
Status: `AI_REVIEW_CHECKLIST`

This file lists mistakes that AI agents must check for when reviewing `{family}` designs.

## Evidence Labels

{evidence_labels}

## Schematic Mistakes

- `NEEDS_HUMAN_REVIEW`: assuming pinout or boot behavior from another package or family.
- `NEEDS_HUMAN_REVIEW`: hidden power pins causing incomplete power nets.
- `NEEDS_HUMAN_REVIEW`: missing reset/debug/programming access.
- `NEEDS_HUMAN_REVIEW`: oscillator values copied without source review.
- `NEEDS_HUMAN_REVIEW`: USB/CAN/RF/power-interface circuits copied from memory.

## PCB Mistakes

- `NEEDS_HUMAN_REVIEW`: footprint selected by package name only.
- `NEEDS_HUMAN_REVIEW`: pin 1 orientation not checked against package drawing.
- `NEEDS_HUMAN_REVIEW`: decoupling placed too far from supply pins.
- `NEEDS_HUMAN_REVIEW`: high-speed, RF, USB, or power layout rules skipped.

## Agent Rule

If any item appears in a project, block promotion until evidence or human acceptance exists.
