# Open KiCad Sample Candidate Discovery Report

Date: 2026-05-03

Status: `DISCOVERY_COMPLETE_IMPORT_BLOCKED_PENDING_USER_APPROVAL`

## Scope

This pass searched for real public KiCad projects that could become benchmark/sample fixtures for KiCad Engine.

No repositories were cloned, downloaded, imported, normalized, repaired, or used to generate outputs.

## Method

- Public web search was used to identify likely candidates.
- GitHub repository metadata and Git tree metadata were queried for a short list of candidates.
- License file names and first lines were checked for candidates whose GitHub license metadata returned `NOASSERTION`.
- File presence was checked by path metadata only, not by cloning repositories.

## Candidates Found

| Candidate | Category Covered | License | `.kicad_pro` | `.kicad_sch` | `.kicad_pcb` | BOM | Gerbers | STEP/3D | Status |
|---|---|---|---|---|---|---|---|---|---|
| `esp-rs/esp-rust-board` | ESP32/USB-C/battery | CERN-OHL-P-2.0 | Yes | Yes | Yes | Yes | Yes | Yes | Candidate |
| `linux-automation/candleLightFD` | STM32/CAN-FD/USB | CERN-OHL v1.2 | Yes | Yes | Yes | Yes | Yes | No | Candidate |
| `CIRCUITSTATE/Mitayi-Pico-D1` | RP2040 | MIT | Yes | Yes | Yes | Yes | Yes | Yes | Candidate |
| `bluetiger9/USB-Type-C-Switch` | USB-C high-speed | MIT | Yes | Yes | Yes | Yes | Yes | No | Candidate |
| `M4a1x/TPS5430` | Power/regulator | CERN-OHL-S-2.0 | Yes | Yes | Yes | No | Yes | Yes | Candidate |
| `tomasr8/attiny85-dev-board` | Beginner MCU board | MIT | Yes | Yes | Yes | No | Yes | No | Candidate |
| `solderparty/bbq20kbd_hw` | RP2040/keyboard/open hardware | CERN-OHL v1.2 | Yes | Yes | Yes | Yes | No | Yes | Candidate |
| `mohamedyanis/STM32L0-ESP32-Breakout-Board` | STM32/ESP32 mixed board | BSD-3-Clause | Yes | Yes | Yes | Yes | Yes | Yes | Candidate |
| KiCad `pic_programmer` demo | Official KiCad demo | GPL-3.0 parent repo, needs subfolder review | Yes | Yes | Yes | No | No | No | Link-only |

## Top 5

1. `tomasr8/attiny85-dev-board`
2. `M4a1x/TPS5430`
3. `esp-rs/esp-rust-board`
4. `CIRCUITSTATE/Mitayi-Pico-D1`
5. `linux-automation/candleLightFD`

## Recommended First Imports

Import only after explicit user approval:

1. `tomasr8/attiny85-dev-board` - small, MIT licensed, complete KiCad project.
2. `M4a1x/TPS5430` - compact power/regulator board with CERN-OHL-S-2.0 license.
3. `esp-rs/esp-rust-board` - complete ESP32-C3 USB-C/battery open hardware project, useful after first two intake workflows are proven.

## Why Not Import Yet

This prompt requested discovery first. Even candidates with clear licenses need:

- Human license/attribution review.
- Public payload exclusion review.
- Scope selection for repositories with multiple revisions or generated outputs.
- Import into `32_OPEN_KICAD_SAMPLE_INTAKE/imported_originals/`, not repo root.
- Normalized copy before any analysis or repair.

## Blocked Or Link-Only Items

- KiCad official `pic_programmer` demo is useful but remains `NEEDS_HUMAN_LICENSE_REVIEW` because it is part of the larger KiCad source mirror with mixed repository licensing context.

## Next Safe Step

Ask the user to approve importing 2 or 3 specific candidates. Recommended first import batch:

- `tomasr8/attiny85-dev-board`
- `M4a1x/TPS5430`
- optionally `esp-rs/esp-rust-board`

Run imports only through `32_OPEN_KICAD_SAMPLE_INTAKE/scripts/import_sample_project.py` or an approved equivalent, and preserve originals read-only.
