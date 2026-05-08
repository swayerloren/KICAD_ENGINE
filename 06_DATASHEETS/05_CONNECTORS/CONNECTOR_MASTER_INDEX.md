# Connector Master Index

Date: 2026-05-02

Status: generic connector source and verification index. No connector datasheets or drawings were downloaded for this update.

## Purpose

This folder is the source-index side of the connector database. It records the connector families and verification work that AI agents must complete before using connector symbols or footprints in KiCad.

Connector errors are high-risk because they often survive ERC/DRC and only appear as wrong mating parts, reversed pin numbering, impossible cable orientation, poor mechanical fit, RF loss, or unusable enclosure alignment.

Companion files:

- `08_COMPONENT_DATABASE/04_CONNECTORS/CONNECTOR_SELECTION_GUIDE.md`
- `08_COMPONENT_DATABASE/04_CONNECTORS/CONNECTOR_RECORDS.md`
- `08_COMPONENT_DATABASE/04_CONNECTORS/connector_records.json`
- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/CONNECTOR_FOOTPRINT_VERIFICATION_RULES.md`
- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/USB_C_CONNECTOR_RULES.md`
- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/RF_CONNECTOR_RULES.md`
- `08_COMPONENT_DATABASE/13_DESIGN_RULE_SNIPPETS/AUTOMOTIVE_CONNECTOR_RULES.md`

## Agent Rules

- Treat every generic connector record as `UNVERIFIED_PLACEHOLDER`.
- Do not use a connector footprint until it is matched to an exact manufacturer part number and drawing.
- Do not infer pin numbering from symbol order, schematic appearance, or connector family name.
- Do not infer orientation from 3D model appearance alone.
- Confirm the mating connector, cable, crimp contacts, shell/keying, and assembly method.
- Confirm current rating, voltage rating, temperature, mating cycles, retention, and environmental rating from the exact datasheet.
- Confirm board-edge, enclosure, panel, cable-bend, antenna, and keepout constraints before PCB release.

## Connector Family Coverage

| Family | Status | Notes |
| --- | --- | --- |
| USB-C | GENERIC_PLACEHOLDERS | USB2-only 16-pin and full-feature 24-pin records exist; exact receptacle drawing required. |
| micro USB | GENERIC_PLACEHOLDER | Generic Micro-B record exists; exact shield tabs and peg geometry required. |
| Barrel jacks | GENERIC_PLACEHOLDER | 5.5x2.1 placeholder exists; switched/non-switched pinout and panel geometry must be verified. |
| JST PH/XH/SH/GH | PARTIAL | PH 2-pin, XH 2-pin, GH 4-pin placeholders exist; SH still missing. |
| Molex | FAMILY_ONLY | Vendor family noted; no exact records yet. |
| TE Connectivity | FAMILY_ONLY | Vendor family noted; no exact records yet. |
| Automotive connectors | GENERIC_PLACEHOLDERS | Sealed automotive and Honda-style sub-harness placeholders exist; exact housing/terminal/seal system required. |
| Terminal blocks | GENERIC_PLACEHOLDER | 3.5mm terminal block placeholder exists; pitch and pin numbering vary by vendor. |
| Pin headers | GENERIC_PLACEHOLDER | 2.54mm pin header placeholder exists; orientation and shrouding remain unresolved. |
| Board-to-board connectors | MISSING | Add after exact mezzanine/board-stack requirements are known. |
| U.FL/IPEX | GENERIC_PLACEHOLDER | MHF1/U.FL placeholder exists; exact brand, height, and mating cable required. |
| SMA / RP-SMA | GENERIC_PLACEHOLDERS | Edge launch and pigtail placeholders exist; RF launch geometry must be fab-stackup-specific. |
| Edge RF connectors | GENERIC_PLACEHOLDER | Covered by SMA edge-launch placeholder; exact connector and board thickness required. |
| Waterproof connectors | FAMILY_ONLY | Covered by sealed automotive placeholder for now; add M-series/IP-rated records later. |

## Generic Records Created

| Record ID | Connector | Verification Status | Notes |
| --- | --- | --- | --- |
| `CONN_USB_C_16PIN_USB2_RECEPTACLE_GENERIC` | USB-C 16-pin USB2-only receptacle | `UNVERIFIED_PLACEHOLDER` | Exact connector, footprint, shell, and CC behavior required. |
| `CONN_USB_C_24PIN_FULL_FEATURE_RECEPTACLE_GENERIC` | USB-C 24-pin full-feature receptacle | `UNVERIFIED_PLACEHOLDER` | Exact connector and high-speed routing requirements required. |
| `CONN_MICRO_USB_B_GENERIC` | micro USB B | `UNVERIFIED_PLACEHOLDER` | Shield tab and mounting peg geometry varies. |
| `CONN_BARREL_JACK_5_5X2_1_GENERIC` | barrel jack 5.5x2.1 | `UNVERIFIED_PLACEHOLDER` | Switched pins and mechanical style vary. |
| `CONN_JST_PH_2PIN_GENERIC` | JST-PH 2-pin | `UNVERIFIED_PLACEHOLDER` | Use exact JST or compatible part drawing. |
| `CONN_JST_XH_2PIN_GENERIC` | JST-XH 2-pin | `UNVERIFIED_PLACEHOLDER` | Larger pitch/power connector family; exact vertical/right-angle drawing required. |
| `CONN_JST_GH_4PIN_GENERIC` | JST-GH 4-pin | `UNVERIFIED_PLACEHOLDER` | Latching low-profile family; exact side/top entry required. |
| `CONN_PIN_HEADER_2_54MM_GENERIC` | 2.54mm pin header | `UNVERIFIED_PLACEHOLDER` | Shrouded, keyed, right-angle, and unshrouded footprints differ. |
| `CONN_TERMINAL_BLOCK_3_5MM_GENERIC` | 3.5mm terminal block | `UNVERIFIED_PLACEHOLDER` | Pin numbering and wire entry direction vary. |
| `CONN_UFL_IPEX_MHF1_GENERIC` | U.FL/IPEX MHF1 | `UNVERIFIED_PLACEHOLDER` | RF height, keepout, and mating cable required. |
| `CONN_SMA_EDGE_LAUNCH_GENERIC` | SMA edge launch | `UNVERIFIED_PLACEHOLDER` | Board thickness and stackup are part of the footprint. |
| `CONN_RP_SMA_PIGTAIL_GENERIC` | RP-SMA pigtail | `UNVERIFIED_PLACEHOLDER` | Usually cable assembly, not a direct board footprint. |
| `CONN_SEALED_AUTOMOTIVE_GENERIC` | generic sealed automotive connector | `UNVERIFIED_PLACEHOLDER` | Housing, terminals, seals, CPA/TPA, and wire gauge required. |
| `CONN_HONDA_SUB_HARNESS_PLACEHOLDER` | generic Honda-style sub-harness connector placeholder | `UNVERIFIED_PLACEHOLDER` | Must be replaced with exact OEM/service connector data. |

## Source Policy

For public GitHub releases:

- Prefer storing links, source metadata, and AI-readable summaries.
- Do not bundle connector drawings or datasheets unless redistribution rights are confirmed.
- For automotive and OEM-style connectors, assume redistribution is not allowed unless explicitly proven otherwise.

## Missing Work

- Add exact manufacturer records for common USB-C receptacles.
- Add exact JST, Molex, TE, Amphenol, Hirose, I-PEX, Samtec, Phoenix Contact, Wurth, and CUI connector part records.
- Add connector footprint verification scripts that compare KiCad pad locations against a structured drawing record.
- Add 3D clearance review workflow for enclosure and cable access.
- Add mating-part and crimp-contact index.
