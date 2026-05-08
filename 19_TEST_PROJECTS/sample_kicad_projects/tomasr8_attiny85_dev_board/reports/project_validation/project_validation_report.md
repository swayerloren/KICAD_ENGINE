# KiCad Project Validation Report

Generated: 2026-05-03T14:58:55
Status: `WARN`

## Project

- Input: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\attiny85.kicad_pro`
- Project file: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\attiny85.kicad_pro`
- Schematic: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\attiny85.kicad_sch`
- PCB: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\attiny85.kicad_pcb`

## Summary

- PASS: 4
- WARN: 8
- FAIL: 0

## Checks

| Status | Check | Summary |
| --- | --- | --- |
| `PASS` | Project File Presence | Checked project, schematic, and PCB source file presence. |
| `WARN` | Project Library Tables And Symbol Libraries | Checked project-local tables and symbol library resolution. |
| `WARN` | Missing Footprint Libraries Or Footprints | Checked footprint libraries and assigned footprint files. |
| `WARN` | Missing 3D Models | Checked 3D model references in the PCB. |
| `PASS` | ERC, DRC, And BOM Export Availability | Checked whether standard KiCad CLI validation/export commands can be run. |
| `PASS` | Unconnected Power Review | Performed static power-symbol and no-connect inventory; ERC is still required. |
| `WARN` | BOM Datasheet Coverage | Checked schematic components for datasheet fields, component database matches, or local datasheet filename hits. |
| `WARN` | Component Database Matches | Matched 2 schematic components against 130 component database records. |
| `WARN` | Connector Orientation Review Needed | Connector-like components require human pinout, mating, orientation, and mechanical review. |
| `WARN` | Polarity-Sensitive Parts Review Needed | Polarity-sensitive components require human orientation and assembly review. |
| `PASS` | RF Layout Review Needed | No static keyword review hits found. |
| `WARN` | USB/CAN/Automotive Rule Review Needed | USB, CAN, LIN, or automotive-like items require protocol-specific review. |

## Details

### Project File Presence

Status: `PASS`

Checked project, schematic, and PCB source file presence.

```json
[
  {
    "project_input": "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE\\19_TEST_PROJECTS\\sample_kicad_projects\\tomasr8_attiny85_dev_board\\attiny85.kicad_pro"
  },
  {
    "project_dir": "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE\\19_TEST_PROJECTS\\sample_kicad_projects\\tomasr8_attiny85_dev_board"
  },
  {
    "project_file": "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE\\19_TEST_PROJECTS\\sample_kicad_projects\\tomasr8_attiny85_dev_board\\attiny85.kicad_pro"
  },
  {
    "schematic_files": [
      "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE\\19_TEST_PROJECTS\\sample_kicad_projects\\tomasr8_attiny85_dev_board\\attiny85.kicad_sch"
    ]
  },
  {
    "pcb_files": [
      "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE\\19_TEST_PROJECTS\\sample_kicad_projects\\tomasr8_attiny85_dev_board\\attiny85.kicad_pcb"
    ]
  }
]
```

### Project Library Tables And Symbol Libraries

Status: `WARN`

Checked project-local tables and symbol library resolution.

```json
[
  {
    "project_local_tables": [
      {
        "exists": false,
        "path": "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE\\19_TEST_PROJECTS\\sample_kicad_projects\\tomasr8_attiny85_dev_board\\sym-lib-table",
        "table": "project_sym"
      },
      {
        "exists": true,
        "path": "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE\\19_TEST_PROJECTS\\sample_kicad_projects\\tomasr8_attiny85_dev_board\\fp-lib-table",
        "table": "project_fp"
      },
      {
        "exists": false,
        "path": "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE\\19_TEST_PROJECTS\\sample_kicad_projects\\tomasr8_attiny85_dev_board\\design-block-lib-table",
        "table": "project_design_block"
      }
    ]
  },
  {
    "symbol_libraries_used": [
      "Connector",
      "Connector_Generic",
      "Device",
      "MCU_Microchip_ATtiny",
      "Regulator_Linear",
      "power"
    ]
  },
  {
    "missing_symbol_libraries_used": []
  },
  {
    "unresolved_symbol_table_entries": [
      {
        "name": "TPS62740DSSR",
        "resolved_path": "C:\\Users\\LJ\\Documents\\PSRD\\PROXIMITY KILL SWITCH\\PCB FOB\\footprints.pretty\\ul_TPS62740DSSR\\KiCADv6\\2026-01-11_21-10-46.kicad_sym",
        "table": "C:\\Users\\LJ\\AppData\\Roaming\\kicad\\9.0\\sym-lib-table",
        "uri": "C:/Users/LJ/Documents/PSRD/PROXIMITY KILL SWITCH/PCB FOB/footprints.pretty/ul_TPS62740DSSR/KiCADv6/2026-01-11_21-10-46.kicad_sym"
      }
    ]
  }
]
```

