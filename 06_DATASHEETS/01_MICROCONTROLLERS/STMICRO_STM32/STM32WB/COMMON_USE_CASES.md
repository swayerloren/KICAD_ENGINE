# STM32WB Common Use Cases

Date: 2026-05-03
Status: `SCAFFOLDED_WITH_AI_SUMMARIES`

## Good Fits

- BLE sensor nodes
- Wireless control products
- Thread/Zigbee-like 802.15.4 designs where supported
- Low-power connected devices

## Design Focus Areas

- RF matching
- antenna keepout
- HSE/LSE clock source
- wireless stack and certification

## When To Avoid

Avoid if RF layout, antenna matching, certification, or wireless firmware maintenance cannot be reviewed.

## AI Agent Selection Rules

- Do not select `STM32WB` only because an example board used it.
- Match required peripherals, voltage domains, memory, package, lifecycle, programming path, and library support before creating a schematic.
- Treat every exact electrical, timing, and package value as `UNKNOWN_REQUIRES_SOURCE` until official part-level sources are recorded.
- For a real KiCad design, create or update a component database record before placing a symbol.
