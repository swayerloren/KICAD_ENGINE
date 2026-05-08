# BOM Export Validation Rules

Status: `ACTIVE_RULES`

## Hard Rules

- BOM validation is not assembly approval.
- Required columns must match the target house: JLCPCB, PCBWay, or universal internal review.
- Every populated BOM line must have nonblank designators.
- Quantity must match comma-separated designator count unless an LJ-approved exception is documented.
- DNP parts must be explicitly marked or excluded according to the assembly plan.
- Connectors, ICs, polarized capacitors, diodes, LEDs, and high-risk parts require exact manufacturer part numbers before upload approval.
- Universal BOM files are acceptable for internal review only; upload packages must use fab-house-specific BOMs.

## Block Export If

- Required columns are missing.
- Designators are blank.
- Quantities do not match designator count.
- Required part identifiers are generic or unresolved for high-risk parts.
- DNP/substitution policy is ambiguous.

