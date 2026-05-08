# Hallucination Risk Log: ESP32_CSI_WIFI_NODE GUI Native Annotation Attempt

Date: `2026-05-06`

Risk level: `MEDIUM`

## Risk

The main risk is overstating a saved-file CLI ERC pass as a successful KiCad GUI-native annotation run.

## Control

Reports explicitly state:

- native annotation dialog opened: `NO`
- annotation applied: `NO`
- schematic saved from GUI: `NO`
- GUI ERC run: `NO`
- reason: `NO_EESCHEMA_WINDOW`

PCB update remains blocked.
