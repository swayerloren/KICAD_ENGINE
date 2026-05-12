# Visual Readability Scorecard

## Purpose

Define the weighted readability score used by
`03_TOOLS/scripts/schematic_layout/score_schematic_readability.py`.

## Categories And Weights

| Category | Weight | Meaning |
| --- | --- | --- |
| Block grouping | 12 | Functional blocks exist and are visually coherent. |
| Local wire clarity | 10 | Local same-block connectivity uses readable short wires. |
| Label usage balance | 8 | Labels are reserved for cross-block or long-distance use. |
| Overlap count | 10 | Estimated visible text/reference overlap stays controlled. |
| Reference readability | 8 | References are visible and not visually colliding. |
| Power flow readability | 12 | Power entry, regulation, and system flow read clearly. |
| USB path readability | 10 | USB connector, ESD, CC, and data resistors read as one block. |
| ESP32 pin readability | 10 | The ESP32 module area has enough whitespace and low clutter. |
| ERC status | 10 | Fresh ERC evidence exists and passes. |
| Annotation status | 5 | Saved-file annotation and native annotation evidence are acceptable. |
| Footprint status | 5 | Physical parts have footprints and no visible review-marker values remain. |

## Status Mapping

- `PASS`: full category weight
- `WARN`: `60%` of the category weight
- `FAIL`: `0%` of the category weight

## Score Interpretation

- `85-100`: `PASS`
- `70-84`: `WARN`
- `<70`: `FAIL`

## Hard-Fail Categories

The overall result is still `FAIL` when any of these categories fail:

- block grouping
- local wire clarity
- overlap count
- power flow readability
- ERC status
- annotation status
- footprint status
