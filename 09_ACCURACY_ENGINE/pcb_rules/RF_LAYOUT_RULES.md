# RF Layout Rules

## Scope

RF modules, antennas, feedlines, U.FL/IPEX, SMA, keepouts, ground stitching, and matching networks.

## Rules

- Follow the module or antenna layout guide.
- Preserve antenna keepouts.
- Keep RF feedline geometry source-backed.
- Do not guess impedance geometry.
- Avoid copper under keepout regions where prohibited.
- Review connector orientation and launch geometry.
- Keep matching network footprints close to the RF path when used.

## Required Flags

- `RF_LAYOUT_REVIEW_REQUIRED`
- `RF_FEEDLINE_REVIEW_REQUIRED`
- `RF_ANTENNA_KEEP_OUT_REVIEW_REQUIRED`
- `RF_CONNECTOR_ORIENTATION_HUMAN_REVIEW_REQUIRED`
