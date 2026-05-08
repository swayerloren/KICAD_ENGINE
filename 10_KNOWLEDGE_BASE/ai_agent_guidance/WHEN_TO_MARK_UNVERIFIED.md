# When To Mark Unverified

Mark data as unverified when:

- It came from memory.
- It came from a generic example.
- It came from a placeholder component record.
- It has no source link.
- The source is not the exact part, package, or connector.
- The KiCad footprint only matches by name.
- The 3D model looks right but the land pattern was not checked.
- The value depends on board stackup, current, temperature, or manufacturing process.

## Required Labels

Use clear labels:

- `UNVERIFIED_PLACEHOLDER`
- `UNVERIFIED_FOOTPRINT`
- `Unknown - requires source verification`
- `Human review required`
- `Candidate only`

## Rule

Unverified does not mean unusable. It means the design cannot be approved until the evidence is found.

