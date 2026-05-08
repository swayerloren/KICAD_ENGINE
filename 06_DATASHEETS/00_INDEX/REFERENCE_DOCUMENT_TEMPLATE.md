# Reference Document Template

Date: 2026-05-02

Status: template for application notes, errata, reference manuals, layout guides, package drawings, design guides, vendor portal notes, and fabrication/assembly references.

## Rules

- Reference documents must be linked to a part, family, package, process, or board-house workflow.
- Do not treat an app note as a replacement for the datasheet unless the vendor explicitly says so.
- Errata must be checked before design release for MCUs, radios, regulators, PHYs, and high-risk ICs.
- Board-house pages can change; record access dates.

## Blank Reference Document Record

```yaml
record_type: REFERENCE_DOCUMENT
record_id: VENDOR_TOPIC_DOCUMENTTYPE
vendor: Unknown - requires source verification
publisher: Unknown - requires source verification
topic: Unknown - requires source verification
related_part_numbers: []
family: Unknown - requires source verification
package: Unknown - requires source verification
document_type: REFERENCE_DOCUMENT
document_title: Unknown - requires source verification
document_number: Unknown - requires source verification
revision: Unknown - requires source verification
document_date: Unknown - requires source verification
source_url: Unknown - requires source verification
source_access_date: Unknown - requires source verification
local_filename: Unknown - requires source verification
local_path: Unknown - requires source verification
copyright_note: Unknown - requires source verification
verification_status: NOT_VERIFIED
related_kicad_symbol: Not applicable unless document is tied to a part
related_kicad_footprint: Not applicable unless document is tied to a package or connector
related_kicad_3d_model: Not applicable unless document is tied to a package or connector
voltage_range: Unknown - requires source verification
current_limits: Unknown - requires source verification
absolute_maximum_ratings: Unknown - requires source verification
recommended_operating_conditions: Unknown - requires source verification
pin_count: Unknown - requires source verification
package_type: Unknown - requires source verification
special_layout_rules: Unknown - requires source verification
known_errata: Unknown - requires source verification
lifecycle_status: Unknown - requires source verification
summary: Unknown - requires source verification
design_impact: Unknown - requires source verification
open_questions:
  - Verify source URL, revision, date, applicability, and design impact before using this document as evidence.
review_history: []
```
