# PCB Quality Gate

This folder is the enforceable read-only PCB quality gate layer.

Purpose:

- run the real judge checks instead of relying on Codex summaries
- combine KiCad DRC, open-net state, schematic parity, trace geometry, USB sanity, connector truth, zone/GND checks, and silkscreen risk into one gate result
- fail gracefully without editing KiCad design files

The scripts here reuse the repo's existing lower-level engines:

- `03_TOOLS/scripts/pcb_geometry/`
- `03_TOOLS/scripts/mechanical_orientation/`
- `03_TOOLS/scripts/project_state/`
- `14_LAYOUT_AUTOMATION/scripts/`

## Canonical Rule Inputs

Run this gate against the current canonical rules:

- `09_ACCURACY_ENGINE/pcb_rules/TRACE_ANGLE_ROUTING_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/PCB_ROUTING_QUALITY_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/USB_C_LAYOUT_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/USB_ESD_PLACEMENT_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/BUCK_REGULATOR_LAYOUT_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/POWER_INTEGRITY_DECOUPLING_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/GROUNDING_AND_RETURN_PATH_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/ESP32_RF_ANTENNA_LAYOUT_RULES.md`
- `09_ACCURACY_ENGINE/pcb_rules/TEST_POINT_LAYOUT_RULES.md`

## Scripts

- `check_pcb_drc.py`
  - checks KiCad DRC violation count and schematic-parity/footprint mismatch count
  - uses explicit KiCad parity mode: `kicad-cli pcb drc --schematic-parity --severity-all --format report`
- `check_open_nets.py`
  - checks unconnected item count and detectable unrouted nets
- `check_trace_geometry.py`
  - checks 90-degree corners, acute angles, excessive detours, boxy perimeter routing, board-edge crossings, RF keepout crossings, and return-path split risk
- `check_testpoint_stubs.py`
  - checks TP stub length and basic leaf-branch topology
- `check_power_widths.py`
  - checks configured power nets against minimum width rules
- `check_usb_pair_routing.py`
  - checks USB pair geometry findings plus pair length/width sanity from project constraints
- `check_zone_and_gnd_stitching.py`
  - checks GND zone presence, zone fill proof, stitching-via count, and reference/value silkscreen overlap risk
- `check_connector_orientation.py`
  - checks connector mouth direction plus RF keepout direction using the mechanical truth layer
- `pcb_quality_report.py`
  - renders a Markdown report from a saved gate JSON result
- `run_pcb_quality_gate.py`
  - runs the full gate and writes the authoritative result

## Constraint Files

- template: `04_KICAD_PROJECTS/_templates/pcb_routing_constraints.template.yaml`
- active project example: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/config/pcb_routing_constraints.yaml`

These files are intentionally stored as JSON-compatible YAML so the repo can parse them with the Python standard library and stay ZIP-portable.

## Canonical Command

```powershell
python 03_TOOLS/scripts/pcb_quality/run_pcb_quality_gate.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
```

Use `--no-fail` to always return `0` while still writing the gate result:

```powershell
python 03_TOOLS/scripts/pcb_quality/run_pcb_quality_gate.py --project 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE --no-fail
```

## Allowed Final Status Codes

- `PASS_FINAL_ROUTING`
- `FAIL_DRC`
- `FAIL_OPEN_NETS`
- `FAIL_TRACE_GEOMETRY`
- `FAIL_TESTPOINT_TOPOLOGY`
- `FAIL_POWER_WIDTHS`
- `FAIL_USB_ROUTING`
- `FAIL_CONNECTOR_ORIENTATION`
- `FAIL_RF_KEEPOUT`
- `FAIL_ZONE_GND`
- `NEEDS_HUMAN_REVIEW`
