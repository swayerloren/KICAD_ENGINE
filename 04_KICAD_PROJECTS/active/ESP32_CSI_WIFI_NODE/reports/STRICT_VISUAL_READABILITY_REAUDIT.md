# Strict Visual Readability Re-Audit

Project: ESP32_CSI_WIFI_NODE  
Date: 2026-05-06  
Scope: schematic visual readability only  
Result: NOT_READY_NEEDS_MORE_VISUAL_REPAIR

## Evidence Generated

Full-page exports:
- `_verification/schematic_visual/full_page/ESP32_CSI_WIFI_NODE.svg`
- `_verification/schematic_visual/full_page/ESP32_CSI_WIFI_NODE.pdf`
- `_verification/schematic_visual/full_page/ESP32_CSI_WIFI_NODE.png`

Close-up crop folder:
- `_verification/schematic_visual/crops/`

Automated crop generation completed, but automated crop generation is not a human-readable visual pass.

## Overall Finding

Visual status: VISUAL_FAIL

The current schematic is improved from earlier states, but it is still not clean enough for LJ visual approval. Multiple rendered close-up crops show text touching or crossing wires, labels crowded into pins/symbols, clipped crop context, unreadable or crowded component values, and review-note/crop framing problems.

PCB update remains blocked.

## Block Results

| Block | Result | Findings |
|---|---:|---|
| input power | FAIL | F1 net labels touch/cross symbol and wires. D1/C2/TVS area is crowded. `TVS_NEEDS_REVIEW` and C2/GND/value text are too close to active circuitry. |
| reverse polarity / protection | FAIL | F1 is clipped at the crop edge. `+5V_FUSED` crosses/touches the fuse. Q1 value and `+5V_PROTECTED` crowd the PMOS area. |
| TVS / input capacitor | FAIL | Crop is poorly framed and includes clipped adjacent Q1/U1 context. `+5V_PROTECTED` and D1 labeling crowd the diode/wire area. |
| buck regulator | FAIL | U1 left-side labels are clipped. `BUCK_SW`, `BUCK_BST`, C5, L1, C1, and C3 text/wires are crowded or touching. ESP32 module text intrudes into the crop. |
| ESP32 module | FAIL | U2 top power/value area remains crowded. Several net labels are too close to pins/wires. The block is inspectable but not professionally readable under the strict rule. |
| USB-C connector | FAIL | CC/DP/DM labels are too close to connector pins/wires. R3 shield area is crowded. Support-part text appears in the crop with poor separation. |
| USB ESD / CC / series resistors | FAIL | U3 GND/value text crosses or touches the ESD wiring. CC resistor crop has stacked/crowded R4/R5/R6/R? text and GND labels. |
| reset / boot | FAIL | R1/R2 refs/values crowd resistor symbols and labels. SW1/SW2 labels visually merge with GND text. Crop boundary clips nearby labels. |
| LEDs | FAIL | D2/D3 net labels touch LED pins/wires. R9 is clipped at the crop boundary. R8/R9 values are still crowded. |
| test pads | FAIL | TP1/TP2/TP3 labels and net text overlap or stack with symbols and GND labels. Several test-pad net labels touch wires/markers. |
| mounting holes | PASS_WITH_WARNING | MH1-MH4 are readable. Crop includes unrelated adjacent decoupling-cap text, so the crop should be reframed, but the mounting-hole items themselves are readable. |
| review notes table | FAIL | Review notes are separated from main circuitry, but the crop is clipped at the right edge and mixes with mounting holes and unrelated cap text. |

## Exact Remaining Visual Defects

- Text and net labels still touch or cross wires around F1, D1, Q1, U1, L1, C1, C3, C5, U3, CC resistors, reset/boot resistors, LEDs, and test pads.
- Several crop windows are poorly framed and include clipped or unrelated circuit content.
- Some component value/reference fields remain too close to symbol bodies or pins.
- Review notes need a cleaner isolated table/crop with no clipping.
- Mounting-hole crop should exclude adjacent decoupling capacitor text even though the holes themselves are readable.

## LJ Review Recommendation

LJ should open KiCad only to confirm the defects listed here, not to approve the schematic for PCB update.

The schematic is not ready for LJ visual approval. A further visual cleanup pass is required before the schematic can be treated as human-readable.

## PCB Update Status

PCB update allowed: NO

Reason: strict visual readability gate failed. The schematic-to-PCB gate must remain blocked until visual defects and high-risk review items are resolved.
