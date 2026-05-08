# Match Schema

Status: required schema for supplier-to-KiCad footprint match records.

## Required Fields

| Field | Required | Notes |
| --- | --- | --- |
| `record_id` | Yes | Stable uppercase identifier. |
| `record_type` | Yes | Use `SUPPLIER_FOOTPRINT_MATCH` or `EXAMPLE_ONLY_SUPPLIER_FOOTPRINT_MATCH`. |
| `manufacturer` | Yes | Manufacturer name from supplier, datasheet, or user input. |
| `mpn` | Yes | Manufacturer part number. |
| `supplier` | Yes | `digikey`, `mouser`, `jlcpcb`, `lcsc`, or `manual_verified`. |
| `supplier_sku` | Yes | Supplier SKU or `UNKNOWN`. |
| `jlc_lcsc_part_number` | Yes | JLCPCB/LCSC part number if applicable, otherwise `UNKNOWN`. |
| `datasheet_url` | Yes | Official or supplier datasheet URL if known. |
| `package_name_from_supplier` | Yes | Supplier package text. Not verification proof. |
| `package_drawing_source` | Yes | Exact drawing source URL/path or `UNKNOWN`. |
| `kicad_symbol_candidate` | Yes | KiCad symbol candidate or `UNKNOWN`. |
| `kicad_footprint_candidate` | Yes | KiCad footprint candidate or `UNKNOWN`. |
| `kicad_3d_model_candidate` | Yes | KiCad 3D model candidate or `UNKNOWN`. |
| `footprint_status` | Yes | `VERIFIED`, `CANDIDATE`, `UNVERIFIED`, or `REJECTED`. |
| `pinout_status` | Yes | `VERIFIED`, `CANDIDATE`, `UNVERIFIED`, or `REJECTED`. |
| `connector_orientation_status` | Yes | `VERIFIED`, `NOT_APPLICABLE`, `UNVERIFIED`, or `REJECTED`. |
| `human_review_required` | Yes | Boolean. Keep true for high-risk categories until reviewed. |
| `confidence_level` | Yes | One of the allowed confidence levels. |
| `high_risk_categories` | Yes | Array of risk labels. |
| `evidence` | Yes | Array of evidence objects. |
| `notes` | Yes | Array of review notes. |
| `created_at` | Yes | ISO-like date or timestamp. |
| `updated_at` | Yes | ISO-like date or timestamp. |

## Allowed Confidence Levels

- `VERIFIED_EXACT_PACKAGE_DRAWING`
- `VERIFIED_VENDOR_FOOTPRINT`
- `MATCHED_BY_PACKAGE_NAME_ONLY`
- `MATCHED_BY_GENERIC_FOOTPRINT`
- `UNVERIFIED`
- `REJECTED`

## Evidence Object

```json
{
  "type": "DATASHEET_URL | PACKAGE_DRAWING | SUPPLIER_PAGE | KICAD_LIBRARY_FILE | HUMAN_REVIEW | OTHER",
  "source": "URL or local path",
  "status": "VERIFIED | PARTIAL | UNVERIFIED | REJECTED",
  "notes": "Short evidence note"
}
```

## Minimal JSON Skeleton

```json
{
  "record_id": "SUPPLIER_VENDOR_MPN",
  "record_type": "SUPPLIER_FOOTPRINT_MATCH",
  "manufacturer": "UNKNOWN",
  "mpn": "UNKNOWN",
  "supplier": "manual_verified",
  "supplier_sku": "UNKNOWN",
  "jlc_lcsc_part_number": "UNKNOWN",
  "datasheet_url": "UNKNOWN",
  "package_name_from_supplier": "UNKNOWN",
  "package_drawing_source": "UNKNOWN",
  "kicad_symbol_candidate": "UNKNOWN",
  "kicad_footprint_candidate": "UNKNOWN",
  "kicad_3d_model_candidate": "UNKNOWN",
  "footprint_status": "UNVERIFIED",
  "pinout_status": "UNVERIFIED",
  "connector_orientation_status": "UNVERIFIED",
  "human_review_required": true,
  "confidence_level": "UNVERIFIED",
  "high_risk_categories": [],
  "evidence": [],
  "notes": ["Placeholder only."],
  "created_at": "2026-05-03",
  "updated_at": "2026-05-03"
}
```

