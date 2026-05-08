# J1 Barrel Jack Orientation Reference

Status: `ACTIVE_PROJECT_REFERENCE`

Generated: `2026-05-07`

Project: `ESP32_CSI_WIFI_NODE`

## Reference Image

Required saved image path:

`04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\references\connector_orientation\barrel_jack_front_back_reference.png`

Current image status: `MANUAL_SAVE_REQUIRED`

Reason: LJ provided the reference image in chat, but the current Codex environment cannot copy the embedded chat image as a binary file. Placeholder record:

`04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\references\connector_orientation\barrel_jack_front_back_reference_IMAGE_MANUAL_SAVE_REQUIRED.md`

## Physical Rule

For CUI/PJ-102AH-style horizontal DC barrel jacks:

- female barrel opening = `FRONT / MATING SIDE`
- 3-pin solder legs = `REAR / BACK SIDE`
- the connector opening must face off-board when used as an edge connector
- the solder pins/backside must face inward toward the PCB body

## J1 Bottom-Edge Placement Rule

For bottom-edge J1 placement:

- female opening faces `DOWN / OFF-BOARD`
- 3-pin solder side faces `UP / INWARD`
- J1 must not be side-mounted unless LJ explicitly approves a side-entry mechanical concept

## Hard Warning

If the 3-pin solder-leg side is closest to the bottom edge, J1 is flipped wrong.

## Current Project Implication

J1 must not be approved until this front/back rule is satisfied in PCB layout and verified by 2D footprint geometry and preferably 3D model evidence.

Do not call J1 orientation `PROVEN` from coordinates alone. Coordinates can locate the part, but they do not identify the connector mouth unless tied to footprint primitives, a manufacturer drawing, a product image, or a verified 3D model.

## 3D Model Note

If the KiCad STEP model is missing, do not claim 3D proof. Use 2D footprint evidence from `F.Fab`, `F.SilkS`, `F.CrtYd`, pad geometry, and a manufacturer/product-image front/back reference as limited proof, and mark:

`3D_PROOF_MISSING`

