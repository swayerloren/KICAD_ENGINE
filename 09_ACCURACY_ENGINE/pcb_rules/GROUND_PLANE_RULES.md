# Ground Plane Rules

## Purpose

Keep return paths and copper zones intentional.

## Rules

- Do not split ground without source-backed intent.
- Review return paths for high-speed, switching, analog, RF, and external-cable currents.
- Stitch grounds where required by layout guidance.
- Keep crystal, RF, USB, CAN, and regulator return loops short and sensible.
- Refill zones before DRC.
- Review thermals for high-current and thermal-pad connections.

## Required Flags

- `GROUND_RETURN_PATH_REVIEW_REQUIRED`
- `ZONE_REFILL_REQUIRED`
- `THERMAL_CONNECTION_REVIEW_REQUIRED`
- `ANALOG_DIGITAL_GROUND_REVIEW_REQUIRED`
