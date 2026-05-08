# Schematic Electrical Blockers Repair Plan

## Session

- Date: 2026-05-03
- Active project: `ESP32_CSI_WIFI_NODE`
- Active schematic: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_sch`
- Active project file: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pro`
- Backup path: `99_BACKUPS/pre_codex_edits/ESP32_CSI_WIFI_NODE_SCHEMATIC_ELECTRICAL_BLOCKERS_20260503_073335`
- PCB update allowed: `NO`

## Input Status

The prompt-requested files were checked before repair planning:

- `SCHEMATIC_ELECTRICAL_AUDIT.md`: missing at requested path.
- `PRE_SCHEMATIC_BOM_LOCK.md`: missing at requested path.
- `SCHEMATIC_READY_PARTS_LIST.md`: missing at requested path.
- `NEEDS_REVIEW_BEFORE_SCHEMATIC.md`: missing at requested path.

Available evidence used instead:

- User's task list of known issues.
- `02_HISTORY/erc_drc_reports/ESP32_CSI_WIFI_NODE_SCHEMATIC_DRAFT_ERC.txt`.
- `02_HISTORY/design_reviews/ESP32_CSI_WIFI_NODE_SCHEMATIC_DRAFT_REVIEW.md`.
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/COMPONENT_SELECTION_PLAN.md`.
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/COMPONENT_SELECTION_REPORT.md`.
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/DATASHEET_CHECKLIST.md`.
- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/SCHEMATIC_VERIFICATION_PLAN.md`.

## Allowed Changes

Only safe schematic corrections backed by project notes are allowed:

- Fix obvious schematic connectivity issues that ERC identifies.
- Normalize power rail labels to the project/BOM naming convention from the user task.
- Update C1 value text to reflect the requested `47uF >=16V NEEDS_REVIEW` state.
- Add or update schematic notes to formalize unresolved high-risk blockers.

## Blocked Changes

Do not:

- Guess or approve AO3401A footprint orientation.
- Guess or approve USB VBUS/backfeed policy.
- Guess or approve USB shield EMC strategy.
- Guess footprints.
- Update or create a PCB.
- Route or place parts.
- Generate manufacturing outputs.

## Planned Resolution By Issue

| Issue | Planned action | Expected status |
|---|---|---|
| Power/status LED circuits electrically incomplete in netlist | Inspect schematic connectivity around the two LED blocks. Fix only dangling-wire or net connection issues that are obvious in the KiCad file. | Fix if safe; otherwise block. |
| AO3401A PMOS symbol pin mapping and footprint orientation | Keep formally blocked. Add/update schematic and audit notes that exact AO3401A symbol/footprint/package drawing review is required. | BLOCKED_NEEDS_REVIEW |
| Power rail naming mismatch | Rename schematic labels from `5V_RAW` to `+5V_IN`, `5V_FUSED` to `+5V_FUSED`, and protected `+5V` rail to `+5V_PROTECTED` where safe. | FIX |
| C1 value/voltage mismatch | Change schematic C1 value text from `47uF_10V_BULK_NEEDS_REVIEW` to `47uF_>=16V_BULK_NEEDS_REVIEW`. | FIX_TEXT_ONLY |
| USB VBUS policy unresolved | Keep formally blocked. Do not connect USB VBUS to board power. | BLOCKED_NEEDS_REVIEW |
| USB shield strategy unresolved | Keep formally blocked. Do not choose an EMC/shield circuit. | BLOCKED_NEEDS_REVIEW |

## Verification Plan

After schematic edits:

1. Run KiCad ERC with `kicad-cli`.
2. Export schematic visual if supported by installed `kicad-cli`.
3. Run a text-based close-up/issue review from schematic evidence and visual export availability.
4. Re-run/update the electrical audit document.
5. Update `reports/SCHEMATIC_TO_PCB_GATE_STATUS.md`.
6. Keep schematic-to-PCB gate `FAIL` or `BLOCKED` if any high-risk blocker remains.

## Rollback Plan

Restore these files from the backup folder if the edits are wrong:

- `kicad/ESP32_CSI_WIFI_NODE.kicad_pro`
- `kicad/ESP32_CSI_WIFI_NODE.kicad_sch`
