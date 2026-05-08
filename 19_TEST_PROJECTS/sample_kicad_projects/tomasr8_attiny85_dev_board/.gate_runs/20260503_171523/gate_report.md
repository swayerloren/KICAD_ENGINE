# KiCad Engine Project Gate Report

**Project:** `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board`
**Timestamp:** 2026-05-03T17:15:23.110854
**Duration:** 3.25s

## Summary

| Metric | Value |
| ------ | ----- |
| Total Gates | 9 |
| Passed | 7 |
| Failed | 2 |
| Not Applicable | 0 |
| **Final Status** | **FAIL** |

## Gate Results

### [PASS] Schematic Annotation (`schematic_annotation_gate`)

**Status:** `PASS`  
**Duration:** 0.00s  

**Evidence Files:**

- `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\.gate_runs\20260503_171523\schematic_annotation_audit.json` (output_file)

**Details:**

```json
{
  "total_references": 0,
  "unique_references": 0,
  "reference_types": {}
}
```

### [FAIL] ERC (Electrical Rules Check) (`erc_gate`)

**Status:** `FAIL`  
**Duration:** 1.45s  

**Blockers:**

- **CRITICAL** `ERC_ERRORS_DETECTED`: ERC detected 6 errors
  - Remediation: Review and fix all ERC errors in schematic
  - Evidence: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\.gate_runs\20260503_171523\erc_report.txt`

**Warnings:**

- ERC detected 1 warnings

**Evidence Files:**

- `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\.gate_runs\20260503_171523\erc_report.txt` (output_file)

**Details:**

```json
{
  "errors": 6,
  "warnings": 1,
  "erc_file": "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE\\19_TEST_PROJECTS\\sample_kicad_projects\\tomasr8_attiny85_dev_board\\.gate_runs\\20260503_171523\\erc_report.txt"
}
```

### [PASS] Schematic Visual Review (`schematic_visual_gate`)

**Status:** `PASS`  
**Duration:** 0.01s  

**Warnings:**

- No full-page schematic exports found

**Evidence Files:**

- `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\reports\CLOSE_UP_REVIEW.md` (output_file)

**Details:**

```json
{
  "close_up_reviews": [
    "CLOSE_UP_REVIEW.md"
  ],
  "status_summary": {
    "full_page_exports": false,
    "close_up_review": true
  }
}
```

### [FAIL] Footprint Audit (`footprint_audit_gate`)

**Status:** `FAIL`  
**Duration:** 0.00s  

**Blockers:**

- **CRITICAL** `MISSING_FOOTPRINT`: J (USB_A) has no footprint assigned
  - Remediation: Assign a valid footprint to each component
  - Evidence: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\attiny85.kicad_sch`
- **CRITICAL** `MISSING_FOOTPRINT`: J (Conn_02x05_Odd_Even) has no footprint assigned
  - Remediation: Assign a valid footprint to each component
  - Evidence: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\attiny85.kicad_sch`
- **CRITICAL** `MISSING_FOOTPRINT`: D (D_Zener) has no footprint assigned
  - Remediation: Assign a valid footprint to each component
  - Evidence: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\attiny85.kicad_sch`
- **CRITICAL** `MISSING_FOOTPRINT`: D (LED) has no footprint assigned
  - Remediation: Assign a valid footprint to each component
  - Evidence: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\attiny85.kicad_sch`
- **CRITICAL** `MISSING_FOOTPRINT`: R (R) has no footprint assigned
  - Remediation: Assign a valid footprint to each component
  - Evidence: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\attiny85.kicad_sch`
- **CRITICAL** `MISSING_FOOTPRINT`: #FLG (PWR_FLAG) has no footprint assigned
  - Remediation: Assign a valid footprint to each component
  - Evidence: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\attiny85.kicad_sch`
- **CRITICAL** `MISSING_FOOTPRINT`: #FLG0101 (PWR_FLAG) has no footprint assigned
  - Remediation: Assign a valid footprint to each component
  - Evidence: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\attiny85.kicad_sch`
- **CRITICAL** `MISSING_FOOTPRINT`: #FLG0102 (PWR_FLAG) has no footprint assigned
  - Remediation: Assign a valid footprint to each component
  - Evidence: `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\attiny85.kicad_sch`

**Evidence Files:**

- `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\.gate_runs\20260503_171523\footprint_audit_report.json` (output_file)

**Details:**

```json
{
  "total_components": 23,
  "with_footprints": 15,
  "missing_footprints": 8,
  "unresolved_footprints": 0,
  "blocked_for_review": 0
}
```

### [PASS] PCB Sync Readiness (`pcb_sync_gate`)

**Status:** `PASS`  
**Duration:** 0.00s  

**Warnings:**

- No SCHEMATIC_TO_PCB_GATE_STATUS.md report found
- No SCHEMATIC_ANNOTATION_AUDIT report found

**Details:**

```json
{
  "gate_status": "REPORT_MISSING"
}
```

### [PASS] DRC (Design Rules Check) (`drc_gate`)

**Status:** `PASS`  
**Duration:** 1.77s  

**Evidence Files:**

- `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\.gate_runs\20260503_171523\drc_report.txt` (output_file)

**Details:**

```json
{
  "violations": 0,
  "warnings": 0,
  "drc_file": "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE\\19_TEST_PROJECTS\\sample_kicad_projects\\tomasr8_attiny85_dev_board\\.gate_runs\\20260503_171523\\drc_report.txt"
}
```

### [PASS] PCB Visual Review (`pcb_visual_gate`)

**Status:** `PASS`  
**Duration:** 0.01s  

**Warnings:**

- No PCB visual exports found

**Evidence Files:**

- `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\reports\PCB_CLOSE_UP_REVIEW.md` (output_file)

**Details:**

```json
{
  "close_up_reviews": [
    "PCB_CLOSE_UP_REVIEW.md"
  ],
  "status_summary": {
    "pcb_exports": false,
    "close_up_review": true
  }
}
```

### [PASS] Unrouted Nets Check (`unrouted_nets_gate`)

**Status:** `PASS`  
**Duration:** 0.00s  

**Warnings:**

- Found 57 nets with minimal routing

**Evidence Files:**

- `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\.gate_runs\20260503_171523\unrouted_nets_report.json` (output_file)

**Details:**

```json
{
  "total_nets": 57,
  "nets_with_tracks": 13,
  "potentially_unrouted": 57,
  "pcb_file": "C:\\Users\\LJ\\GitHub\\KICAD_ENGINE\\19_TEST_PROJECTS\\sample_kicad_projects\\tomasr8_attiny85_dev_board\\attiny85.kicad_pcb"
}
```

### [PASS] Fabrication Readiness (`fab_readiness_gate`)

**Status:** `PASS`  
**Duration:** 0.00s  

**Warnings:**

- No Gerber files found in fabrication directory
- No drill files found in fabrication directory
- No BOM file found in fabrication directory
- No FINAL_PCB_VERIFICATION_BEFORE_FAB report found
- No NOT_FINAL_FAB_PACKAGE_AUDIT report found

**Evidence Files:**

- `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board\.gate_runs\20260503_171523\fab_readiness_report.json` (output_file)

**Details:**

```json
{
  "outputs": {
    "gerbers": [],
    "drill": [],
    "bom": [],
    "pick_place": [],
    "step": [],
    "not_final": []
  },
  "has_final_verification": false,
  "has_fab_audit": false,
  "readiness_status": "NOT_READY"
}
```
