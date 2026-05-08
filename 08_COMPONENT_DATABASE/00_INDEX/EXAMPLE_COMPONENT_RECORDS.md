# Example Component Records

Date: 2026-05-02

Status: placeholder records only. These are not verified design data.

## Required Warning

Every record in this file and `example_component_records.json` starts with `UNVERIFIED_PLACEHOLDER`. Do not use these records to place schematic symbols, assign footprints, route layouts, choose support components, or release fabrication outputs until source verification is complete.

Required unknown value:

```text
Unknown - requires source verification
```

## Shared Placeholder Fields

Unless a record explicitly says otherwise, these fields are placeholders:

| Field | Value |
| --- | --- |
| package | Unknown - requires source verification |
| KiCad symbol candidates | Unknown - requires source verification |
| KiCad footprint candidates | Unknown - requires source verification |
| 3D model candidates | Unknown - requires source verification |
| datasheet local path | Unknown - requires source verification |
| datasheet source URL placeholder | Unknown - requires source verification |
| verified status | UNVERIFIED_PLACEHOLDER |
| pinout status | UNVERIFIED_PLACEHOLDER |
| footprint status | UNVERIFIED_PLACEHOLDER |
| layout notes | Unknown - requires source verification |
| power notes | Unknown - requires source verification |
| communication notes | Unknown - requires source verification |
| required external parts | Unknown - requires source verification |
| reference circuits | Unknown - requires source verification |
| known errata | Unknown - requires source verification |
| source confidence | UNVERIFIED_PLACEHOLDER |

## Records

### ESP32-S3-WROOM-1

- part number: ESP32-S3-WROOM-1
- vendor: Espressif
- family: ESP32_S3
- category: 01_MICROCONTROLLERS
- package: Unknown - requires source verification
- KiCad symbol candidates: Unknown - requires source verification
- KiCad footprint candidates: Unknown - requires source verification
- 3D model candidates: Unknown - requires source verification
- datasheet local path: Unknown - requires source verification
- datasheet source URL placeholder: Unknown - requires source verification
- verified status: UNVERIFIED_PLACEHOLDER
- pinout status: UNVERIFIED_PLACEHOLDER
- footprint status: UNVERIFIED_PLACEHOLDER
- layout notes: Verify module keepouts, RF rules, antenna guidance, and boot/debug constraints before design use.
- power notes: Unknown - requires source verification
- communication notes: Unknown - requires source verification
- common mistakes: Treating module pinout, boot strapping, and antenna guidance as generic across variants.
- AI warnings: Do not assume the WROOM-1 and WROOM-1U layouts are interchangeable.
- suitable use cases: Planning placeholder only.
- not suitable use cases: Final schematic, footprint assignment, RF layout, or BOM selection before verification.
- required external parts: Unknown - requires source verification
- reference circuits: Unknown - requires source verification
- known errata: Unknown - requires source verification
- source confidence: UNVERIFIED_PLACEHOLDER

### ESP32-S3-WROOM-1U

- part number: ESP32-S3-WROOM-1U
- vendor: Espressif
- family: ESP32_S3
- category: 01_MICROCONTROLLERS
- package: Unknown - requires source verification
- KiCad symbol candidates: Unknown - requires source verification
- KiCad footprint candidates: Unknown - requires source verification
- 3D model candidates: Unknown - requires source verification
- datasheet local path: Unknown - requires source verification
- datasheet source URL placeholder: Unknown - requires source verification
- verified status: UNVERIFIED_PLACEHOLDER
- pinout status: UNVERIFIED_PLACEHOLDER
- footprint status: UNVERIFIED_PLACEHOLDER
- layout notes: Verify external antenna connector, RF feed, keepout, and module land pattern before design use.
- power notes: Unknown - requires source verification
- communication notes: Unknown - requires source verification
- common mistakes: Treating external antenna and onboard antenna variants as layout-equivalent.
- AI warnings: Do not choose antenna path, RF footprint, or keepout from memory.
- suitable use cases: Planning placeholder only.
- not suitable use cases: Final RF layout or fabrication output before verification.
- required external parts: Unknown - requires source verification
- reference circuits: Unknown - requires source verification
- known errata: Unknown - requires source verification
- source confidence: UNVERIFIED_PLACEHOLDER

### STM32F103C8T6

