# Development Board Record Template

Date: 2026-05-02

Status: template for development boards, modules on carrier boards, vendor eval boards, Nucleo boards, Discovery boards, Pico-style boards, and reference board schematics.

## Rules

- A development board record is not a substitute for the component datasheets of parts used on the board.
- Do not copy a dev board circuit into a KiCad project without checking datasheets, errata, and layout guidance for each critical part.
- Record schematic, BOM, layout files, user guides, and source URLs separately.
- Use `Unknown - requires source verification` for unchecked fields.

## Blank Development Board Record

```yaml
record_type: DEV_BOARD
record_id: VENDOR_BOARD
vendor: Unknown - requires source verification
board_name: Unknown - requires source verification
board_revision: Unknown - requires source verification
primary_part_number: Unknown - requires source verification
family: Unknown - requires source verification
document_type: DEV_BOARD_SCHEMATIC
document_title: Unknown - requires source verification
revision: Unknown - requires source verification
document_date: Unknown - requires source verification
source_url: Unknown - requires source verification
source_access_date: Unknown - requires source verification
local_filename: Unknown - requires source verification
local_path: Unknown - requires source verification
copyright_note: Unknown - requires source verification
verification_status: NOT_VERIFIED
related_documents:
  datasheet: Unknown - requires source verification
  user_guide: Unknown - requires source verification
  schematic: Unknown - requires source verification
  bom: Unknown - requires source verification
  layout_files: Unknown - requires source verification
related_kicad_symbol: Unknown - requires source verification
related_kicad_footprint: Unknown - requires source verification
related_kicad_3d_model: Unknown - requires source verification
voltage_range: Unknown - requires source verification
current_limits: Unknown - requires source verification
absolute_maximum_ratings: Unknown - requires source verification
recommended_operating_conditions: Unknown - requires source verification
pin_count: Unknown - requires source verification
package_type: Development board - exact dimensions require source verification
special_layout_rules: Unknown - requires source verification
known_errata: Unknown - requires source verification
lifecycle_status: Unknown - requires source verification
interfaces: []
connectors: []
debug_programming: Unknown - requires source verification
power_sources: []
mechanical_notes: Unknown - requires source verification
open_questions:
  - Verify board revision, schematic revision, BOM, connector pinout, voltage domains, and license before using as a design reference.
review_history: []
```
