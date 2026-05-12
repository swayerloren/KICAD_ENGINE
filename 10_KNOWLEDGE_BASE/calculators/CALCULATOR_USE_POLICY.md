# Calculator Use Policy

Status: `CANONICAL_CALCULATOR_USE_POLICY`

## Hard Rules

1. Calculators are aids, not proof.
2. Record the source or formula behind every number that affects an engineering
   decision.
3. Trace-width, impedance, thermal, and power calculations must record board
   context and assumptions.
4. If the required assumptions are unknown, the result stays `UNVERIFIED`.
5. A calculator result does not override datasheet limits, fabricator rules, or
   KiCad ERC/DRC.

## Approved Use

- quick resistor-divider sizing
- quick RC filter sizing
- quick buck-feedback divider sizing
- first-pass trace-width planning when the chosen current-density assumption is
  explicitly recorded

## Not Approved As Sole Evidence

- final copper-width signoff
- impedance-control release approval
- thermal-signoff claims
- EMI/EMC compliance claims
- connector or footprint proof

## Required Record

For any calculator-backed decision, record:

- tool/script name
- input values
- formula or source note
- board/context assumptions
- result
- independent validation path

