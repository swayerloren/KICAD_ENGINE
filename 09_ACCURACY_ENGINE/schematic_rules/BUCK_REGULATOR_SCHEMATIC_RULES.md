# Buck Regulator Schematic Rules

## Mandatory Rules

- The input path, regulator IC, inductor, output capacitors, and feedback/support parts must read as one functional block.
- Show the power flow in order:
  - input
  - protection if present
  - regulator
  - inductor
  - output storage/distribution
- Keep local regulator support connections wired when that improves readability.
- Do not scatter bootstrap, feedback, compensation, or enable parts across unrelated regions.
- Values may remain unknown only when explicitly marked in review records, not as a hidden guess.

## Blocking Conditions

- regulator support parts are visually detached
- power flow order is unclear
- support nets are label-heavy when local wiring would be clearer

## Source Registry References

- `url_010082` - ROHM buck PCB layout application note
- `url_010083` - onsemi switching-converter layout note
- `url_009915` - TI TPS62180 datasheet
- `url_009918` - TI TPS62933 datasheet
