# Part Record Template

Date: 2026-05-02

Status: `TEMPLATE_WITH_UNVERIFIED_EXAMPLES`

This template defines the minimum datasheet/source record needed before KiCad Engine can make source-backed claims about a part. It is intentionally strict: a source link does not prove pinout, package, footprint, lifecycle, or layout rules until the relevant fields are verified and cited.

## How Agents Should Use This Template

Create a record when a part, module, connector, dev board, errata item, reference manual, package drawing, or application note becomes relevant to a project or component database entry. Fill only what is known from a cited source or user-provided fact. Keep all unknown values explicit and route high-risk gaps to `MISSING_DATASHEETS.md`, the family `NEEDS_RESEARCH.md`, or an issue log.

Do not copy vendor PDF text into public repo records. Summarize in your own words, store source links, and mark redistribution status. If a local PDF exists, record whether it is `LOCAL_PRIVATE_ONLY`, `LINK_ONLY_PUBLIC`, or `REDISTRIBUTION_CONFIRMED`.

## Use

Copy the YAML block for each curated component. Do not treat the examples as verified component data.

Required unknown value:

```text
Unknown - requires source verification
```

## Verification Status Values

| Status | Meaning |
| --- | --- |
| `NOT_VERIFIED` | Placeholder or incomplete record; not usable for design approval. |
| `SOURCE_LINK_ONLY` | Official or public source link exists, but fields have not been extracted and checked. |
| `PARTIALLY_VERIFIED` | Some claims are verified; unresolved fields remain blocked. |
| `VERIFIED_BY_DATASHEET` | The specific field was checked against an authoritative datasheet or package drawing. |
| `VERIFIED_BY_VENDOR_REFERENCE` | The specific field was checked against an official vendor reference design or board schematic. |
| `USER_CONFIRMED` | User accepted a specific claim for a specific project; still record evidence limits. |
| `NEEDS_HUMAN_REVIEW` | AI cannot approve the field without human decision. |

## Fields That Block KiCad Approval

Do not approve a symbol, footprint, schematic block, BOM line, or fab output if any of these remain unknown for a selected exact part:

- `source_url`
- `revision` or source access date
- `pin_count`
- `package_type`
- `related_kicad_symbol`
- `related_kicad_footprint`
- `footprint_verification_notes`
- `absolute_maximum_ratings`
- `recommended_operating_conditions`
- `special_layout_rules` when the part touches power, USB, RF, CAN, clocking, high current, high voltage, or connectors
- `connector_orientation_notes` for connectors and modules

## Blank Part Record

```yaml
record_type: PART
record_id: VENDOR_PART
vendor: Unknown - requires source verification
part_number: Unknown - requires source verification
family: Unknown - requires source verification
package: Unknown - requires source verification
document_type: DATASHEET
document_title: Unknown - requires source verification
revision: Unknown - requires source verification
document_date: Unknown - requires source verification
source_url: Unknown - requires source verification
source_access_date: Unknown - requires source verification
local_filename: Unknown - requires source verification
local_path: Unknown - requires source verification
copyright_note: Unknown - requires source verification
verification_status: NOT_VERIFIED
related_kicad_symbol: Unknown - requires source verification
related_kicad_footprint: Unknown - requires source verification
related_kicad_3d_model: Unknown - requires source verification
symbol_verification_notes: Unknown - requires source verification
footprint_verification_notes: Unknown - requires source verification
voltage_range: Unknown - requires source verification
current_limits: Unknown - requires source verification
absolute_maximum_ratings: Unknown - requires source verification
recommended_operating_conditions: Unknown - requires source verification
pin_count: Unknown - requires source verification
package_type: Unknown - requires source verification
special_layout_rules: Unknown - requires source verification
known_errata: Unknown - requires source verification
lifecycle_status: Unknown - requires source verification
used_in_projects: []
bom_notes: Unknown - requires source verification
connector_orientation_notes: Unknown - requires source verification
power_budget_notes: Unknown - requires source verification
open_questions:
  - Verify authoritative source URL.
  - Verify document revision and date.
  - Verify package and pin count.
  - Verify KiCad symbol, footprint, and 3D model.
  - Verify operating limits, absolute maximum ratings, layout rules, errata, and lifecycle status.
review_history: []
```

