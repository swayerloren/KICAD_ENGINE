# Thermal Mechanical Rules

## Canonical Status

This file is the canonical rule surface for thermal and mechanical layout
interaction.

## Mandatory Rules

- Keep heat-generating parts away from antenna keepouts and sensitive connectors when practical.
- Preserve mechanical access for USB, barrel jacks, buttons, and mounting hardware.
- Review whether thermal relief, copper spreading, or exposed-pad grounding is required for hot parts.
- Do not bury service buttons, test pads, or connectors behind tall or hot components.
- Move silkscreen references away from pads, holes, and mechanical hardware.

## Blocking Conditions

- hot part crowds RF or connector mouth
- mechanical access is blocked by part height or copper use
- silkscreen reference overlaps pads, holes, or hardware
- enclosure or user-access assumptions are guessed instead of reviewed

## Source Registry References

- `url_004538` - JLCPCB assembly design-requirements reference
- `url_004540` - JLCPCB PCB design-guideline reference
- `url_006903` - Eurocircuits PCB design-guideline reference
