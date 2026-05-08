# ESP32_CSI_WIFI_NODE JLCPCB Upload Checklist

Date: 2026-05-07

Package status: `NOT_CREATED`

Upload status: `UPLOAD_BLOCKED`

Final classification: `EXPORT_BLOCKED`

## Upload Decision

Do not upload this project to JLCPCB. No NOT_FINAL JLCPCB review package was created because the export preconditions failed.

## Required Package Items

| Item | Status | Notes |
|---|---:|---|
| NOT_FINAL package folder | `MISSING_BLOCKED` | No `NOT_FINAL_JLCPCB_REVIEW_<timestamp>` folder was created. |
| Gerber ZIP | `MISSING_BLOCKED` | No PCB exists. |
| Drill files | `MISSING_BLOCKED` | No PCB exists. |
| BOM CSV | `MISSING_BLOCKED` | Production BOM review is `BOM_BLOCKED`. |
| CPL / pick-and-place CSV | `MISSING_BLOCKED` | No PCB placement exists. |
| Schematic PDF | `MISSING_BLOCKED` | No partial package was generated. |
| PCB top/bottom PDFs or images | `MISSING_BLOCKED` | No PCB exists. |
| STEP review model | `MISSING_BLOCKED` | No PCB exists. |
| ERC report copy | `MISSING_BLOCKED` | Package folder was not created. |
| DRC report copy | `MISSING_BLOCKED` | DRC is `NOT_RUN_NO_PCB`. |
| Manifest | `MISSING_BLOCKED` | Package folder was not created. |
| ZIP package | `MISSING_BLOCKED` | Package folder was not created. |

## Gate Checklist

| Gate | Required status | Current status |
|---|---:|---:|
| LJ approved NOT_FINAL export | `YES` | `YES_FROM_PROMPT` |
| ERC | `PASS` | `PASS_REPORTED` |
| Schematic-to-PCB gate | `PASS` | `FAIL` |
| PCB file exists | `YES` | `NO` |
| DRC | `PASS_OR_ACCEPTED_NONBLOCKING` | `NOT_RUN_NO_PCB` |
| No unrouted nets | `YES` | `UNKNOWN_NO_PCB` |
| JLCPCB DFM/DFA review | `PASS_OR_ACCEPTED` | `JLCPCB_REVIEW_BLOCKED` |
| BOM review | `PASS_OR_ACCEPTED` | `BOM_BLOCKED` |
| Manifest marks all outputs NOT_FINAL | `YES` | `NOT_APPLICABLE_NO_PACKAGE` |

## Required Closure Before Upload

1. Do not upload until a real NOT_FINAL package exists.
2. Do not upload until the PCB exists and DRC/unrouted checks are current.
3. Do not upload until JLCPCB and BOM blockers are resolved or explicitly accepted by LJ as nonblocking review risks.
4. Do not treat any future package as production-ready unless the separate production gate passes.

