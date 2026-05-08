# Hallucination Risk Log: MCU Datasheet Tree Upgrade

Date: 2026-05-03
Risk: `MEDIUM`

## Risk

Large generated datasheet trees can create false confidence if agents mistake structured stubs for researched component knowledge.

## Mitigations Used

- Generated files mark unknowns `UNKNOWN_REQUIRES_SOURCE`.
- Verification statuses remain `UNVERIFIED` or `NEEDS_HUMAN_REVIEW`.
- No exact datasheet specifications were invented.
- No footprints, pinouts, or package drawings were approved.
- Reports explicitly classify the output as scaffolded summaries.

## Required Future Behavior

Before using any generated MCU file for schematic or PCB work, agents must add official source links and verify exact part, pinout, package, symbol, footprint, boot/debug, power, clock, and layout data.
