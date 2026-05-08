# Power Package Footprint Gaps

Status: `UNVERIFIED_FOOTPRINT_GAP_REPORT`

- Power rows require exact package/thermal drawing, pad numbering, exposed pad, copper/thermal requirements, and layout-loop review.

## Candidate Rows

| Priority | Part | Category | Candidate Count | Exact Verification | Notes |
| --- | --- | --- | ---: | --- | --- |
| `P0_MISSING_CANDIDATES` | `LM2596` | `02_POWER` | 0 | `UNVERIFIED` | Power/thermal package and layout risk. |
| `P0_MISSING_CANDIDATES` | `AMS1117-3.3` | `02_POWER` | 0 | `UNVERIFIED` | Regulator package and pinout variant risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `polyfuse generic` | `05_PROTECTION` | 10 | `UNVERIFIED` | Package and current rating risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `TVS diode generic` | `05_PROTECTION` | 10 | `UNVERIFIED` | Polarity/package risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `ESD diode array generic` | `05_PROTECTION` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
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
| `P1_PACKAGE_DRAWING_REVIEW` | `generic Schottky reverse polarity diode` | `02_POWER` | 10 | `UNVERIFIED` | Exact package drawing verification required before use. |
| `P1_PACKAGE_DRAWING_REVIEW` | `generic P-channel MOSFET reverse polarity circuit` | `02_POWER` | 10 | `UNVERIFIED` | Gate/source/drain pin mapping risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `CAN TVS diode generic` | `05_PROTECTION` | 10 | `UNVERIFIED` | Polarity/package risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `LM2596` | `02_POWER` | 10 | `UNVERIFIED` | Power/thermal package and layout risk. |
| `P0_MISSING_CANDIDATES` | `AMS1117-3.3` | `02_POWER` | 0 | `UNVERIFIED` | Regulator package and pinout variant risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `TVS diode generic` | `05_PROTECTION` | 10 | `UNVERIFIED` | Polarity/package risk. |
| `P1_PACKAGE_DRAWING_REVIEW` | `polyfuse generic` | `05_PROTECTION` | 10 | `UNVERIFIED` | Package and current rating risk. |

## Approval Rule

A row in this report is not a verified footprint. Approval requires exact manufacturer package drawing, pad numbering, orientation, courtyard, paste/mask, 3D/mechanical review where useful, and human review for high-risk categories.
