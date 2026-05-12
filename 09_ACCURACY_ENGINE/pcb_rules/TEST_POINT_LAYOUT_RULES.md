# Test Point Layout Rules

## Canonical Status

This file is the canonical PCB rule surface for test-point placement and
routing access.

## Mandatory Rules

- Test pads must be intentional leaf access points, not long route destinations.
- Test-point stubs longer than `5 mm` are rejected unless explicitly justified.
- Group debug and service test points into a readable access area when practical.
- Keep test pads out of RF keepouts, connector mouths, and tight mechanical zones.
- Do not let test-point convenience ruin USB, RF, or power-loop geometry.

## Blocking Conditions

- long TP stubs
- TP routes create acute or right-angle geometry
- TP placement forces a sensitive net detour
- TP placement blocks connector or mounting access

## Source Registry References

- `url_004538` - JLCPCB assembly design-requirements reference
- `url_004540` - JLCPCB PCB design-guideline reference
- `url_006903` - Eurocircuits PCB design-guideline reference
