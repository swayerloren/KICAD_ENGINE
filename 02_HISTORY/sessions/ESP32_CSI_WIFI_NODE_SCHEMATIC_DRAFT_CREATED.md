# ESP32_CSI_WIFI_NODE Schematic Draft Created

Date: 2026-05-02

Workspace: `C:\Users\LJ\KICAD_ENGINE`

Active project: `ESP32_CSI_WIFI_NODE`

Active project path: `C:\Users\LJ\KICAD_ENGINE\04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE`

## Startup And Authorization

- Read required startup files before KiCad edits.
- Confirmed active project name and active project path.
- Confirmed target KiCad files are inside `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE`.
- User explicitly requested rough schematic creation.
- No PCB layout, Gerbers, manufacturing outputs, repositories, tools, secrets, or finished reference projects were modified.

## Backup

Backup/snapshot created before KiCad source creation:

`99_BACKUPS\pre_codex_edits\ESP32_CSI_WIFI_NODE_SCHEMATIC_DRAFT_20260502_143643`

## Rollback Plan

To roll back this session, restore the active project folder from:

`99_BACKUPS\pre_codex_edits\ESP32_CSI_WIFI_NODE_SCHEMATIC_DRAFT_20260502_143643`

Then remove or revert these history/index/memory updates if they are no longer true:

- `02_HISTORY\erc_drc_reports\ESP32_CSI_WIFI_NODE_SCHEMATIC_DRAFT_ERC.txt`
- `02_HISTORY\design_reviews\ESP32_CSI_WIFI_NODE_SCHEMATIC_DRAFT_REVIEW.md`
- `02_HISTORY\sessions\ESP32_CSI_WIFI_NODE_SCHEMATIC_DRAFT_CREATED.md`
- `01_MEMORY\projects\ESP32_CSI_WIFI_NODE\PROJECT_MEMORY.md`
- `00_CODEX_START\CURRENT_PROJECT.md`
- `00_CODEX_START\PROJECT_INDEX.md`

## Files Created

- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_pro`
- `04_KICAD_PROJECTS\active\ESP32_CSI_WIFI_NODE\kicad\ESP32_CSI_WIFI_NODE.kicad_sch`
- `02_HISTORY\erc_drc_reports\ESP32_CSI_WIFI_NODE_SCHEMATIC_DRAFT_ERC.txt`
- `02_HISTORY\design_reviews\ESP32_CSI_WIFI_NODE_SCHEMATIC_DRAFT_REVIEW.md`
- `02_HISTORY\sessions\ESP32_CSI_WIFI_NODE_SCHEMATIC_DRAFT_CREATED.md`

## Files Updated

- `01_MEMORY\projects\ESP32_CSI_WIFI_NODE\PROJECT_MEMORY.md`
- `00_CODEX_START\CURRENT_PROJECT.md`
- `00_CODEX_START\PROJECT_INDEX.md`

## Schematic Blocks Drafted

- Barrel jack 5 V input with center-positive note.
- PTC fuse and PMOS reverse-polarity protection concept.
- 5 V TVS and bulk input capacitor.
- AP63203WU-7 3.3 V buck regulator block.
- ESP32-S3-WROOM-1U-N16R8 module draft.
- EN/reset and BOOT circuits.
- USB-C native USB programming/debug with CC resistors, USB ESD, series resistors, and VBUS/shield notes.
- Power LED and simple status LED.
- Test pads for power, reset/boot, UART, and optional USB D+/D- review.
- Mounting hole symbols and antenna/enclosure mechanical notes.

## ERC

ERC command completed and report was saved:

`02_HISTORY\erc_drc_reports\ESP32_CSI_WIFI_NODE_SCHEMATIC_DRAFT_ERC.txt`

Final ERC result for this rough draft:

- Messages: 6 total.
- Errors: 5.
- Warnings: 1.

Remaining items:

- Add power flags or equivalent ERC drivers for GND, protected +5 V, and +3.3 V.
- Clean up LED wiring in the KiCad schematic so the indicator circuits are ERC-clean.
- Resolve AP63203WU cached-symbol/library mismatch by using a verified library symbol or local symbol strategy.

## Notes

- USB VBUS is intentionally not connected to board +5 V in the rough draft.
- Footprints remain blank or unfinalized where MPN/footprint verification is still open.
- The rough schematic is not layout-ready and not fabrication-ready.
