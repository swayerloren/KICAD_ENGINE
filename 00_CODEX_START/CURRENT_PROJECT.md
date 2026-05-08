Active project name: ESP32_CSI_WIFI_NODE
Active project path: 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE
Current task mode: ACTIVE_DESIGN_PROJECT_LIVE_PCB_EXISTS_PARTIAL_ROUTING_BLOCKED
Current priority: Keep the live board read-only for now, verify existing routed traces, and resolve placement/mechanical plus routing blockers before any new routing

# Current Project

This file controls whether Codex may inspect or edit KiCad project files.

## Rules
- If active project name is `NONE`, do not edit KiCad project files.
- If active project path is `NONE`, do not edit KiCad project files.
- Before protected edits, confirm backups in `99_BACKUPS/pre_codex_edits/`.
- Before design changes, state the files likely to change, verification plan, and rollback plan.

## Update Fields When Selecting A Project
- Active project name.
- Active project path.
- Current task mode.
- Current priority.
- Allowed edit boundaries.
- Required verification.
- Relevant memory files.
- Relevant history files.

## Active Project Details
- Allowed edit boundaries for current state: documentation, verification planning, project memory, project history, live placement/mechanical/orientation review, existing-trace audit and repair analysis, and explicit repair-only work under `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad` when a pre-edit backup is confirmed. Do not continue routing, zones, JLCPCB review, production review, export, or signoff until the live blocker reports are resolved and the formal gates are updated.
- Required verification: ERC after schematic creation or edits; DRC after PCB creation or edits; BOM, footprint, netlist, datasheet, connector, polarity/orientation, power/protection, antenna/mechanical, and visual review before fabrication-style outputs are treated as anything beyond `NOT_FINAL`.
- Relevant memory files: `01_MEMORY\GLOBAL_MEMORY.md`, `01_MEMORY\DESIGN_RULES_MEMORY.md`, `01_MEMORY\COMPONENT_PREFERENCES.md`, `01_MEMORY\FAB_HOUSE_PREFERENCES.md`, `01_MEMORY\projects\ESP32_CSI_WIFI_NODE\PROJECT_MEMORY.md`.
- Relevant history files: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\LIVE_PCB_TRUTH_AUDIT.md`, `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\PCB_PLACEMENT_CURRENT_STATE_REPORT.md`, `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\ROUTING_CURRENT_STATE_REPORT.md`, `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\CURRENT_EXISTING_TRACE_AUDIT.md`, `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\SCHEMATIC_TO_PCB_GATE_STATUS.md`, `02_HISTORY\sessions\ESP32_CSI_WIFI_NODE_LIVE_PCB_TRUTH_AUDIT_SESSION.md`, `02_HISTORY\sessions\ESP32_CSI_WIFI_NODE_EXISTING_TRACE_AUDIT_SESSION.md`, `02_HISTORY\command_logs\ESP32_CSI_WIFI_NODE_LIVE_PCB_TRUTH_AUDIT_COMMANDS.md`, `02_HISTORY\command_logs\ESP32_CSI_WIFI_NODE_EXISTING_TRACE_AUDIT_COMMANDS.md`.
