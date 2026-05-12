# Buck Regulator Layout Rules

## Canonical Status

This file is the canonical buck-layout rule surface for switching regulators.

## Mandatory Rules

- Keep the hot switching loop as small as possible.
- Keep input capacitors close to the regulator input and power ground return.
- Keep the switch node, bootstrap parts, and inductor tightly clustered.
- Keep output capacitors close to the inductor and regulator output return.
- Keep `BUCK_SW` short and away from USB, RF, reset/boot, and antenna areas.
- Do not route sensitive nets through the switch-node field.
- Use direct return paths and avoid split-ground current loops.

## Review Rules

- Regulator cluster review must explicitly call out:
  - input loop
  - switch loop
  - output loop
  - `BUCK_SW` exposure
  - noisy-to-sensitive spacing

## Blocking Conditions

- long `BUCK_SW`
- input/output caps remote from the regulator cluster
- switch-node copper under or through sensitive regions
- regulator placement that forces perimeter or rectangular power routing

## Source Registry References

- `url_010082` - ROHM buck-converter PCB layout application note
- `url_010083` - onsemi switching-converter layout note
- `url_009893` - TI compensation / layout-related power note
- `url_009915` - TI TPS62180 datasheet
- `url_009918` - TI TPS62933 datasheet
