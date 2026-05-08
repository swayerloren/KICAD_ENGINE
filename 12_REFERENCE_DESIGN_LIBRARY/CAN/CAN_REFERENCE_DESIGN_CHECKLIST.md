# CAN Reference Design Checklist

## Source And License

- Vendor/project owner identified.
- License and redistribution status recorded.

## Technical Review

- Classical CAN or CAN FD identified.
- MCU CAN peripheral reviewed.
- Transceiver part and package reviewed.
- VCC/VIO compatibility reviewed.
- Termination policy reviewed.
- CANH/CANL connector pinout reviewed.
- Protection and common-mode choke strategy reviewed.

## Reuse Warnings

- Do not copy termination without bus topology.
- Do not copy transceiver if CAN FD support is required but absent.
- Do not copy connector pinout without harness review.

## Human Review Needed

- Bus topology.
- Connector pinout.
- Termination.
- Protection for exposed or automotive harnesses.

