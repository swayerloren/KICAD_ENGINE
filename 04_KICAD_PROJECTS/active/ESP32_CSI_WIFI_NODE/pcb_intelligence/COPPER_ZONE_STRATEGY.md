# Copper Zone Strategy

No zones should be created until placement is repaired and approved.

## Planned Strategy

- `B.Cu`: solid `GND` plane after placement approval.
- `F.Cu`: local `GND` pours where helpful after critical placement and routing decisions.
- No copper in ESP32 antenna/U.FL/RF keepout.
- Prioritize low-impedance return near USB ESD and buck regulator ground.
- Use thermal relief policy later; direct/solid GND may be appropriate for ESD/high-current returns where constraints allow.

## Current Gate

Zone creation remains blocked because placement is not repaired and LJ has not visually approved placement.