## Example Records

These examples are schema examples only. Exact specifications have not been verified from datasheets in this task.

### ESP32-S3-WROOM-1

```yaml
record_type: PART
record_id: ESPRESSIF_ESP32-S3-WROOM-1
vendor: Espressif
part_number: ESP32-S3-WROOM-1
family: ESP32_S3
package: Unknown - requires source verification
document_type: MODULE_DATASHEET
document_title: Unknown - requires source verification
revision: Unknown - requires source verification
document_date: Unknown - requires source verification
source_url: Unknown - requires source verification
source_access_date: Unknown - requires source verification
local_filename: ESPRESSIF_ESP32-S3-WROOM-1_ESP32_S3_PKG_UNKNOWN_MODULE_DATASHEET_REV_UNKNOWN_DATE_UNKNOWN.pdf
local_path: 06_DATASHEETS/01_MICROCONTROLLERS/ESPRESSIF/ESP32_S3
copyright_note: Unknown - requires source verification
verification_status: NOT_VERIFIED
related_kicad_symbol: Unknown - requires source verification
related_kicad_footprint: Unknown - requires source verification
related_kicad_3d_model: Unknown - requires source verification
symbol_verification_notes: Unknown - requires source verification
footprint_verification_notes: Unknown - requires source verification
voltage_range: Unknown - requires source verification
current_limits: Unknown - requires source verification
absolute_maximum_ratings: Unknown - requires source verification
recommended_operating_conditions: Unknown - requires source verification
pin_count: Unknown - requires source verification
package_type: Unknown - requires source verification
special_layout_rules: Unknown - requires source verification
known_errata: Unknown - requires source verification
lifecycle_status: Unknown - requires source verification
used_in_projects: []
bom_notes: Unknown - requires source verification
connector_orientation_notes: Unknown - requires source verification
power_budget_notes: Unknown - requires source verification
open_questions:
  - Verify module pinout, antenna keepout, power requirements, boot strapping, and lifecycle status from the Espressif source document.
review_history: []
```

### ESP32-S3-WROOM-1U

```yaml
record_type: PART
record_id: ESPRESSIF_ESP32-S3-WROOM-1U
vendor: Espressif
part_number: ESP32-S3-WROOM-1U
family: ESP32_S3
package: Unknown - requires source verification
document_type: MODULE_DATASHEET
document_title: Unknown - requires source verification
revision: Unknown - requires source verification
document_date: Unknown - requires source verification
source_url: Unknown - requires source verification
source_access_date: Unknown - requires source verification
local_filename: ESPRESSIF_ESP32-S3-WROOM-1U_ESP32_S3_PKG_UNKNOWN_MODULE_DATASHEET_REV_UNKNOWN_DATE_UNKNOWN.pdf
local_path: 06_DATASHEETS/01_MICROCONTROLLERS/ESPRESSIF/ESP32_S3
copyright_note: Unknown - requires source verification
verification_status: NOT_VERIFIED
related_kicad_symbol: Unknown - requires source verification
related_kicad_footprint: Unknown - requires source verification
related_kicad_3d_model: Unknown - requires source verification
symbol_verification_notes: Unknown - requires source verification
footprint_verification_notes: Unknown - requires source verification
voltage_range: Unknown - requires source verification
current_limits: Unknown - requires source verification
absolute_maximum_ratings: Unknown - requires source verification
recommended_operating_conditions: Unknown - requires source verification
pin_count: Unknown - requires source verification
package_type: Unknown - requires source verification
special_layout_rules: Unknown - requires source verification
known_errata: Unknown - requires source verification
lifecycle_status: Unknown - requires source verification
used_in_projects: []
bom_notes: Unknown - requires source verification
connector_orientation_notes: Unknown - requires source verification
power_budget_notes: Unknown - requires source verification
open_questions:
  - Verify external antenna connector requirements, module pinout, antenna/RF layout rules, and lifecycle status from the Espressif source document.
review_history: []
```

