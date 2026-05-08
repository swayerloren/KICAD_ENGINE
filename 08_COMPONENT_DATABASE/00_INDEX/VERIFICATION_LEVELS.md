# Verification Levels

Date: 2026-05-02

Status: allowed verification flags for component database records.

## Flags

| Flag | Meaning | What It Does Not Mean |
| --- | --- | --- |
| `UNVERIFIED_PLACEHOLDER` | Record exists only as a placeholder or planning stub. | It is not approved for design decisions. |
| `VERIFIED_FROM_DATASHEET` | The field or record was checked against an authoritative datasheet or package drawing. | It does not prove KiCad symbol or footprint correctness unless those were checked too. |
| `VERIFIED_FROM_VENDOR_REFERENCE_DESIGN` | The field was checked against a vendor reference design, app note, eval board, or design guide. | It does not automatically apply to every use case or board stackup. |
| `VERIFIED_FROM_KICAD_LIBRARY` | A KiCad symbol, footprint, or 3D model candidate was inspected in the local KiCad library or project library. | It does not prove it matches the datasheet. |
| `USER_CONFIRMED` | The user explicitly confirmed the field, part, or design choice. | It should still be recorded with scope and date. |

## Promotion Rules

- Promote individual fields, not whole records, when possible.
- A record can have mixed verification state.
- A clean ERC/DRC result does not promote component data.
- A symbol name match does not promote footprint status.
- A footprint name match does not promote land pattern status.
- A vendor reference circuit does not remove the need for datasheet review.

## Required Status Language

Use direct status values:

- `UNVERIFIED_PLACEHOLDER`
- `PINOUT_UNVERIFIED`
- `FOOTPRINT_UNVERIFIED`
- `SYMBOL_CANDIDATE_ONLY`
- `FOOTPRINT_CANDIDATE_ONLY`
- `DATASHEET_PATH_PENDING`
- `SOURCE_URL_PENDING`
- `USER_CONFIRMED`

Avoid vague status words such as `good`, `fine`, `ok`, `probably`, or `standard`.

## Promotion Gate

A record must stay `UNVERIFIED_PLACEHOLDER` until at least one specific field has evidence. Promotion is field-level:

- Datasheet source can be verified while footprint remains unverified.
- KiCad symbol candidate can be verified as present while pinout remains unverified.
- Footprint candidate can be verified as present while package match remains unverified.
- Package drawing can be verified while 3D model remains unverified.

Use `16_VERIFICATION_RECORDS/` for the evidence that justifies any promotion.
