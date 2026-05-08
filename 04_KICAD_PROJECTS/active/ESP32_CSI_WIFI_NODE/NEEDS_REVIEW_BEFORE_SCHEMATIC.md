# Needs Review Before Schematic Footprint Assignment

Project: `ESP32_CSI_WIFI_NODE`  
Date: `2026-05-06`  
Status: `OPEN`

This list must be resolved or explicitly accepted before the schematic is edited to assign footprints.

## Critical Review Items

### 1. Barrel Jack `J1`

- Current value: `5.5x2.1_CENTER_POSITIVE_NEEDS_REVIEW`
- Current candidate: `Connector_BarrelJack:BarrelJack_CUI_PJ-102AH_Horizontal` as a reference only.
- Blocker: exact 5.5 mm OD / 2.1 mm ID right-angle barrel jack MPN is not selected.
- Required review:
  - Exact datasheet drawing.
  - Pin numbering and switched-contact behavior.
  - Mechanical edge direction and enclosure clearance.
  - Current rating.
  - Center-positive marking strategy.
- Status: `BLOCKED_NO_EXACT_PART`

### 2. PTC Fuse `F1`

- Current value: `PTC_HOLD_CURRENT_NEEDS_REVIEW`
- Candidate MPN/class: Littelfuse `1206L110THYR` or equivalent.
- Candidate footprint: `Fuse:Fuse_1206_3216Metric`
- Required review:
  - Hold/trip current against final load and adapter rating.
  - Temperature derating in enclosure.
  - Resistance and voltage drop.
  - Exact part availability.
- Status: `CANDIDATE_NEEDS_HUMAN_REVIEW`

### 3. PMOS Reverse Polarity `Q1`

- Current value: `AO3401A_CLASS_PMOS_PINMAP_BLOCKED_NEEDS_REVIEW`
- Candidate footprint: `Package_TO_SOT_SMD:SOT-23`
- Required review:
  - Exact AO3401A pin mapping.
  - Source/gate/drain schematic symbol mapping.
  - SOT-23 footprint pad numbering.
  - Protection circuit orientation.
  - Gate-source protection need.
- Status: `CANDIDATE_NEEDS_HUMAN_REVIEW`

### 4. TVS `D1`

- Current value: `5V_TVS_NEEDS_REVIEW`
- Candidate MPN/class: Littelfuse `SMAJ5.0A` class.
- Candidate footprint: `Diode_SMD:D_SMA`
- Required review:
  - Exact unidirectional/bidirectional choice.
  - Polarity and cathode marking.
  - Standoff/leakage/clamp suitability for 5 V adapter tolerance.
  - Placement relative to fuse, PMOS, and input capacitor.
- Status: `CANDIDATE_NEEDS_HUMAN_REVIEW`

### 5. Bulk Capacitor `C1`

- Current value: `47uF_>=16V_BULK_NEEDS_REVIEW`
- Blocker: exact capacitor type and package are not selected.
- Required review:
  - MLCC versus electrolytic/tantalum/polymer choice.
  - ESR, ripple, voltage rating, derating, and inrush.
  - Footprint and polarity if polarized.
- Status: `BLOCKED_NO_PACKAGE`

### 6. Buck Regulator `U1` And Support Parts

- Regulator value: `AP63203WU-7_3V3_2A_NEEDS_REVIEW`
- Candidate footprint: `Package_TO_SOT_SMD:TSOT-23-6`
- Required review:
  - AP63203 WU/TSOT26 drawing against KiCad footprint.
  - Thermal pad/no-thermal-pad details.
  - Pin mapping and orientation.
  - Switch-node layout constraints.
- Support blockers:
  - `L1` exact 3.9 uH inductor MPN/package not selected.
  - `C2`, `C3`, `C4` package and voltage/derating not selected.
  - `C5` candidate 0603 bootstrap cap still needs package acceptance.
- Status: `CANDIDATE_NEEDS_HUMAN_REVIEW` for `U1`; `BLOCKED_NO_EXACT_PART` or `BLOCKED_NO_PACKAGE` for support parts.

### 7. ESP32 Module `U2`

- Current value: `ESP32-S3-WROOM-1U-N16R8`
- Candidate footprint: `RF_Module:ESP32-S3-WROOM-1`
- Required review:
  - Exact Espressif module order code.
  - WROOM-1U land-pattern compatibility with KiCad `ESP32-S3-WROOM-1` footprint.
  - U.FL/MHF I antenna connector mechanical clearance.
  - Module keepout, pigtail bend, enclosure/SMA routing.
- Status: `CANDIDATE_NEEDS_HUMAN_REVIEW`

### 8. USB-C Connector `J2`

- Current value: `USB_C_RECEPTACLE_USB2_NEEDS_REVIEW`
- Candidate footprint: `Connector_USB:USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal`
- Required review:
  - Exact GCT USB4105 suffix.
  - Manufacturer drawing against KiCad footprint.
  - Pin numbering and shell/mechanical tab orientation.
  - Board-edge/enclosure alignment.
  - USB VBUS policy and shield/EMC strategy.
- Status: `CANDIDATE_NEEDS_HUMAN_REVIEW`

### 9. USB ESD `U3`

- Current value: `TPD2EUSB30_OR_EQ_NEEDS_REVIEW`
- Candidate footprint: `Package_TO_SOT_SMD:SOT-23-6` as candidate only.
- Blocker: exact orderable/package not selected.
- Required review:
  - Exact package suffix.
  - Pinout against schematic symbol.
  - Orientation relative to connector and D+/D- routing.
  - Capacitance and USB layout constraints.
- Status: `BLOCKED_NO_EXACT_PART`

### 10. Switches `SW1`, `SW2`

- Candidate footprint: `Button_Switch_SMD:Panasonic_EVQPUJ_EVQPUA` as candidate only.
- Blocker: exact tactile switch MPN not selected.
- Required review:
  - Orientation.
  - Actuation direction.
  - Enclosure access.
  - Footprint drawing.
- Status: `BLOCKED_NO_EXACT_PART`

### 11. LEDs `D2`, `D3`

- Candidate footprint: `LED_SMD:LED_0603_1608Metric`
- Blocker: exact LED color/package/MPN not selected.
- Required review:
  - Polarity.
  - Visibility in enclosure.
  - Resistor values versus selected LED forward voltage and target current.
  - Status LED GPIO assignment.
- Status: `BLOCKED_NO_EXACT_PART`

### 12. Test Pads `TP1` Through `TP9`

- Candidate footprint: `TestPoint:TestPoint_Pad_D1.5mm`
- Required review:
  - Probe access in enclosure.
  - Silkscreen label readability.
  - USB D+/D- stub risk for `TP8` and `TP9`.
- Status: `CANDIDATE_NEEDS_HUMAN_REVIEW`

### 13. Mounting Holes `MH1` Through `MH4`

- Candidate footprint: `MountingHole:MountingHole_2.7mm_M2.5`
- Required review:
  - Final screw size.
  - NPTH versus plated intent.
  - Copper keepout.
  - Standoff diameter, washer clearance, board outline, and enclosure fit.
- Status: `CANDIDATE_NEEDS_HUMAN_REVIEW`

## Schematic Edit Gate

Do not assign footprints in the schematic until LJ reviews this file and either:

1. Selects exact MPNs and packages, or
2. Explicitly accepts provisional package defaults for low-risk passives, or
3. Directs Codex to assign candidates while preserving `NEEDS_HUMAN_REVIEW` flags.

Current decision: `SCHEMATIC_FOOTPRINT_ASSIGNMENT_BLOCKED`
