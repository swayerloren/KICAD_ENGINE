# Datasheet Summary Template

Date: 2026-05-02

Status: template for human- and AI-readable extracted datasheet summaries.

## Rules

- A summary is evidence extracted from a source document, not a replacement for the source.
- Every value must cite a page, section, table, or figure when the datasheet is actually reviewed.
- If a value has not been checked, use `Unknown - requires source verification`.
- Do not summarize copyrighted documents by copying long passages. Paraphrase and cite document location.

## Blank Datasheet Summary

```yaml
record_type: DATASHEET_SUMMARY
record_id: VENDOR_PART_DATASHEET_SUMMARY
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
verification_status: NOT_VERIFIED
summary_author: Unknown - requires source verification
summary_date: Unknown - requires source verification

identification:
  exact_part_number: Unknown - requires source verification
  variants_covered: Unknown - requires source verification
  lifecycle_status: Unknown - requires source verification

electrical:
  voltage_range: Unknown - requires source verification
  current_limits: Unknown - requires source verification
  absolute_maximum_ratings: Unknown - requires source verification
  recommended_operating_conditions: Unknown - requires source verification
  power_budget_notes: Unknown - requires source verification

pinout_and_package:
  pin_count: Unknown - requires source verification
  package_type: Unknown - requires source verification
  pinout_notes: Unknown - requires source verification
  orientation_notes: Unknown - requires source verification
  package_drawing_reference: Unknown - requires source verification

kicad_links:
  related_kicad_symbol: Unknown - requires source verification
  related_kicad_footprint: Unknown - requires source verification
  related_kicad_3d_model: Unknown - requires source verification
  symbol_verification_notes: Unknown - requires source verification
  footprint_verification_notes: Unknown - requires source verification

layout_and_design:
  special_layout_rules: Unknown - requires source verification
  decoupling_notes: Unknown - requires source verification
  thermal_notes: Unknown - requires source verification
  rf_or_high_speed_notes: Unknown - requires source verification
  connector_orientation_notes: Unknown - requires source verification

errata_and_risk:
  known_errata: Unknown - requires source verification
  design_risks: Unknown - requires source verification
  open_questions:
    - Verify all fields against the source datasheet before design use.

citations:
  - field: Unknown - requires source verification
    source_location: Unknown - requires source verification
    note: Unknown - requires source verification

review_history: []
```
