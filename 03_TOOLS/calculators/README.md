# Calculator Scripts

Status: `FIRST_PASS_SIZING_TOOLS_ONLY`

These scripts are small first-pass engineering aids. They are not final proof.

Read before use:

- `10_KNOWLEDGE_BASE/calculators/CALCULATOR_USE_POLICY.md`
- `10_KNOWLEDGE_BASE/calculators/PCB_CALCULATOR_SOURCE_INDEX.md`
- `09_ACCURACY_ENGINE/verification_rules/CALCULATOR_RESULT_EVIDENCE_RULES.md`

Included scripts:

- `trace_width_calculator_stub.py`
  - width from current plus a recorded current-density assumption
- `voltage_divider_calculator.py`
  - solve one resistor in a standard divider
- `buck_feedback_calculator.py`
  - solve one resistor in a standard buck feedback divider
- `rc_filter_calculator.py`
  - solve cutoff frequency or one missing RC value

Rule: calculator output must be validated independently before it is treated as
engineering evidence.

