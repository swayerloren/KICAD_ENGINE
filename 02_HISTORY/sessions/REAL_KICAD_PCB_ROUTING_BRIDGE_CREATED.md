# REAL_KICAD_PCB_ROUTING_BRIDGE_CREATED

Date: `2026-05-07`

## Summary

Built the read-only bridge from copied KiCad PCB files into the routing-engine schema and real-board audit flow. Validated the bridge on a copied open sample board without touching the active project.

## Key Outcomes

- created real-board extraction scripts for board outline, nets, pads, tracks, vias, zones, keepouts, and net classes
- created a full-board schema extractor and copied-board audit runner
- validated extraction through KiCad's own Python and `kicad-cli pcb drc --format json`
- fixed the zone/keepout misclassification that initially turned ordinary copper zones into fake routing keepouts
- confirmed copied-board live-test readiness
- kept active-project routing blocked

## Safety Result

No `ESP32_CSI_WIFI_NODE` KiCad design files were edited.
