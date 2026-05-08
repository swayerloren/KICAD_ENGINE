# Real Board Routing Bridge Tests

## Purpose

This folder holds copied-board inputs, generated outputs, and generated reports for the real KiCad PCB to routing-engine bridge.

The bridge is for:

- read-only `.kicad_pcb` extraction
- routing-schema generation
- copied-board routing audit dry runs
- DRC-coupled routing-engine precheck

It is not for:

- editing active project boards
- routing production boards
- manufacturing export

## Directory Use

- `sample_inputs/`
  - path manifests or copied non-production test boards
- `outputs/`
  - generated JSON and Markdown artifacts from extraction and audit scripts
- `reports/`
  - higher-level test summaries

## Current Safe Input Sources

Current copied-board candidates inside this repo include:

- `32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/tomasr8_attiny85_dev_board/attiny85.kicad_pcb`
- `32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/m4a1x_tps5430/TPS5430.kicad_pcb`
- `32_OPEN_KICAD_SAMPLE_INTAKE/normalized_samples/esp_rs_esp_rust_board/hardware/esp-rust-board/esp-rust-board.kicad_pcb`
- `04_KICAD_PROJECTS/active/COMMAND_LINK_VERIFIED_REFERENCE/COMMAND LINK DRAFT.kicad_pcb`

Do not use the active project original board as the first bridge test target.