### STM32F103C8T6

```yaml
record_type: PART
record_id: STMICRO_STM32F103C8T6
vendor: STMicroelectronics
part_number: STM32F103C8T6
family: STM32F1
package: Unknown - requires source verification
document_type: DATASHEET
document_title: Unknown - requires source verification
revision: Unknown - requires source verification
document_date: Unknown - requires source verification
source_url: Unknown - requires source verification
source_access_date: Unknown - requires source verification
local_filename: STMICRO_STM32F103C8T6_STM32F1_PKG_UNKNOWN_DATASHEET_REV_UNKNOWN_DATE_UNKNOWN.pdf
local_path: 06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32F1
copyright_note: Unknown - requires source verification
verification_status: NOT_VERIFIED
related_kicad_symbol: Unknown - requires source verification
related_kicad_footprint: Unknown - requires source verification
related_kicad_3d_model: Unknown - requires source verification
symbol_verification_notes: Unknown - requires source verification
footprint_verification_notes: Unknown - requires source verification
voltage_range: Unknown - requires source verification
current_limits: Unknown - requires source verification
absolute_maximum_ratings: Unknown - requires source verification
recommended_operating_conditions: Unknown - requires source verification
pin_count: Unknown - requires source verification
package_type: Unknown - requires source verification
special_layout_rules: Unknown - requires source verification
known_errata: Unknown - requires source verification
lifecycle_status: Unknown - requires source verification
used_in_projects: []
bom_notes: Unknown - requires source verification
connector_orientation_notes: Unknown - requires source verification
power_budget_notes: Unknown - requires source verification
open_questions:
  - Verify exact package, reference manual, errata, boot/debug pins, oscillator rules, and decoupling rules.
review_history: []
```

### STM32F411CEU6

```yaml
record_type: PART
record_id: STMICRO_STM32F411CEU6
vendor: STMicroelectronics
part_number: STM32F411CEU6
family: STM32F4
package: Unknown - requires source verification
document_type: DATASHEET
document_title: Unknown - requires source verification
revision: Unknown - requires source verification
document_date: Unknown - requires source verification
source_url: Unknown - requires source verification
source_access_date: Unknown - requires source verification
local_filename: STMICRO_STM32F411CEU6_STM32F4_PKG_UNKNOWN_DATASHEET_REV_UNKNOWN_DATE_UNKNOWN.pdf
local_path: 06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32F4
copyright_note: Unknown - requires source verification
verification_status: NOT_VERIFIED
related_kicad_symbol: Unknown - requires source verification
related_kicad_footprint: Unknown - requires source verification
related_kicad_3d_model: Unknown - requires source verification
symbol_verification_notes: Unknown - requires source verification
footprint_verification_notes: Unknown - requires source verification
voltage_range: Unknown - requires source verification
current_limits: Unknown - requires source verification
absolute_maximum_ratings: Unknown - requires source verification
recommended_operating_conditions: Unknown - requires source verification
pin_count: Unknown - requires source verification
package_type: Unknown - requires source verification
special_layout_rules: Unknown - requires source verification
known_errata: Unknown - requires source verification
lifecycle_status: Unknown - requires source verification
used_in_projects: []
bom_notes: Unknown - requires source verification
connector_orientation_notes: Unknown - requires source verification
power_budget_notes: Unknown - requires source verification
open_questions:
  - Verify package, USB requirements if used, oscillator rules, ST-LINK/debug interface, reference manual, and errata.
review_history: []
```

### PIC16F877A

