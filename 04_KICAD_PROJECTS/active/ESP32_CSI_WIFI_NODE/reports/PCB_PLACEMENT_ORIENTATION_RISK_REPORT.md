# ESP32_CSI_WIFI_NODE PCB Placement Orientation Risk Report

Date: 2026-05-06

Status: `NOT_RUN_NO_ACTUAL_PLACEMENT`

No footprints were placed during this session. The risks below are required review flags for the future placement pass.

## Required Review Rules Applied

- Connector orientation: `CONNECTOR_ORIENTATION_HUMAN_REVIEW_REQUIRED`
- Polarity/orientation: `POLARITY_HUMAN_REVIEW_REQUIRED`
- USB layout: `USB_LAYOUT_REVIEW_REQUIRED`
- Power layout: `POWER_LAYOUT_REVIEW_REQUIRED`
- RF layout: `RF_LAYOUT_REVIEW_REQUIRED`

## Connector Risks

| Item | Risk | Current status |
|---|---|---|
| `J1` barrel jack | Edge orientation, center pin polarity, mechanical overhang, cable access | `CONNECTOR_ORIENTATION_HUMAN_REVIEW_REQUIRED` |
| `J2` USB-C | Receptacle orientation, shell position, board-edge alignment, pin numbering, 3D model direction | `USB_CONNECTOR_ORIENTATION_HUMAN_REVIEW_REQUIRED` |
| ESP32-S3-WROOM-1U U.FL / pigtail area | RF connector/cable exit and antenna keepout clearance | `RF_CONNECTOR_ORIENTATION_HUMAN_REVIEW_REQUIRED` |
| Test pads | Accessibility after connector/module placement | `HUMAN_REVIEW_REQUIRED` |

## Polarity And Pin-1 Risks

| Item | Risk | Current status |
|---|---|---|
| `Q1` power MOSFET | Source/drain/gate orientation and footprint pad mapping | `POLARITY_HUMAN_REVIEW_REQUIRED` |
| `D1` input TVS/protection diode | Cathode/anode orientation, footprint marking, protected node mapping | `POLARITY_HUMAN_REVIEW_REQUIRED` |
| `D2`, `D3` LEDs | LED polarity, silkscreen readability, visible-edge orientation | `POLARITY_HUMAN_REVIEW_REQUIRED` |
| `U1` buck regulator | Pin 1, thermal pad, switch-node side, datasheet layout direction | `POLARITY_HUMAN_REVIEW_REQUIRED` |
| `U2` ESP32-S3 module | Pin 1/module orientation, antenna/U.FL clearance, bootstrapping pin access | `POLARITY_HUMAN_REVIEW_REQUIRED` |
| `U3` USB ESD array | Data-line pad order and orientation relative to connector and ESP32 pins | `POLARITY_HUMAN_REVIEW_REQUIRED` |
| `SW1`, `SW2` reset/boot switches | Pin pairing and accessible-edge orientation | `HUMAN_REVIEW_REQUIRED` |

## USB Layout Risks

| Item | Risk | Current status |
|---|---|---|
| `J2 -> U3` | ESD must be close to USB-C connector and avoid long stubs | `USB_ESD_PLACEMENT_REVIEW_REQUIRED` |
| `U3 -> R6/R7 -> U2` | D+/D- path must remain short and paired as practical | `USB_DIFF_PAIR_REVIEW_REQUIRED` |
| `R4/R5` CC resistors | Must be close to USB-C connector with correct CC pin mapping | `USB_LAYOUT_REVIEW_REQUIRED` |
| USB shield/shell | Shield connection strategy must be intentional and reviewable | `USB_LAYOUT_REVIEW_REQUIRED` |

## Power Layout Risks

| Item | Risk | Current status |
|---|---|---|
| `J1 -> F1 -> Q1 -> D1/C1` | Input protection must be close to the power entry path | `INPUT_PROTECTION_REVIEW_REQUIRED` |
| `U1/L1/C2/C3/C4/C5` | Buck hot loop, switch node, input/output capacitors, and thermal path | `POWER_LAYOUT_REVIEW_REQUIRED` |
| `+3V3` rail | Current path width, return current, and decoupling placement | `POWER_LAYOUT_REVIEW_REQUIRED` |
| Regulator thermal area | Copper and via strategy not yet defined | `THERMAL_REVIEW_REQUIRED` |

## RF Layout Risks

| Item | Risk | Current status |
|---|---|---|
| ESP32 antenna/U.FL region | Antenna keepout and pigtail bend radius must be preserved | `RF_ANTENNA_KEEP_OUT_REVIEW_REQUIRED` |
| RF feedline / U.FL path | Impedance geometry must not be guessed | `RF_FEEDLINE_REVIEW_REQUIRED` |
| Copper under RF keepout | Must follow module layout guide before zones or pours are added | `RF_LAYOUT_REVIEW_REQUIRED` |

## Disposition

Orientation risk result: `HUMAN_REVIEW_REQUIRED_AFTER_ACTUAL_PLACEMENT`

The next valid step is not routing. The next valid PCB editing step is blocked until the schematic-to-PCB gate passes, a PCB exists, and mechanical setup/outline exists.
