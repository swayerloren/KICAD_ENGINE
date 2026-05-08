# Routing Input Schema

## Purpose

Define the normalized JSON input format for the routing-planning and routing-audit scripts under `14_LAYOUT_AUTOMATION/scripts/`.

This schema is for planning, fixture testing, and copied-board analysis. It does not edit KiCad files.

## Required Top-Level Fields

```json
{
  "schema_version": "1.0",
  "project": "STRING",
  "board_path": "STRING",
  "board_outline": {},
  "components": [],
  "footprints": [],
  "pads": [],
  "net_classes": {},
  "nets": [],
  "keepouts": [],
  "zones": [],
  "layer_rules": {},
  "via_rules": {},
  "trace_rules": {},
  "ground_strategy": {},
  "routing_status": {},
  "tracks": [],
  "traces": [],
  "vias": [],
  "not_extracted": []
}
```

## Top-Level Objects

### `board_outline`

Required fields:

- `shape`
- `width_mm`
- `height_mm`
- `allowed_signal_layers`

Optional fields:

- `corner_radius_mm`
- `notes`

### `components`

Each component object should include:

- `ref`
- `kind`
- `x_mm`
- `y_mm`
- `rotation_deg`
- `side`

Optional:

- `fixed_mechanical`
- `notes`

### `pads`

Each pad object should include:

- `id`
- `component`
- `pad_name`
- `net`
- `x_mm`
- `y_mm`
- `layer`

Optional:

- `role`

### `net_classes`

Dictionary keyed by net-class name.

Each net-class object should include:

- `width_mm`
- `clearance_mm`
- `allowed_layers`
- `via_allowed`

Optional:

- `max_vias`
- `pair_routing`
- `notes`

### `nets`

Each net object should include:

- `name`
- `role`
- `net_class`
- `routing_priority`
- `routing_status`

Recommended fields:

- `critical`
- `power`
- `usb`
- `ground`
- `pads`
- `paired_with`
- `must_avoid_keepouts`
- `trace_width_rule`
- `clearance_rule`
- `layer_rule`
- `via_rule`
- `review_required`
- `notes`

### `keepouts`

Each keepout object should include:

- `name`
- `type`
- `xmin`
- `ymin`
- `xmax`
- `ymax`

Optional but supported:

- `geometry`
- `points`
- `layer`
- `source`

Supported `type` values:

- `RF_KEEPOUT`
- `ANTENNA_KEEPOUT`
- `CONNECTOR_KEEPOUT`
- `MECHANICAL_KEEPOUT`

If polygon points are available from KiCad, prefer:

- `geometry: "POLYGON"`
- `points: [{ "x_mm": ..., "y_mm": ... }, ...]`

If exact polygon extraction is not available, use the bounding-box fields and record the limitation under `not_extracted`.

### `layer_rules`

Required fields:

- `available_layers`
- `default_signal_layer`

Optional:

- `usb_preferred_layers`
- `power_preferred_layers`
- `critical_net_layer_bias`

### `via_rules`

Required fields:

- `critical_reason_required`
- `default_allowed`

Optional:

- `max_default_vias`
- `notes`

### `trace_rules`

Required fields:

- `default_width_mm`
- `default_clearance_mm`

Optional:

- `usb_target_width_mm`
- `power_target_widths_mm`
- `avoid_right_angles`

### `ground_strategy`

Required fields:

- `present`
- `strategy`

Optional:

- `stitching_regions`
- `local_return_requirements`
- `notes`

### `routing_status`

Required fields:

- `phase`

Optional:

- `drc_risk`
- `all_critical_planned`
- `unconnected_count`
- `ratsnest_status`
- `notes`

### `traces`

Each trace object should include:

- `id`
- `net`
- `routing_status`
- `critical`
- `via_count`
- `via_reason`
- `segments`

Each segment should include:

- `x1`
- `y1`
- `x2`
- `y2`
- `layer`
- `width_mm`

Optional trace fields:

- `review_required`
- `notes`

## Optional Raw-Board Extraction Fields

When the input was generated from a real `.kicad_pcb`, these additional top-level fields are allowed:

- `board_path`
- `footprints`
- `tracks`
- `vias`
- `zones`
- `edge_cuts`
- `not_extracted`

These fields are for bridge transparency and auditability. The routing engine may ignore them if it only needs the normalized planning fields.

## Required Semantic Coverage

The input must be able to represent:

- board outline
- components
- pads
- nets
- net classes
- critical nets
- power nets
- USB D+/D-
- RF keepouts
- antenna keepouts
- via rules
- trace width rules
- clearance rules
- layer rules
- routing priority
- routing status
- trace-by-trace audit inputs

## Hard-Block Data Conditions

Treat the fixture as invalid when:

- `project` is missing
- `board_outline` is missing
- `nets` is missing or empty
- `net_classes` is missing or empty
- any net references an unknown net class
- USB D+/D- pairing is incomplete in a USB fixture
- keepout objects are malformed
- trace segments are malformed
