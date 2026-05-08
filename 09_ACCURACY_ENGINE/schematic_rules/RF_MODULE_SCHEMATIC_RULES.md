# RF Module Schematic Rules

## Scope

RF modules, antennas, U.FL/IPEX, SMA, matching networks, keepouts, shields, and RF supply filtering.

## Rules

- Use the module vendor hardware design guide.
- Verify every module pad against the module datasheet.
- Preserve required no-connect, keepout, antenna, and ground pad rules.
- Do not add arbitrary RF matching parts without a source-backed reference design.
- Flag antenna path, connector orientation, and feedline layout for human review.
- Check RF module peak-current and decoupling requirements.
- Treat regulatory/module certification notes as design constraints.

## Required Review Flags

- `RF_MODULE_PINOUT_VERIFIED`
- `RF_ANTENNA_KEEP_OUT_REVIEW_REQUIRED`
- `RF_CONNECTOR_ORIENTATION_HUMAN_REVIEW_REQUIRED`
- `RF_LAYOUT_REVIEW_REQUIRED`
- `RF_CERTIFICATION_NOTE_REVIEW_REQUIRED`

## Exit Criteria

RF schematic blocks are not complete until module pinout, antenna/connector strategy, keepout, and layout constraints are reviewed.
