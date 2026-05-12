# Buck Regulator Layout Checklist

Rules:

- `09_ACCURACY_ENGINE/pcb_rules/BUCK_REGULATOR_LAYOUT_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/POWER_INTEGRITY_DECOUPLING_RULES.md`

## Checks

- Input capacitor is close to the regulator input loop.
- Switch node is short.
- Inductor is close to the switch node.
- Output capacitors are close to the inductor/regulator output.
- Sensitive nets stay away from `BUCK_SW`.
- Decoupling and return paths are local and direct.