```yaml
record_type: PART
record_id: MICROCHIP_PIC16F877A
vendor: Microchip
part_number: PIC16F877A
family: PIC16
package: Unknown - requires source verification
document_type: DATASHEET
document_title: Unknown - requires source verification
revision: Unknown - requires source verification
document_date: Unknown - requires source verification
source_url: Unknown - requires source verification
source_access_date: Unknown - requires source verification
local_filename: MICROCHIP_PIC16F877A_PIC16_PKG_UNKNOWN_DATASHEET_REV_UNKNOWN_DATE_UNKNOWN.pdf
local_path: 06_DATASHEETS/01_MICROCONTROLLERS/MICROCHIP_PIC/PIC16
copyright_note: Unknown - requires source verification
verification_status: NOT_VERIFIED
related_kicad_symbol: Unknown - requires source verification
related_kicad_footprint: Unknown - requires source verification
related_kicad_3d_model: Unknown - requires source verification
symbol_verification_notes: Unknown - requires source verification
footprint_verification_notes: Unknown - requires source verification
voltage_range: Unknown - requires source verification
current_limits: Unknown - requires source verification
absolute_maximum_ratings: Unknown - requires source verification
recommended_operating_conditions: Unknown - requires source verification
pin_count: Unknown - requires source verification
package_type: Unknown - requires source verification
special_layout_rules: Unknown - requires source verification
known_errata: Unknown - requires source verification
lifecycle_status: Unknown - requires source verification
used_in_projects: []
bom_notes: Unknown - requires source verification
connector_orientation_notes: Unknown - requires source verification
power_budget_notes: Unknown - requires source verification
open_questions:
  - Verify exact package option, programming/debug requirements, oscillator/reset rules, and errata.
review_history: []
```

### PIC18F4550

```yaml
record_type: PART
record_id: MICROCHIP_PIC18F4550
vendor: Microchip
part_number: PIC18F4550
family: PIC18
package: Unknown - requires source verification
document_type: DATASHEET
document_title: Unknown - requires source verification
revision: Unknown - requires source verification
document_date: Unknown - requires source verification
source_url: Unknown - requires source verification
source_access_date: Unknown - requires source verification
local_filename: MICROCHIP_PIC18F4550_PIC18_PKG_UNKNOWN_DATASHEET_REV_UNKNOWN_DATE_UNKNOWN.pdf
local_path: 06_DATASHEETS/01_MICROCONTROLLERS/MICROCHIP_PIC/PIC18
copyright_note: Unknown - requires source verification
verification_status: NOT_VERIFIED
related_kicad_symbol: Unknown - requires source verification
related_kicad_footprint: Unknown - requires source verification
related_kicad_3d_model: Unknown - requires source verification
symbol_verification_notes: Unknown - requires source verification
footprint_verification_notes: Unknown - requires source verification
voltage_range: Unknown - requires source verification
current_limits: Unknown - requires source verification
absolute_maximum_ratings: Unknown - requires source verification
recommended_operating_conditions: Unknown - requires source verification
pin_count: Unknown - requires source verification
package_type: Unknown - requires source verification
special_layout_rules: Unknown - requires source verification
known_errata: Unknown - requires source verification
lifecycle_status: Unknown - requires source verification
used_in_projects: []
bom_notes: Unknown - requires source verification
connector_orientation_notes: Unknown - requires source verification
power_budget_notes: Unknown - requires source verification
open_questions:
  - Verify USB electrical requirements, oscillator requirements, programming/debug requirements, package, and errata.
review_history: []
```

### RP2040

```yaml
record_type: PART
record_id: RASPBERRY_PI_RP2040
vendor: Raspberry Pi
part_number: RP2040
family: RP2040
package: Unknown - requires source verification
document_type: DATASHEET
document_title: Unknown - requires source verification
revision: Unknown - requires source verification
document_date: Unknown - requires source verification
source_url: Unknown - requires source verification
source_access_date: Unknown - requires source verification
local_filename: RASPBERRY_PI_RP2040_RP2040_PKG_UNKNOWN_DATASHEET_REV_UNKNOWN_DATE_UNKNOWN.pdf
local_path: 06_DATASHEETS/01_MICROCONTROLLERS/RASPBERRY_PI_RP2040_RP2350
copyright_note: Unknown - requires source verification
verification_status: NOT_VERIFIED
related_kicad_symbol: Unknown - requires source verification
related_kicad_footprint: Unknown - requires source verification
related_kicad_3d_model: Unknown - requires source verification
symbol_verification_notes: Unknown - requires source verification
footprint_verification_notes: Unknown - requires source verification
voltage_range: Unknown - requires source verification
current_limits: Unknown - requires source verification
absolute_maximum_ratings: Unknown - requires source verification
recommended_operating_conditions: Unknown - requires source verification
pin_count: Unknown - requires source verification
package_type: Unknown - requires source verification
special_layout_rules: Unknown - requires source verification
known_errata: Unknown - requires source verification
lifecycle_status: Unknown - requires source verification
used_in_projects: []
bom_notes: Unknown - requires source verification
connector_orientation_notes: Unknown - requires source verification
power_budget_notes: Unknown - requires source verification
open_questions:
  - Verify package, boot flash requirements, USB requirements, power sequencing, oscillator rules, and reference design guidance.
review_history: []
```

