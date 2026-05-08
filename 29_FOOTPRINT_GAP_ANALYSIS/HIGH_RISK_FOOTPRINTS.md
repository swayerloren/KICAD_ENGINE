# High-Risk Footprints

Status: `UNVERIFIED_FOOTPRINT_GAP_REPORT`

## How Agents Should Use This Report

This report identifies footprint categories that are likely to cause electrical, mechanical, assembly, or fabrication failures if selected by name only. It is a triage report, not a verification report. Every row remains blocked for production use until exact package/mechanical review is complete and a supporting verification record exists.

## High-Risk Categories

| Category | Why High Risk | Required Evidence |
| --- | --- | --- |
| USB-C connectors | Shell tabs, pin numbering, row orientation, board edge, CC/VBUS/shield policy. | Exact MPN drawing, mating orientation, KiCad footprint pad review, human review. |
| RF connectors | Edge launch geometry, impedance, ground stitching, gender, pigtail compatibility. | Exact drawing, RF layout review, mechanical review. |
| ESP32 and RF modules | Land pattern, antenna keepout, castellated pads, module variant differences. | Vendor module drawing and keepout guidance. |
| STM32 and MCU packages | Package suffix can change body, pitch, exposed pad, or pin count. | Datasheet/package drawing and symbol pinout review. |
| PMOS/SOT-23 parts | Source/gate/drain mapping varies by symbol and footprint. | Datasheet pinout plus KiCad pad mapping review. |
| ESD arrays | Flow-through orientation and pin numbering are easy to reverse. | Datasheet pin map and layout recommendation. |
| Regulators | Thermal pad, switching node, capacitor layout, and package variants matter. | Datasheet package drawing and layout guidance. |
| Barrel/automotive connectors | Mechanical fit, pin numbering, panel/board edge orientation. | Exact manufacturer drawing and human review. |
| Mounting holes/test pads | Drill/plating/clearance and access are project/fab dependent. | Fab limits and mechanical requirements. |

## Status Rule

Candidate count only means a text search found possible KiCad footprints. It does not mean any candidate is correct. Keep `Exact Verification` as `UNVERIFIED` until exact package drawing, pad numbering, orientation, courtyard, paste/mask, and mechanical review are complete.

## Candidate Rows

