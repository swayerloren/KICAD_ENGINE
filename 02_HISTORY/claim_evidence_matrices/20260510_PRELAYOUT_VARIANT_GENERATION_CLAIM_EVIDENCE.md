# Claim Evidence Matrix - Prelayout Variant Generation

| Claim | Evidence Source | Claim Status | Confidence | Risk | Human Review Required | Open Issue |
| --- | --- | --- | --- | --- | --- | --- |
| Three fresh prelayout variants were generated under `prelayout_variants/20260510_093811` | `04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/prelayout_variants/20260510_093811/variant_A`, `variant_B`, `variant_C` | `VERIFIED_BY_FILE` | High | Low | No | None |
| `VARIANT_B` is the current recommended planning candidate | `variant_comparison.json`, `PCB_PRELAYOUT_RECOMMENDED_VARIANT.md` | `VERIFIED_BY_FILE` | High | Low | No | None |
| Real placement and routing remain blocked | `prelayout_gate_result.json`, `LIVE_PROJECT_STATE.json`, `trace_quality.json` | `VERIFIED_BY_FILE` | High | Medium | Yes | `02_HISTORY/issue_logs/20260510_ESP32_CSI_WIFI_NODE_PRELAYOUT_VARIANT_PACKET_BLOCKED.md` |
| `J2` orientation is mechanically proven for bottom-edge use | `usb_c_orientation_audit.json` | `VERIFIED_BY_FILE` | High | Medium | No | None |
| `U2` antenna keepout faces outward and passes audit | `esp32_antenna_orientation_audit.json` | `VERIFIED_BY_FILE` | High | Medium | No | None |
| `J1` is not fully proven because the exact 3D model is unresolved | `barrel_jack_orientation_audit.json` | `VERIFIED_BY_FILE` | High | High | Yes | `02_HISTORY/issue_logs/20260510_ESP32_CSI_WIFI_NODE_PRELAYOUT_VARIANT_PACKET_BLOCKED.md` |
| The live board still fails routing geometry | `live_trace_geometry/trace_quality.json` | `VERIFIED_BY_FILE` | High | High | Yes | `02_HISTORY/issue_logs/20260510_ESP32_CSI_WIFI_NODE_PRELAYOUT_VARIANT_PACKET_BLOCKED.md` |
