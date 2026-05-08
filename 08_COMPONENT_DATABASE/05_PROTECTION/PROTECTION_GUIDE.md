# Protection Guide

Date: 2026-05-02

Status: AI-readable starter guide. Use this to steer review and part selection, not as final design authority.

## Scope

This guide covers ESD arrays, TVS diodes, surge protection, data-line protection, and bus protection used near connectors and board boundaries.

## What Agents Should Verify

| Item | Why It Matters |
| --- | --- |
| Working standoff voltage | Protection must not conduct during normal operation. |
| Clamping behavior | Protected IC pins must stay within survivable limits during transients. |
| Capacitance | High-speed interfaces can fail if ESD capacitance is too high. |
| Surge or ESD rating | IEC and automotive requirements vary by product class. |
| Directionality | Unidirectional and bidirectional parts behave differently on data and power lines. |
| Package and pinout | ESD arrays often have similar names but incompatible footprints. |
| Ground return path | A long or narrow ground path can make protection ineffective. |

## KiCad Workflow

1. Identify every external connector and board-edge interface.
2. For each signal, determine voltage domain, speed, bus topology, and exposure level.
3. Select candidate protection symbols only after the target part family is known.
4. Match the footprint to the exact package drawing, not only to pin count.
5. Place protection near the connector and route the transient path to chassis or board ground deliberately.
6. Run ERC/DRC and visually inspect pin numbering, polarity, and routing.

## Common Mistakes

- Using a high-capacitance TVS on USB data or RF paths.
- Using a power TVS package for a data-line ESD array.
- Placing ESD protection far from the connector.
- Routing the protected trace through long stubs before reaching the clamp.
- Omitting the ground via strategy near the protection component.
- Treating a generic diode symbol as proof that the footprint is correct.

## Placeholder Policy

All generic records in this folder stay `UNVERIFIED_PLACEHOLDER` until the exact source document and footprint evidence are recorded.
