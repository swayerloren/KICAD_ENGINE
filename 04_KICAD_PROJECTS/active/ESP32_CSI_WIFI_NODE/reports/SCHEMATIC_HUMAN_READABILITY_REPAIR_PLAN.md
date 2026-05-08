# Schematic Human Readability Repair Plan

Project: `ESP32_CSI_WIFI_NODE`

Target schematic: `kicad/ESP32_CSI_WIFI_NODE.kicad_sch`

Backup: `99_BACKUPS/pre_codex_edits/20260506_170404_ESP32_CSI_WIFI_NODE_human_readable_schematic_relayout`

Status: `PLAN_BEFORE_EDIT`

## Scope

This pass is a schematic drawing/layout repair only. It may edit symbol positions, text positions, label positions, short visible values, and schematic note placement. It must not edit the PCB, update PCB from schematic, route, create zones, or generate manufacturing outputs.

## Known Problem

The schematic currently passes ERC and file-level annotation checks but fails human readability. The latest strict audit reports visible overlap and crowding in input power, buck regulator, USB-C/ESD, ESP32 module, reset/boot, and LED areas.

## Relayout Strategy

1. Keep the same schematic circuit intent and candidate footprint fields.
2. Move long review text out of active circuitry into a separate review-notes table.
3. Keep visible values short while preserving detailed review status in hidden fields and reports.
4. Separate circuitry into readable zones:
   - input power
   - reverse-polarity/fuse/TVS protection
   - buck regulator
   - ESP32 module
   - USB-C connector
   - USB ESD/CC/series resistors
   - reset/boot
   - LEDs
   - test pads
   - mounting holes/mechanical notes
   - review-notes table
5. Use net labels instead of long wires where it improves readability.
6. Move labels away from symbol bodies and pins while preserving electrical connection through short wires where needed.
7. Hide `PWR_FLAG` values if they visually clutter power rails.
8. Do not mark any high-risk footprint as verified.

## Planned Block Changes

| Block | Planned action |
| --- | --- |
| Input power | Keep J1/F1/Q1/D1/C1 in a left-to-right power path, increase spacing, move PWR_FLAG text away or hide it, and keep rail labels clear of symbols. |
| Buck regulator | Separate AP63203, inductor, bootstrap cap, input cap, and output caps with enough whitespace for values and labels. |
| ESP32 module | Keep U2 central, move decoupling caps away from the module body, and keep pin net labels outside the symbol body. |
| USB-C | Keep connector pins readable and move CC, ESD, and series resistor support circuits away from connector pin text. |
| Reset/boot | Split EN/reset and BOOT/GPIO0 into two readable rows with labels not touching pins. |
| LEDs | Space LED chains and shorten visible values. |
| Test pads | Add short labeled stubs so net labels do not sit on test point symbols. |
| Mounting holes | Space holes and keep mechanical notes outside the symbols. |
| Review notes | Move long review statements into a separate text table away from active circuitry. |

## Verification Plan

After editing:

1. Run ERC.
2. Run schematic annotation checker.
3. Run schematic completeness checker if available.
4. Run BOM lock alignment checker if available.
5. Run NEEDS_REVIEW marker checker.
6. Run schematic visual export/crop workflow.
7. Inspect rendered evidence if possible.
8. Report automated crop status separately from human-readable visual status.
9. Keep schematic-to-PCB gate blocked unless every required gate passes and all high-risk items are resolved.

## Rollback Plan

Restore `ESP32_CSI_WIFI_NODE.kicad_sch` and `ESP32_CSI_WIFI_NODE.kicad_pro` from:

`99_BACKUPS/pre_codex_edits/20260506_170404_ESP32_CSI_WIFI_NODE_human_readable_schematic_relayout`
