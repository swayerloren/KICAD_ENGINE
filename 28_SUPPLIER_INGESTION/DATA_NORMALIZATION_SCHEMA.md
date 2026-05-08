# Data Normalization Schema

Status: `SCHEMA_DRAFT`

## Canonical Record

```json
{
  "schema_version": "supplier_part_normalized_v0.1",
  "verification_status": "UNVERIFIED",
  "source": {
    "supplier": "Unknown",
    "source_type": "official_api | user_csv | manual_source_link",
    "source_url": "",
    "source_file": "",
    "retrieved_at": "",
    "terms_review_status": "UNVERIFIED"
  },
  "manufacturer": {
    "name": "",
    "manufacturer_part_number": "",
    "lifecycle_status": "UNKNOWN"
  },
  "supplier_part": {
    "supplier_sku": "",
    "supplier_part_url": "",
    "description": "",
    "category": ""
  },
  "package": {
    "supplier_package": "",
    "manufacturer_package": "",
    "pin_count": "",
    "package_confidence": "UNVERIFIED"
  },
  "inventory_price": {
    "currency": "",
    "stock_quantity": null,
    "minimum_order_quantity": null,
    "price_breaks": []
  },
  "datasheets": [],
  "footprint_risk": {
    "kicad_symbol_candidates": [],
    "kicad_footprint_candidates": [],
    "footprint_status": "UNVERIFIED",
    "risk_notes": []
  },
  "notes": []
}
```

## Rules

- Preserve raw source identifiers in normalized fields.
- Do not coerce uncertain fields into exact values.
- Use `UNVERIFIED` when field mapping is incomplete.
- Use `retrieved_at` or import date for time-sensitive fields.
