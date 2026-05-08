# ESP32_CSI_WIFI_NODE Visual Check Report

Generated: 2026-05-06

## Automated Outputs

| Output | Path |
| --- | --- |
| Full-page SVG | `_verification/schematic_visual/full_page/ESP32_CSI_WIFI_NODE.svg` |
| Full-page PDF | `_verification/schematic_visual/full_page/ESP32_CSI_WIFI_NODE.pdf` |
| Full-page PNG | `_verification/schematic_visual/full_page/ESP32_CSI_WIFI_NODE.png` |
| Close-up crops | `_verification/schematic_visual/crops/` |
| Automated close-up review | `reports/CLOSE_UP_REVIEW.md` |

Automated crop generation status: `PASS_AUTOMATED`

## Human-Readable Visual Judgment

Human-readable visual status: `FAIL`

Automated crop generation is not visual approval. Rendered crop inspection found remaining visual defects.

## Defects Found

- Buck regulator area remains crowded around U1 labels, D1/C2/C1/C3/C5/L1 text, and BUCK_SW/BST labels.
- USB support area remains crowded around ESD GND/value fields and CC/series resistor labels.
- LED area remains crowded around PLED/SLED node labels and resistor values.
- Some crop windows include adjacent partial blocks and need further tuning before they are reliable evidence.

## Safe Use

Do not mark this schematic as ready for PCB update or fabrication workflow. Use the exported images only as evidence for the next repair pass.