- part number: STM32F103C8T6
- vendor: STMicroelectronics
- family: STM32F1
- category: 01_MICROCONTROLLERS
- package: Unknown - requires source verification
- KiCad symbol candidates: Unknown - requires source verification
- KiCad footprint candidates: Unknown - requires source verification
- 3D model candidates: Unknown - requires source verification
- datasheet local path: Unknown - requires source verification
- datasheet source URL placeholder: Unknown - requires source verification
- verified status: UNVERIFIED_PLACEHOLDER
- pinout status: UNVERIFIED_PLACEHOLDER
- footprint status: UNVERIFIED_PLACEHOLDER
- layout notes: Verify oscillator, reset, boot, SWD/debug, decoupling, and package rules.
- power notes: Unknown - requires source verification
- communication notes: Unknown - requires source verification
- common mistakes: Assuming board-module pinouts or clone board conventions apply to the bare MCU.
- AI warnings: Do not use package/pin count from memory.
- suitable use cases: Planning placeholder only.
- not suitable use cases: Bare MCU schematic before datasheet/reference-manual review.
- required external parts: Unknown - requires source verification
- reference circuits: Unknown - requires source verification
- known errata: Unknown - requires source verification
- source confidence: UNVERIFIED_PLACEHOLDER

### STM32F411CEU6

- part number: STM32F411CEU6
- vendor: STMicroelectronics
- family: STM32F4
- category: 01_MICROCONTROLLERS
- package: Unknown - requires source verification
- KiCad symbol candidates: Unknown - requires source verification
- KiCad footprint candidates: Unknown - requires source verification
- 3D model candidates: Unknown - requires source verification
- datasheet local path: Unknown - requires source verification
- datasheet source URL placeholder: Unknown - requires source verification
- verified status: UNVERIFIED_PLACEHOLDER
- pinout status: UNVERIFIED_PLACEHOLDER
- footprint status: UNVERIFIED_PLACEHOLDER
- layout notes: Verify oscillator, USB if used, reset, boot, SWD/debug, decoupling, and package rules.
- power notes: Unknown - requires source verification
- communication notes: Unknown - requires source verification
- common mistakes: Assuming a dev-board circuit covers the exact bare part and package.
- AI warnings: Do not infer package or footprint from suffix without source check.
- suitable use cases: Planning placeholder only.
- not suitable use cases: Final MCU placement or footprint selection before package drawing review.
- required external parts: Unknown - requires source verification
- reference circuits: Unknown - requires source verification
- known errata: Unknown - requires source verification
- source confidence: UNVERIFIED_PLACEHOLDER

### PIC16F877A

- part number: PIC16F877A
- vendor: Microchip
- family: PIC16
- category: 01_MICROCONTROLLERS
- package: Unknown - requires source verification
- KiCad symbol candidates: Unknown - requires source verification
- KiCad footprint candidates: Unknown - requires source verification
- 3D model candidates: Unknown - requires source verification
- datasheet local path: Unknown - requires source verification
- datasheet source URL placeholder: Unknown - requires source verification
- verified status: UNVERIFIED_PLACEHOLDER
- pinout status: UNVERIFIED_PLACEHOLDER
- footprint status: UNVERIFIED_PLACEHOLDER
- layout notes: Verify oscillator, reset/MCLR, programming/debug header, decoupling, and package option.
- power notes: Unknown - requires source verification
- communication notes: Unknown - requires source verification
- common mistakes: Assuming all package variants share the same footprint.
- AI warnings: Do not use legacy PIC assumptions without datasheet and programming guide review.
- suitable use cases: Planning placeholder only.
- not suitable use cases: Production design before package, programming, and lifecycle verification.
- required external parts: Unknown - requires source verification
- reference circuits: Unknown - requires source verification
- known errata: Unknown - requires source verification
- source confidence: UNVERIFIED_PLACEHOLDER

### PIC18F4550

- part number: PIC18F4550
- vendor: Microchip
- family: PIC18
- category: 01_MICROCONTROLLERS
- package: Unknown - requires source verification
- KiCad symbol candidates: Unknown - requires source verification
- KiCad footprint candidates: Unknown - requires source verification
- 3D model candidates: Unknown - requires source verification
- datasheet local path: Unknown - requires source verification
- datasheet source URL placeholder: Unknown - requires source verification
- verified status: UNVERIFIED_PLACEHOLDER
- pinout status: UNVERIFIED_PLACEHOLDER
- footprint status: UNVERIFIED_PLACEHOLDER
- layout notes: Verify USB, oscillator, reset/MCLR, programming/debug header, decoupling, and package option.
- power notes: Unknown - requires source verification
- communication notes: USB notes require source verification.
- common mistakes: Treating USB support as complete without checking oscillator, VUSB, ESD, connector, and firmware requirements.
- AI warnings: Do not generate a USB schematic from memory.
- suitable use cases: Planning placeholder only.
- not suitable use cases: USB production design before datasheet and reference circuit review.
- required external parts: Unknown - requires source verification
- reference circuits: Unknown - requires source verification
- known errata: Unknown - requires source verification
- source confidence: UNVERIFIED_PLACEHOLDER

