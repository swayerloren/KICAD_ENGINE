# FOOTPRINT_PACKAGE_AUDIT_OPEN_ISSUES

Status: `OPEN`

Date: 2026-05-03

Project: `ESP32_CSI_WIFI_NODE`

## Issue Summary

Footprint/package verification failed before PCB update because no physical schematic component has an assigned footprint or populated schematic datasheet field.

## Blocking Evidence

- Physical schematic symbols: `43`
- Assigned footprints: `0`
- Populated datasheet fields: `0`
- Missing BOM lock: `PRE_SCHEMATIC_BOM_LOCK.md`
- Missing schematic-ready parts list: `SCHEMATIC_READY_PARTS_LIST.md`

## Required Resolution

Before PCB update, each physical component must have:

- exact MPN or explicit `NEEDS_REVIEW`;
- source/datasheet or package drawing link;
- KiCad footprint assignment;
- package drawing to footprint verification;
- symbol pin to footprint pad verification for pinout/polarity-sensitive parts;
- connector/mechanical orientation review where applicable.

## High-Risk Items

- `J2` USB-C connector
- `Q1` AO3401A-class PMOS
- `U2` ESP32-S3 module
- `U3` USB ESD device
- `U1` AP63203 regulator
- `J1` barrel jack
- `F1` PTC fuse
- `D1` TVS diode
- `TP1`-`TP9` test pads
- `MH1`-`MH4` mounting holes

## Gate Impact

`reports/SCHEMATIC_TO_PCB_GATE_STATUS.md` remains `FAIL`.

