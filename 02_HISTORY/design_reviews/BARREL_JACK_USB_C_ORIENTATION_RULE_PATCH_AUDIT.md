# Barrel Jack And USB-C Orientation Rule Patch Audit

Status: `ACTIVE_EVIDENCE`

Generated: `2026-05-07`

Project: `ESP32_CSI_WIFI_NODE`

## Scope

Documentation, rules, prompt-pack, memory, and history update only. No KiCad schematic, PCB, project, symbol, footprint, routing, copper-zone, BOM, CPL, STEP, Gerber, or fabrication-output files were edited or generated.

## Image Evidence Status

LJ provided the barrel jack reference image in chat. The image was visible in the conversation but not exposed as a binary file in the current Codex environment.

Required image paths:

- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\references\connector_orientation\barrel_jack_front_back_reference.png`
- `10_KNOWLEDGE_BASE\connectors\images\barrel_jack_front_back_reference.png`

Current status: `MANUAL_SAVE_REQUIRED`

Placeholder records were created at:

- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\references\connector_orientation\barrel_jack_front_back_reference_IMAGE_MANUAL_SAVE_REQUIRED.md`
- `10_KNOWLEDGE_BASE\connectors\images\barrel_jack_front_back_reference_IMAGE_MANUAL_SAVE_REQUIRED.md`

## Barrel Jack Rule Added

For horizontal DC barrel jacks:

- female circular opening = `FRONT / MATING SIDE`
- 3-pin solder-leg side = `BACK / REAR SIDE`
- edge-mounted opening faces off-board
- bottom-edge opening faces down/off-board
- bottom-edge 3-pin solder side faces up/inward
- do not approve from coordinates alone
- require 3D when available, footprint geometry, and manufacturer/product-image evidence

## USB-C Rule Strengthened

USB-C edge placement now requires:

- receptacle mouth/opening faces off-board
- bottom-edge mouth faces down/off-board
- footprint `PCB Edge` indicator aligns with board `Edge.Cuts`
- pads remain on-board
- shell/body overhang is mechanically expected by the footprint
- no approval from coordinates alone
- 2D footprint proof and 3D screenshot proof where available

## Validation Summary

- Barrel jack rule file created: `YES`
- Connector edge rules updated: `YES`
- Pill-style rules and checklist updated: `YES`
- Prompt pack updated: `YES`
- Global memory updated: `YES`
- Project memory updated: `YES`
- KiCad design files changed: `NO`
- Routing allowed: `NO`

