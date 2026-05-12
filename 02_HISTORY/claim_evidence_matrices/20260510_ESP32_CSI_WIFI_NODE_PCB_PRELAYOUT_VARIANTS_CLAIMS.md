# Claim / Evidence Matrix

| Claim | Evidence |
| --- | --- |
| The fresh prelayout run generated exactly three variants. | `prelayout_variants/20260510_135250/prelayout_gate_result.json`, `prelayout_variants/20260510_135250/variant_comparison.json` |
| `VARIANT_B` is the selected winner. | `reports/PCB_PRELAYOUT_RECOMMENDED_VARIANT.md`, `prelayout_variants/20260510_135250/packet_summary.json` |
| `VARIANT_B` wins because it ties on total score and then wins on fewer projected open nets. | `reports/PCB_PRELAYOUT_VARIANT_COMPARISON_REPORT.md` |
| `J2` USB-C orientation is proven but `J1` still requires human review. | `reports/PCB_PRELAYOUT_CONNECTOR_ORIENTATION_AUDIT.md`, `reports/mechanical_orientation/20260510_usb_c_orientation_audit.json`, `reports/mechanical_orientation/20260510_barrel_jack_orientation_audit.json` |
| `U2` antenna keepout is respected in the selected planning packet. | `prelayout_variants/20260510_135250/variant_B/connector_orientation_proof.md`, `reports/mechanical_orientation/20260510_esp32_antenna_orientation_audit.json` |
| The projected angle score for the selected variant is `100 / 100`. | `reports/PCB_PRELAYOUT_RECOMMENDED_VARIANT.md`, `prelayout_variants/20260510_135250/variant_B/route_angle_audit.json` |
| Real placement may not be applied yet. | `reports/PCB_PRELAYOUT_RECOMMENDED_VARIANT.md`, `prelayout_variants/20260510_135250/packet_summary.json` |