Recommended next steps:
- Document unresolved symbol library table URIs; do not patch global tables automatically unless the user requests it.
- Consider project-local library tables for reproducible projects that should not depend silently on global config.

### Missing Footprint Libraries Or Footprints

Status: `WARN`

Checked footprint libraries and assigned footprint files.

```json
[
  {
    "footprint_assignments_checked": 27
  },
  {
    "unresolved_footprint_libraries": []
  },
  {
    "missing_footprint_files": []
  },
  {
    "unresolved_footprint_table_entries": [
      {
        "name": "FOOTPRINT",
        "resolved_path": "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE\\19_TEST_PROJECTS\\sample_kicad_projects\\tomasr8_attiny85_dev_board\\footprints.pretty",
        "table": "C:\\Users\\LJ\\AppData\\Roaming\\kicad\\9.0\\fp-lib-table",
        "uri": "${KIPRJMOD}/footprints.pretty"
      },
      {
        "name": "footprints",
        "resolved_path": "C:\\Users\\LJ\\Documents\\PSRD\\PROXIMITY KILL SWITCH\\PCB FOB\\footprints.pretty",
        "table": "C:\\Users\\LJ\\AppData\\Roaming\\kicad\\9.0\\fp-lib-table",
        "uri": "C:/Users/LJ/Documents/PSRD/PROXIMITY KILL SWITCH/PCB FOB/footprints.pretty"
      }
    ]
  }
]
```

### Missing 3D Models

Status: `WARN`

Checked 3D model references in the PCB.

```json
[
  {
    "model_references_checked": 12
  },
  {
    "missing_models": []
  },
  {
    "unresolved_model_paths": [
      {
        "footprint_id": "Connector_PinSocket_2.54mm:PinSocket_2x05_P2.54mm_Vertical",
        "model": "${KICAD6_3DMODEL_DIR}/Connector_PinSocket_2.54mm.3dshapes/PinSocket_2x05_P2.54mm_Vertical.wrl",
        "reference": "",
        "resolved_path": null
      },
      {
        "footprint_id": "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal",
        "model": "${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal.wrl",
        "reference": "",
        "resolved_path": null
      },
      {
        "footprint_id": "LED_SMD:LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder",
        "model": "${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_1206_3216Metric.wrl",
        "reference": "",
        "resolved_path": null
      },
      {
        "footprint_id": "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal",
        "model": "${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal.wrl",
        "reference": "",
        "resolved_path": null
      },
      {
        "footprint_id": "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal",
        "model": "${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal.wrl",
        "reference": "",
        "resolved_path": null
      },
      {
        "footprint_id": "Package_DIP:DIP-8_W7.62mm_Socket",
        "model": "${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/DIP-8_W7.62mm_Socket.wrl",
        "reference": "",
        "resolved_path": null
      },
      {
        "footprint_id": "LED_SMD:LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder",
        "model": "${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_1206_3216Metric.wrl",
        "reference": "",
        "resolved_path": null
      },
      {
        "footprint_id": "Diode_THT:D_DO-34_SOD68_P7.62mm_Horizontal",
        "model": "${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/D_DO-34_SOD68_P7.62mm_Horizontal.wrl",
        "reference": "",
        "resolved_path": null
      },
      {
        "footprint_id": "Package_TO_SOT_SMD:SOT-223-3_TabPin2",
        "model": "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/SOT-223.wrl",
        "reference": "",
        "resolved_path": null
      },
      {
        "footprint_id": "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal",
        "model": "${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal.wrl",
        "reference": "",
        "resolved_path": null
      },
      {
        "footprint_id": "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal",
        "model": "${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal.wrl",
        "reference": "",
        "resolved_path": null
      },
      {
        "footprint_id": "Diode_THT:D_DO-34_SOD68_P7.62mm_Horizontal",
        "model": "${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/D_DO-34_SOD68_P7.62mm_Horizontal.wrl",
        "reference": "",
        "resolved_path": null
      }
    ]
  }
]
```

