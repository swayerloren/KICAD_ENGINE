# Missing Footprint Candidates

Status: `UNVERIFIED_FOOTPRINT_GAP_REPORT`

- Component records checked: 125
- Rows requiring verification or missing candidates: 125

## How Agents Should Use This Report

Use this report to decide which footprints need source research, installed-library inspection, or project-local library creation. Do not use it to approve footprints. A row with candidates means "search found possible names," not "footprint is correct."

## Required Follow-Up Fields

Before any row can be closed, create or update a verification record with:

- exact manufacturer part number,
- package/orderable suffix,
- package drawing source URL or local private source note,
- KiCad library and footprint name,
- pad-number comparison,
- body, pitch, drill, courtyard, fab, and silkscreen review notes,
- connector orientation or polarity review where applicable,
- 3D model status if mechanical fit matters,
- human reviewer or `NEEDS_HUMAN_REVIEW`.

## Closure Statuses

| Status | Meaning |
| --- | --- |
| `CANDIDATES_FOUND_UNVERIFIED` | Candidate names exist; package review not complete. |
| `NO_CANDIDATE_FOUND` | No likely installed KiCad footprint found; consider project-local footprint creation. |
| `PROJECT_LOCAL_REQUIRED` | Exact footprint should be created in a project-local library. |
| `VERIFIED_WITH_DRAWING` | Exact package drawing and KiCad footprint review complete. |
| `REJECTED` | Candidate footprint was checked and does not match the package/drawing. |

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
| `P2_VERIFY_BEFORE_USE` | `8 MHz crystal generic` | `09_PASSIVES` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P2_VERIFY_BEFORE_USE` | `40 MHz crystal generic` | `09_PASSIVES` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
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
| `P2_VERIFY_BEFORE_USE` | `MCP2562` | `03_COMMUNICATION` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P2_VERIFY_BEFORE_USE` | `MCP2562FD` | `03_COMMUNICATION` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P2_VERIFY_BEFORE_USE` | `SN65HVD230` | `03_COMMUNICATION` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P2_VERIFY_BEFORE_USE` | `TJA1051` | `03_COMMUNICATION` | 1 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_MISSING_CANDIDATES` | `TJA1042` | `03_COMMUNICATION` | 0 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_MISSING_CANDIDATES` | `MCP2003` | `03_COMMUNICATION` | 0 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_MISSING_CANDIDATES` | `MAX3485` | `03_COMMUNICATION` | 0 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P2_VERIFY_BEFORE_USE` | `SN65HVD75` | `03_COMMUNICATION` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `CH340C` | `03_COMMUNICATION` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `CP2102N` | `03_COMMUNICATION` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `FT232RL` | `03_COMMUNICATION` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `USBLC6-2SC6` | `03_COMMUNICATION` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `TUSB320` | `03_COMMUNICATION` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. |
| `P2_VERIFY_BEFORE_USE` | `W5500` | `03_COMMUNICATION` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P2_VERIFY_BEFORE_USE` | `LAN8720` | `03_COMMUNICATION` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P2_VERIFY_BEFORE_USE` | `PCA9306` | `03_COMMUNICATION` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P2_VERIFY_BEFORE_USE` | `TXS0108E` | `03_COMMUNICATION` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P2_VERIFY_BEFORE_USE` | `TXB0108` | `03_COMMUNICATION` | 3 | `UNVERIFIED` | Exact package drawing verification required before use. |
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
| `P2_VERIFY_BEFORE_USE` | `0.1uF decoupling capacitor generic` | `09_PASSIVES` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P2_VERIFY_BEFORE_USE` | `10uF bulk capacitor generic` | `09_PASSIVES` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P2_VERIFY_BEFORE_USE` | `22pF crystal load capacitor generic` | `09_PASSIVES` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P2_VERIFY_BEFORE_USE` | `10k pull-up resistor generic` | `09_PASSIVES` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P2_VERIFY_BEFORE_USE` | `0 ohm jumper resistor generic` | `09_PASSIVES` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P2_VERIFY_BEFORE_USE` | `ferrite bead generic` | `09_PASSIVES` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P2_VERIFY_BEFORE_USE` | `common mode choke generic` | `09_PASSIVES` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P2_VERIFY_BEFORE_USE` | `8 MHz crystal generic` | `09_PASSIVES` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P2_VERIFY_BEFORE_USE` | `16 MHz crystal generic` | `09_PASSIVES` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P2_VERIFY_BEFORE_USE` | `40 MHz crystal generic` | `09_PASSIVES` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P2_VERIFY_BEFORE_USE` | `32.768 kHz crystal generic` | `09_PASSIVES` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `RF antenna pigtail generic` | `10_RF_AND_ANTENNAS` | 10 | `UNVERIFIED` | Connector orientation and mating-part risk. |
| `P2_VERIFY_BEFORE_USE` | `PCB antenna keepout generic` | `10_RF_AND_ANTENNAS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `U.FL to SMA pigtail generic` | `10_RF_AND_ANTENNAS` | 10 | `UNVERIFIED` | RF connector mechanical compatibility risk. Connector orientation and mating-part risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `ESP32-S3-WROOM-1` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Module land pattern and antenna keepout risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `ESP32-S3-WROOM-1U` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Module land pattern and antenna keepout risk. Connector orientation and mating-part risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `STM32F103C8T6` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `STM32F411CEU6` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `PIC16F877A` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `PIC18F4550` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `RP2040` | `01_MICROCONTROLLERS` | 2 | `UNVERIFIED` | QFN package drawing and exposed pad risk. |
| `P2_VERIFY_BEFORE_USE` | `MCP2562FD` | `03_COMMUNICATION` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P2_VERIFY_BEFORE_USE` | `SN65HVD230` | `03_COMMUNICATION` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `LM2596` | `02_POWER` | 10 | `UNVERIFIED` | Power/thermal package and layout risk. |
| `P0_MISSING_CANDIDATES` | `AMS1117-3.3` | `02_POWER` | 0 | `UNVERIFIED` | Regulator package and pinout variant risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `USB-C 16-pin receptacle generic` | `04_CONNECTORS` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `U.FL connector generic` | `10_RF_AND_ANTENNAS` | 10 | `UNVERIFIED` | RF connector mechanical compatibility risk. Connector orientation and mating-part risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `TVS diode generic` | `05_PROTECTION` | 10 | `UNVERIFIED` | Polarity/package risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `polyfuse generic` | `05_PROTECTION` | 10 | `UNVERIFIED` | Package and current rating risk. |

## Approval Rule

A row in this report is not a verified footprint. Approval requires exact manufacturer package drawing, pad numbering, orientation, courtyard, paste/mask, 3D/mechanical review where useful, and human review for high-risk categories.
