# Power Input Protection Rules

Date: 2026-05-02

Status: AI guidance. Apply only after project input voltage, current, environment, connector, and safety requirements are known.

## Core Rule

Every external power input must be treated as an untrusted interface until the project proves otherwise.

Agents must check:

- Normal input-voltage range.
- Maximum credible input voltage.
- Reverse-polarity exposure.
- Hot-plug and inrush behavior.
- Short-circuit and overload behavior.
- Surge, ESD, and transient exposure.
- Connector current rating and polarity marking.
- Return path and chassis/enclosure relationship.
- Fault energy available from the source.

## Typical Front-End Order

For low-voltage DC boards, inspect or design the front end in this order:

1. Connector and mechanical polarity.
2. Fuse, PTC, eFuse, or other current limiting.
3. TVS or surge clamp when external transients are credible.
4. Reverse-polarity element: Schottky diode, P-channel MOSFET, N-channel MOSFET plus controller, or ideal-diode controller.
5. EMI/filtering when needed.
6. Bulk capacitance and local input capacitance.
7. Regulator or load switch.
8. Test point and rail label.

The order is not universal. For some systems the TVS must be before or after the fuse depending on fault-energy and clamp coordination. Agents must verify the intended protection chain from source documents.

## Fuse And PTC Rules

- Select hold current, trip current, voltage rating, resistance, and temperature derating from the exact part datasheet.
- Do not assume a resettable PTC protects semiconductors from fast faults.
- Check whether the upstream power source can supply enough current to trip the PTC.
- Check whether the protected circuit can tolerate the PTC leakage and post-trip temperature.
- Place current protection so downstream shorts do not burn traces or connectors before the fuse reacts.

## TVS Rules

- TVS standoff voltage must exceed the normal operating rail including tolerance.
- Clamp voltage must be below the downstream absolute maximum under the specified pulse, or additional protection is needed.
- Surge energy must be coordinated with source impedance and fuse behavior.
- Package power rating is not enough; verify waveform, pulse duration, and derating.
- Put the TVS close to the connector with a low-impedance return path.
- Avoid long thin traces between connector, TVS, and ground return.
- For data lines, capacitance matters. Do not use a power TVS on high-speed data.

## Reverse Polarity Rules

- Series Schottky protection is simple but creates voltage drop and heat.
- P-channel MOSFET protection can reduce drop, but the body diode orientation and gate-source rating must be checked.
- Add gate protection when the input range can exceed the MOSFET gate-source limit.
- Dedicated ideal-diode or reverse-protection controllers can improve behavior, but they are not generic replacements.
- Verify startup, load dump, reverse current, and fault behavior from the exact controller datasheet.

## eFuse Rules

- eFuses can provide current limit, inrush control, overvoltage behavior, reverse-current blocking, fault reporting, or thermal shutdown depending on part.
- Do not assume all eFuses include every protection feature.
- Check operating voltage, current limit range, package thermal resistance, SOA, startup into capacitance, and fault retry behavior.
- Check whether the part survives the upstream transient. An eFuse downstream of an unhandled surge can still fail.

## Agent Blockers

Stop and ask for requirements or mark the design incomplete if any of these are unknown:

- Maximum input voltage.
- Maximum load current.
- Input source type.
- Reverse-polarity exposure.
- Required safety standard or transient standard.
- Whether the output may connect to a user-accessible connector.
- Whether the rail powers a battery charger or battery-backed system.
