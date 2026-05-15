# Schematic Visual Audit Rules

## Rule

Human-readable visual review is a separate gate from ERC, annotation, and crop
generation.

## Required Visual Evidence

- full-page render
- close-up block crops
- block-by-block review record
- no unresolved `NOT_REVIEWED` sections
- current human-drafting checker output when the sheet was recently cleaned up,
  relabeled, or visually redrawn:
  `03_TOOLS/scripts/schematic_quality/check_schematic_human_drafting_quality.py`
- separate object/net proof when a visually emphasized power, ground, or common
  return rail is part of the review claim
- separate topology proof when reset/boot or other local control clusters were
  redrawn for presentation

## Automatic Fail Conditions

- visible reference/value/label/text overlaps
- visible footprint/library/path fields in normal view
- visible unresolved placeholder references
- review notes crowding active circuitry
- crop report status only `AUTOMATED_CROP_PASS_ONLY`
- labels used as a shortcut for poor symbol orientation or avoidable short
  local wiring
- local MCU support circuitry that still reads as label islands instead of a
  readable physical cluster
- visually emphasized rails or return paths that are not proven as real wires
  on the intended nets
- reset/boot topology that is visually hidden, ambiguous, or suggests unsafe
  switch behavior
- reference/value text that does not clearly belong to its own symbol
- power, ground, or common-return presentation that obscures current flow or
  looks like decorative graphics

## Pass Condition

Use `VISUAL_PASS` only when rendered images were actually reviewed, every block
is readable, symbol orientation and wire flow look intentionally drafted, and
no critical local block still depends on avoidable labels, ambiguous visual
rails, or hidden local control topology.

Do not turn critical local drafting debt into a soft visual pass. If reset/
boot, local MCU support, or emphasized power/ground/return rails remain
ambiguous, the correct result is `VISUAL_FAIL`.