### MCP2562FD

```yaml
record_type: PART
record_id: MICROCHIP_MCP2562FD
vendor: Microchip
part_number: MCP2562FD
family: CAN
package: Unknown - requires source verification
document_type: DATASHEET
document_title: Unknown - requires source verification
revision: Unknown - requires source verification
document_date: Unknown - requires source verification
source_url: Unknown - requires source verification
source_access_date: Unknown - requires source verification
local_filename: MICROCHIP_MCP2562FD_CAN_PKG_UNKNOWN_DATASHEET_REV_UNKNOWN_DATE_UNKNOWN.pdf
local_path: 06_DATASHEETS/04_COMMUNICATION
copyright_note: Unknown - requires source verification
verification_status: NOT_VERIFIED
related_kicad_symbol: Unknown - requires source verification
related_kicad_footprint: Unknown - requires source verification
related_kicad_3d_model: Unknown - requires source verification
symbol_verification_notes: Unknown - requires source verification
footprint_verification_notes: Unknown - requires source verification
voltage_range: Unknown - requires source verification
current_limits: Unknown - requires source verification
absolute_maximum_ratings: Unknown - requires source verification
recommended_operating_conditions: Unknown - requires source verification
pin_count: Unknown - requires source verification
package_type: Unknown - requires source verification
special_layout_rules: Unknown - requires source verification
known_errata: Unknown - requires source verification
lifecycle_status: Unknown - requires source verification
used_in_projects: []
bom_notes: Unknown - requires source verification
connector_orientation_notes: Unknown - requires source verification
power_budget_notes: Unknown - requires source verification
open_questions:
  - Verify CAN FD transceiver pinout, VIO/VDD behavior, termination/protection guidance, package, and errata.
review_history: []
```

### LM2596

```yaml
record_type: PART
record_id: TI_LM2596
vendor: Texas Instruments / exact manufacturer requires verification
part_number: LM2596
family: POWER_REGULATOR
package: Unknown - requires source verification
document_type: DATASHEET
document_title: Unknown - requires source verification
revision: Unknown - requires source verification
document_date: Unknown - requires source verification
source_url: Unknown - requires source verification
source_access_date: Unknown - requires source verification
local_filename: TI_LM2596_POWER_REGULATOR_PKG_UNKNOWN_DATASHEET_REV_UNKNOWN_DATE_UNKNOWN.pdf
local_path: 06_DATASHEETS/03_POWER
copyright_note: Unknown - requires source verification
verification_status: NOT_VERIFIED
related_kicad_symbol: Unknown - requires source verification
related_kicad_footprint: Unknown - requires source verification
related_kicad_3d_model: Unknown - requires source verification
symbol_verification_notes: Unknown - requires source verification
footprint_verification_notes: Unknown - requires source verification
voltage_range: Unknown - requires source verification
current_limits: Unknown - requires source verification
absolute_maximum_ratings: Unknown - requires source verification
recommended_operating_conditions: Unknown - requires source verification
pin_count: Unknown - requires source verification
package_type: Unknown - requires source verification
special_layout_rules: Unknown - requires source verification
known_errata: Unknown - requires source verification
lifecycle_status: Unknown - requires source verification
used_in_projects: []
bom_notes: Unknown - requires source verification
connector_orientation_notes: Unknown - requires source verification
power_budget_notes: Unknown - requires source verification
open_questions:
  - Verify exact manufacturer, adjustable/fixed variant, package, inductor/diode/capacitor requirements, thermal limits, and layout guidance.
review_history: []
```

