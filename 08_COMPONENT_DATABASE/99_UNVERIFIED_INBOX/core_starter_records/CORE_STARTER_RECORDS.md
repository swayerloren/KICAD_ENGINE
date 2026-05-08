# Core Starter Component Records

Status: `UNVERIFIED_PLACEHOLDER_SET`

These starter records are intentionally conservative. They provide routing and review placeholders only; they do not approve any symbol, footprint, pinout, package, 3D model, schematic use, PCB use, BOM release, or manufacturing decision.

Every exact value, package, pinout, symbol, footprint, land pattern, connector orientation, and 3D model must be verified from source documents and/or the user's installed KiCad libraries before use.

## Records

### ESPRESSIF_ESP32_S3_WROOM_1

- Part number: `ESP32-S3-WROOM-1`
- Vendor: `Espressif`
- Category: `01_MICROCONTROLLERS`
- Datasheet path or source URL placeholder: `Unknown - requires source verification`
- KiCad symbol candidates: `RF_Module:ESP32-S3-WROOM-1 candidate if present locally - verify pinout before use`
- KiCad footprint candidates: `RF_Module:ESP32-S3-WROOM-1 candidate if present locally - verify land pattern and keepout before use`
- Package drawing status: `UNVERIFIED`
- 3D model status: `UNVERIFIED`
- Verification status: `UNVERIFIED_PLACEHOLDER`
- Pinout status: `UNVERIFIED`
- Common mistakes: assuming the module land pattern is correct without checking datasheet keepout; ignoring boot/strap pins; ignoring RF antenna keepout.
- Human review required flag: `YES`

### ESPRESSIF_ESP32_S3_WROOM_1U

- Part number: `ESP32-S3-WROOM-1U`
- Vendor: `Espressif`
- Category: `01_MICROCONTROLLERS`
- Datasheet path or source URL placeholder: `Unknown - requires source verification`
- KiCad symbol candidates: `RF_Module:ESP32-S3-WROOM-1 may be a pinout candidate only - verify U variant before use`
- KiCad footprint candidates: `RF_Module:ESP32-S3-WROOM-1U candidate if present locally - verify land pattern, antenna connector, and keepout before use`
- Package drawing status: `UNVERIFIED`
- 3D model status: `UNVERIFIED`
- Verification status: `UNVERIFIED_PLACEHOLDER`
- Pinout status: `UNVERIFIED`
- Common mistakes: treating WROOM-1 and WROOM-1U as mechanically interchangeable; skipping external antenna connector review; assuming U.FL/IPEX compatibility.
- Human review required flag: `YES`

### STMICRO_STM32F103C8T6

- Part number: `STM32F103C8T6`
- Vendor: `STMicroelectronics`
- Category: `01_MICROCONTROLLERS`
- Datasheet path or source URL placeholder: `Unknown - requires source verification`
- KiCad symbol candidates: `Unknown - run KiCad library search and verify exact pinout`
- KiCad footprint candidates: `Unknown - exact package drawing required for the orderable suffix`
- Package drawing status: `UNVERIFIED`
- 3D model status: `UNVERIFIED`
- Verification status: `UNVERIFIED_PLACEHOLDER`
- Pinout status: `UNVERIFIED`
- Common mistakes: assuming package from suffix without source check; omitting BOOT0/debug/reset requirements; missing VDDA/VSSA and decoupling review.
- Human review required flag: `YES`

### STMICRO_STM32F411CEU6

- Part number: `STM32F411CEU6`
- Vendor: `STMicroelectronics`
- Category: `01_MICROCONTROLLERS`
- Datasheet path or source URL placeholder: `Unknown - requires source verification`
- KiCad symbol candidates: `Unknown - run KiCad library search and verify exact pinout`
- KiCad footprint candidates: `Unknown - exact package drawing required for the orderable suffix`
- Package drawing status: `UNVERIFIED`
- 3D model status: `UNVERIFIED`
- Verification status: `UNVERIFIED_PLACEHOLDER`
- Pinout status: `UNVERIFIED`
- Common mistakes: copying Black Pill assumptions into a bare-chip design; missing SWD/BOOT0/reset; choosing footprint before package drawing verification.
- Human review required flag: `YES`

### MICROCHIP_PIC16F877A