### RP2040

- part number: RP2040
- vendor: Raspberry Pi
- family: RP2040
- category: 01_MICROCONTROLLERS
- package: Unknown - requires source verification
- KiCad symbol candidates: Unknown - requires source verification
- KiCad footprint candidates: Unknown - requires source verification
- 3D model candidates: Unknown - requires source verification
- datasheet local path: Unknown - requires source verification
- datasheet source URL placeholder: Unknown - requires source verification
- verified status: UNVERIFIED_PLACEHOLDER
- pinout status: UNVERIFIED_PLACEHOLDER
- footprint status: UNVERIFIED_PLACEHOLDER
- layout notes: Verify external flash, crystal, USB, regulator, boot, and layout/reference-design requirements.
- power notes: Unknown - requires source verification
- communication notes: Unknown - requires source verification
- common mistakes: Missing or misconfiguring external flash and boot support parts.
- AI warnings: Do not assume Pico board wiring equals a custom bare-chip design.
- suitable use cases: Planning placeholder only.
- not suitable use cases: Bare-chip design before datasheet and hardware design guide review.
- required external parts: Unknown - requires source verification
- reference circuits: Unknown - requires source verification
- known errata: Unknown - requires source verification
- source confidence: UNVERIFIED_PLACEHOLDER

### MCP2562FD

- part number: MCP2562FD
- vendor: Microchip
- family: CAN
- category: 03_COMMUNICATION
- package: Unknown - requires source verification
- KiCad symbol candidates: Unknown - requires source verification
- KiCad footprint candidates: Unknown - requires source verification
- 3D model candidates: Unknown - requires source verification
- datasheet local path: Unknown - requires source verification
- datasheet source URL placeholder: Unknown - requires source verification
- verified status: UNVERIFIED_PLACEHOLDER
- pinout status: UNVERIFIED_PLACEHOLDER
- footprint status: UNVERIFIED_PLACEHOLDER
- layout notes: Verify CAN bus protection, termination, common-mode choke needs, and connector pinout.
- power notes: Unknown - requires source verification
- communication notes: CAN FD details require source verification.
- common mistakes: Confusing logic voltage, bus voltage, standby pins, and termination placement.
- AI warnings: Do not assume CAN transceivers are pin-compatible.
- suitable use cases: Planning placeholder only.
- not suitable use cases: Vehicle or noisy bus design before protection and datasheet review.
- required external parts: Unknown - requires source verification
- reference circuits: Unknown - requires source verification
- known errata: Unknown - requires source verification
- source confidence: UNVERIFIED_PLACEHOLDER

### SN65HVD230

- part number: SN65HVD230
- vendor: Texas Instruments
- family: CAN
- category: 03_COMMUNICATION
- package: Unknown - requires source verification
- KiCad symbol candidates: Unknown - requires source verification
- KiCad footprint candidates: Unknown - requires source verification
- 3D model candidates: Unknown - requires source verification
- datasheet local path: Unknown - requires source verification
- datasheet source URL placeholder: Unknown - requires source verification
- verified status: UNVERIFIED_PLACEHOLDER
- pinout status: UNVERIFIED_PLACEHOLDER
- footprint status: UNVERIFIED_PLACEHOLDER
- layout notes: Verify CAN termination, ESD/TVS needs, mode pins, and package.
- power notes: Unknown - requires source verification
- communication notes: CAN transceiver behavior requires source verification.
- common mistakes: Assuming it is suitable for every CAN or CAN FD design without checking speed and voltage requirements.
- AI warnings: Do not select it for a bus before source verification.
- suitable use cases: Planning placeholder only.
- not suitable use cases: Final CAN interface without datasheet and system requirements review.
- required external parts: Unknown - requires source verification
- reference circuits: Unknown - requires source verification
- known errata: Unknown - requires source verification
- source confidence: UNVERIFIED_PLACEHOLDER

