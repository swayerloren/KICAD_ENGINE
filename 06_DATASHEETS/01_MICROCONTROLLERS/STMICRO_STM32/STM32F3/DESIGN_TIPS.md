# STM32F3 Design Tips

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Practical Tips

- Start from the exact ST product page and order code, not only a family name.
- Use STM32CubeMX for pin-planning assistance, then verify against the datasheet and reference manual.
- Keep SWD and reset accessible on prototypes.
- Keep boot-mode recovery accessible until firmware and option-byte policy are proven.
- Reserve pins for oscillators, USB, CAN/FDCAN, RF, external memory, and analog functions before assigning LEDs or test pads.
- Review every supply pin and analog rail before assuming a generic STM32 decoupling pattern.
- Use official Nucleo/Discovery/EVAL schematics as references only after matching exact board revision.

## Family-Specific Watch Items

- analog partitioning
- VREF and VDDA filtering
- comparator/op-amp pin mapping
- motor-control noise containment

## AI No-Guess Rules

- Do not invent clock values, capacitor values, regulator current, USB pullups, CAN termination, crystal load capacitors, or pin alternate functions.
- Mark missing values as `UNKNOWN_REQUIRES_SOURCE` or `NEEDS_RESEARCH`.
- Do not approve a KiCad footprint without exact package drawing evidence.