### USB-C Receptacle Generic

```yaml
record_type: PART
record_id: GENERIC_USB-C-RECEPTACLE
vendor: Generic - exact manufacturer required
part_number: USB-C receptacle generic
family: CONNECTOR_USB-C
package: Unknown - requires source verification
document_type: DATASHEET
document_title: Unknown - requires source verification
revision: Unknown - requires source verification
document_date: Unknown - requires source verification
source_url: Unknown - requires source verification
source_access_date: Unknown - requires source verification
local_filename: GENERIC_USB-C-RECEPTACLE_CONNECTOR_USB-C_PKG_UNKNOWN_DATASHEET_REV_UNKNOWN_DATE_UNKNOWN.pdf
local_path: 06_DATASHEETS/05_CONNECTORS
copyright_note: Unknown - requires source verification
verification_status: NOT_VERIFIED
related_kicad_symbol: Unknown - requires source verification
related_kicad_footprint: Unknown - requires source verification
related_kicad_3d_model: Unknown - requires source verification
symbol_verification_notes: Unknown - requires source verification
footprint_verification_notes: Unknown - requires source verification
voltage_range: Unknown - requires source verification
current_limits: Unknown - requires source verification
absolute_maximum_ratings: Unknown - requires source verification
recommended_operating_conditions: Unknown - requires source verification
pin_count: Unknown - requires source verification
package_type: Unknown - requires source verification
special_layout_rules: Unknown - requires source verification
known_errata: Unknown - requires source verification
lifecycle_status: Generic placeholder - exact part required before design use
used_in_projects: []
bom_notes: Unknown - requires source verification
connector_orientation_notes: Unknown - requires source verification
power_budget_notes: Unknown - requires source verification
open_questions:
  - Replace generic record with exact manufacturer part before PCB layout; verify pad map, shell pads, mating orientation, board edge, CC role, current rating, and 3D model.
review_history: []
```

### U.FL Connector Generic

```yaml
record_type: PART
record_id: GENERIC_U.FL-CONNECTOR
vendor: Generic / U.FL-compatible - exact manufacturer required
part_number: U.FL connector generic
family: CONNECTOR_RF
package: Unknown - requires source verification
document_type: DATASHEET
document_title: Unknown - requires source verification
revision: Unknown - requires source verification
document_date: Unknown - requires source verification
source_url: Unknown - requires source verification
source_access_date: Unknown - requires source verification
local_filename: GENERIC_U.FL-CONNECTOR_CONNECTOR_RF_PKG_UNKNOWN_DATASHEET_REV_UNKNOWN_DATE_UNKNOWN.pdf
local_path: 06_DATASHEETS/05_CONNECTORS
copyright_note: Unknown - requires source verification
verification_status: NOT_VERIFIED
related_kicad_symbol: Unknown - requires source verification
related_kicad_footprint: Unknown - requires source verification
related_kicad_3d_model: Unknown - requires source verification
symbol_verification_notes: Unknown - requires source verification
footprint_verification_notes: Unknown - requires source verification
voltage_range: Unknown - requires source verification
current_limits: Unknown - requires source verification
absolute_maximum_ratings: Unknown - requires source verification
recommended_operating_conditions: Unknown - requires source verification
pin_count: Unknown - requires source verification
package_type: Unknown - requires source verification
special_layout_rules: Unknown - requires source verification
known_errata: Unknown - requires source verification
lifecycle_status: Generic placeholder - exact part required before design use
used_in_projects: []
bom_notes: Unknown - requires source verification
connector_orientation_notes: Unknown - requires source verification
power_budget_notes: Unknown - requires source verification
open_questions:
  - Replace generic record with exact manufacturer part before PCB layout; verify footprint, pad orientation, RF feed geometry, keepout, height, mating connector, and 3D model.
review_history: []
```
