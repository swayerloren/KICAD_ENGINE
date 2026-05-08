# KiCad Engine Project Gate Report

**Project:** `C:\Users\LJ\GitHub\KICAD_ENGINE\19_TEST_PROJECTS\sample_kicad_projects\tomasr8_attiny85_dev_board`
**Timestamp:** 2026-05-03T17:14:27.439158
**Duration:** 3.26s

## Summary

| Metric | Value |
| ------ | ----- |
| Total Gates | 9 |
| Passed | 0 |
| Failed | 9 |
| Not Applicable | 0 |
| **Final Status** | **FAIL** |

## Gate Results

### [FAIL] Schematic Annotation (`schematic_annotation_gate`)

**Status:** `FAIL`  
**Duration:** 0.00s  

**Blockers:**

- **CRITICAL** `GATE_EXECUTION_ERROR`: Gate execution failed: 'GateResult' object has no attribute 'add_evidence'

### [FAIL] ERC (Electrical Rules Check) (`erc_gate`)

**Status:** `FAIL`  
**Duration:** 1.42s  

**Blockers:**

- **CRITICAL** `ERC_ERROR`: Unexpected error during ERC: 'GateResult' object has no attribute 'add_evidence'

### [FAIL] Schematic Visual Review (`schematic_visual_gate`)

**Status:** `FAIL`  
**Duration:** 0.00s  

**Blockers:**

- **CRITICAL** `GATE_EXECUTION_ERROR`: Gate execution failed: 'GateResult' object has no attribute 'add_warning'

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
- **CRITICAL** `FOOTPRINT_AUDIT_ERROR`: Error during footprint audit: 'GateResult' object has no attribute 'add_evidence'

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

### [FAIL] PCB Sync Readiness (`pcb_sync_gate`)

**Status:** `FAIL`  
**Duration:** 0.00s  

**Blockers:**

- **CRITICAL** `GATE_EXECUTION_ERROR`: Gate execution failed: 'GateResult' object has no attribute 'add_warning'

### [FAIL] DRC (Design Rules Check) (`drc_gate`)

**Status:** `FAIL`  
**Duration:** 1.82s  

**Blockers:**

- **CRITICAL** `DRC_ERROR`: Unexpected error during DRC: 'GateResult' object has no attribute 'add_evidence'

### [FAIL] PCB Visual Review (`pcb_visual_gate`)

**Status:** `FAIL`  
**Duration:** 0.00s  

**Blockers:**

- **CRITICAL** `GATE_EXECUTION_ERROR`: Gate execution failed: 'GateResult' object has no attribute 'add_warning'

### [FAIL] Unrouted Nets Check (`unrouted_nets_gate`)

**Status:** `FAIL`  
**Duration:** 0.00s  

**Blockers:**

- **CRITICAL** `GATE_EXECUTION_ERROR`: Gate execution failed: 'GateResult' object has no attribute 'add_warning'

### [FAIL] Fabrication Readiness (`fab_readiness_gate`)

**Status:** `FAIL`  
**Duration:** 0.00s  

**Blockers:**

- **CRITICAL** `GATE_EXECUTION_ERROR`: Gate execution failed: 'GateResult' object has no attribute 'add_warning'
