# Automotive 12V Power Rules

Date: 2026-05-02

Status: guidance only. This repo must not claim automotive qualification without standards-based testing and verified component ratings.

## Core Warning

Automotive 12V is not a clean 12V bench supply. Agents must assume a vehicle supply can include reverse battery, jump start, cranking dips, load dump, alternator noise, inductive spikes, ESD, EMI, temperature extremes, and ground offsets unless the project explicitly says otherwise.

## Required Inputs Before Design

- Nominal system: 12V, 24V, or both.
- Required operating range.
- Required survival range.
- Load dump standard and pulse definition.
- Reverse-battery duration and current source.
- Cold-crank behavior.
- Jump-start voltage.
- EMI/EMC requirements.
- Ambient temperature range.
- Maximum board current.
- Whether the design is safety-relevant or only hobby/bench-adjacent.

## Typical Protection Blocks

An automotive input may include:

- Input connector with correct current and environmental rating.
- Fuse or resettable protection coordinated with wire harness and source.
- Reverse-battery protection using diode, MOSFET, or controller.
- Load-dump and surge TVS with appropriate energy rating.
- EMI filter with layout and saturation checks.
- Wide-input buck regulator or pre-regulator.
- Load switch or eFuse when controlled startup or fault reporting is needed.
- Bulk capacitance rated for voltage, ripple current, and temperature.
- Local decoupling for downstream rails.

This is a topology checklist, not a complete reference design.

## TVS And Surge Rules

- Select standoff voltage, breakdown voltage, clamp voltage, peak pulse power, pulse waveform, and package from the exact datasheet.
- Confirm downstream semiconductors survive the clamped voltage.
- Confirm upstream fuse or source impedance prevents the TVS from being destroyed during sustained overvoltage.
- Automotive TVS parts are often much larger than logic-level ESD parts. Do not substitute by package alone.

## Reverse Battery Rules

- Schottky diode protection wastes power and heats under load.
- P-channel MOSFET protection needs body-diode, gate-source, SOA, and transient checks.
- N-channel MOSFET plus controller or ideal-diode controller can reduce loss but increases design complexity.
- Verify behavior during dynamic reverse-polarity events, not just static reverse connection.

## Regulator Rules

- The regulator input rating must cover the protected input range, not just nominal battery voltage.
- Check startup under cold crank and overvoltage survival under load dump or jump start.
- Check thermal dissipation at maximum ambient.
- Check EMI guidance from the regulator datasheet.
- Buck switch-node routing, diode/inductor placement, and input loop area matter more than schematic correctness alone.

## Agent Blockers

Do not mark an automotive input design ready if any of these are missing:

- Defined transient standard.
- Exact TVS part and pulse rating.
- Reverse-battery protection analysis.
- Regulator input transient survival.
- Thermal analysis.
- Fuse coordination.
- Connector and harness current rating.
- DRC plus visual review of high-current copper, clearances, and polarity markings.

## Public Claim Rule

Use wording such as `automotive-style input protection planning` until testing, standards evidence, and component ratings support stronger claims.
