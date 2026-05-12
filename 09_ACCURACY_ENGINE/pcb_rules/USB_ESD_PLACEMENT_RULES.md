# USB ESD Placement Rules

## Canonical Status

This file defines the required local placement behavior for USB ESD protection.

## Mandatory Rules

- USB ESD devices must sit close to the connector entry point.
- Place ESD before long on-board USB routing.
- Use a short, flow-through path between connector pins, ESD device, and the protected downstream route.
- Keep the ESD return to ground short and low-inductance.
- Do not place the USB ESD part far downstream near the MCU/module if the connector entry remains exposed.

## Blocking Conditions

- ESD device is far from the connector
- USB path makes a long detour before reaching ESD
- ESD placement creates a long stub on `D+` or `D-`
- ESD ground path is obviously long or thin

## Source Registry References

- `url_009904` - TI TPD2E2U06 datasheet
- `url_009905` - TI TPD4E02B04 datasheet
- `url_009906` - TI TPD4E110 datasheet
- `url_009907` - TI TPD4E1U06 datasheet
- `url_010103` - Wurth USB protection/filtering note
