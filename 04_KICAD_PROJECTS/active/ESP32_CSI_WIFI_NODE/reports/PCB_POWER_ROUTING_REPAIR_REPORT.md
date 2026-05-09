# PCB Power Routing Repair Report

Date: `2026-05-09`

Project: `ESP32_CSI_WIFI_NODE`

PCB: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

Status: `POWER_ROUTING_REPAIR_COMPLETE_HUMAN_REVIEW_REQUIRED`

## Scope

Limited live-board routing repair pass for the `J1 / F1 / Q1 / D3 / U1 / L1 / C6 / C7 / SW1` power-input and buck-converter area only.

Formal project routing gates remain blocked, so this pass was performed under:

- `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/history/quality_gate_failures/2026-05-09_power_routing_user_override_exception.md`

## Backup

- project backup: `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/backups/ESP32_CSI_WIFI_NODE_power_routing_20260509_142756.kicad_pcb`
- repo backup: `99_BACKUPS/pre_codex_edits/ESP32_CSI_WIFI_NODE_power_routing_20260509_142756.kicad_pcb`

## Nets Changed

- `/+5V_PROTECTED`
- `/BUCK_SW`
- `/BUCK_BST`
- `+3V3`
- `GND`

## Exact Routing Changes

### `/+5V_PROTECTED`

- removed the previous local geometry between `D3`, `C2`, `C5`, `Q1`, and `U1`
- rebuilt the route as a 45-degree path from `D3` into the `C2/C5/U1` node
- kept the main protected 5 V spine at `0.75 mm`
- kept the short `U1` breakout segment at `0.50 mm` near the regulator pads

### `/BUCK_SW`

- removed and rebuilt the local `U1` to `L1` switching path
- kept the path straight, short, and direct on `F.Cu`
- widened the local switching segment to `0.60 mm`

### `/BUCK_BST`

- removed and rebuilt the local `U1` to `C6` bootstrap path
- preserved short, clean 45-degree geometry
- kept width at `0.25 mm` because this is a bootstrap connection, not a main power rail

### `+3V3`

- removed the prior local detour/via pattern near `U1`, `L1`, and `C7`
- restored a direct local output path from `L1` into the `C7/C8` output node
- restored the `C8` tie on `F.Cu` after a trial-pass disconnect was detected and corrected
- kept the local high-current output segments at `0.60 mm`
- kept the longer existing downstream trunk at `0.50 mm` where it was already outside the compact buck loop
- kept the `U1` feedback sense connection at `0.25 mm` because `U1` pin 1 is the `FB` node, not the high-current output pin

### `GND`

- added one new local input-side GND via near the input-cap return area at `(19.000, 72.600)`
- added one new local output-side GND via near the output-cap return area at `(43.500, 65.975)`
- removed a trial-positioned GND via at `(18.200, 71.800)` after live DRC showed a clearance hit to `/+5V_PROTECTED`

## Areas Intentionally Not Changed In This Pass

- `/+5V_IN` was left in place at `0.75 mm`; it was already short and acceptable
- `/+5V_FUSED` was left in place at `0.75 mm`; it was already short and acceptable
- `TP1` on `/+5V_PROTECTED` remains open
- unrelated control and USB opens were not touched: `/BOOT0`, `/ESP_EN`, `/DM_C`, `/DM_E`, `/DP_C`, `/DP_E`
- no schematic, footprint, or antenna-area edits were made

## DRC Result

Command: `kicad-cli pcb drc --format json --output 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/PCB_POWER_ROUTING_REPAIR_DRC.json 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/kicad/ESP32_CSI_WIFI_NODE.kicad_pcb`

Result:

- `0` violations
- `17` unconnected items

Remaining open/unrouted nets seen in DRC:

- `/+5V_PROTECTED` to `TP1`
- `/BOOT0`
- `/ESP_EN`
- `/DM_C`
- `/DM_E`
- `/DP_C`
- `/DP_E`

## Zones

- zones refilled: `YES`

## File Change Confirmation

- schematic changed: `NO`
- PCB changed: `YES`
- footprint changes: `NO`

## Hash Evidence

- pre-edit PCB hash: `ac0eed2054906b272aa516b627c1a22312f952c8`
- post-edit PCB hash: `a6876ff219831d5261d5acbbea7fa95d05c10f85`
