# USB Layout Rules

## Scope

USB data pairs, USB-C connector footprints, VBUS, ESD, shield, and routing.

## Rules

- Verify connector footprint and orientation.
- Route differential pairs with appropriate geometry for the project/fab.
- Avoid stubs and unnecessary vias.
- Place ESD protection near connector when used.
- Review VBUS fuse/protection path.
- Treat shield/shell connection as an intentional design decision.

## Required Flags

- `USB_LAYOUT_REVIEW_REQUIRED`
- `USB_CONNECTOR_ORIENTATION_HUMAN_REVIEW_REQUIRED`
- `USB_DIFF_PAIR_REVIEW_REQUIRED`
- `USB_ESD_PLACEMENT_REVIEW_REQUIRED`
