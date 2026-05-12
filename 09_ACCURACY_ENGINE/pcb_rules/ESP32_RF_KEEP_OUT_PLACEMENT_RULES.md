# ESP32 RF Keepout Placement Rules

Status: `MANDATORY_FOR_ESP32_MODULE_LAYOUT`

These rules apply to ESP32 module boards, especially WROOM, WROVER, MINI, and U.FL/pigtail variants.

Use `08_COMPONENT_DATABASE/mechanical_orientation/esp32_module_antenna_orientation_rules.md` as the orientation truth reference for antenna-facing checks.

## Placement Rule

For ESP32 module boards, place the module near the top edge with the antenna/U.FL/RF keepout facing the top edge unless there is a documented reason not to.

The RF keepout must not be trapped in the board middle.

## Keepout Must Be Clear Of

- Copper zones.
- Routed traces.
- Vias.
- Components.
- Mounting holes.
- Test pads.
- Silkscreen clutter.
- Enclosure posts.
- Connector shells or cable paths.

## Footprint Width Check

Before accepting a compact board:

1. Compare the ESP32 footprint/courtyard/keepout width to board width.
2. If the footprint or keepout extends beyond the board side edges, classify:
   - `BLOCKED_BY_U2_FOOTPRINT_WIDTH`, or
   - `REQUIRES_LJ_EXPLICIT_ACCEPTANCE`.
3. Do not silently accept a centered module whose keepout/courtyard hangs over a narrow board.

## Mounting Hole Rule

Do not place mounting holes inside or adjacent to the ESP32 antenna/U.FL/RF keepout unless a manufacturer mechanical drawing explicitly permits it.

Top corner holes on narrow ESP32 module boards are often not practical. Use two-hole or shifted-hole strategies only when documented and approved.

## Routing Gate

Routing is blocked until:

- RF keepout direction is verified.
- Keepout is clear.
- Board width versus module footprint is accepted.
- Any drill, pad, or footprint-library issue on the ESP32 module is classified and resolved or explicitly accepted.
