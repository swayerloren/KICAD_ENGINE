# Fab File Format Rules Validation Report

Status: `PASS_WITH_EXPECTED_WARNINGS`

Generated: `2026-05-07`

Source: `T_E_M_P\file format.md`

## Validation Results

| Check | Result |
|---|---|
| Source markdown analyzed | `PASS` |
| JLCPCB BOM/CPL facts extracted | `PASS` |
| PCBWay BOM/centroid facts extracted | `PASS` |
| Universal BOM/PNP facts extracted | `PASS` |
| Required package folder rules documented | `PASS` |
| Pre-upload checks documented | `PASS` |
| Python syntax check for validators | `PASS` |
| JSON schemas parse | `PASS` |
| JLCPCB BOM template validates | `PASS_WITH_WARNING` |
| JLCPCB CPL template validates | `PASS_WITH_WARNING` |
| PCBWay BOM template validates | `PASS_WITH_WARNING` |
| PCBWay centroid template validates | `PASS_WITH_WARNING` |
| Universal BOM template validates | `PASS_WITH_WARNING` |
| Universal pick-and-place template validates | `PASS_WITH_WARNING` |
| Package folder validator syntax | `PASS` |
| KiCad design files changed | `NO` |
| Manufacturing output package generated | `NO` |

## Expected Warning

Every CSV validator prints:

```text
WARN: connector orientation, polarity, pin 1, and pick-and-place rotation review is still required; CSV validation is not assembly approval
```

This warning is intentional. BOM/CPL/centroid validation does not prove assembly correctness.

## Current Rule

JLCPCB/PCBWay export remains blocked until final PCB/export gates pass. Required evidence includes DRC with schematic parity, no-unrouted proof, Gerber/drill review, validated house-specific BOM and placement files, assembly notes, orientation checks, and LJ approval.

