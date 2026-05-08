# Connector Footprint Gaps

Status: `UNVERIFIED_FOOTPRINT_GAP_REPORT`

## How Agents Should Use This Report

Connector rows require exact manufacturer part number, drawing, pin numbering, mating connector, cable or board-edge orientation, 3D/mechanical review, and human review. A connector footprint must never be approved because it has the same pitch, pin count, or generic family name.

## Required Connector Verification Evidence

| Evidence | Required Before Approval |
| --- | --- |
| Exact MPN | Yes. Generic connector names remain `UNVERIFIED`. |
| Manufacturer drawing | Yes. Must show pad pattern, shell tabs, pin numbering, and mechanical outline. |
| Mating connector/cable | Required when orientation or mechanical compatibility matters. |
| Board-edge direction | Required for USB, barrel, RF edge launch, terminal blocks, automotive, and external connectors. |
| KiCad footprint review | Pad numbers, pad sizes, drills, shell/mechanical pads, courtyard, fab outline, silk, pin-1 mark. |
| 3D/mechanical review | Required for board-edge, enclosure, tall, RF, USB-C, and cable-facing connectors. |
| Human review | Required for all connector approval. |

## Closure Statuses

Use `VERIFIED_WITH_DRAWING_AND_HUMAN_REVIEW` only when all evidence above is recorded. Otherwise use `CANDIDATE_ONLY`, `NEEDS_MPN`, `NEEDS_DRAWING`, `NEEDS_ORIENTATION_REVIEW`, or `REJECTED`.

## Candidate Rows

| Priority | Part | Category | Candidate Count | Exact Verification | Notes |
| --- | --- | --- | ---: | --- | --- |
| `P0_HUMAN_MECHANICAL_REVIEW` | `USB-C 16-pin receptacle generic` | `04_CONNECTORS` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `U.FL connector generic` | `04_CONNECTORS` | 3 | `UNVERIFIED` | RF connector mechanical compatibility risk. Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `SMA edge connector generic` | `04_CONNECTORS` | 10 | `UNVERIFIED` | RF connector gender/orientation/edge-launch risk. Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `ESP32-S3-WROOM-1U` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Module land pattern and antenna keepout risk. Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `PIC18F4550` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `ATmega32U4` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `generic USB TVS diode` | `02_POWER` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. Polarity/package risk. |
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
| `P0_HUMAN_MECHANICAL_REVIEW` | `RF antenna pigtail generic` | `10_RF_AND_ANTENNAS` | 10 | `UNVERIFIED` | Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `U.FL to SMA pigtail generic` | `10_RF_AND_ANTENNAS` | 10 | `UNVERIFIED` | RF connector mechanical compatibility risk. Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `ESP32-S3-WROOM-1U` | `01_MICROCONTROLLERS` | 10 | `UNVERIFIED` | Module land pattern and antenna keepout risk. Connector orientation and mating-part risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `USB-C 16-pin receptacle generic` | `04_CONNECTORS` | 10 | `UNVERIFIED` | USB and USB-C connector footprint/orientation risk. |
| `P0_HUMAN_MECHANICAL_REVIEW` | `U.FL connector generic` | `10_RF_AND_ANTENNAS` | 10 | `UNVERIFIED` | RF connector mechanical compatibility risk. Connector orientation and mating-part risk. |

## Approval Rule

A row in this report is not a verified footprint. Approval requires exact manufacturer package drawing, pad numbering, orientation, courtyard, paste/mask, 3D/mechanical review where useful, and human review for high-risk categories.
