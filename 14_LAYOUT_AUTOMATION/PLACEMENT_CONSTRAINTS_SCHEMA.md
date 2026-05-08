# Placement Constraints Schema

## Purpose

Define the normalized JSON schema used by the automatic placement scripts.

## Top-Level Object

```json
{
  "project": "ESP32_CSI_WIFI_NODE",
  "board": {
    "width_mm": 24.0,
    "height_mm": 60.0,
    "shape": "rounded_rectangle",
    "edge_clearance_mm": 1.0
  },
  "placement_settings": {
    "default_gap_mm": 0.5,
    "group_gap_mm": 1.0,
    "test_pad_row_gap_mm": 1.0
  },
  "components": []
}
```

## Component Object

Each component should use:

```json
{
  "ref": "J2",
  "role": "USB_C",
  "group": "USB_PATH",
  "width_mm": 8.9,
  "height_mm": 7.4,
  "courtyard_width_mm": 9.5,
  "courtyard_height_mm": 8.2,
  "preferred_edge": "bottom",
  "rotation_deg": 0,
  "side": "top",
  "fixed_mechanical": true,
  "must_be_accessible": true,
  "requires_keepout": false,
  "keepout_width_mm": 0.0,
  "keepout_height_mm": 0.0,
  "anchor_ref": null,
  "current_flow_order": 0,
  "notes": "USB-C mouth faces off-board."
}
```

## Role Expectations

Recognized high-value roles:

- `MOUNTING_HOLE`
- `USB_C`
- `BARREL_JACK`
- `EDGE_CONNECTOR`
- `RF_MODULE`
- `RF_CONNECTOR`
- `ESD_USB`
- `USB_SERIES`
- `USB_CC`
- `FUSE`
- `TVS`
- `PMOS_PROTECTION`
- `INPUT_CAP`
- `REGULATOR`
- `INDUCTOR`
- `OUTPUT_CAP`
- `DECOUPLING_CAP`
- `MCU_SUPPORT`
- `RESET_BUTTON`
- `BOOT_BUTTON`
- `LED`
- `TEST_PAD`
- `PASSIVE_LOW_RISK`

## Derived Fields

The generator may add:

- `placement_stage`
- `stage_name`
- `must_be_edge_facing`
- `must_be_near_ref`
- `must_be_near_edge`
- `must_avoid_keepout_refs`
- `placement_priority`

## Required Validity Rules

- Every component must have `ref`, `role`, `width_mm`, `height_mm`, `courtyard_width_mm`, and `courtyard_height_mm`.
- Every board must define width, height, shape, and edge clearance.
- Edge connectors must define `preferred_edge`.
- RF modules must define keepout dimensions.
- Fixed mechanical components must be marked `fixed_mechanical: true`.
- Test pads must be marked `must_be_accessible: true`.

## Failure Conditions

Treat the schema input as blocked if:

- board dimensions are missing
- a fixed mechanical connector has no preferred edge
- an RF module has no keepout dimensions
- a component has no courtyard dimensions
- required placement roles are missing from the plan
