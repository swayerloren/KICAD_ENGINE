# Net Class Schema

## Purpose

Define the normalized net-class fields consumed by the routing engine.

## Required Fields

Each net class must define:

- `width_mm`
- `clearance_mm`
- `allowed_layers`
- `via_allowed`

## Recommended Fields

- `max_vias`
- `pair_routing`
- `impedance_sensitive`
- `high_current`
- `review_required`
- `notes`

## Example

```json
{
  "POWER_5V": {
    "width_mm": 0.75,
    "clearance_mm": 0.25,
    "allowed_layers": ["F.Cu", "B.Cu"],
    "via_allowed": true,
    "max_vias": 1,
    "high_current": true
  },
  "USB_PAIR": {
    "width_mm": 0.25,
    "clearance_mm": 0.15,
    "allowed_layers": ["F.Cu", "B.Cu"],
    "via_allowed": true,
    "max_vias": 1,
    "pair_routing": "MATCHED_PAIR",
    "impedance_sensitive": true,
    "review_required": true
  }
}
```

## Interpretation Rules

- Power net classes should carry wider trace defaults than general signals.
- USB pair classes should declare pair-routing sensitivity.
- RF-adjacent or impedance-sensitive classes should always remain review-required.
- A net that references an unknown net class is invalid input.
