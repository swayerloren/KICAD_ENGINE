# AI Quality Scripts

These scripts create AI self-review, scorecard, claim/evidence, uncertainty, hallucination-risk, and quality-gate records.

## Safety

- Non-destructive.
- Do not edit KiCad design files.
- Do not delete old logs.
- Create timestamped markdown files.
- Support global and project scopes.
- Mark records with claim status, severity, confidence, risk label, gate result, and human-review flag.
- Refuse obvious secret-looking content.

## Scripts

- `create_ai_self_review.py`
- `create_response_scorecard.py`
- `create_claim_evidence_matrix.py`
- `create_uncertainty_log.py`
- `create_hallucination_risk_log.py`
- `create_quality_gate_failure.py`
- `build_current_known_problems.py`
- `build_ai_quality_index.py`

## Example

```powershell
python 03_TOOLS/scripts/ai_quality/create_response_scorecard.py --repo-root . --scope global --title "Session scorecard" --overall-score 80 --evidence-support 16 --kicad-correctness 16 --datasheet-accuracy 12 --safety-compliance 13 --memory-routing 8 --uncertainty-disclosure 8 --usefulness 7 --risk-label MEDIUM_RISK --gate-result PASS_WITH_WARNINGS
```

