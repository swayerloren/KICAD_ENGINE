# PCB Placement Ready Checklist

Use with:

- `09_ACCURACY_ENGINE/pcb_rules/USB_C_LAYOUT_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/BUCK_REGULATOR_LAYOUT_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/ESP32_RF_ANTENNA_LAYOUT_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/MOUNTING_HOLE_MECHANICAL_RULES.md`

## Checks

- Connector orientation proof exists for `J1` / `J2` or the connector is blocked.
- ESP32 antenna edge and keepout are proven.
- USB local cluster is compact and on the correct edge.
- Buck cluster is compact and not crowding USB or RF.
- Test pads are grouped and not mixed into sensitive clusters.
- Mounting-hole count and clearances are proven.
- Silkscreen references are clear of pads and holes.
- At least three prelayout variants exist.
- One selected variant passes the prelayout gate.
