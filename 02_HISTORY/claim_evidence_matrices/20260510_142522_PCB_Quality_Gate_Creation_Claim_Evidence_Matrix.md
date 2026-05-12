# PCB Quality Gate Creation Claim Evidence Matrix

Record kind: `claim_evidence_matrix`
Created: `2026-05-10T14:25:22`
Scope: `global`
Project: `N/A`
Severity: `MEDIUM`
Confidence: `HIGH`
Claim status: `VERIFIED_BY_FILE`
Risk label: `MEDIUM_RISK`
Gate result: `PASS_WITH_WARNINGS`
Human review required: `YES`

## Matrix

| Claim | Evidence | Claim Status | Confidence | Risk | Human Review Required | Issue |
| --- | --- | --- | --- | --- | --- | --- |
| The repo now has an enforceable PCB quality gate that checks DRC, schematic parity, open nets, trace geometry, testpoint topology, power widths, USB routing, connector orientation, and zone/GND status. | 03_TOOLS/scripts/pcb_quality/; 04_KICAD_PROJECTS/_templates/pcb_routing_constraints.template.yaml; 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/config/pcb_routing_constraints.yaml; 04_KICAD_PROJECTS/active/ESP32_CSI_WIFI_NODE/reports/pcb_quality_gate/20260510_quality_gate_creation_v2/PCB_QUALITY_GATE_REPORT.md | `VERIFIED_BY_FILE` | `HIGH` | `MEDIUM_RISK` | `YES` | The active board remains blocked by real parity, connectivity, geometry, USB, and connector-proof failures. |

## Details

The claim is supported by the new pcb_quality script set, the CI workflow, the project constraints files, the corrected parity-mode DRC helper, and the generated live failing evidence packet for ESP32_CSI_WIFI_NODE.
