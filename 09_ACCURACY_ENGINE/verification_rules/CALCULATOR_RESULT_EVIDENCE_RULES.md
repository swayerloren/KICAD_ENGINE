# Calculator Result Evidence Rules

Status: `MANDATORY_FOR_NUMERIC_DECISIONS`

## Hard Rules

1. Calculators are aids, not proof unless the formula or source is recorded.
2. Record all assumptions that materially affect the result.
3. If stackup, copper weight, thermal-rise target, voltage tolerance, or
   component tolerance is unknown, the result remains `UNVERIFIED`.
4. Do not use calculator output alone to claim:
   - final trace width approval
   - impedance-control approval
   - thermal-signoff
   - EMC compliance
5. Calculator-backed numbers must be cross-checked against the governing
   datasheet, board-house rule, or independent calculation.

## Minimum Record

- calculator/tool name
- input values
- formula or source note
- output values
- context notes
- independent validation path

## Examples

- `voltage_divider_calculator.py` plus the target IC datasheet input-current
  limits
- `buck_feedback_calculator.py` plus the regulator datasheet equation
- `trace_width_calculator_stub.py` plus chosen copper/thermal assumptions and
  fabricator capability cross-check

