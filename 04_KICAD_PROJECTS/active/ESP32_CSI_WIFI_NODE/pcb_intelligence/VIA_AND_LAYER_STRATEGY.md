# Via And Layer Strategy

Layer assumption from current project planning: 2-layer board.

## Via Policy By Net Type

- GND: use stitching/return vias near USB ESD, regulator ground, and board perimeter only where they do not clutter or enter RF keepout.
- `/BUCK_SW` and `/BUCK_BST`: avoid vias; keep on same layer and very short.
- USB D+/D-: avoid vias; if unavoidable, use symmetric pair treatment and keep stubs minimal.
- +5 V and +3V3: vias acceptable when current path and return path remain low impedance.
- Low-speed/debug/test nets: vias acceptable after critical routing.

## No-Via Areas

- ESP32 RF keepout.
- Connector mechanical overhang/cable path areas.
- Mounting-hole clearance areas.