### LM2596

- part number: LM2596
- vendor: Unknown - requires source verification
- family: BUCK_REGULATOR
- category: 02_POWER
- package: Unknown - requires source verification
- KiCad symbol candidates: Unknown - requires source verification
- KiCad footprint candidates: Unknown - requires source verification
- 3D model candidates: Unknown - requires source verification
- datasheet local path: Unknown - requires source verification
- datasheet source URL placeholder: Unknown - requires source verification
- verified status: UNVERIFIED_PLACEHOLDER
- pinout status: UNVERIFIED_PLACEHOLDER
- footprint status: UNVERIFIED_PLACEHOLDER
- layout notes: Verify switching-loop layout, diode/inductor/capacitor selection, thermal path, and package.
- power notes: Unknown - requires source verification
- communication notes: Not applicable unless used near sensitive signals; source verification still required.
- common mistakes: Copying module-board assumptions into a custom switching regulator layout.
- AI warnings: Do not choose passives or layout from memory.
- suitable use cases: Planning placeholder only.
- not suitable use cases: Final power design without datasheet, thermal, and layout review.
- required external parts: Unknown - requires source verification
- reference circuits: Unknown - requires source verification
- known errata: Unknown - requires source verification
- source confidence: UNVERIFIED_PLACEHOLDER

### AMS1117-3.3

- part number: AMS1117-3.3
- vendor: Unknown - requires source verification
- family: LINEAR_REGULATOR
- category: 02_POWER
- package: Unknown - requires source verification
- KiCad symbol candidates: Unknown - requires source verification
- KiCad footprint candidates: Unknown - requires source verification
- 3D model candidates: Unknown - requires source verification
- datasheet local path: Unknown - requires source verification
- datasheet source URL placeholder: Unknown - requires source verification
- verified status: UNVERIFIED_PLACEHOLDER
- pinout status: UNVERIFIED_PLACEHOLDER
- footprint status: UNVERIFIED_PLACEHOLDER
- layout notes: Verify package pinout, thermal dissipation, capacitor requirements, and regulator stability.
- power notes: Unknown - requires source verification
- communication notes: Not applicable.
- common mistakes: Assuming every AMS1117-branded part has the same pinout, stability requirements, or thermal behavior.
- AI warnings: Do not use generic regulator modules as proof for a board-level implementation.
- suitable use cases: Planning placeholder only.
- not suitable use cases: Final power design before source and thermal verification.
- required external parts: Unknown - requires source verification
- reference circuits: Unknown - requires source verification
- known errata: Unknown - requires source verification
- source confidence: UNVERIFIED_PLACEHOLDER

### USB-C 16-Pin Receptacle Generic

- part number: USB-C 16-pin receptacle generic
- vendor: Generic
- family: USB_C_CONNECTOR
- category: 04_CONNECTORS
- package: Unknown - requires source verification
- KiCad symbol candidates: Unknown - requires source verification
- KiCad footprint candidates: Unknown - requires source verification
- 3D model candidates: Unknown - requires source verification
- datasheet local path: Unknown - requires source verification
- datasheet source URL placeholder: Unknown - requires source verification
- verified status: UNVERIFIED_PLACEHOLDER
- pinout status: UNVERIFIED_PLACEHOLDER
- footprint status: UNVERIFIED_PLACEHOLDER
- layout notes: Verify pad map, shell pads, board edge placement, CC role, ESD, shield grounding, and mechanical orientation.
- power notes: Unknown - requires source verification
- communication notes: USB role and speed require source verification.
- common mistakes: Mirroring the connector, using the wrong pin count, or applying the wrong CC resistor role.
- AI warnings: Replace generic record with exact manufacturer part before schematic or PCB work.
- suitable use cases: Placeholder for requirements capture only.
- not suitable use cases: Final connector selection or footprint assignment.
- required external parts: Unknown - requires source verification
- reference circuits: Unknown - requires source verification
- known errata: Unknown - requires source verification
- source confidence: UNVERIFIED_PLACEHOLDER

### U.FL Connector Generic

