# Final Human-Readable Schematic Repair Plan

Project: `ESP32_CSI_WIFI_NODE`

Generated: `2026-05-06 18:17:26 -04:00`

Target schematic: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch`

Backup path:

`99_BACKUPS/pre_codex_edits/20260506_181726_ESP32_CSI_WIFI_NODE_final_human_readable_schematic_repair`

## Pre-Edit Evidence

- Current ERC before visual cleanup: `PASS`, 0 violations.
- Current ERC does not contain `Schematic is not fully annotated`.
- Stored unresolved-reference scan found no `J?`, `R?`, `C?`, `D?`, `U?`, `Q?`, `F?`, `SW?`, `TP?`, `MH?`, `L?`, `Y?`, `#PWR?`, or `#FLG?`.
- Current visual status before this pass: `VISUAL_FAIL`, based on `reports/STRICT_VISUAL_READABILITY_REAUDIT.md`.

## Edit Scope

Allowed:

- Move schematic symbols, wires, labels, block titles, and notes for readability.
- Reposition reference/value fields.
- Shorten visible review-heavy values while preserving part intent.
- Keep detailed review status in reports/table notes.
- Adjust visual crop block definitions.

Forbidden:

- Do not edit PCB.
- Do not update PCB from schematic.
- Do not route.
- Do not generate manufacturing outputs.
- Do not change circuit intent.
- Do not mark high-risk parts as verified.
- Do not change footprint assignments except to preserve existing fields if present.

## Cleanup Strategy

1. Keep the schematic on one sheet but reorganize it into clean left-to-right blocks:
   - Input power
   - Fuse / reverse polarity / TVS
   - Buck regulator
   - ESP32 module
   - USB-C connector
   - USB ESD / CC / USB series resistors
   - Reset / boot
   - LEDs
   - Test pads
   - Mounting holes
   - Review notes table
2. Move long review details out of active circuitry and into a separate review table.
3. Shorten visible high-risk values:
   - `AO3401A_REV` -> `AO3401A_REVIEW`
   - `AP63203_NEEDS_REVIEW` -> `AP63203_REVIEW`
   - `TVS_NEEDS_REVIEW` -> `TVS_REVIEW`
   - `USB-C_NEEDS_REVIEW` -> `USB-C_REVIEW`
   - `USB_ESD_REV` -> `USB_ESD_REVIEW`
   - `RESET_EN_REVIEW` -> `RESET_SW_REVIEW`
   - `BOOT_GPIO0_REVIEW` -> `BOOT_SW_REVIEW`
4. Reposition visible references and values away from wires, pins, symbol bodies, and power symbols.
5. Keep `#PWR` and `#FLG` references hidden and unique.
6. Use net labels to avoid long cross-sheet wiring where it improves readability.
7. Regenerate full-page visual outputs and close-up crops after editing.
8. Only classify `READY_FOR_LJ_VISUAL_REVIEW` if rendered full-page/crops are actually inspected and no obvious overlap remains.

## Verification Plan

After editing:

- Run `kicad-cli sch erc`.
- Run direct unresolved-reference scan.
- Export placed-symbol reference table and duplicate check.
- Run schematic visual export/crop workflow.
- Inspect full-page image and every crop.
- Update `SCHEMATIC_TO_PCB_GATE_STATUS.md`.

Rollback plan: restore `ESP32_CSI_WIFI_NODE.kicad_sch` from the backup folder listed above.
