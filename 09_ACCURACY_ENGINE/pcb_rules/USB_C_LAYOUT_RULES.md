# USB-C Layout Rules

## Canonical Status

This file is the canonical PCB layout rule surface for USB-C receptacles and
their local support circuitry.

## Mandatory Rules

- Place the USB-C receptacle on the intended board edge with the mouth facing off-board.
- Keep the USB local cluster compact:
  - `J2 -> ESD -> series resistors -> MCU/module USB pins`
- Keep `CC1` and `CC2` resistors close to the receptacle.
- Keep `D+` and `D-` short, paired, and visually parallel where practical.
- Avoid long USB stubs, loopbacks, or perimeter detours.
- Do not route USB through RF keepouts or across broken return paths.
- Shield, shell, and chassis strategy must be an intentional reviewed decision.

## Blocking Conditions

- connector mouth faces inward
- `CC` resistors are remote from the connector
- USB data path is long, split, or obviously unpaired
- USB route crosses RF keepout or obvious return-path split
- USB layout relies on guessed connector orientation

## Required Evidence

- connector orientation proof
- USB layout checklist
- trace-geometry audit
- PCB quality gate USB result

## Source Registry References

- `url_009659` - TI USB layout app note
- `url_009667` - TI USB-C / interface layout app note
- `url_009899` - TI USB protection/layout app note
- `url_009900` - TI USB protection/layout app note
- `url_009901` - TI USB protection/layout app note
