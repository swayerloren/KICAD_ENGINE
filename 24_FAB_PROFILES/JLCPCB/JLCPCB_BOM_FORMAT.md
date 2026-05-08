# JLCPCB BOM Format

Status: `ACTIVE_RULES`

## Required Columns

```csv
Comment,Designator,Footprint,LCSC Part #,Quantity,Manufacturer,Manufacturer Part Number,Notes
```

## Column Meaning

| Column | Requirement | Purpose |
|---|---|---|
| Comment | Required | Value/specification such as `10k 1%` or `100nF 50V` |
| Designator | Required | Comma-separated references such as `R1,R2,R3` |
| Footprint | Required | Package/footprint such as `0603`, `SOT-23`, `LQFP-48` |
| LCSC Part # | Strongly recommended | JLCPCB/LCSC sourcing part number |
| Quantity | Recommended | Quantity per board |
| Manufacturer | Recommended | Manufacturer name |
| Manufacturer Part Number | Recommended | Exact MPN |
| Notes | Optional | DNP, orientation, substitution, special handling |

## Rules

- Do not rely on generic names such as resistor or capacitor.
- Group identical parts on one line when possible.
- Quantity must match designator count.
- Do not distinguish parts by reference designator letter case.

