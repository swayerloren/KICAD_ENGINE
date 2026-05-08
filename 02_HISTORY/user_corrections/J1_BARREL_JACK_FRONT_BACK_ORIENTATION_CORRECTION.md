# J1 Barrel Jack Front/Back Orientation Correction

Status: `USER_CONFIRMED`

Generated: `2026-05-07`

Project: `ESP32_CSI_WIFI_NODE`

## Correction

LJ provided a physical reference image and clarified that for CUI/PJ-102AH-style horizontal DC barrel jacks:

- female circular barrel opening = `FRONT / MATING SIDE`
- 3-pin solder-leg side = `BACK / REAR SIDE`
- bottom-edge female opening must face `DOWN / OFF-BOARD`
- bottom-edge 3-pin solder side must face `UP / INWARD`

## Required Behavior Change

Codex/Claude must not confuse the 3-pin solder side with the barrel opening. Do not approve barrel jack orientation from coordinates alone. Use exact 3D model when available, footprint `F.Fab`/`F.SilkS`/`F.CrtYd`, and manufacturer/product-image evidence.

## Evidence Records

- `09_ACCURACY_ENGINE\pcb_rules\BARREL_JACK_ORIENTATION_RULES.md`
- `10_KNOWLEDGE_BASE\connectors\BARREL_JACK_ORIENTATION_GUIDE.md`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\references\connector_orientation\J1_BARREL_JACK_ORIENTATION_REFERENCE.md`

Image binary status: `MANUAL_SAVE_REQUIRED`