- Part number: `PIC16F877A`
- Vendor: `Microchip`
- Category: `01_MICROCONTROLLERS`
- Datasheet path or source URL placeholder: `Unknown - requires source verification`
- KiCad symbol candidates: `Unknown - run KiCad library search and verify package-specific pinout`
- KiCad footprint candidates: `Unknown - exact package suffix and package drawing required`
- Package drawing status: `UNVERIFIED`
- 3D model status: `UNVERIFIED`
- Verification status: `UNVERIFIED_PLACEHOLDER`
- Pinout status: `UNVERIFIED`
- Common mistakes: ignoring exact package variant; missing MCLR/ICSP requirements; assuming oscillator and voltage limits from memory.
- Human review required flag: `YES`

### MICROCHIP_PIC18F4550

- Part number: `PIC18F4550`
- Vendor: `Microchip`
- Category: `01_MICROCONTROLLERS`
- Datasheet path or source URL placeholder: `Unknown - requires source verification`
- KiCad symbol candidates: `Unknown - run KiCad library search and verify package-specific pinout`
- KiCad footprint candidates: `Unknown - exact package suffix and package drawing required`
- Package drawing status: `UNVERIFIED`
- 3D model status: `UNVERIFIED`
- Verification status: `UNVERIFIED_PLACEHOLDER`
- Pinout status: `UNVERIFIED`
- Common mistakes: assuming USB support means the schematic is complete; missing oscillator/USB/MCLR/ICSP details; selecting a footprint before package suffix is known.
- Human review required flag: `YES`

### RASPBERRY_PI_RP2040

- Part number: `RP2040`
- Vendor: `Raspberry Pi`
- Category: `01_MICROCONTROLLERS`
- Datasheet path or source URL placeholder: `Unknown - requires source verification`
- KiCad symbol candidates: `Unknown - run KiCad library search and verify pinout`
- KiCad footprint candidates: `Unknown - exact package drawing required`
- Package drawing status: `UNVERIFIED`
- 3D model status: `UNVERIFIED`
- Verification status: `UNVERIFIED_PLACEHOLDER`
- Pinout status: `UNVERIFIED`
- Common mistakes: omitting required external flash review; assuming crystal and USB details; skipping boot/debug and power decoupling review.
- Human review required flag: `YES`

### MICROCHIP_MCP2562FD

- Part number: `MCP2562FD`
- Vendor: `Microchip`
- Category: `03_COMMUNICATION`
- Datasheet path or source URL placeholder: `Unknown - requires source verification`
- KiCad symbol candidates: `Unknown - run KiCad library search and verify pinout`
- KiCad footprint candidates: `Unknown - exact package suffix and package drawing required`
- Package drawing status: `UNVERIFIED`
- 3D model status: `UNVERIFIED`
- Verification status: `UNVERIFIED_PLACEHOLDER`
- Pinout status: `UNVERIFIED`
- Common mistakes: assuming CAN FD transceiver implies CAN FD controller support; omitting termination/protection review; mixing voltage domains.
- Human review required flag: `YES`

### TI_SN65HVD230

- Part number: `SN65HVD230`
- Vendor: `Texas Instruments`
- Category: `03_COMMUNICATION`
- Datasheet path or source URL placeholder: `Unknown - requires source verification`
- KiCad symbol candidates: `Unknown - run KiCad library search and verify pinout`
- KiCad footprint candidates: `Unknown - exact package suffix and package drawing required`
- Package drawing status: `UNVERIFIED`
- 3D model status: `UNVERIFIED`
- Verification status: `UNVERIFIED_PLACEHOLDER`
- Pinout status: `UNVERIFIED`
- Common mistakes: using 5 V assumptions on 3.3 V CAN parts; omitting CAN termination and transient protection review; assuming package from board-module examples.
- Human review required flag: `YES`

### TI_LM2596

- Part number: `LM2596`
- Vendor: `Texas Instruments or compatible manufacturer - requires exact source verification`
- Category: `02_POWER`
- Datasheet path or source URL placeholder: `Unknown - requires source verification`
- KiCad symbol candidates: `Unknown - run KiCad library search and verify exact variant`
- KiCad footprint candidates: `Unknown - exact package and thermal drawing required`
- Package drawing status: `UNVERIFIED`
- 3D model status: `UNVERIFIED`
- Verification status: `UNVERIFIED_PLACEHOLDER`
- Pinout status: `UNVERIFIED`
- Common mistakes: using module-board assumptions for bare IC design; ignoring inductor/diode/capacitor selection; poor switch-node layout; ignoring thermal limits.
- Human review required flag: `YES`