- part number: U.FL connector generic
- vendor: Generic
- family: RF_CONNECTOR
- category: 04_CONNECTORS
- package: Unknown - requires source verification
- KiCad symbol candidates: Unknown - requires source verification
- KiCad footprint candidates: Unknown - requires source verification
- 3D model candidates: Unknown - requires source verification
- datasheet local path: Unknown - requires source verification
- datasheet source URL placeholder: Unknown - requires source verification
- verified status: UNVERIFIED_PLACEHOLDER
- pinout status: UNVERIFIED_PLACEHOLDER
- footprint status: UNVERIFIED_PLACEHOLDER
- layout notes: Verify exact connector footprint, RF launch, keepout, height, mating connector, and 3D model.
- power notes: Not applicable unless vendor datasheet says otherwise.
- communication notes: RF path and impedance details require source verification.
- common mistakes: Treating U.FL-compatible connectors as footprint-interchangeable.
- AI warnings: Replace generic record with exact manufacturer part before PCB layout.
- suitable use cases: Placeholder for RF connector planning.
- not suitable use cases: Final RF layout or antenna-feed design.
- required external parts: Unknown - requires source verification
- reference circuits: Unknown - requires source verification
- known errata: Unknown - requires source verification
- source confidence: UNVERIFIED_PLACEHOLDER

### SMA Edge Connector Generic

- part number: SMA edge connector generic
- vendor: Generic
- family: RF_CONNECTOR
- category: 04_CONNECTORS
- package: Unknown - requires source verification
- KiCad symbol candidates: Unknown - requires source verification
- KiCad footprint candidates: Unknown - requires source verification
- 3D model candidates: Unknown - requires source verification
- datasheet local path: Unknown - requires source verification
- datasheet source URL placeholder: Unknown - requires source verification
- verified status: UNVERIFIED_PLACEHOLDER
- pinout status: UNVERIFIED_PLACEHOLDER
- footprint status: UNVERIFIED_PLACEHOLDER
- layout notes: Verify exact edge-launch geometry, board thickness, ground stitching, RF launch, and connector orientation.
- power notes: Not applicable unless vendor datasheet says otherwise.
- communication notes: RF path and impedance details require source verification.
- common mistakes: Ignoring board thickness and launch geometry.
- AI warnings: Do not route RF edge launch from generic memory.
- suitable use cases: Placeholder for RF connector planning.
- not suitable use cases: Final RF/mechanical design before exact part verification.
- required external parts: Unknown - requires source verification
- reference circuits: Unknown - requires source verification
- known errata: Unknown - requires source verification
- source confidence: UNVERIFIED_PLACEHOLDER

### Polyfuse Generic

- part number: polyfuse generic
- vendor: Generic
- family: RESETTABLE_FUSE
- category: 05_PROTECTION
- package: Unknown - requires source verification
- KiCad symbol candidates: Unknown - requires source verification
- KiCad footprint candidates: Unknown - requires source verification
- 3D model candidates: Unknown - requires source verification
- datasheet local path: Unknown - requires source verification
- datasheet source URL placeholder: Unknown - requires source verification
- verified status: UNVERIFIED_PLACEHOLDER
- pinout status: UNVERIFIED_PLACEHOLDER
- footprint status: UNVERIFIED_PLACEHOLDER
- layout notes: Verify thermal environment, copper area, clearance, and resettable-fuse derating guidance.
- power notes: Current hold/trip behavior requires exact source verification.
- communication notes: Not applicable.
- common mistakes: Choosing hold current without temperature derating or trip-time review.
- AI warnings: Do not select from generic current rating alone.
- suitable use cases: Placeholder for protection planning.
- not suitable use cases: Final overcurrent protection choice before derating review.
- required external parts: Unknown - requires source verification
- reference circuits: Unknown - requires source verification
- known errata: Unknown - requires source verification
- source confidence: UNVERIFIED_PLACEHOLDER

### TVS Diode Generic

- part number: TVS diode generic
- vendor: Generic
- family: TVS
- category: 05_PROTECTION
- package: Unknown - requires source verification
- KiCad symbol candidates: Unknown - requires source verification
- KiCad footprint candidates: Unknown - requires source verification
- 3D model candidates: Unknown - requires source verification
- datasheet local path: Unknown - requires source verification
- datasheet source URL placeholder: Unknown - requires source verification
- verified status: UNVERIFIED_PLACEHOLDER
- pinout status: UNVERIFIED_PLACEHOLDER
- footprint status: UNVERIFIED_PLACEHOLDER
- layout notes: Verify placement close to connector, ground return path, package, and surge/ESD rating.
- power notes: Working voltage, clamping voltage, and power rating require exact source verification.
- communication notes: Check signal capacitance for high-speed lines.
- common mistakes: Using a TVS with the wrong working voltage or capacitance.
- AI warnings: Do not choose TVS parts without system voltage and transient requirements.
- suitable use cases: Placeholder for protection planning.
- not suitable use cases: Final protection circuit before source and system review.
- required external parts: Unknown - requires source verification
- reference circuits: Unknown - requires source verification
- known errata: Unknown - requires source verification
- source confidence: UNVERIFIED_PLACEHOLDER

