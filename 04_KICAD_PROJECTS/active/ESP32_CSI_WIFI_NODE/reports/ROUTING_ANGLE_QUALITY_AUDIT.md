# Routing Angle Quality Audit

Date: `2026-05-07`

Project: `ESP32_CSI_WIFI_NODE`

Audited nets:

- `/+5V_IN`
- `/+5V_FUSED`
- `/+5V_PROTECTED`
- `/BUCK_SW`
- `/BUCK_BST`
- `+3V3`

## Method

An automated KiCad-Python audit inspected the Stage 1/2 routed segments and evaluated:

- exact 90-degree bends
- acute bends sharper than 45 degrees
- short zig-zag candidates
- long diagonal shortcuts
- via count

Audit interpretation rules:

- only real degree-2 bend nodes were counted as angle defects
- collinear split points were ignored
- the intentional near-horizontal `+3V3` bottom escape was not treated as a diagonal shortcut

## Result

| Check | Result |
|---|---|
| Exact 90-degree bends | `0` |
| Acute bends `< 45 deg` | `0` |
| Short zig-zag candidates | `0` |
| Long diagonal shortcuts | `0` |
| Stage 1/2 via count | `2` |

## Notes

- The retained via pair is on local `+3V3` only.
- The `+3V3` bottom-layer run is an intentional clean escape chosen to avoid a poor top-side entry into `L1 pad 2`.
- `BUCK_SW` is now a straight compact local path through `U1 -> C6 -> L1`.
- `BUCK_BST` is now a short local 45-plus-horizontal connection with no crossing.

## Conclusion

The Stage 1/2 local routing passes the requested angle-quality standard for this phase:

- no 90-degree corners remain
- no sharper-than-45-degree bends remain
- no crude scripted zig-zag geometry remains
