# Case Study Source Index

Status: `LINK_FIRST_INDEX`

## Confidence Tiers

- `HIGH`: official manufacturer app notes, datasheets, or KiCad docs
- `MEDIUM`: university or structured training material
- `LOW_TO_MEDIUM`: fabricator workflow notes and mixed tutorials
- `LOW`: forum/video/search/index captures

## Good-Board Example Inputs

- `url_000043` `docs.espressif.com`
- `url_010086` `ti.com`
- `url_010093` `ti.com`
- `url_010100` `ti.com`

## Bad-Board Example Inputs

- `url_010180` `pcb.mit.edu`
- `url_008388` `richtek.com`

## Source Handling

- Official-source lessons should already be represented in
  `09_ACCURACY_ENGINE/`, `33_PCB_PRELAYOUT_ENGINE/`, `34_SCHEMATIC_QUALITY_ENGINE/`,
  or `35_FOOTPRINT_PACKAGE_ENGINE/`.
- Low-confidence captures remain raw only in quarantine or migration history.

