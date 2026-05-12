# Engineering Rules Migration Summary

This summary records the normalized rule themes drained from:

- engineering-rules intake root
- USB-C / ESD intake
- buck-regulator intake
- PCB layout / grounding / EMI / SI intake
- manufacturer layout-guide intake
- RF / Wi-Fi antenna intake
- power-integrity / decoupling intake
- signal-integrity / high-speed intake
- thermal / mechanical / enclosure intake
- test / debug / validation intake

## Canonical Outputs

- enforceable rules now live in `09_ACCURACY_ENGINE/`
- schematic readability enforcement also lives in `34_SCHEMATIC_QUALITY_ENGINE/`
- prelayout scoring/gating links live in `33_PCB_PRELAYOUT_ENGINE/`
- read-only routing enforcement lives in `03_TOOLS/scripts/pcb_quality/`

## Source Registry References

- `url_009659`
- `url_009667`
- `url_009904`
- `url_009905`
- `url_009915`
- `url_009918`
- `url_010082`
- `url_010083`
- `url_000005`
- `url_004540`
- `url_006903`
