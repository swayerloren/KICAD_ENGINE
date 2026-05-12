# Task Type To Knowledge Map

Status: `CANONICAL_ROUTER_KNOWLEDGE_MAP`

Use this table after `TASK_ROUTER.md` picks the primary route. It maps the
route to the canonical knowledge surfaces that should be read first.

Historical migration provenance is part of repo history, not a routing input.

| Route | Canonical Knowledge First Reads |
| --- | --- |
| `SCHEMATIC_CREATE_OR_REPAIR` | `34_SCHEMATIC_QUALITY_ENGINE/`, `09_ACCURACY_ENGINE/schematic_rules/`, `10_KNOWLEDGE_BASE/training/`, `10_KNOWLEDGE_BASE/case_studies/` |
| `SCHEMATIC_VISUAL_CLEANUP` | `34_SCHEMATIC_QUALITY_ENGINE/`, `10_KNOWLEDGE_BASE/training/`, `10_KNOWLEDGE_BASE/peer_review/` |
| `NATIVE_ANNOTATION` | `33_KICAD_GUI_AUTOMATION/`, `10_KNOWLEDGE_BASE/kicad_core/`, `10_KNOWLEDGE_BASE/kicad_python_api/` |
| `FOOTPRINT_PACKAGE_GATE` | `35_FOOTPRINT_PACKAGE_ENGINE/`, `08_COMPONENT_DATABASE/`, `11_LIBRARY_FACTORY/`, `06_DATASHEETS/` |
| `PCB_UPDATE_FROM_SCHEMATIC` | `34_SCHEMATIC_QUALITY_ENGINE/`, `35_FOOTPRINT_PACKAGE_ENGINE/`, `10_KNOWLEDGE_BASE/kicad_core/`, active project `schematic_intelligence/` |
| `PCB_PRELAYOUT_VARIANT_PLANNING` | `33_PCB_PRELAYOUT_ENGINE/`, `10_KNOWLEDGE_BASE/pcb_layout/`, `10_KNOWLEDGE_BASE/rf_wifi/`, `08_COMPONENT_DATABASE/mechanical_orientation/` |
| `PCB_PLACEMENT` | `33_PCB_PRELAYOUT_ENGINE/`, `10_KNOWLEDGE_BASE/pcb_layout/`, `10_KNOWLEDGE_BASE/power_integrity/`, `10_KNOWLEDGE_BASE/rf_wifi/` |
| `CONNECTOR_ORIENTATION_AUDIT` | `08_COMPONENT_DATABASE/mechanical_orientation/`, `10_KNOWLEDGE_BASE/rf_wifi/`, `10_KNOWLEDGE_BASE/dfm_assembly/` |
| `PCB_ROUTING` | `10_KNOWLEDGE_BASE/pcb_layout/`, `10_KNOWLEDGE_BASE/usb_c/`, `10_KNOWLEDGE_BASE/power_integrity/`, `33_PCB_PRELAYOUT_ENGINE/` |
| `TRACE_GEOMETRY_AUDIT` | `10_KNOWLEDGE_BASE/pcb_layout/`, `10_KNOWLEDGE_BASE/case_studies/`, `26_AGENT_QUALITY/` |
| `PCB_COPPER_ZONES` | `10_KNOWLEDGE_BASE/power_integrity/`, `10_KNOWLEDGE_BASE/rf_wifi/`, `10_KNOWLEDGE_BASE/pcb_layout/` |
| `FAB_EXPORT` | `24_FAB_PROFILES/`, `10_KNOWLEDGE_BASE/dfm_assembly/`, `10_KNOWLEDGE_BASE/compliance_emc_safety/`, `17_RELEASE_BUILD/` |
| `MEMORY_MAINTENANCE` | `01_MEMORY/`, `02_HISTORY/`, `10_KNOWLEDGE_BASE/retrieval_indexes/`, `26_AGENT_QUALITY/` |
| `OPEN_SOURCE_TOOL_USE` | `03_TOOLS/open_source_integrations/`, `10_KNOWLEDGE_BASE/retrieval_indexes/`, `10_KNOWLEDGE_BASE/kicad_core/`, `10_KNOWLEDGE_BASE/calculators/` |