| Priority | Part | Category | Candidate Count | Exact Verification | Notes |
| --- | --- | --- | ---: | --- | --- |
| `P1_PACKAGE_DRAWING_REVIEW` | `ESP32-S3-WROOM-1` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Module land pattern and antenna keepout risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `ESP32-S3-WROOM-1U` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Module land pattern and antenna keepout risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `STM32F103C8T6` | `01_MICROCONTROLLERS` | 4 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `STM32F411CEU6` | `01_MICROCONTROLLERS` | 1 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_MISSING_CANDIDATES` | `PIC16F877A` | `01_MICROCONTROLLERS` | 0 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_MISSING_CANDIDATES` | `PIC18F4550` | `01_MICROCONTROLLERS` | 0 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `RP2040` | `01_MICROCONTROLLERS` | 2 | `UNVERIFIED` | QFN package drawing and exposed pad risk. |
| `P0_MISSING_CANDIDATES` | `MCP2562FD` | `03_COMMUNICATION` | 0 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_MISSING_CANDIDATES` | `SN65HVD230` | `03_COMMUNICATION` | 0 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_MISSING_CANDIDATES` | `LM2596` | `02_POWER` | 0 | `UNVERIFIED` | Power/thermal package and layout risk. |
| `P0_MISSING_CANDIDATES` | `AMS1117-3.3` | `02_POWER` | 0 | `UNVERIFIED` | Regulator package and pinout variant risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `USB-C 16-pin receptacle generic` | `04_CONNECTORS` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `U.FL connector generic` | `04_CONNECTORS` | 3 | `UNVERIFIED` | RF connector mechanical compatibility risk. Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `SMA edge connector generic` | `04_CONNECTORS` | 10 | `UNVERIFIED` | RF connector gender/orientation/edge-launch risk. Connector orientation and mating-part risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `polyfuse generic` | `05_PROTECTION` | 10 | `UNVERIFIED` | Package and current rating risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `TVS diode generic` | `05_PROTECTION` | 10 | `UNVERIFIED` | Polarity/package risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `ESD diode array generic` | `05_PROTECTION` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `ESP32-WROOM-32` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Module land pattern and antenna keepout risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `ESP32-WROVER` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Module land pattern and antenna keepout risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `ESP32-S3-WROOM-1` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Module land pattern and antenna keepout risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `ESP32-S3-WROOM-1U` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Module land pattern and antenna keepout risk. Connector orientation and mating-part risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `ESP32-S3-MINI-1` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Module land pattern and antenna keepout risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `ESP32-C3-MINI-1` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Module land pattern and antenna keepout risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `ESP32-C6-WROOM-1` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Module land pattern and antenna keepout risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `ESP32-H2-MINI-1` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Module land pattern and antenna keepout risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `PIC16F877A` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `PIC16F18346` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `PIC18F4550` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `PIC18F25K80` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_MISSING_CANDIDATES` | `PIC24FJ64GA002` | `01_MICROCONTROLLERS` | 0 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_MISSING_CANDIDATES` | `dsPIC33CK256MP506` | `01_MICROCONTROLLERS` | 0 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `PIC32MX250F128D` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `ATmega328P` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `ATtiny85` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `ATmega32U4` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `STM32F103C8T6` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `STM32F401CCU6` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `STM32F411CEU6` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `STM32F405RGT6` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `STM32G030F6P6` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `STM32G431CBT6` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `STM32H743VIT6` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `STM32U575ZIT6` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `STM32WB55RGV6` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_MISSING_CANDIDATES` | `LM2596` | `02_POWER` | 0 | `UNVERIFIED` | Power/thermal package and layout risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `MP1584` | `02_POWER` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_MISSING_CANDIDATES` | `AMS1117-3.3` | `02_POWER` | 0 | `UNVERIFIED` | Regulator package and pinout variant risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `AP2112K-3.3` | `02_POWER` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_MISSING_CANDIDATES` | `MCP1700` | `02_POWER` | 0 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_MISSING_CANDIDATES` | `TLV755P` | `02_POWER` | 0 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_MISSING_CANDIDATES` | `MIC5504` | `02_POWER` | 0 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `TPS5430` | `02_POWER` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `TPS62177` | `02_POWER` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `TP4056` | `02_POWER` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_MISSING_CANDIDATES` | `MCP73831` | `02_POWER` | 0 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `generic resettable polyfuse` | `02_POWER` | 10 | `UNVERIFIED` | Package and current rating risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `generic SMAJ TVS diode` | `02_POWER` | 10 | `UNVERIFIED` | Polarity/package risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `generic USB TVS diode` | `02_POWER` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. Polarity/package risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `generic Schottky reverse polarity diode` | `02_POWER` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `generic P-channel MOSFET reverse polarity circuit` | `02_POWER` | 10 | `UNVERIFIED` | Gate/source/drain pin mapping risk. |
| `P0_MISSING_CANDIDATES` | `TJA1042` | `03_COMMUNICATION` | 0 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_MISSING_CANDIDATES` | `MCP2003` | `03_COMMUNICATION` | 0 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_MISSING_CANDIDATES` | `MAX3485` | `03_COMMUNICATION` | 0 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `CH340C` | `03_COMMUNICATION` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `CP2102N` | `03_COMMUNICATION` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `FT232RL` | `03_COMMUNICATION` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `USBLC6-2SC6` | `03_COMMUNICATION` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `TUSB320` | `03_COMMUNICATION` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `USB-C 16-pin USB2-only receptacle generic` | `04_CONNECTORS` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `USB-C 24-pin full-feature receptacle generic` | `04_CONNECTORS` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `micro USB B generic` | `04_CONNECTORS` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `barrel jack 5.5x2.1 generic` | `04_CONNECTORS` | 10 | `UNVERIFIED` | Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `JST-PH 2-pin generic` | `04_CONNECTORS` | 10 | `UNVERIFIED` | Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `JST-XH 2-pin generic` | `04_CONNECTORS` | 10 | `UNVERIFIED` | Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `JST-GH 4-pin generic` | `04_CONNECTORS` | 10 | `UNVERIFIED` | Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `2.54mm pin header generic` | `04_CONNECTORS` | 10 | `UNVERIFIED` | Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `3.5mm terminal block generic` | `04_CONNECTORS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `U.FL/IPEX MHF1 generic` | `04_CONNECTORS` | 10 | `UNVERIFIED` | RF connector mechanical compatibility risk. Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `SMA edge launch generic` | `04_CONNECTORS` | 10 | `UNVERIFIED` | RF connector gender/orientation/edge-launch risk. Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `RP-SMA pigtail generic` | `04_CONNECTORS` | 10 | `UNVERIFIED` | RF connector gender/orientation/edge-launch risk. Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `generic sealed automotive connector` | `04_CONNECTORS` | 10 | `UNVERIFIED` | Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `generic Honda-style sub-harness connector placeholder` | `04_CONNECTORS` | 10 | `UNVERIFIED` | Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `USB ESD diode array generic` | `05_PROTECTION` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `CAN TVS diode generic` | `05_PROTECTION` | 10 | `UNVERIFIED` | Polarity/package risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `RF antenna pigtail generic` | `10_RF_AND_ANTENNAS` | 10 | `UNVERIFIED` | Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `U.FL to SMA pigtail generic` | `10_RF_AND_ANTENNAS` | 10 | `UNVERIFIED` | RF connector mechanical compatibility risk. Connector orientation and mating-part risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `ESP32-S3-WROOM-1` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Module land pattern and antenna keepout risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `ESP32-S3-WROOM-1U` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Module land pattern and antenna keepout risk. Connector orientation and mating-part risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `STM32F103C8T6` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `STM32F411CEU6` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `PIC16F877A` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `PIC18F4550` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `RP2040` | `01_MICROCONTROLLERS` | 2 | `UNVERIFIED` | QFN package drawing and exposed pad risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `LM2596` | `02_POWER` | 10 | `UNVERIFIED` | Power/thermal package and layout risk. |
| `P0_MISSING_CANDIDATES` | `AMS1117-3.3` | `02_POWER` | 0 | `UNVERIFIED` | Regulator package and pinout variant risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `USB-C 16-pin receptacle generic` | `04_CONNECTORS` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `U.FL connector generic` | `10_RF_AND_ANTENNAS` | 10 | `UNVERIFIED` | RF connector mechanical compatibility risk. Connector orientation and mating-part risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `TVS diode generic` | `05_PROTECTION` | 10 | `UNVERIFIED` | Polarity/package risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `polyfuse generic` | `05_PROTECTION` | 10 | `UNVERIFIED` | Package and current rating risk. |

## Approval Rule

A row in this report is not a verified footprint. Approval requires exact manufacturer package drawing, pad numbering, orientation, courtyard, paste/mask, 3D/mechanical review where useful, and human review for high-risk categories.
