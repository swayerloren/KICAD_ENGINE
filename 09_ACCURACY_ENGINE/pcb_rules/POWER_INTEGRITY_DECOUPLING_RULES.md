# Power Integrity Decoupling Rules

## Canonical Status

This file is the canonical rule surface for decoupling placement and basic
power-integrity review.

## Mandatory Rules

- Decoupling capacitors must sit near the IC power pins they support.
- Use the shortest practical path from supply pin to capacitor to return.
- Do not group all capacitors in a remote “cap bank” that ignores individual pin access.
- Keep regulator output decoupling local to the regulator/load handoff.
- Keep digital decoupling returns on a continuous ground reference.
- Treat wide power traces without local decoupling as incomplete.

## Blocking Conditions

- decoupling capacitor is visibly remote from the pin it supports
- power pin reaches the rail before the local capacitor
- return path to ground is indirect or obviously broken
- noisy switch-node copper cuts through decoupling return paths

## Source Registry References

- `url_010082` - ROHM buck PCB layout note
- `url_010083` - onsemi converter layout note
- `url_009915` - TI TPS62180 datasheet
- `url_009918` - TI TPS62933 datasheet
