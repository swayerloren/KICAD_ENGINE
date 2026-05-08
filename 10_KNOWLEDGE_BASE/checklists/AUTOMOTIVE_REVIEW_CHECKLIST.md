# Automotive Review Checklist

Automotive designs need explicit environment assumptions.

## Required Evidence

- Nominal and transient input voltage requirements.
- Reverse-polarity requirement.
- Fuse and protection requirements.
- Connector and harness pinout.
- Temperature range.
- Load dump or surge requirement if applicable.

## Review Steps

- Check input protection chain.
- Check TVS and fuse sizing.
- Check reverse-polarity behavior.
- Check regulator maximum input and thermal risk.
- Check connector retention, keying, and orientation.
- Check CAN/LIN/ignition/wake signal protection.
- Check ground return and chassis strategy.

## Stop Conditions

Stop if the automotive environment is described only as "12 V" without transient, polarity, fuse, and connector assumptions.

