# Inventory Price Schema

## Purpose

Define time-sensitive stock and price metadata without treating it as permanent design truth.

## Fields

- `supplier`
- `supplier_sku`
- `manufacturer_part_number`
- `currency`
- `stock_quantity`
- `factory_stock_quantity`
- `minimum_order_quantity`
- `order_multiple`
- `lead_time`
- `price_breaks`
- `retrieved_at`
- `source_url`
- `source_file`
- `verification_status`

## Price Break Format

```json
{
  "quantity": 1,
  "unit_price": null,
  "currency": "USD",
  "status": "UNVERIFIED"
}
```

## Rules

- Price and stock are snapshots, not durable facts.
- Do not publish private quotes unless permission is clear.
- Do not use stale availability data for final BOM decisions.
