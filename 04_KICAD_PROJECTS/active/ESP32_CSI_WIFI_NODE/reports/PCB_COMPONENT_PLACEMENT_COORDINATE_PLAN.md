# PCB Component Placement Coordinate Plan

Project: ESP32_CSI_WIFI_NODE  
Date: 2026-05-07  
Status: `COORDINATE_PLAN_CREATED`  
Scope: planning only. Do not treat these as placed PCB coordinates until Phase 5.

## Coordinate Rules

- Board: `100 mm x 65 mm`
- Origin: lower-left
- All coordinates are mm.
- Coordinates are footprint nominal centers unless explicitly marked as an edge-alignment target.
- Rotation is an initial assumption for placement implementation and must be checked against actual KiCad footprint orientation.
- `0 deg` means use the footprint's native library orientation.

## Mechanical Fixed Items

| Ref | Footprint | X | Y | Rotation | Placement note |
|---|---|---:|---:|---:|---|
| `MH1` | `MountingHole_2.7mm_M2.5` | 5.0 | 5.0 | 0 | NPTH, no copper, 3 mm clearance |
| `MH2` | `MountingHole_2.7mm_M2.5` | 95.0 | 5.0 | 0 | NPTH, no copper, 3 mm clearance |
| `MH3` | `MountingHole_2.7mm_M2.5` | 5.0 | 60.0 | 0 | NPTH, no copper, 3 mm clearance |
| `MH4` | `MountingHole_2.7mm_M2.5` | 95.0 | 60.0 | 0 | NPTH, no copper, 3 mm clearance |

## Connectors

| Ref | Value | Footprint | X | Y | Rotation | Placement note |
|---|---|---|---:|---:|---:|---|
| `J1` | `JACK_5V` | `BarrelJack_CUI_PJ-102AH_Horizontal` | 4.0 | 17.0 | 180 | Mouth faces left/off-board; align actual opening to `x=0` |
| `J2` | `USB-C_NEEDS_REVIEW` | `USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal` | 96.5 | 18.0 | 0 | Mouth faces right/off-board; align connector edge to `x=100` |

## ESP32 Module

| Ref | Value | Footprint | X | Y | Rotation | Placement note |
|---|---|---|---:|---:|---:|---|
| `U2` | `ESP32-S3-WROOM-1U` | `RF_Module:ESP32-S3-WROOM-1` | 69.0 | 43.0 | 0 | Top/right half; antenna/U.FL/pigtail keepout toward top edge; footprint/value mismatch requires review |

## Power Path

| Ref | Value | Footprint | X | Y | Rotation | Placement note |
|---|---|---|---:|---:|---:|---|
| `F1` | `PTC_1206` | `Fuse_1206_3216Metric` | 19.0 | 17.0 | 0 | Immediately after J1 |
| `Q1` | `AO3401A_REV` | `SOT-23` | 29.0 | 17.0 | 0 | After F1; pin map resolved, package orientation still review item |
| `D3` | `TVS_NEEDS_REVIEW` | `D_SMA` | 36.0 | 13.0 | 90 | Close to protected input and GND return |
| `C2` | `10uF_IN` | `C_0805_2012Metric` | 39.0 | 20.5 | 90 | U1 input decoupling |
| `C5` | `47uF_16V` | `C_1206_3216Metric` | 42.0 | 15.0 | 90 | Bulk input cap near U1 IN/GND |
| `U1` | `AP63203_NEEDS_REVIEW` | `TSOT-23-6` | 49.0 | 25.0 | 0 | Buck regulator, away from USB/RF |
| `L1` | `3.9uH_REV` | `L_Vishay_IFSC-1515AH_4x4x1.8mm` | 57.0 | 25.0 | 0 | Adjacent to U1 SW |
| `C6` | `100nF_CBST` | `C_0603_1608Metric` | 49.0 | 30.0 | 0 | Tight to U1 BST/SW |
| `C7` | `22uF_OUT` | `C_1206_3216Metric` | 61.0 | 31.5 | 90 | +3V3 output cap |
| `C8` | `22uF_OUT` | `C_1206_3216Metric` | 65.0 | 31.5 | 90 | +3V3 output cap |
| `TP1` | `TP_5V` | `TestPoint_Pad_D1.5mm` | 25.0 | 6.5 | 0 | Bottom test row |
| `TP3` | `TP_3V3` | `TestPoint_Pad_D1.5mm` | 37.0 | 6.5 | 0 | Bottom test row |
| `TP5` | `TP_GND` | `TestPoint_Pad_D1.5mm` | 61.0 | 6.5 | 0 | Bottom test row |

## ESP32 Support / Decoupling

