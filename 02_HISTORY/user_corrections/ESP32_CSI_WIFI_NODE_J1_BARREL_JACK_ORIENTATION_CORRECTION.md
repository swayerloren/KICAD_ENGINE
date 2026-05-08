# ESP32_CSI_WIFI_NODE J1 Barrel Jack Orientation Correction

Date/time: `2026-05-07T13:49:21-04:00`

Status: `ACTIVE_USER_CORRECTION`

## Correction

LJ corrected the J1 barrel jack orientation interpretation:

- For the CUI/PJ-102AH-style horizontal barrel jack, the 3-pin solder-leg side is the back side.
- The female barrel plug opening is the opposite/front side.
- Prior orientation reports that treated the pad-cluster side as the mouth/front side are superseded for J1.

## Applied In This Session

J1 was changed from `(14.0,93.2)`, rotation `180 deg`, to `(14.0,80.8)`, rotation `0 deg`, so the local `+Y` long-body/female-opening side faces the bottom edge and the pad cluster remains inward/on-board.

## Rule For Future Agents

Do not approve CUI/PJ-102AH-style barrel-jack mouth direction from coordinates alone. Use footprint geometry plus correct physical orientation: 3-pin solder-leg side is back; opposite side is female barrel opening.

