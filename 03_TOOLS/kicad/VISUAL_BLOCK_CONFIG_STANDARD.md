# Visual Block Config Standard

## Purpose

Project-specific visual block configs tell KiCad Engine where to crop a full-page schematic render for close-up review.

Default path:

`_verification/schematic_visual/visual_blocks.json`

## Schema

```json
{
  "schema": "kicad_engine.schematic_visual_blocks.v1",
  "coordinate_system": "normalized",
  "blocks": [
    {
      "name": "input_power",
      "title": "Input Power",
      "units": "normalized",
      "x": 0.02,
      "y": 0.06,
      "width": 0.22,
      "height": 0.24,
      "review_required": true,
      "notes": "Adjust per project."
    }
  ]
}
```

## Coordinates

Supported `units`:

- `normalized`: `x`, `y`, `width`, and `height` are fractions of the SVG viewBox.
- `svg` or `viewbox`: coordinates are direct SVG viewBox units.

Normalized coordinates are portable across page sizes but may need manual tuning. SVG coordinates are more exact but tied to the KiCad export viewBox.

## Required Default Block Names

- `input_power`
- `reverse_polarity`
- `tvs_input_cap`
- `buck_regulator`
- `esp32_module`
- `usb_c_connector`
- `usb_esd`
- `cc_resistors`
- `reset_boot`
- `leds`
- `test_pads`
- `mounting_holes`
- `mechanical_notes`

## AI Agent Rules

- Do not treat default block positions as verified.
- Adjust block coordinates only in the project config, not in KiCad design files.
- Regenerate crops after config changes.
- Link `CLOSE_UP_REVIEW.md` and crop paths from the schematic-to-PCB gate status.
- Keep unresolved crop misses as `VISUAL_REVIEW_INCOMPLETE`.

## Public Release Notes

Visual block configs may contain project layout information but should not contain secrets. They are generated review configuration, not fabrication output.