| Ref | Value | Footprint | X | Y | Rotation | Placement note |
|---|---|---|---:|---:|---:|---|
| `C3` | `10uF_MOD` | `C_0805_2012Metric` | 57.0 | 38.0 | 90 | Close to U2 3V3/GND side after U2 orientation confirmed |
| `C4` | `100nF_MOD` | `C_0603_1608Metric` | 60.0 | 38.0 | 90 | Close to U2 3V3/GND side |
| `C1` | `1uF_EN` | `C_0603_1608Metric` | 53.0 | 14.0 | 0 | Near reset/EN network and SW2 |
| `R1` | `10k_EN` | `R_0603_1608Metric` | 53.0 | 11.5 | 0 | Near reset/EN network |
| `R2` | `10k_BOOT` | `R_0603_1608Metric` | 43.0 | 11.5 | 0 | Near boot switch |

## USB Support

| Ref | Value | Footprint | X | Y | Rotation | Placement note |
|---|---|---|---:|---:|---:|---|
| `U3` | `USB_ESD_REV` | `SOT-23-6` | 85.0 | 18.0 | 0 | Within 5-10 mm of J2 signal pins if pinout allows |
| `R6` | `5.1k_CC1` | `R_0603_1608Metric` | 87.0 | 13.0 | 0 | Close to J2 CC1 |
| `R7` | `5.1k_CC2` | `R_0603_1608Metric` | 87.0 | 15.0 | 0 | Close to J2 CC2 |
| `R8` | `22R_D-` | `R_0603_1608Metric` | 80.5 | 19.0 | 0 | Between U3 and U2 USB pins |
| `R9` | `22R_D+` | `R_0603_1608Metric` | 80.5 | 21.0 | 0 | Between U3 and U2 USB pins |
| `TP8` | `TP_D+_REV` | `TestPoint_Pad_D1.5mm` | 67.0 | 6.5 | 0 | Stub risk; keep optional/reviewed |
| `TP9` | `TP_D-_REV` | `TestPoint_Pad_D1.5mm` | 73.0 | 6.5 | 0 | Stub risk; keep optional/reviewed |

## Reset, Boot, LEDs, and Low-Speed

| Ref | Value | Footprint | X | Y | Rotation | Placement note |
|---|---|---|---:|---:|---:|---|
| `SW1` | `BOOT_GPIO0_REVIEW` | `Panasonic_EVQPUJ_EVQPUA` | 40.0 | 8.0 | 0 | Accessible bottom edge |
| `SW2` | `RESET_EN_REVIEW` | `Panasonic_EVQPUJ_EVQPUA` | 50.0 | 8.0 | 0 | Accessible bottom edge |
| `D1` | `PWR_LED` | `LED_0603_1608Metric` | 58.0 | 8.0 | 0 | Visible bottom/front edge |
| `R3` | `2.2k` | `R_0603_1608Metric` | 58.0 | 11.0 | 0 | Close to D1 |
| `D2` | `STATUS_LED` | `LED_0603_1608Metric` | 64.0 | 8.0 | 0 | Visible bottom/front edge |
| `R4` | `2.2k` | `R_0603_1608Metric` | 64.0 | 11.0 | 0 | Close to D2 |
| `R5` | `0R_DNI` | `R_0603_1608Metric` | 89.0 | 23.0 | 0 | USB shield/GND policy option near J2 |
| `TP2` | `TP_EN` | `TestPoint_Pad_D1.5mm` | 31.0 | 6.5 | 0 | Bottom test row |
| `TP4` | `TP_BOOT` | `TestPoint_Pad_D1.5mm` | 43.0 | 6.5 | 0 | Bottom test row |
| `TP6` | `TP_U0TXD` | `TestPoint_Pad_D1.5mm` | 49.0 | 6.5 | 0 | Bottom test row |
| `TP7` | `TP_U0RXD` | `TestPoint_Pad_D1.5mm` | 55.0 | 6.5 | 0 | Bottom test row |

## Reserved Keepout Areas

| Area | Coordinates | Purpose |
|---|---|---|
| MH1 keepout | center `(5,5)`, radius `4.35` | component/copper clearance |
| MH2 keepout | center `(95,5)`, radius `4.35` | component/copper clearance |
| MH3 keepout | center `(5,60)`, radius `4.35` | component/copper clearance |
| MH4 keepout | center `(95,60)`, radius `4.35` | component/copper clearance |
| J1 connector | `x=0..18`, `y=8..28` | barrel jack body/plug clearance |
| J2 connector | `x=84..100`, `y=8..29` | USB-C body/cable/support area |
| U2 RF/antenna | `x=52..86`, `y=52..65` | no copper/components until actual keepout confirmed |
| Buck switch | `x=47..61`, `y=22..31` | compact local high-dV/dt loop only |

## Implementation Notes For Later Placement

- Place fixed mechanical items first: outline, holes, J1, J2, U2.
- Then place power path left-to-center.
- Then place USB support between J2 and U2.
- Then place bottom controls, LEDs, and test pads.
- Keep all text readable and outside pads.
- Do not route while applying these coordinates.
