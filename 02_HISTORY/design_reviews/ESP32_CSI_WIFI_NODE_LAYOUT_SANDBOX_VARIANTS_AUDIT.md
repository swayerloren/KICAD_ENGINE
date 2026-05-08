# ESP32_CSI_WIFI_NODE Layout Sandbox Variants Audit

Date: `2026-05-07`

## Scope

Project-local sandbox planning only. No KiCad schematic, PCB, or manufacturing files were edited.

## Files Created

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/layout_sandbox/VARIANT_A_COMPACT_DEV_BOARD_STYLE.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/layout_sandbox/VARIANT_B_CONNECTOR_MECHANICAL_OPTIMIZED.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/layout_sandbox/VARIANT_C_ROUTING_POWER_RF_OPTIMIZED.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/layout_sandbox/VARIANT_COMPARISON_SCORECARD.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/layout_sandbox/SELECTED_LAYOUT_PLAN.md`

## Files Updated

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/CURRENT_PROJECT_STATE.md`
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/memory/CURRENT_BLOCKERS.md`
- `FOR CHAT GPT.MD`

## Planning Result

- Three sandbox variants were created.
- `VARIANT_C_ROUTING_POWER_RF_OPTIMIZED` is the highest-scoring non-failed sandbox concept.
- Variant statuses:
  - `VARIANT_A`: `NEEDS_HUMAN_REVIEW`
  - `VARIANT_B`: `NEEDS_HUMAN_REVIEW`
  - `VARIANT_C`: `NEEDS_HUMAN_REVIEW`
- Real KiCad PCB work remains blocked.

## Why Variant C Won

- Best overall balance of left-side power entry, right-side USB corridor, and protected upper-right RF connector/pigtail space.
- Cleanest projected power path and USB path.
- Better routing feasibility than the compact variant.
- Better electrical flow than the mechanical-first variant.

## Remaining Blockers

- Board dimensions are still assumptions.
- Exact USB-C and barrel-jack package/footprint lock is unresolved by project gate evidence.
- `U2` `ESP32-S3-WROOM-1U-N16R8` RF connector and pigtail service zone still need LJ review.
- Asymmetrical shape choice in Variant C needs LJ approval.
- Upstream `SCHEMATIC_TO_PCB_GATE_STATUS.md` and `FOOTPRINT_PACKAGE_GATE_REPORT.md` remain `FAIL`.

## Validation

- Project-local variant files exist.
- The sandbox scoring scripts successfully scored all three variants and selected Variant C as the front-runner.
- Final active-project KiCad hashes matched the pre-edit baseline.