Recommended next steps:
- Resolve unknown 3D model variables before relying on visual/mechanical review.

### ERC, DRC, And BOM Export Availability

Status: `PASS`

Checked whether standard KiCad CLI validation/export commands can be run.

```json
[
  {
    "bom_export_available": true,
    "bom_wrapper": "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE\\03_TOOLS\\scripts\\export_bom.ps1",
    "drc_available": true,
    "drc_wrapper": "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE\\03_TOOLS\\scripts\\run_drc.ps1",
    "erc_available": true,
    "erc_wrapper": "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE\\03_TOOLS\\scripts\\run_erc.ps1",
    "kicad_cli": {
      "available": true,
      "error": "",
      "exit_code": 0,
      "path": "C:\\Program Files\\KiCad\\9.0\\bin\\kicad-cli.exe",
      "version_output": "9.0.7"
    }
  }
]
```

### Unconnected Power Review

Status: `PASS`

Performed static power-symbol and no-connect inventory; ERC is still required.

```json
[
  {
    "power_symbols_found": 2
  },
  {
    "pwr_flags_found": 2
  },
  {
    "no_connect_markers_found": 0
  },
  {
    "sample_power_symbols": [
      {
        "datasheet": "~",
        "exclude_from_bom": false,
        "file": "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE\\19_TEST_PROJECTS\\sample_kicad_projects\\tomasr8_attiny85_dev_board\\attiny85.kicad_sch",
        "footprint": "",
        "in_bom": true,
        "lib_id": "power:PWR_FLAG",
        "library": "power",
        "on_board": true,
        "raw_properties": {
          "Datasheet": "~",
          "Footprint": "",
          "Reference": "#FLG0101",
          "Value": "PWR_FLAG"
        },
        "reference": "#FLG0101",
        "symbol": "PWR_FLAG",
        "value": "PWR_FLAG"
      },
      {
        "datasheet": "~",
        "exclude_from_bom": false,
        "file": "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE\\19_TEST_PROJECTS\\sample_kicad_projects\\tomasr8_attiny85_dev_board\\attiny85.kicad_sch",
        "footprint": "",
        "in_bom": true,
        "lib_id": "power:PWR_FLAG",
        "library": "power",
        "on_board": true,
        "raw_properties": {
          "Datasheet": "~",
          "Footprint": "",
          "Reference": "#FLG0102",
          "Value": "PWR_FLAG"
        },
        "reference": "#FLG0102",
        "symbol": "PWR_FLAG",
        "value": "PWR_FLAG"
      }
    ]
  }
]
```

Recommended next steps:
- Run ERC before trusting power connectivity; static text inspection cannot prove every power pin is driven.
- Review hidden power pins and PWR_FLAG placement manually for regulators, connectors, and MCU power rails.

### BOM Datasheet Coverage

Status: `WARN`

Checked schematic components for datasheet fields, component database matches, or local datasheet filename hits.

