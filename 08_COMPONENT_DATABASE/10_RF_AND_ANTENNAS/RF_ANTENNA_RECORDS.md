# RF And Antenna Records

Date: 2026-05-02

Status: generic placeholders. These records are routing and review prompts, not approved RF parts.

## Records

| Record ID | Part / Topic | Category | Status | Primary Checks |
| --- | --- | --- | --- | --- |
| `RF_ANTENNA_PIGTAIL_GENERIC` | RF antenna pigtail generic | Cable/antenna accessory | `UNVERIFIED_PLACEHOLDER` | Connector family, gender, cable loss, frequency range, strain relief |
| `RF_PCB_ANTENNA_KEEPOUT_GENERIC` | PCB antenna keepout generic | Layout keepout | `UNVERIFIED_PLACEHOLDER` | Vendor keepout, board edge clearance, copper restriction, enclosure proximity |
| `RF_UFL_TO_SMA_PIGTAIL_GENERIC` | U.FL to SMA pigtail generic | Cable transition | `UNVERIFIED_PLACEHOLDER` | U.FL/IPEX series, SMA or RP-SMA gender, cable length/loss, mating connector |

## RF Antenna Pigtail Generic

- Use for: documenting that an off-board antenna cable is required.
- Do not use for: selecting a board connector or antenna without exact RF and mechanical details.
- Layout warning: cable exit path and connector strain relief must be reviewed in 3D/mechanical context.

## PCB Antenna Keepout Generic

- Use for: documenting copper and component keepout intent around a PCB antenna or module antenna.
- Do not use for: final layout without the antenna or module vendor drawing.
- Layout warning: keepouts affect copper pours, vias, board outline, mounting holes, enclosure material, and nearby cables.

## U.FL To SMA Pigtail Generic

- Use for: documenting a common lab or enclosure transition from a board RF connector to an SMA-family external connector.
- Do not use for: assuming U.FL/MHF compatibility or SMA/RP-SMA gender.
- Layout warning: board-side connector footprint, pigtail height, cable bend radius, and enclosure clearance must all be checked.

## Promotion Checklist

- Exact cable or antenna vendor part selected.
- Frequency range, insertion loss, VSWR/return loss, and connector family recorded.
- Mating connector and gender verified.
- 3D/mechanical clearance reviewed.
- PCB feedline and connector footprint reviewed against stackup.
