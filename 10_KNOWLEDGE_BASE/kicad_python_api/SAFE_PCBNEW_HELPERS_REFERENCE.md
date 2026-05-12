# Safe Pcbnew Helpers Reference

Status: `NORMALIZED_REFERENCE`

The repo helper module is:

- `03_TOOLS/scripts/kicad_api/safe_pcbnew_helpers.py`

## Intended Helpers

- `safe_call`
  - guarded method call with a default fallback
- `safe_net_name`
  - read item net name without assuming every object exposes the same chain
- `safe_layer_name`
  - resolve a readable layer name when possible
- `safe_track_width`
  - width lookup for track-like items
- `safe_via_drill`
  - drill lookup for via-like items
- `safe_position`
  - extract XY when available

## Rule

Use helpers for extraction and reporting. Do not use them as proof that KiCad
validation passed.

## Source Registry References

- `url_000951`
- `url_000954`
- `url_000956`
- `url_000959`
- `url_000960`
- `url_000962`
