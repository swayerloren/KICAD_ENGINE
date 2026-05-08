# Universal BOM Format

Status: `ACTIVE_RULES`

Use the universal BOM for internal review and conversion into fab-house-specific BOMs.

## Columns

```csv
Line #,Comment,Quantity,Designator,Footprint,Package,Type,LCSC Part #,Manufacturer,Manufacturer Part Number,Distributor,Distributor Part Number,Part Description,Notes,DNP
```

## Rules

- `Line #`, `Comment`, `Quantity`, `Designator`, `Footprint`, and `Package` must be present.
- `Quantity` must match the comma-separated designator count unless a documented exception exists.
- DNP parts must be clearly marked in `DNP` and/or `Notes`.
- Exact manufacturer part numbers are required before upload approval for ICs, connectors, and polarized/high-risk parts.
- Capacitor voltage rating and resistor power rating must be included when relevant.
- Universal BOM files are not direct upload approval for JLCPCB or PCBWay.

