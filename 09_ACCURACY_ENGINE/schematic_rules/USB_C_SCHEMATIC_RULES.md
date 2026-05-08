# USB-C Schematic Rules

## Scope

USB-C receptacles, USB2-only designs, full-feature designs, VBUS power paths, CC pins, ESD, shields, and connector footprints.

## Rules

- Identify whether the connector is USB2-only, USB3/full-feature, power-only, source, sink, or dual-role.
- Use the exact receptacle pinout and footprint.
- Verify CC resistor requirements from the intended role.
- Do not short or ignore SuperSpeed pins on a full-feature connector without design intent.
- Protect USB data and VBUS where required.
- Treat shield and shell connections as design decisions.
- Check VBUS voltage/current path and fuse/protection.

## Required Review Flags

- `USB_C_CONNECTOR_ORIENTATION_HUMAN_REVIEW_REQUIRED`
- `USB_CC_ROLE_REVIEW_REQUIRED`
- `USB_ESD_REVIEW_REQUIRED`
- `USB_VBUS_POWER_PATH_REVIEW_REQUIRED`
- `USB_LAYOUT_REVIEW_REQUIRED`

## Exit Criteria

USB-C schematic blocks are not complete until connector pin numbering, CC behavior, VBUS handling, ESD/protection, and layout constraints are reviewed.
