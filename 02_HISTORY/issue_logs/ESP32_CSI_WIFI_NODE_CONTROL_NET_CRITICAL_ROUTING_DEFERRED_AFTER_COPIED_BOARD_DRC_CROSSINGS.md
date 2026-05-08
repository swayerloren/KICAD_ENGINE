# ESP32_CSI_WIFI_NODE Control-Net Critical Routing Deferred After Copied-Board DRC Crossings

Status: `OPEN`

Date: `2026-05-08`

## Issue

The real board now has a clean live `+3V3` completion pass, but `/BOOT0` and `/ESP_EN` could not be added in the same live pass without creating copied-board DRC crossings/shorts against the accepted `+3V3` corridor.

## Evidence

- copied-board rehearsals under `99_BACKUPS\pre_codex_edits\20260508_071914_ESP32_CSI_WIFI_NODE_real_pcb_critical_routing_pass_1`
- accepted live report: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\REAL_PCB_CRITICAL_ROUTING_PASS_1_REPORT.md`
- accepted live trace audit: `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\reports\REAL_PCB_CRITICAL_TRACE_AUDIT.md`

## Required Follow-Up

1. run a dedicated copied-board control-net study for `/BOOT0`
2. run a dedicated copied-board control-net study for `/ESP_EN`
3. preserve the accepted `+3V3` route geometry while solving those branches
4. only then bring the clean result onto the live board
