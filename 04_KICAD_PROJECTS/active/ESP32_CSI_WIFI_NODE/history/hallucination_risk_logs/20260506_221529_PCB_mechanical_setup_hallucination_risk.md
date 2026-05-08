# PCB Mechanical Setup Hallucination Risk Log

Date: `2026-05-06 22:15:29 -04:00`

Risk: inventing applied board outline, holes, constraints, keepouts, DRC, or visual exports when no PCB exists.

## Controls

- Confirmed `ESP32_CSI_WIFI_NODE.kicad_pcb` does not exist.
- Reported planned coordinates as planning-only.
- Reported DRC as `NOT_RUN_NO_PCB`.
- Reported top/bottom image exports as `NOT_RUN_NO_PCB`.
- Kept component placement status as `NO`.

Classification: `CONTROLLED`
