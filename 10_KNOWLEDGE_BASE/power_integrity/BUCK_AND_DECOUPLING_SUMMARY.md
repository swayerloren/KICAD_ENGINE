# Buck And Decoupling Summary

## Key Points

- Keep hot loops small.
- Keep input and output capacitors local to the switching cluster.
- Keep `BUCK_SW` short and isolated from USB, RF, and controls.
- Local decoupling belongs near the pins it supports.

## Canonical Rule Links

- `09_ACCURACY_ENGINE/pcb_rules/BUCK_REGULATOR_LAYOUT_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/POWER_INTEGRITY_DECOUPLING_RULES.md`
- `09_ACCURACY_ENGINE/schematic_rules/BUCK_REGULATOR_SCHEMATIC_RULES.md`
- `09_ACCURACY_ENGINE/schematic_rules/DECOUPLING_SCHEMATIC_RULES.md`

## Source Registry References

- `url_010082`
- `url_010083`
- `url_009893`
- `url_009915`
- `url_009918`
