# Task To Tool Map

Status: `CANONICAL_RETRIEVAL_TOOL_MAP`

This is the retrieval-index mirror of
`00_CODEX_START/TASK_TYPE_TO_TOOL_MAP.md`.

| Route | Tool Stack |
| --- | --- |
| `SCHEMATIC_CREATE_OR_REPAIR` | `03_TOOLS/scripts/schematic_quality/`, `03_TOOLS/scripts/schematic_layout/`, `kicad-cli` ERC |
| `SCHEMATIC_VISUAL_CLEANUP` | `03_TOOLS/scripts/schematic_layout/`, `03_TOOLS/kicad/run_schematic_visual_check.ps1` |
| `NATIVE_ANNOTATION` | `33_KICAD_GUI_AUTOMATION/scripts/windows/` |
| `FOOTPRINT_PACKAGE_GATE` | `03_TOOLS/scripts/footprint_package/`, `03_TOOLS/scripts/mechanical_orientation/` |
| `PCB_UPDATE_FROM_SCHEMATIC` | `03_TOOLS/scripts/project_gate/check_phase_allowed.py`, `kicad-cli pcb drc --schematic-parity` |
| `PCB_PRELAYOUT_VARIANT_PLANNING` | `03_TOOLS/scripts/pcb_prelayout/`, `03_TOOLS/scripts/mechanical_orientation/` |
| `PCB_PLACEMENT` | `03_TOOLS/scripts/pcb_prelayout/`, `03_TOOLS/scripts/pcb_quality/check_connector_orientation.py` |
| `CONNECTOR_ORIENTATION_AUDIT` | `03_TOOLS/scripts/mechanical_orientation/` |
| `PCB_ROUTING` | `03_TOOLS/scripts/pcb_quality/`, `03_TOOLS/scripts/pcb_geometry/`, optional wrappers from `03_TOOLS/open_source_integrations/` |
| `TRACE_GEOMETRY_AUDIT` | `03_TOOLS/scripts/pcb_geometry/`, `03_TOOLS/scripts/pcb_quality/check_trace_geometry.py` |
| `PCB_COPPER_ZONES` | `03_TOOLS/scripts/pcb_quality/run_pcb_quality_gate.py`, `kicad-cli pcb drc` |
| `FAB_EXPORT` | `03_TOOLS/scripts/fabrication/`, `03_TOOLS/scripts/pcb_quality/`, release validators under `17_RELEASE_BUILD/` |
| `MEMORY_MAINTENANCE` | `03_TOOLS/scripts/maintenance/`, `03_TOOLS/scripts/knowledge_migration/rebuild_knowledge_indexes.py` |
| `OPEN_SOURCE_TOOL_USE` | `setup/verify_optional_kicad_tools.py`, `03_TOOLS/open_source_integrations/`, `03_TOOLS/calculators/` |