```json
[
  {
    "components_with_datasheet_evidence": 3
  },
  {
    "components_missing_datasheet_evidence": [
      {
        "footprint": "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal",
        "library": "Device",
        "reference": "R2",
        "value": "66"
      },
      {
        "footprint": "Diode_THT:D_DO-34_SOD68_P7.62mm_Horizontal",
        "library": "Device",
        "reference": "D1",
        "value": "3.6 Zener"
      },
      {
        "footprint": "Connector_PinSocket_2.54mm:PinSocket_2x05_P2.54mm_Vertical",
        "library": "Connector_Generic",
        "reference": "J2",
        "value": "Conn_02x05_Odd_Even"
      },
      {
        "footprint": "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal",
        "library": "Device",
        "reference": "R4",
        "value": "470"
      },
      {
        "footprint": "Diode_THT:D_DO-34_SOD68_P7.62mm_Horizontal",
        "library": "Device",
        "reference": "D2",
        "value": "3.6 Zener"
      },
      {
        "footprint": "LED_SMD:LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder",
        "library": "Device",
        "reference": "D4",
        "value": "LED"
      },
      {
        "footprint": "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal",
        "library": "Device",
        "reference": "R3",
        "value": "66"
      },
      {
        "footprint": "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal",
        "library": "Device",
        "reference": "R5",
        "value": "470"
      },
      {
        "footprint": "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal",
        "library": "Device",
        "reference": "R1",
        "value": "1K5"
      },
      {
        "footprint": "LED_SMD:LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder",
        "library": "Device",
        "reference": "D3",
        "value": "LED"
      }
    ]
  }
]
```

Recommended next steps:
- Add source links, component database records, or local datasheet references for BOM components before release.

### Component Database Matches

Status: `WARN`

Matched 2 schematic components against 130 component database records.

```json
[
  {
    "matched_components": [
      {
        "matches": [
          {
            "part_number": "ATtiny85",
            "record_id": "MICROCHIP_ATTINY85",
            "source_file": "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE\\08_COMPONENT_DATABASE\\01_MICROCONTROLLERS\\microchip_part_records.json",
            "verified_status": "UNVERIFIED_PLACEHOLDER"
          }
        ],
        "reference": "U1",
        "value": "ATtiny85-20P"
      },
      {
        "matches": [
          {
            "part_number": "AMS1117-3.3",
            "record_id": "GENERIC_AMS1117-3.3",
            "source_file": "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE\\08_COMPONENT_DATABASE\\00_INDEX\\example_component_records.json",
            "verified_status": "UNVERIFIED_PLACEHOLDER"
          },
          {
            "part_number": "AMS1117-3.3",
            "record_id": "POWER_AMS1117_3V3",
            "source_file": "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE\\08_COMPONENT_DATABASE\\02_POWER\\power_part_records.json",
            "verified_status": "UNVERIFIED_PLACEHOLDER"
          },
          {
            "part_number": "AMS1117-3.3",
            "record_id": "AMS_AMS1117_3V3",
            "source_file": "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE\\08_COMPONENT_DATABASE\\99_UNVERIFIED_INBOX\\core_starter_records\\core_starter_records.json",
            "verified_status": null
          }
        ],
        "reference": "U2",
        "value": "AMS1117-3.3"
      }
    ]
  },
  {
    "unmatched_components": [
      {
        "footprint": "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal",
        "reference": "R2",
        "value": "66"
      },
      {
        "footprint": "Diode_THT:D_DO-34_SOD68_P7.62mm_Horizontal",
        "reference": "D1",
        "value": "3.6 Zener"
      },
      {
        "footprint": "Connector_PinSocket_2.54mm:PinSocket_2x05_P2.54mm_Vertical",
        "reference": "J2",
        "value": "Conn_02x05_Odd_Even"
      },
      {
        "footprint": "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal",
        "reference": "R4",
        "value": "470"
      },
      {
        "footprint": "Diode_THT:D_DO-34_SOD68_P7.62mm_Horizontal",
        "reference": "D2",
        "value": "3.6 Zener"
      },
      {
        "footprint": "LED_SMD:LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder",
        "reference": "D4",
        "value": "LED"
      },
      {
        "footprint": "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal",
        "reference": "R3",
        "value": "66"
      },
      {
        "footprint": "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal",
        "reference": "R5",
        "value": "470"
      },
      {
        "footprint": "My footprints:MOLEX_48037-0001",
        "reference": "J1",
        "value": "USB_A"
      },
      {
        "footprint": "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal",
        "reference": "R1",
        "value": "1K5"
      },
      {
        "footprint": "LED_SMD:LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder",
        "reference": "D3",
        "value": "LED"
      }
    ]
  }
]
```

