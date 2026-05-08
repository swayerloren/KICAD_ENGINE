# Supplier Part Schema

## Required Fields

- `supplier`
- `source_type`
- `manufacturer_name`
- `manufacturer_part_number`
- `supplier_sku`
- `supplier_part_url`
- `description`
- `category`
- `verification_status`
- `retrieved_at`

## Optional Fields

- `lifecycle_status`
- `rohs_status`
- `reach_status`
- `country_of_origin`
- `eccn`
- `hts_code`
- `packaging`
- `minimum_order_quantity`
- `order_multiple`

## Verification Rules

- MPN and supplier SKU must not be merged unless both are present and source-backed.
- Supplier description is not a substitute for datasheet verification.
- Lifecycle status must include source date.
- Compliance fields must remain `UNVERIFIED` unless source-backed.