### AMS_AMS1117_3V3

- Part number: `AMS1117-3.3`
- Vendor: `AMS or compatible manufacturer - requires exact source verification`
- Category: `02_POWER`
- Datasheet path or source URL placeholder: `Unknown - requires source verification`
- KiCad symbol candidates: `Unknown - run KiCad library search and verify regulator pinout`
- KiCad footprint candidates: `Unknown - exact package drawing required`
- Package drawing status: `UNVERIFIED`
- 3D model status: `UNVERIFIED`
- Verification status: `UNVERIFIED_PLACEHOLDER`
- Pinout status: `UNVERIFIED`
- Common mistakes: assuming all 1117 pinouts/packages are interchangeable; ignoring dropout and thermal dissipation; using wrong capacitor assumptions.
- Human review required flag: `YES`

### GENERIC_USB_C_16PIN_RECEPTACLE

- Part number: `USB-C 16-pin receptacle generic`
- Vendor: `Generic - exact manufacturer required`
- Category: `04_CONNECTORS`
- Datasheet path or source URL placeholder: `Unknown - exact manufacturer drawing required`
- KiCad symbol candidates: `Unknown - exact connector pinout required`
- KiCad footprint candidates: `Do not select until exact manufacturer part number and drawing are known`
- Package drawing status: `MISSING`
- 3D model status: `UNVERIFIED`
- Verification status: `UNVERIFIED_PLACEHOLDER`
- Pinout status: `UNVERIFIED`
- Common mistakes: using a generic USB-C footprint; mirrored orientation; wrong CC/SBU/shield pins; assuming all 16-pin USB-C receptacles share a footprint.
- Human review required flag: `YES`

### GENERIC_UFL_CONNECTOR

- Part number: `U.FL connector generic`
- Vendor: `Generic - exact manufacturer required`
- Category: `10_RF_AND_ANTENNAS`
- Datasheet path or source URL placeholder: `Unknown - exact manufacturer drawing required`
- KiCad symbol candidates: `Connector:Coaxial connector candidate only - verify exact pin/pad behavior`
- KiCad footprint candidates: `Do not select until exact U.FL/IPEX/MHF series and drawing are known`
- Package drawing status: `MISSING`
- 3D model status: `UNVERIFIED`
- Verification status: `UNVERIFIED_PLACEHOLDER`
- Pinout status: `UNVERIFIED`
- Common mistakes: treating U.FL, IPEX, and MHF variants as interchangeable; wrong connector orientation; missing cable keepout and RF ground review.
- Human review required flag: `YES`

### GENERIC_TVS_DIODE

- Part number: `TVS diode generic`
- Vendor: `Generic - exact manufacturer required`
- Category: `05_PROTECTION`
- Datasheet path or source URL placeholder: `Unknown - exact part and datasheet required`
- KiCad symbol candidates: `Device:D_TVS candidate only - verify polarity and pinout`
- KiCad footprint candidates: `Unknown - exact package drawing required`
- Package drawing status: `MISSING`
- 3D model status: `UNVERIFIED`
- Verification status: `UNVERIFIED_PLACEHOLDER`
- Pinout status: `UNVERIFIED`
- Common mistakes: choosing standoff voltage/capacitance from memory; wrong polarity/orientation; placing protection too far from connector.
- Human review required flag: `YES`

### GENERIC_POLYFUSE

- Part number: `polyfuse generic`
- Vendor: `Generic - exact manufacturer required`
- Category: `05_PROTECTION`
- Datasheet path or source URL placeholder: `Unknown - exact part and datasheet required`
- KiCad symbol candidates: `Device:Polyfuse candidate only - verify use and rating`
- KiCad footprint candidates: `Unknown - exact package drawing required`
- Package drawing status: `MISSING`
- 3D model status: `UNVERIFIED`
- Verification status: `UNVERIFIED_PLACEHOLDER`
- Pinout status: `UNVERIFIED`
- Common mistakes: assuming a resettable fuse protects semiconductors quickly; ignoring hold/trip current and temperature derating; choosing footprint before package drawing.
- Human review required flag: `YES`