### ESD Diode Array Generic

- part number: ESD diode array generic
- vendor: Generic
- family: ESD_ARRAY
- category: 05_PROTECTION
- package: Unknown - requires source verification
- KiCad symbol candidates: Unknown - requires source verification
- KiCad footprint candidates: Unknown - requires source verification
- 3D model candidates: Unknown - requires source verification
- datasheet local path: Unknown - requires source verification
- datasheet source URL placeholder: Unknown - requires source verification
- verified status: UNVERIFIED_PLACEHOLDER
- pinout status: UNVERIFIED_PLACEHOLDER
- footprint status: UNVERIFIED_PLACEHOLDER
- layout notes: Verify channel mapping, ground pin, connector placement, line capacitance, and package orientation.
- power notes: Unknown - requires source verification
- communication notes: Verify suitability for USB, CAN, RF, or other protected interface.
- common mistakes: Swapping protected-line pins or choosing excessive capacitance.
- AI warnings: Do not assign footprint or line mapping without exact datasheet.
- suitable use cases: Placeholder for interface-protection planning.
- not suitable use cases: Final high-speed or RF protection before source verification.
- required external parts: Unknown - requires source verification
- reference circuits: Unknown - requires source verification
- known errata: Unknown - requires source verification
- source confidence: UNVERIFIED_PLACEHOLDER

### 8 MHz Crystal Generic

- part number: 8 MHz crystal generic
- vendor: Generic
- family: CRYSTAL
- category: 09_PASSIVES
- package: Unknown - requires source verification
- KiCad symbol candidates: Unknown - requires source verification
- KiCad footprint candidates: Unknown - requires source verification
- 3D model candidates: Unknown - requires source verification
- datasheet local path: Unknown - requires source verification
- datasheet source URL placeholder: Unknown - requires source verification
- verified status: UNVERIFIED_PLACEHOLDER
- pinout status: UNVERIFIED_PLACEHOLDER
- footprint status: UNVERIFIED_PLACEHOLDER
- layout notes: Verify load capacitance, ESR, drive level, package, guard/ground recommendations, and MCU oscillator requirements.
- power notes: Not applicable unless source says otherwise.
- communication notes: Clock-source suitability requires target IC verification.
- common mistakes: Choosing load capacitors without calculating from crystal and PCB capacitance.
- AI warnings: Do not select crystal or caps from frequency alone.
- suitable use cases: Placeholder for clock planning.
- not suitable use cases: Final oscillator circuit before crystal and MCU datasheet review.
- required external parts: Unknown - requires source verification
- reference circuits: Unknown - requires source verification
- known errata: Unknown - requires source verification
- source confidence: UNVERIFIED_PLACEHOLDER

### 40 MHz Crystal Generic

- part number: 40 MHz crystal generic
- vendor: Generic
- family: CRYSTAL
- category: 09_PASSIVES
- package: Unknown - requires source verification
- KiCad symbol candidates: Unknown - requires source verification
- KiCad footprint candidates: Unknown - requires source verification
- 3D model candidates: Unknown - requires source verification
- datasheet local path: Unknown - requires source verification
- datasheet source URL placeholder: Unknown - requires source verification
- verified status: UNVERIFIED_PLACEHOLDER
- pinout status: UNVERIFIED_PLACEHOLDER
- footprint status: UNVERIFIED_PLACEHOLDER
- layout notes: Verify load capacitance, ESR, drive level, package, guard/ground recommendations, and target-radio or MCU clock requirements.
- power notes: Not applicable unless source says otherwise.
- communication notes: Clock-source suitability requires target IC verification.
- common mistakes: Treating all 40 MHz crystals as interchangeable for RF modules or MCUs.
- AI warnings: Do not select crystal or caps from frequency alone.
- suitable use cases: Placeholder for clock/RF planning.
- not suitable use cases: Final oscillator/RF design before source verification.
- required external parts: Unknown - requires source verification
- reference circuits: Unknown - requires source verification
- known errata: Unknown - requires source verification
- source confidence: UNVERIFIED_PLACEHOLDER
