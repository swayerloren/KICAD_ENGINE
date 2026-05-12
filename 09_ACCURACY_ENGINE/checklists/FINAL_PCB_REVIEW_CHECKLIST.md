# Final PCB Review Checklist

Use with:

- `09_ACCURACY_ENGINE/pcb_rules/TRACE_ANGLE_ROUTING_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/PCB_ROUTING_QUALITY_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/USB_C_LAYOUT_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/BUCK_REGULATOR_LAYOUT_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/ESP32_RF_ANTENNA_LAYOUT_RULES.md`
- `09_ACCURACY_ENGINE/verification_rules/FOOTPRINT_DATASHEET_MATCH_RULES.md`

## Checks

- ERC evidence exists.
- Schematic parity passes.
- DRC passes.
- No unrouted nets remain.
- PCB quality gate passes.
- Trace geometry passes.
- USB routing passes.
- Power-width checks pass.
- Connector orientation proof passes or approved exception exists.
- RF keepout proof passes.
- GND zones and stitching are reviewed.
- Test pads remain short-stub leaf access points.
- Silkscreen is clear of pads and holes.
- Human review decisions are recorded.
