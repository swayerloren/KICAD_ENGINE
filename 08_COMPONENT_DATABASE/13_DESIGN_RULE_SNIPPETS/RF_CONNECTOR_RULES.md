# RF Connector Rules

Date: 2026-05-02

Status: mandatory RF connector guidance. Generic RF connector records are placeholders only.

## Core Rule

RF connector choice includes connector geometry, board stackup, impedance launch, ground return, antenna cable, and enclosure. A footprint alone is not an RF design.

## U.FL / IPEX MHF1

- Verify exact brand and family: Hirose U.FL, I-PEX MHF1, or compatible variants are not automatically identical.
- Verify connector height and mating cable plug.
- Verify mating-cycle limit and whether the connector is serviceable by users.
- Place close to the RF module or matching network.
- Maintain keepout around the connector and cable path.
- Do not route high-current or noisy digital lines under the RF launch.

## SMA Edge Launch

- Edge-launch SMA footprints depend on board thickness, dielectric stackup, copper thickness, launch geometry, and connector model.
- Use the connector manufacturer's launch recommendation for the selected board stackup.
- Add ground vias according to the connector guidance.
- Keep solder mask, copper clearance, and edge plating assumptions explicit.
- Verify whether the connector is end-launch, vertical, right-angle, or bulkhead style.

## RP-SMA Pigtail

- RP-SMA pigtail usually means a cable assembly with a panel/bulkhead connector and a board-end connector such as U.FL/MHF.
- The PCB footprint may be for the board-end connector, not the RP-SMA connector.
- Verify cable length, bend radius, antenna connector gender, panel hole, nut/washer clearance, and strain relief.

## Common Mistakes

- Treating U.FL and MHF variants as interchangeable.
- Using an SMA edge footprint without checking board thickness.
- Placing RF connectors under enclosure features or too close to mounting screws.
- Forgetting antenna keepout and cable bend space.
- Using an RP-SMA symbol as if it were a direct board footprint.
- Ignoring 50 ohm launch and ground via requirements.

## AI Release Rule

RF connector records remain `UNVERIFIED_PLACEHOLDER` until exact connector, mating cable, board stackup, launch geometry, 3D clearance, and RF routing review are complete.