Recommended next steps:
- Create or update component database records for unmatched BOM values before relying on AI part intelligence.

### Connector Orientation Review Needed

Status: `WARN`

Connector-like components require human pinout, mating, orientation, and mechanical review.

```json
[
  {
    "footprint": "Connector_PinSocket_2.54mm:PinSocket_2x05_P2.54mm_Vertical",
    "matched_keywords": [
      "connector",
      "conn"
    ],
    "reference": "J2",
    "value": "Conn_02x05_Odd_Even"
  },
  {
    "footprint": "My footprints:MOLEX_48037-0001",
    "matched_keywords": [
      "connector",
      "conn",
      "usb",
      "molex"
    ],
    "reference": "J1",
    "value": "USB_A"
  }
]
```

Recommended next steps:
- Review every listed connector against exact manufacturer drawing, mating connector, pin 1, and cable exit direction.

### Polarity-Sensitive Parts Review Needed

Status: `WARN`

Polarity-sensitive components require human orientation and assembly review.

```json
[
  {
    "footprint": "Diode_THT:D_DO-34_SOD68_P7.62mm_Horizontal",
    "matched_keywords": [
      "diode",
      "zener"
    ],
    "reference": "D1",
    "value": "3.6 Zener"
  },
  {
    "footprint": "Diode_THT:D_DO-34_SOD68_P7.62mm_Horizontal",
    "matched_keywords": [
      "diode",
      "zener"
    ],
    "reference": "D2",
    "value": "3.6 Zener"
  },
  {
    "footprint": "LED_SMD:LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder",
    "matched_keywords": [
      "led"
    ],
    "reference": "D4",
    "value": "LED"
  },
  {
    "footprint": "LED_SMD:LED_1206_3216Metric_Pad1.42x1.75mm_HandSolder",
    "matched_keywords": [
      "led"
    ],
    "reference": "D3",
    "value": "LED"
  }
]
```

Recommended next steps:
- Review polarity marks, pin 1/cathode/anode/source-drain orientation, and silkscreen for every listed item.

### RF Layout Review Needed

Status: `PASS`

No static keyword review hits found.

### USB/CAN/Automotive Rule Review Needed

Status: `WARN`

USB, CAN, LIN, or automotive-like items require protocol-specific review.

```json
[
  {
    "footprint": "Package_TO_SOT_SMD:SOT-223-3_TabPin2",
    "matched_keywords": [
      "lin"
    ],
    "reference": "U2",
    "value": "AMS1117-3.3"
  },
  {
    "footprint": "My footprints:MOLEX_48037-0001",
    "matched_keywords": [
      "usb"
    ],
    "reference": "J1",
    "value": "USB_A"
  },
  {
    "net_or_text_keyword_hits": [
      "lin",
      "usb"
    ]
  }
]
```

Recommended next steps:
- Apply USB, CAN/LIN, and automotive power/protection rules from the component database before release.

## Recommended Next Steps

- Document unresolved symbol library table URIs; do not patch global tables automatically unless the user requests it.
- Consider project-local library tables for reproducible projects that should not depend silently on global config.
- Resolve unknown 3D model variables before relying on visual/mechanical review.
- Run ERC before trusting power connectivity; static text inspection cannot prove every power pin is driven.
- Review hidden power pins and PWR_FLAG placement manually for regulators, connectors, and MCU power rails.
- Add source links, component database records, or local datasheet references for BOM components before release.
- Create or update component database records for unmatched BOM values before relying on AI part intelligence.
- Review every listed connector against exact manufacturer drawing, mating connector, pin 1, and cable exit direction.
- Review polarity marks, pin 1/cathode/anode/source-drain orientation, and silkscreen for every listed item.
- Apply USB, CAN/LIN, and automotive power/protection rules from the component database before release.
- Do not treat this project as release-ready until FAIL/WARN items are reviewed.
- Do not apply automatic fixes; make changes only after active project approval, backup, and verification plan.

## Safety

- This validation report is read-only.
- No automatic fixes were attempted.
- KiCad ERC/DRC and human review are still required before release.
