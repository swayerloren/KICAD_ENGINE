# AI Reliability Memory

Status: `ACTIVE_PROJECT_MEMORY`

Project-specific reliability rules for AI work on `ESP32_CSI_WIFI_NODE`.

## Rules

- Treat all connector, RF, USB-C, power-path, regulator, footprint, and pinout claims as high-risk until source-backed.
- Keep the project `NOT_FINAL` until ERC, DRC, BOM, datasheet, symbol, footprint, connector, polarity, mechanical, and visual review gates pass.
- Do not infer exact ESP32 module, USB-C connector, barrel jack, U.FL/SMA, regulator, or mounting footprint correctness from generic library candidates.

