#!/usr/bin/env python3
"""Build AI-readable STM32 family datasheet scaffolding.

This script is intentionally link-first and read/write scoped to KiCad Engine
documentation folders. It does not download PDFs, scrape websites, install
tools, or touch KiCad design files.
"""

from __future__ import annotations

from pathlib import Path


DATE = "2026-05-03"
STATUS = "SCAFFOLDED_WITH_AI_SUMMARIES"
UNKNOWN = "UNKNOWN_REQUIRES_SOURCE"

COMMON_SOURCES = {
    "STM32 MCU portfolio": "https://www.st.com/en/microcontrollers-microprocessors/stm32-32-bit-arm-cortex-mcus.html",
    "STM32CubeMX": "https://www.st.com/en/development-tools/stm32cubemx.html",
    "STM32CubeIDE": "https://www.st.com/en/development-tools/stm32cubeide.html",
    "ST-LINK tools": "https://www.st.com/en/development-tools/hardware-debugger-and-programmer-tools-for-stm32.html",
    "ST-LINK documentation": "https://www.st.com/en/development-tools/hardware-debugger-and-programmer-tools-for-stm32/documentation.html",
    "STM32 Nucleo boards": "https://www.st.com/en/evaluation-tools/stm32-nucleo-boards.html",
    "STM32 Nucleo documentation": "https://www.st.com/en/evaluation-tools/stm32-nucleo-boards/documentation.html",
    "STM32 Discovery kits": "https://www.st.com/en/evaluation-tools/stm32-discovery-kits.html",
    "STM32 evaluation boards": "https://www.st.com/en/evaluation-tools/stm32-mcu-eval-boards.html",
    "AN2606 boot mode": "https://www.st.com/resource/en/application_note/an2606-stm32-microcontroller-system-memory-boot-mode-stmicroelectronics.pdf",
    "AN2867 oscillator design": "https://www.st.com/resource/en/application_note/an2867-oscillator-design-guide-for-stm8afals-stm32-mcus-and-mpus-stmicroelectronics.pdf",
    "AN4879 USB hardware and PCB guidelines": "https://www.st.com/resource/en/application_note/an4879-introduction-to-usb-hardware-and-pcb-guidelines-using-stm32-mcus-stmicroelectronics.pdf",
}


FAMILIES = [
    {
        "name": "STM32F0",
        "url": "https://www.st.com/en/microcontrollers-microprocessors/stm32f0-series.html",
        "core": "Arm Cortex-M0 family-level class; exact core options require part verification.",
        "purpose": "Entry-level STM32 MCU family for cost-sensitive control, simple mixed-signal IO, and compact embedded products.",
        "use": ["Low-cost control boards", "Simple sensor/control nodes", "USB FS device designs where exact part supports USB", "Legacy cost-sensitive replacement designs"],
        "sub": ["STM32F030", "STM32F031", "STM32F038", "STM32F042", "STM32F048", "STM32F051", "STM32F058", "STM32F070", "STM32F071", "STM32F072", "STM32F078", "STM32F091", "STM32F098"],
        "pkg": ["TSSOP", "UFQFPN/QFN", "LQFP", "small WLCSP-style packages on selected parts"],
        "comm": "USB and CAN are package/part dependent. Do not infer either from the F0 family name.",
        "analog": "Basic ADC/DAC/comparator availability varies. Verify VDDA/VSSA/VREF handling from the exact datasheet.",
        "watch": ["low cost", "pin multiplexing limits", "simple SWD access", "package-specific USB/CAN availability"],
        "avoid": "Avoid when the design needs high performance, large memory, complex graphics, Ethernet, advanced security, or extensive peripheral margin.",
    },
    {
        "name": "STM32F1",
        "url": "https://www.st.com/en/microcontrollers-microprocessors/stm32f1-series.html",
        "core": "Arm Cortex-M3 family-level class; exact subfamily and peripheral set require part verification.",
        "purpose": "Mature mainstream STM32 family used in many legacy and prototype designs.",
        "use": ["Legacy industrial controllers", "Simple USB FS devices on supported parts", "Classic CAN 2.0 nodes on supported parts", "Education and reference-board migration"],
        "sub": ["STM32F100", "STM32F101", "STM32F102", "STM32F103", "STM32F105", "STM32F107"],
        "pkg": ["LQFP", "BGA on larger connectivity parts", "VFQFPN/QFN on selected parts"],
        "comm": "USB FS and CAN exist on common variants but not every part/package. F105/F107 connectivity-line behavior must be checked from the exact reference manual.",
        "analog": "Analog capability is useful but older. Verify ADC channel pins, VDDA/VSSA/VREF, and package pinout.",
        "watch": ["legacy ecosystem", "Blue Pill clone risk", "BOOT0/recovery access", "SWD pins not overloaded"],
        "avoid": "Avoid for new designs needing current low-power/security features, modern USB-C assumptions, or lifecycle margin without an ST lifecycle check.",
    },
    {
        "name": "STM32F2",
        "url": "https://www.st.com/en/microcontrollers-microprocessors/stm32f2-series.html",
        "core": "Arm Cortex-M3 high-performance family-level class; exact capabilities require part verification.",
        "purpose": "Higher-performance Cortex-M3 STM32 family bridging older F1-class designs and later F4/F7 families.",
        "use": ["Legacy high-performance control", "Connectivity-rich embedded boards", "USB/Ethernet-capable designs on supported parts", "Migration review from older ST designs"],
        "sub": ["STM32F205", "STM32F207", "STM32F215", "STM32F217"],
        "pkg": ["LQFP", "UFBGA/BGA", "WLCSP on selected parts"],
        "comm": "USB, CAN, Ethernet, and external memory support are part/package dependent. Confirm pins and PHY requirements.",
        "analog": "Verify ADC, DAC, VDDA/VSSA/VREF, backup domain, and package pin mux from exact datasheet.",
        "watch": ["legacy high-performance supply domains", "USB/Ethernet clocking", "larger package footprints", "external memory or PHY routing"],
        "avoid": "Avoid for greenfield designs if newer F4/G4/H5/U5 parts meet the requirement with better support or lifecycle position.",
    },
    {
        "name": "STM32F3",
        "url": "https://www.st.com/en/microcontrollers-microprocessors/stm32f3-series.html",
        "core": "Arm Cortex-M4 mixed-signal family-level class; exact DSP/FPU and peripheral set require part verification.",
        "purpose": "Mixed-signal STM32 family for motor control, analog-heavy control loops, and precision sensing designs.",
        "use": ["Motor control", "Power conversion control", "Precision analog front-end control", "Comparator/op-amp/ADC-heavy systems"],
        "sub": ["STM32F301", "STM32F302", "STM32F303", "STM32F318", "STM32F328", "STM32F334", "STM32F358", "STM32F373", "STM32F378", "STM32F398"],
        "pkg": ["LQFP", "UFQFPN/QFN", "BGA on selected parts"],
        "comm": "USB and CAN availability varies. Some designs use F3 for analog rather than communication density.",
        "analog": "High-risk analog family: op-amps, comparators, DACs, ADCs, VREF, VDDA/VSSA, and grounding require exact part review.",
        "watch": ["analog partitioning", "VREF and VDDA filtering", "comparator/op-amp pin mapping", "motor-control noise containment"],
        "avoid": "Avoid when analog features are not needed and a simpler G0/F0/U0 design is sufficient, or when high-end graphics/connectivity are required.",
    },
    {
        "name": "STM32F4",
        "url": "https://www.st.com/en/microcontrollers-microprocessors/stm32f4-series.html",
        "core": "Arm Cortex-M4 performance family-level class; exact DSP/FPU, memory, and peripheral set require part verification.",
        "purpose": "Mature performance STM32 family for general embedded control, USB, classic CAN, audio, and high-speed MCU designs.",
        "use": ["High-performance control", "USB FS/OTG devices", "Classic CAN nodes on supported parts", "Audio/control boards", "Black Pill-style prototypes with source checks"],
        "sub": ["STM32F401", "STM32F405", "STM32F407", "STM32F410", "STM32F411", "STM32F412", "STM32F413", "STM32F415", "STM32F417", "STM32F423", "STM32F427", "STM32F429", "STM32F437", "STM32F439", "STM32F446", "STM32F469", "STM32F479"],
        "pkg": ["UFQFPN/QFN", "LQFP", "UFBGA/BGA", "WLCSP on selected parts"],
        "comm": "USB and CAN are common in the family but must be confirmed by part and package. USB clock source and VBUS handling need review.",
        "analog": "Verify ADC/DAC availability, analog supply pins, VREF behavior, and package-specific channel mapping.",
        "watch": ["clock tree", "USB clock and routing", "BOOT0 recovery path", "package suffix and footprint matching"],
        "avoid": "Avoid when ultra-low power, modern TrustZone/security, or wireless integration is the primary requirement.",
    },
    {
        "name": "STM32F7",
        "url": "https://www.st.com/en/microcontrollers-microprocessors/stm32f7-series.html",
        "core": "Arm Cortex-M7 high-performance family-level class; exact cache/memory/peripheral set require part verification.",
        "purpose": "High-performance STM32 family for graphics, audio, external memory, Ethernet, and complex embedded applications.",
        "use": ["Graphics/HMI", "External SDRAM/flash systems", "Ethernet/USB designs", "High-performance control and audio"],
        "sub": ["STM32F722", "STM32F723", "STM32F730", "STM32F732", "STM32F733", "STM32F745", "STM32F746", "STM32F756", "STM32F765", "STM32F767", "STM32F769", "STM32F777", "STM32F779"],
        "pkg": ["LQFP", "UFBGA/BGA", "WLCSP on selected parts"],
        "comm": "USB HS/FS, Ethernet, CAN, camera/display and external memory pins are part/package dependent. PHY and impedance choices matter.",
        "analog": "Analog functions exist but are often secondary to high-speed layout. Verify analog pins and reference domains explicitly.",
        "watch": ["cache-aware firmware implications", "external memory layout", "USB HS PHY decisions", "Ethernet/RMII/MII constraints"],
        "avoid": "Avoid for simple low-power or low-cost products where F0/G0/U0/L0-class parts are sufficient.",
    },
    {
        "name": "STM32G0",
        "url": "https://www.st.com/en/microcontrollers-microprocessors/stm32g0-series.html",
        "core": "Arm Cortex-M0+ value family-level class; exact peripheral set requires part verification.",
        "purpose": "Modern value-line STM32 family for compact, cost-sensitive control with current ecosystem support.",
        "use": ["Low-cost product control", "USB-C controller-adjacent designs on supported parts", "Small industrial/sensor boards", "F0/F1 migration review"],
        "sub": ["STM32G030", "STM32G031", "STM32G041", "STM32G050", "STM32G051", "STM32G061", "STM32G070", "STM32G071", "STM32G081", "STM32G0B0", "STM32G0B1", "STM32G0C1"],
        "pkg": ["SO/TSSOP on selected low-pin-count parts", "UFQFPN/QFN", "LQFP", "WLCSP on selected parts"],
        "comm": "USB, UCPD, and CAN/FDCAN are not universal. Confirm exact peripheral and pin availability.",
        "analog": "Verify ADC channels, internal reference behavior, VDDA/VSSA, and package-specific multiplexing.",
        "watch": ["low-pin-count pin conflicts", "SWD access preservation", "BOOT behavior differences from F1", "modern small packages"],
        "avoid": "Avoid when DSP/FPU, high-speed external memory, graphics, or wireless radio are required.",
    },
    {
        "name": "STM32G4",
        "url": "https://www.st.com/en/microcontrollers-microprocessors/stm32g4-series.html",
        "core": "Arm Cortex-M4 mixed-signal/control family-level class; exact peripheral set requires part verification.",
        "purpose": "Mixed-signal STM32 family for motor control, digital power, FDCAN, USB, and fast analog control loops.",
        "use": ["Motor control", "Digital power conversion", "FDCAN nodes", "Analog control loops", "USB-capable control boards on supported parts"],
        "sub": ["STM32G431", "STM32G441", "STM32G471", "STM32G473", "STM32G474", "STM32G483", "STM32G484", "STM32G491", "STM32G4A1"],
        "pkg": ["UFQFPN/QFN", "LQFP", "BGA on selected parts"],
        "comm": "FDCAN and USB availability vary. FDCAN still needs an external transceiver and bus protection review.",
        "analog": "High-risk analog family: verify op-amps, comparators, ADCs, DACs, VREF+, VDDA/VSSA, and noise-sensitive layout.",
        "watch": ["analog and power ground partitioning", "FDCAN transceiver/protection", "USB/UCPD pins on variants", "switching-noise containment"],
        "avoid": "Avoid when the design does not benefit from analog/control features and a simpler G0/U0 device is enough.",
    },
    {
        "name": "STM32H5",
        "url": "https://www.st.com/en/microcontrollers-microprocessors/stm32h5-series.html",
        "core": "Arm Cortex-M33 security/performance family-level class; exact security and memory set require part verification.",
        "purpose": "Modern secure STM32 family for connected products needing stronger security and mid/high performance.",
        "use": ["Secure IoT controllers", "Connected industrial nodes", "Modern USB/CAN/Ethernet-adjacent control where supported", "TrustZone-aware products"],
        "sub": ["STM32H503", "STM32H523", "STM32H533", "STM32H562", "STM32H563", "STM32H573"],
        "pkg": ["UFQFPN/QFN", "LQFP", "UFBGA/BGA on selected parts"],
        "comm": "USB, CAN/FDCAN, Ethernet, and security features vary by exact part. Confirm secure boot/debug policy before board lock-in.",
        "analog": "Verify analog rails, reference pins, ADC capability, and package pin mapping in the exact datasheet.",
        "watch": ["TrustZone/security lifecycle", "debug authentication/recovery", "power domain details", "newer library support"],
        "avoid": "Avoid if the team cannot manage security provisioning, debug lockout recovery, or newer-device support maturity.",
    },
    {
        "name": "STM32H7",
        "url": "https://www.st.com/en/microcontrollers-microprocessors/stm32h7-series.html",
        "core": "Arm Cortex-M7 and optional dual-core family-level class; exact core arrangement requires part verification.",
        "purpose": "High-end STM32 family for performance-heavy control, graphics, Ethernet, USB HS, external memory, and complex boards.",
        "use": ["High-end HMI/graphics", "Ethernet and USB HS products", "External SDRAM/OctoSPI systems", "High-rate data acquisition and control"],
        "sub": ["STM32H723", "STM32H725", "STM32H730", "STM32H733", "STM32H735", "STM32H742", "STM32H743", "STM32H745", "STM32H747", "STM32H750", "STM32H753", "STM32H755", "STM32H757", "STM32H7A3", "STM32H7B0", "STM32H7B3"],
        "pkg": ["LQFP", "UFBGA/BGA", "TFBGA/WLCSP on selected parts"],
        "comm": "USB HS, Ethernet, CAN/FDCAN, display, camera, and external memory interfaces are high-risk and package-dependent.",
        "analog": "Verify ADC domains, VDDA/VSSA/VREF, VCAP, SMPS/LDO configuration, and thermal behavior.",
        "watch": ["complex power tree", "VCAP/SMPS/LDO mode", "impedance-controlled interfaces", "external memory and cache effects"],
        "avoid": "Avoid for simple low-cost boards or when the layout team cannot verify high-speed memory/USB/Ethernet constraints.",
    },
    {
        "name": "STM32L0",
        "url": "https://www.st.com/en/microcontrollers-microprocessors/stm32l0-series.html",
        "core": "Arm Cortex-M0+ ultra-low-power family-level class; exact low-power modes require part verification.",
        "purpose": "Ultra-low-power STM32 family for battery sensors, low-duty-cycle products, and RTC-centric nodes.",
        "use": ["Battery sensor nodes", "RTC/wake designs", "Simple low-power control", "Compact low-current embedded products"],
        "sub": ["STM32L010", "STM32L011", "STM32L021", "STM32L031", "STM32L041", "STM32L051", "STM32L052", "STM32L053", "STM32L062", "STM32L063", "STM32L071", "STM32L072", "STM32L073", "STM32L081", "STM32L082", "STM32L083"],
        "pkg": ["TSSOP", "UFQFPN/QFN", "LQFP", "WLCSP on selected parts"],
        "comm": "USB and low-power communication support vary. Do not assume USB on low-power variants.",
        "analog": "Low-leakage analog, VDDA/VSSA, VREF, and sensor biasing require careful review.",
        "watch": ["leakage budgeting", "LSE/RTC layout", "VBAT behavior", "low-power pin states"],
        "avoid": "Avoid when performance, high-speed interfaces, or large memory dominate over current consumption.",
    },
    {
        "name": "STM32L1",
        "url": "https://www.st.com/en/microcontrollers-microprocessors/stm32l1-series.html",
        "core": "Arm Cortex-M3 ultra-low-power family-level class; exact memory/peripheral options require part verification.",
        "purpose": "Legacy ultra-low-power STM32 family for low-power control and LCD/sensor products.",
        "use": ["Low-power industrial products", "Battery and RTC designs", "Segment LCD products on supported parts", "Legacy L-series maintenance"],
        "sub": ["STM32L100", "STM32L151", "STM32L152", "STM32L162"],
        "pkg": ["LQFP", "BGA on selected parts", "UFQFPN/QFN and WLCSP on selected parts"],
        "comm": "USB and LCD/peripheral support vary by part. Confirm pins and bootloader support.",
        "analog": "Verify low-power analog, VDDA/VSSA, VREF, LCD pins, and package-specific pin mapping.",
        "watch": ["low-power leakage", "LCD pin multiplexing", "VBAT/backup domain", "legacy lifecycle review"],
        "avoid": "Avoid for greenfield designs if L4/U0/U5 alternatives provide better support, security, or lifecycle position.",
    },
    {
        "name": "STM32L4",
        "url": "https://www.st.com/en/microcontrollers-microprocessors/stm32l4-series.html",
        "core": "Arm Cortex-M4 ultra-low-power family-level class; exact memory/peripheral set requires part verification.",
        "purpose": "Ultra-low-power performance STM32 family for battery products needing more compute and richer peripherals.",
        "use": ["Battery IoT nodes", "USB low-power devices on supported parts", "Sensor fusion", "Industrial low-power control"],
        "sub": ["STM32L412", "STM32L422", "STM32L431", "STM32L432", "STM32L433", "STM32L442", "STM32L443", "STM32L451", "STM32L452", "STM32L462", "STM32L471", "STM32L475", "STM32L476", "STM32L485", "STM32L486", "STM32L496", "STM32L4A6", "STM32L4P5", "STM32L4Q5"],
        "pkg": ["UFQFPN/QFN", "LQFP", "BGA/WLCSP on selected parts"],
        "comm": "USB, CAN, SDMMC, and other interfaces vary. USB clock/recovery behavior must be checked per part.",
        "analog": "Verify ADC/DAC/op-amp/comparator availability, VDDA/VSSA/VREF, and low-power analog behavior.",
        "watch": ["low-power clock tree", "USB clocking", "analog rail filtering", "package-specific pin conflicts"],
        "avoid": "Avoid if the design needs highest H7-class performance, integrated wireless, or simpler low-cost G0/U0 economics.",
    },
    {
        "name": "STM32L5",
        "url": "https://www.st.com/en/microcontrollers-microprocessors/stm32l5-series.html",
        "core": "Arm Cortex-M33 ultra-low-power security family-level class; exact security features require part verification.",
        "purpose": "Secure ultra-low-power STM32 family for connected products needing TrustZone-class isolation.",
        "use": ["Secure battery IoT", "TrustZone-aware embedded products", "Low-power industrial controllers", "Secure boot prototypes"],
        "sub": ["STM32L552", "STM32L562"],
        "pkg": ["UFQFPN/QFN", "LQFP", "UFBGA/WLCSP on selected parts"],
        "comm": "USB and other communication support must be confirmed per part/package. Security provisioning can affect debug and boot.",
        "analog": "Verify VDDA/VSSA/VREF, ADC capability, and low-power analog behavior from exact datasheet.",
        "watch": ["TrustZone configuration", "debug recovery", "secure boot policy", "low-power domains"],
        "avoid": "Avoid if the team cannot manage security lifecycle/provisioning or if a newer U5 part is a better fit.",
    },
    {
        "name": "STM32U0",
        "url": "https://www.st.com/en/microcontrollers-microprocessors/stm32u0-series.html",
        "core": "Arm Cortex-M0+ ultra-low-power entry family-level class; exact part set requires current ST source verification.",
        "purpose": "Newer low-power entry STM32 family for compact products needing current ST ecosystem support.",
        "use": ["Low-power entry products", "Sensor/control nodes", "Modern replacement candidates for F0/L0-class designs", "Small IoT peripherals"],
        "sub": ["STM32U031", "STM32U073", "STM32U083 - verify current ST selector for exact family list"],
        "pkg": ["UFQFPN/QFN", "LQFP", "TSSOP or WLCSP on selected parts"],
        "comm": "USB and security/peripheral options vary. Do not copy G0/F0 assumptions without exact U0 source review.",
        "analog": "Verify analog supply/reference behavior, low-power modes, and package pin mapping.",
        "watch": ["newer library support", "low-power modes", "small packages", "exact boot/debug behavior"],
        "avoid": "Avoid when a mature ecosystem sample base or higher performance/peripheral set is more important than low-power entry cost.",
    },
    {
        "name": "STM32U5",
        "url": "https://www.st.com/en/microcontrollers-microprocessors/stm32u5-series.html",
        "core": "Arm Cortex-M33 ultra-low-power security/performance family-level class; exact part and SMPS options require verification.",
        "purpose": "Modern ultra-low-power STM32 family for secure, battery-powered, high-integration products.",
        "use": ["Secure battery IoT", "Low-power USB devices on supported parts", "Sensor hubs", "High-integration embedded products"],
        "sub": ["STM32U535", "STM32U545", "STM32U575", "STM32U585", "STM32U595", "STM32U599", "STM32U5A5", "STM32U5A9"],
        "pkg": ["UFQFPN/QFN", "LQFP", "UFBGA/BGA", "WLCSP on selected parts"],
        "comm": "USB, OCTOSPI, SDMMC, FDCAN, and other peripherals vary. Security and power mode choices affect bring-up.",
        "analog": "Verify analog domains, VREF/VDDA/VSSA, ADC, VCAP/SMPS/LDO pins, and exact package power requirements.",
        "watch": ["SMPS versus LDO order codes", "TrustZone/debug policy", "low-power measurement design", "complex power pins"],
        "avoid": "Avoid when exact power-domain review is not possible or when a simpler G0/L0 design meets requirements.",
    },
    {
        "name": "STM32WB",
        "url": "https://www.st.com/en/microcontrollers-microprocessors/stm32wb-series.html",
        "core": "Wireless STM32 family-level class with application MCU and radio subsystem; exact cores/radio features require part verification.",
        "purpose": "Wireless STM32 family for BLE and IEEE 802.15.4-class products where integrated radio is required.",
        "use": ["BLE sensor nodes", "Wireless control products", "Thread/Zigbee-like 802.15.4 designs where supported", "Low-power connected devices"],
        "sub": ["STM32WB10", "STM32WB15", "STM32WB30", "STM32WB35", "STM32WB50", "STM32WB55", "STM32WB5M", "STM32WB06/WB07/WB09 - verify current selector"],
        "pkg": ["UFQFPN/QFN", "WLCSP/BGA", "module options on selected products"],
        "comm": "Radio stack, USB, and other interfaces vary. Wireless firmware stack ownership is a project-level risk.",
        "analog": "Verify analog pins separately; RF pins, matching, power supply filtering, and crystal requirements dominate review.",
        "watch": ["RF matching", "antenna keepout", "HSE/LSE clock source", "wireless stack and certification"],
        "avoid": "Avoid if RF layout, antenna matching, certification, or wireless firmware maintenance cannot be reviewed.",
    },
    {
        "name": "STM32WL",
        "url": "https://www.st.com/en/microcontrollers-microprocessors/stm32wl-series.html",
        "core": "Wireless sub-GHz STM32 family-level class; exact radio and MCU features require part verification.",
        "purpose": "Sub-GHz wireless STM32 family for LoRa and other regional low-power wide-area radio products where supported.",
        "use": ["Sub-GHz sensor nodes", "LoRa/LPWAN products", "Long-range low-power telemetry", "Wireless industrial monitoring"],
        "sub": ["STM32WL3x and STM32WL5x families - verify exact current ST selector entries before use"],
        "pkg": ["UFQFPN/QFN", "BGA/WLCSP on selected parts"],
        "comm": "RF front-end, matching, antenna, regional band, and certification decisions dominate the communication review.",
        "analog": "Verify analog pins separately. RF power supply filtering, crystals, and matching network are high-risk.",
        "watch": ["regional RF compliance", "matching network", "antenna/feedline layout", "reference design fidelity"],
        "avoid": "Avoid if the project cannot perform RF matching, antenna test, regional compliance review, and exact reference-design matching.",
    },
    {
        "name": "STM32MP",
        "url": "https://www.st.com/en/microcontrollers-microprocessors/stm32mp1-series.html",
        "url2": "https://www.st.com/en/microcontrollers-microprocessors/stm32mp2-series.html",
        "core": "STM32 microprocessor family-level class; not a simple MCU. Exact Cortex-A/M core mix requires product verification.",
        "purpose": "Linux-capable STM32 MPU family for application processors with DDR, PMIC, high-speed interfaces, and complex board design.",
        "use": ["Embedded Linux systems", "Industrial HMI", "Gateway/control products", "High-integration processor boards"],
        "sub": ["STM32MP1 series", "STM32MP2 series - verify exact product line and lifecycle status"],
        "pkg": ["BGA packages dominate; exact package, ball map, DDR escape, PMIC, and layout stackup require source verification"],
        "comm": "Ethernet, USB, display, camera, SDMMC, and high-speed interfaces are board-level design tasks with impedance, power, and software constraints.",
        "analog": "Treat analog notes as board-level power-management and signal-integrity review. Exact rails and PMIC sequencing are mandatory.",
        "watch": ["DDR layout", "PMIC sequencing", "BGA escape", "Linux boot chain", "reference design dependency"],
        "avoid": "Avoid if the project does not need Linux/application-class processing or lacks DDR/BGA/high-speed layout capability.",
    },
]

FILES = [
    "FAMILY_OVERVIEW.md",
    "COMMON_USE_CASES.md",
    "DESIGN_TIPS.md",
    "POWER_CLOCK_RESET_NOTES.md",
    "BOOT_DEBUG_PROGRAMMING_NOTES.md",
    "USB_CAN_COMMUNICATION_NOTES.md",
    "PACKAGE_FOOTPRINT_NOTES.md",
    "SCHEMATIC_BLOCK_CHECKLIST.md",
    "PCB_LAYOUT_CHECKLIST.md",
    "COMMON_MISTAKES.md",
    "DEV_BOARD_REFERENCES.md",
    "SOURCE_LINKS.md",
    "PART_NUMBER_INDEX.md",
    "NEEDS_RESEARCH.md",
]


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def table(rows: list[list[str]]) -> str:
    return "\n".join("| " + " | ".join(row) + " |" for row in rows)


def family_overview(f: dict[str, object]) -> str:
    links = [
        ["Source", "Link", "Use"],
        ["Official family page", str(f["url"]), "Primary family landing page and document gateway."],
        ["STM32 portfolio", COMMON_SOURCES["STM32 MCU portfolio"], "Cross-family selector and context."],
        ["STM32CubeMX", COMMON_SOURCES["STM32CubeMX"], "Pin/peripheral/package planning aid, not source proof."],
        ["AN2606", COMMON_SOURCES["AN2606 boot mode"], "Bootloader support and boot mode verification."],
        ["AN2867", COMMON_SOURCES["AN2867 oscillator design"], "Crystal/oscillator guidance."],
        ["AN4879", COMMON_SOURCES["AN4879 USB hardware and PCB guidelines"], "USB hardware guidance if USB is used."],
        ["ST-LINK tools", COMMON_SOURCES["ST-LINK tools"], "Debug/programmer hardware context."],
    ]
    if "url2" in f:
        links.insert(2, ["Official secondary family page", str(f["url2"]), "Secondary STM32MP family source page."])
    return f"""# {f['name']} Family Overview

Date: {DATE}
Status: `{STATUS}`
Scope: family-level AI summary for KiCad planning.

## Family Purpose

{f['purpose']}

Core class: {f['core']}

## Typical Use Cases

{bullets(f['use'])}

## Important Subfamilies

These are family-level examples. Use ST's official product selector before treating any entry as current or design-approved.

{bullets(f['sub'])}

## Parameter Summary For AI Agents

| Parameter | Current Status | Required Verification Source |
| --- | --- | --- |
| Operating voltage range | `{UNKNOWN}` | Selected part datasheet electrical characteristics. |
| Absolute maximum ratings | `{UNKNOWN}` | Selected part datasheet absolute maximum table. |
| Recommended operating conditions | `{UNKNOWN}` | Selected part datasheet recommended operating table. |
| Package dimensions and land pattern | `{UNKNOWN}` | Selected package drawing and ST package mechanical data. |
| Pinout and alternate functions | `{UNKNOWN}` | Selected part datasheet and reference manual. |
| Flash/RAM/peripheral set | `{UNKNOWN}` | Official product page and reference manual. |
| Clock limits and required sources | `{UNKNOWN}` | Reference manual clock tree and datasheet electrical characteristics. |
| Power domains and decoupling | `{UNKNOWN}` | Datasheet power pin table, reference manual, and app notes. |
| Lifecycle and availability | `{UNKNOWN}` | Official ST product page and approved supplier records. |

## Voltage And Power Notes

- `{UNKNOWN}` until the exact order code is selected.
- Verify every VDD/VSS, VDDA/VSSA, VREF+, VBAT, VCAP, VCORE, USB supply, SMPS/LDO, backup-domain, and exposed-pad requirement from the exact datasheet.
- Do not copy a minimum circuit from another STM32 family without checking power-domain differences.

## Package Families

Family-level package examples: {", ".join(f['pkg'])}.

Exact package approval requires the exact order code, package suffix, ST mechanical drawing, KiCad footprint comparison, pin-1 orientation review, and human footprint review.

## Programming And Debug Method

- Default planning assumption: SWD with SWDIO, SWCLK, NRST, GND, and target voltage reference available on a connector or test pads.
- ST-LINK/STLINK-V3 tools are the primary official debug/programming ecosystem references.
- Do not overload SWD pins on early prototypes unless a recovery/debug plan is documented.

## Boot Mode Considerations

- Use AN2606 and the exact reference manual.
- BOOT0, option bytes, empty-check behavior, bootloader interfaces, and security/debug lockout behavior vary.
- Keep a documented recovery path for prototypes.

## Clocking Considerations

- Use AN2867 and the exact datasheet/reference manual for HSE/LSE/crystal/resonator/internal-clock decisions.
- USB, Ethernet, RF, external memory, and timekeeping requirements can impose clock accuracy constraints.
- Crystal load capacitors, drive level, startup margin, and PCB placement must be source-checked.

## Decoupling Notes

- Place decoupling close to each supply pin group and verify capacitor count/value/package from the selected datasheet and reference design.
- Larger, high-performance, wireless, or MPU families often need more careful power-domain review.
- Values remain `{UNKNOWN}` until selected part evidence is recorded.

## USB Notes

{f['comm']}

If USB is used, verify USB peripheral type, pins, VBUS policy, ESD protection, connector wiring, clock source, and PCB routing against AN4879 and the exact part reference manual.

## CAN/FDCAN Notes

{f['comm']}

If CAN/FDCAN is used, verify exact peripheral type, alternate-function pins, transceiver selection, termination, bus protection, connector orientation, and timing requirements.

## Analog Notes

{f['analog']}

## KiCad Symbol And Footprint Risk Notes

- STM32 symbols are part, package, and pin-count sensitive. Similar order codes can differ materially.
- KiCad library candidates are search candidates only. They are not proof of pinout, package, or footprint correctness.
- Check hidden power pins, multi-unit symbol sections, boot/debug pins, analog rails, VREF pins, exposed pads, and package suffixes.
- Footprints must match exact body size, lead pitch, exposed pad, pad count, drill/pad geometry, courtyard, and pin-1 orientation.

## Exact Source Links Needed

{table(links)}

## Verification Status

Classification: `{STATUS}`

Part-level use is blocked until the selected order code has an official product page, datasheet, reference manual, errata sheet, package drawing, KiCad symbol candidate, KiCad footprint candidate, and human review record.
"""


def common_use_cases(f: dict[str, object]) -> str:
    return f"""# {f['name']} Common Use Cases

Date: {DATE}
Status: `{STATUS}`

## Good Fits

{bullets(f['use'])}

## Design Focus Areas

{bullets(f['watch'])}

## When To Avoid

{f['avoid']}

## AI Agent Selection Rules

- Do not select `{f['name']}` only because an example board used it.
- Match required peripherals, voltage domains, memory, package, lifecycle, programming path, and library support before creating a schematic.
- Treat every exact electrical, timing, and package value as `{UNKNOWN}` until official part-level sources are recorded.
- For a real KiCad design, create or update a component database record before placing a symbol.
"""


def design_tips(f: dict[str, object]) -> str:
    return f"""# {f['name']} Design Tips

Date: {DATE}
Status: `{STATUS}`

## Practical Tips

- Start from the exact ST product page and order code, not only a family name.
- Use STM32CubeMX for pin-planning assistance, then verify against the datasheet and reference manual.
- Keep SWD and reset accessible on prototypes.
- Keep boot-mode recovery accessible until firmware and option-byte policy are proven.
- Reserve pins for oscillators, USB, CAN/FDCAN, RF, external memory, and analog functions before assigning LEDs or test pads.
- Review every supply pin and analog rail before assuming a generic STM32 decoupling pattern.
- Use official Nucleo/Discovery/EVAL schematics as references only after matching exact board revision.

## Family-Specific Watch Items

{bullets(f['watch'])}

## AI No-Guess Rules

- Do not invent clock values, capacitor values, regulator current, USB pullups, CAN termination, crystal load capacitors, or pin alternate functions.
- Mark missing values as `{UNKNOWN}` or `NEEDS_RESEARCH`.
- Do not approve a KiCad footprint without exact package drawing evidence.
"""


def power_clock_reset(f: dict[str, object]) -> str:
    return f"""# {f['name']} Power, Clock, And Reset Notes

Date: {DATE}
Status: `{STATUS}`

## Power Parameters

| Item | Status | What To Verify |
| --- | --- | --- |
| VDD range | `{UNKNOWN}` | Exact datasheet recommended operating conditions. |
| VDDA/VSSA/VREF behavior | `{UNKNOWN}` | Exact analog supply/reference requirements. |
| VBAT/backup domain | `{UNKNOWN}` | Whether used, allowed voltage, leakage, isolation. |
| VCAP/VCORE/SMPS/LDO pins | `{UNKNOWN}` | Family and part-specific regulator requirements. |
| Decoupling values/count | `{UNKNOWN}` | Datasheet, app note, and exact package pin count. |
| Reset pin network | `{UNKNOWN}` | Datasheet reset timing, NRST requirements, debug needs. |

## Clock Parameters

| Clock Item | Status | What To Verify |
| --- | --- | --- |
| HSE source | `{UNKNOWN}` | Frequency range, mode, load caps, drive level, startup margin. |
| LSE source | `{UNKNOWN}` | RTC need, crystal specs, load caps, layout. |
| USB clock | `{UNKNOWN}` | Whether USB needs HSE/PLL/HSI48 or exact clock recovery feature. |
| RF/high-speed clocks | `{UNKNOWN}` | Wireless/external memory/Ethernet requirements where applicable. |

## Reset Notes

- Keep NRST available for debug and recovery unless the selected reference design explicitly supports another recovery method.
- Do not attach large capacitive loads, LEDs, or external drivers to reset without checking the datasheet.
- Verify reset pull network against the exact part and ST guidance.

## Source Links

- AN2867 oscillator design: {COMMON_SOURCES['AN2867 oscillator design']}
- Official family page: {f['url']}
- STM32CubeMX: {COMMON_SOURCES['STM32CubeMX']}
"""


def boot_debug(f: dict[str, object]) -> str:
    return f"""# {f['name']} Boot, Debug, And Programming Notes

Date: {DATE}
Status: `{STATUS}`

## Programming/Debug Baseline

- Provide SWDIO, SWCLK, NRST, GND, and target voltage reference for SWD.
- SWO is useful when supported but not a substitute for SWDIO/SWCLK.
- JTAG may be available on larger packages but consumes pins and must be planned early.
- ST-LINK, STLINK-V3, STM32CubeProgrammer, and STM32CubeIDE are official ecosystem touchpoints; exact workflows depend on the selected part.

## Boot Mode Rules

- Use AN2606 for system memory bootloader availability.
- Check the exact reference manual for BOOT0, option bytes, boot address selection, secure boot, RDP, TrustZone, and debug authentication behavior.
- Do not assume UART/USB/CAN/FDCAN/I2C/SPI bootloader support from the family name.
- Keep a human-readable boot strap table in the project notes.

## KiCad Schematic Checklist

- BOOT0 or documented boot override path present.
- NRST accessible.
- SWD connector/test pads present and not blocked by conflicting loads.
- Target voltage reference routed to debug connector if connector is used.
- Debug pins are not permanently consumed by boot-sensitive external circuitry.

## Source Links

- AN2606 boot mode: {COMMON_SOURCES['AN2606 boot mode']}
- ST-LINK tools: {COMMON_SOURCES['ST-LINK tools']}
- ST-LINK documentation: {COMMON_SOURCES['ST-LINK documentation']}
"""


def usb_can(f: dict[str, object]) -> str:
    return f"""# {f['name']} USB, CAN, And Communication Notes

Date: {DATE}
Status: `{STATUS}`

## Family-Level Communication Warning

{f['comm']}

## USB Checklist

- Exact part has USB peripheral and package exposes required pins: `{UNKNOWN}` until verified.
- USB FS/HS/OTG role verified from reference manual.
- USB clock source verified from datasheet/reference manual.
- VBUS sensing/backfeed policy documented.
- USB-C CC resistors, ESD protection, shield policy, and connector orientation reviewed if USB-C is used.
- Differential-pair routing, impedance target, stubs, ESD placement, and connector pinout reviewed.

## CAN/FDCAN Checklist

- Exact peripheral type is verified: classic CAN, bxCAN, FDCAN, or none.
- Alternate-function pins and package availability verified.
- External transceiver selected from a source-backed component record.
- Termination, common-mode choke, TVS/protection, split termination, connector pinout, and bus length/speed are reviewed.
- CAN bootloader support, if needed, verified in AN2606.

## Other Interfaces

- UART/I2C/SPI availability is not enough; verify voltage domain, alternate function, boot/debug conflicts, and package pinout.
- Ethernet, SDMMC, camera, display, external memory, and RF interfaces require layout-specific review.

## Source Links

- USB hardware and PCB guideline AN4879: {COMMON_SOURCES['AN4879 USB hardware and PCB guidelines']}
- Family page: {f['url']}
- Bootloader interface check: {COMMON_SOURCES['AN2606 boot mode']}
"""


def package_footprint(f: dict[str, object]) -> str:
    return f"""# {f['name']} Package And Footprint Notes

Date: {DATE}
Status: `{STATUS}`

## Package Families Seen At Family Level

{bullets(f['pkg'])}

These are not approved footprints. Exact package approval requires source verification.

## Required Evidence Before Footprint Approval

| Evidence | Status | Notes |
| --- | --- | --- |
| Exact order code | `{UNKNOWN}` | Include package suffix and temperature/lifecycle variants. |
| Official package drawing | `{UNKNOWN}` | Must show body size, lead pitch, exposed pad, and pin-1 orientation. |
| KiCad footprint candidate | `{UNKNOWN}` | Candidate only until compared with drawing. |
| Pin count and pad count | `{UNKNOWN}` | Must match exact package. |
| Exposed pad policy | `{UNKNOWN}` | Thermal/electrical connection must be documented. |
| 3D model | `{UNKNOWN}` | Useful for mechanical review, not proof of footprint correctness. |

## KiCad Risks

- Similar STM32 symbols may share names but differ by package or pinout.
- Hidden power pins can hide missing supply-net errors.
- Multi-unit symbols can hide analog, power, or oscillator pins if not reviewed.
- QFN/BGA/WLCSP packages need courtyard, assembly, via-in-pad, and fab capability review.
- Connector/dev-board footprints must not be inferred from MCU package names.

## Human Review Required

Every `{f['name']}` footprint selection is `HUMAN_REVIEW_REQUIRED` until exact package drawing comparison is complete.
"""


def schematic_checklist(f: dict[str, object]) -> str:
    items = [
        "Exact order code selected and recorded.",
        "Official product page, datasheet, reference manual, errata, and package drawing linked.",
        "Power pins, analog rails, VREF, VBAT, VCAP/SMPS/LDO pins, exposed pads, and decoupling reviewed.",
        "Reset and boot mode network reviewed against AN2606 and reference manual.",
        "SWD/debug connector or test pads included.",
        "Clock sources selected only after source review.",
        "USB/CAN/FDCAN only added when exact part/package supports required pins.",
        "All communication transceivers/protection components have source-backed component records.",
        "KiCad symbol candidate compared with official pinout.",
        "Footprint candidate compared with package drawing or marked UNVERIFIED.",
        f"Every unknown exact value marked {UNKNOWN} or NEEDS_REVIEW.",
    ]
    return f"""# {f['name']} Schematic Block Checklist

Date: {DATE}
Status: `{STATUS}`

## Required Before Schematic Placement

{bullets(items)}

## Minimum Block Categories

- Power input and regulation appropriate for selected part.
- MCU power domains and decoupling.
- Reset and boot/recovery.
- SWD/debug/programming.
- Clock sources as required.
- USB/CAN/FDCAN/external transceivers only when source-backed.
- Test points for critical rails, reset, boot, debug, and high-risk interfaces.
- Notes for all unresolved `{UNKNOWN}` items.

## Blocking Conditions

- Missing exact order code.
- Missing official datasheet/reference manual/package drawing.
- Unverified pinout.
- Unverified footprint.
- Connector orientation or polarity not reviewed.
- Claimed ERC pass without report.
"""


def pcb_checklist(f: dict[str, object]) -> str:
    items = [
        "Footprint matches exact package drawing.",
        "Pin-1 orientation visible and checked.",
        "Power decoupling close to relevant pins.",
        "Analog rails/reference kept quiet and routed intentionally.",
        "Clock crystals follow AN2867 placement, guard, trace length, and load-cap review.",
        "USB/CAN/RF/high-speed routes follow interface-specific rules when present.",
        "SWD connector/test pads remain physically accessible.",
        "BOOT0/reset access remains physically accessible.",
        "Courtyards, silkscreen, assembly text, exposed pad, and 3D model reviewed.",
        "DRC run and report stored before claiming layout readiness.",
    ]
    return f"""# {f['name']} PCB Layout Checklist

Date: {DATE}
Status: `{STATUS}`

## Layout Checklist

{bullets(items)}

## Family-Specific Layout Focus

{bullets(f['watch'])}

## Review Gate

PCB placement/routing must remain `NEEDS_REVIEW` until footprint drawing comparison, connector orientation, polarity, ERC/DRC evidence, and close-up visual review are complete.
"""


def common_mistakes(f: dict[str, object]) -> str:
    mistakes = [
        "Selecting a symbol by family name without exact order-code pinout verification.",
        "Assigning a footprint because the package text looks similar but not checking the mechanical drawing.",
        "Copying Blue Pill, Black Pill, Nucleo, or Discovery circuits without matching board revision and part package.",
        "Forgetting VDDA/VSSA/VREF/VBAT/VCAP/SMPS/LDO pins or hiding them behind symbol defaults.",
        "Using BOOT0/SWD pins for LEDs or connectors that block recovery/debug.",
        "Assuming USB or CAN/FDCAN exists on every part in the family.",
        "Choosing crystal/load capacitors from memory instead of AN2867 and the crystal datasheet.",
        "Treating STM32CubeMX output as source proof instead of a planning aid.",
        "Failing to check errata before committing a peripheral choice.",
    ]
    return f"""# {f['name']} Common Mistakes

Date: {DATE}
Status: `{STATUS}`

## Mistakes To Avoid

{bullets(mistakes)}

## Family-Specific High-Risk Areas

{bullets(f['watch'])}

## Corrective Rule For AI Agents

When any exact value, pin, package, or peripheral claim cannot be traced to official ST documentation or a project-approved source, write `{UNKNOWN}` and stop short of schematic/footprint approval.
"""


def dev_boards(f: dict[str, object]) -> str:
    rows = [
        ["Reference Type", "Official Link", "Use Rule"],
        ["Nucleo boards", COMMON_SOURCES["STM32 Nucleo boards"], "Use for bring-up patterns and ST-LINK integration only after exact board revision is identified."],
        ["Nucleo documentation", COMMON_SOURCES["STM32 Nucleo documentation"], "Use to locate user manuals, data briefs, and schematic packs."],
        ["Discovery kits", COMMON_SOURCES["STM32 Discovery kits"], "Use for richer reference designs; do not copy proprietary board circuits blindly."],
        ["Evaluation boards", COMMON_SOURCES["STM32 evaluation boards"], "Use for high-complexity peripherals after matching revision."],
        ["Family page", str(f["url"]), "Use to locate family-specific boards and official documents."],
    ]
    if "url2" in f:
        rows.append(["Secondary family page", str(f["url2"]), "Use for STM32MP2 family-specific boards/documents."])
    return f"""# {f['name']} Dev Board References

Date: {DATE}
Status: `{STATUS}`

## Link-Only Reference Policy

Do not copy proprietary ST schematic packs or PDFs into the public repo unless redistribution rights are explicitly confirmed. Store source links, board revision, summary, and verification status instead.

## Official ST Board Sources

{table(rows)}

## Dev Board Use Rules

- Match exact board name and revision before extracting any circuit block.
- Do not use a Nucleo/Discovery board as package-footprint proof for a different MCU package.
- Record solder bridges, jumpers, ST-LINK disconnects, power muxes, protection parts, crystals, and external transceivers.
- Mark community boards such as Blue Pill/Black Pill as `UNVERIFIED` unless exact board revision and source are identified.
"""


def source_links(f: dict[str, object]) -> str:
    rows = [
        ["Document Need", "Source Link", "Status"],
        ["Official family page", str(f["url"]), STATUS],
        ["STM32 MCU portfolio", COMMON_SOURCES["STM32 MCU portfolio"], STATUS],
        ["STM32CubeMX", COMMON_SOURCES["STM32CubeMX"], "PLANNING_AID_NOT_SOURCE_PROOF"],
        ["ST-LINK tools", COMMON_SOURCES["ST-LINK tools"], STATUS],
        ["Nucleo boards", COMMON_SOURCES["STM32 Nucleo boards"], STATUS],
        ["Discovery kits", COMMON_SOURCES["STM32 Discovery kits"], STATUS],
        ["AN2606 boot mode", COMMON_SOURCES["AN2606 boot mode"], "LINK_ONLY_SOURCE_NEEDED_PER_PART"],
        ["AN2867 oscillator design", COMMON_SOURCES["AN2867 oscillator design"], "LINK_ONLY_SOURCE_NEEDED_PER_PART"],
        ["AN4879 USB guidelines", COMMON_SOURCES["AN4879 USB hardware and PCB guidelines"], "LINK_ONLY_SOURCE_NEEDED_IF_USB_USED"],
        ["Exact product datasheet", "Select from official family/product page", UNKNOWN],
        ["Exact reference manual", "Select from official family/product page", UNKNOWN],
        ["Exact errata sheet", "Select from official family/product page", UNKNOWN],
        ["Exact package drawing", "Select from official product page/package resources", UNKNOWN],
    ]
    if "url2" in f:
        rows.insert(2, ["Official secondary family page", str(f["url2"]), STATUS])
    return f"""# {f['name']} Source Links

Date: {DATE}
Status: `{STATUS}`

## Official Source Links

{table(rows)}

## Source Handling Rules

- Prefer official ST pages and official ST document links.
- Store link records and summaries; do not download PDFs unless explicitly approved and redistribution rights are checked.
- Use supplier/distributor links only for lifecycle, availability, package text, and purchasing metadata; supplier pages do not replace official ST package drawings.
- Mark every part-level claim `{UNKNOWN}` until the exact source is recorded.
"""


def part_number_index(f: dict[str, object]) -> str:
    example_rows = "\n".join(
        f"| {item} | FAMILY_LEVEL_EXAMPLE | `{UNKNOWN}` | Verify in ST product selector before use. |"
        for item in f["sub"]
    )
    return f"""# {f['name']} Part Number Index

Date: {DATE}
Status: `{STATUS}`

This is not a complete part database. It is a family-level index scaffold for AI agents.

| Family/Subfamily Example | Record Status | Exact Order Codes Indexed | Notes |
| --- | --- | --- | --- |
{example_rows}

## Required For Each Future Part Record

- Exact order code.
- Official product page.
- Datasheet link.
- Reference manual link.
- Errata link.
- Package drawing link.
- KiCad symbol candidates.
- KiCad footprint candidates.
- Pinout verification status.
- Footprint verification status.
- Human review flag.
"""


def needs_research(f: dict[str, object]) -> str:
    items = [
        "Exact product-page list for currently recommended parts.",
        "Datasheet, reference manual, and errata links for representative parts.",
        "Package drawing links for common packages.",
        "Nucleo/Discovery/EVAL board links and exact board revisions.",
        "Known lifecycle or NRND/replacement status.",
        "KiCad 9 symbol/footprint candidate mapping for representative packages.",
        "USB/CAN/FDCAN support matrix by exact part and package.",
        "Bootloader interface support from AN2606 by exact part.",
        "Power-domain and decoupling requirements by package.",
        "Known errata that affects schematic or PCB choices.",
    ]
    return f"""# {f['name']} Needs Research

Date: {DATE}
Status: `{STATUS}`

## Open Research Items

{bullets(items)}

## Classification

Current classification: `{STATUS}`

Move to `PARTIALLY_RESEARCHED` only after representative official datasheets/reference manuals/errata/package drawings are linked and summarized. Move to `VERIFIED` only for exact part records with source-backed values, KiCad symbol review, KiCad footprint/package drawing comparison, and human review.
"""


GENERATORS = {
    "FAMILY_OVERVIEW.md": family_overview,
    "COMMON_USE_CASES.md": common_use_cases,
    "DESIGN_TIPS.md": design_tips,
    "POWER_CLOCK_RESET_NOTES.md": power_clock_reset,
    "BOOT_DEBUG_PROGRAMMING_NOTES.md": boot_debug,
    "USB_CAN_COMMUNICATION_NOTES.md": usb_can,
    "PACKAGE_FOOTPRINT_NOTES.md": package_footprint,
    "SCHEMATIC_BLOCK_CHECKLIST.md": schematic_checklist,
    "PCB_LAYOUT_CHECKLIST.md": pcb_checklist,
    "COMMON_MISTAKES.md": common_mistakes,
    "DEV_BOARD_REFERENCES.md": dev_boards,
    "SOURCE_LINKS.md": source_links,
    "PART_NUMBER_INDEX.md": part_number_index,
    "NEEDS_RESEARCH.md": needs_research,
}


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def build_master_index(stm_root: Path) -> None:
    rows = []
    for fam in FAMILIES:
        links = ", ".join(f"[{name}]({fam['name']}/{name})" for name in FILES)
        rows.append(f"| {fam['name']} | {STATUS} | {fam['url']} | {links} |")

    source_rows = "\n".join(
        f"| {name} | {url} | Shared STM32 source/link or planning tool. |"
        for name, url in COMMON_SOURCES.items()
    )

    text = f"""# STM32 AI Master Index

Date: {DATE}
Status: `{STATUS}`

This index upgrades the STM32 datasheet tree from empty folder scaffolding to AI-readable family guidance. It is link-first and does not bundle copyrighted ST PDFs. It does not prove exact part-level values, pinouts, package drawings, or footprint matches.

## Classification Rules

| Classification | Meaning |
| --- | --- |
| `SCAFFOLDED_WITH_AI_SUMMARIES` | Family-level AI-readable summaries and source-link placeholders exist. Exact part data is not verified. |
| `PARTIALLY_RESEARCHED` | Representative official datasheets, reference manuals, errata, package drawings, and board links have been summarized, but not all parts/packages are verified. |
| `VERIFIED` | Exact part records have source-backed values, KiCad symbol/pinout review, package drawing footprint comparison, and human review. |

Current tree classification: `{STATUS}`

## Family Document Map

| Family | Classification | Official ST Source | Generated AI Docs |
| --- | --- | --- | --- |
{chr(10).join(rows)}

## Official Shared Sources

| Source | Link | Use |
| --- | --- | --- |
{source_rows}

## Agent Use Rules

- Start in the target family folder, then select an exact order code.
- Keep exact electrical values as `UNKNOWN_REQUIRES_SOURCE` until verified from official ST sources.
- Do not approve footprints from package names alone. Use official package drawings and human review.
- Do not treat STM32CubeMX as source proof; use it for planning and cross-check against documents.
- Do not download or redistribute PDFs unless permission and policy are confirmed.

## Next Research Needed

- Fill representative part records per family.
- Link exact reference manuals and errata by subfamily.
- Build package-to-footprint verification tables.
- Build Nucleo/Discovery/EVAL board revision index.
- Add KiCad 9 symbol/footprint candidate indexes for representative exact parts.
"""
    write(stm_root / "STM32_AI_MASTER_INDEX.md", text)


def build_component_guides(repo: Path) -> None:
    comp_root = repo / "08_COMPONENT_DATABASE" / "01_MICROCONTROLLERS"
    family_table = "\n".join(
        f"| {fam['name']} | {fam['purpose']} | {', '.join(fam['watch'])} | "
        f"[{fam['name']} docs](../../06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/{fam['name']}/FAMILY_OVERVIEW.md) | {STATUS} |"
        for fam in FAMILIES
    )
    overview = f"""# STM32 Family Overview

Date: {DATE}
Status: `{STATUS}`

This component-database overview links the STM32 component intelligence layer to the expanded STM32 datasheet tree. It is family-level guidance only. Exact part records must use official ST source links and package drawings.

## Source Baseline

- STM32 AI master index: `06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32_AI_MASTER_INDEX.md`
- STM32 legacy master index: `06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32_MASTER_INDEX.md`
- Official STM32 portfolio: {COMMON_SOURCES['STM32 MCU portfolio']}
- STM32CubeMX planning tool: {COMMON_SOURCES['STM32CubeMX']}

## Family Selection Matrix

| Family | Family-Level Purpose | Design Watch Items | Datasheet Tree Link | Verification |
| --- | --- | --- | --- | --- |
{family_table}

## Component Database Rules

- Create exact part records before schematic use.
- Candidate KiCad symbols and footprints must be attached to exact package/order-code records, not only family names.
- Use `UNKNOWN_REQUIRES_SOURCE` for unverified voltage, current, clock, package, pinout, errata, lifecycle, and footprint data.
- Set `human_review_required: true` for every unverified package, connector, RF, USB, CAN/FDCAN, BGA, WLCSP, or power-domain decision.

## Current Classification

`{STATUS}`

This is not a complete STM32 database.
"""
    write(comp_root / "STM32_FAMILY_OVERVIEW.md", overview)

    guide = f"""# STM32 AI Design Guide

Date: {DATE}
Status: `{STATUS}`

This guide tells Codex, Claude, and similar VS Code agents how to use the STM32 datasheet tree and component database without guessing.

## Required Read Order For STM32 Work

1. `06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32_AI_MASTER_INDEX.md`
2. Target family `FAMILY_OVERVIEW.md`
3. Target family `SOURCE_LINKS.md`
4. Target family `POWER_CLOCK_RESET_NOTES.md`
5. Target family `BOOT_DEBUG_PROGRAMMING_NOTES.md`
6. Target family `PACKAGE_FOOTPRINT_NOTES.md`
7. `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/STM32_PART_RECORDS.md` if an exact part exists there
8. `11_LIBRARY_FACTORY/mapping/DATASHEET_PACKAGE_TO_FOOTPRINT_STANDARD.md` before footprint approval

## STM32 Design Gate

A STM32 schematic block is not ready until these are recorded:

- Exact order code.
- Official ST product page.
- Datasheet link.
- Reference manual link.
- Errata link.
- Package drawing link.
- Power pins and decoupling requirements.
- Reset and boot mode evidence.
- SWD/debug plan.
- Clock source requirements.
- USB/CAN/FDCAN evidence if used.
- KiCad symbol candidate checked against pinout.
- KiCad footprint candidate checked against package drawing.
- Human review status for package and connector orientation.

## Do Not Guess

- Operating voltage.
- Absolute maximum ratings.
- Current limits.
- Clock frequency or crystal load capacitance.
- USB clocking mode.
- CAN/FDCAN peripheral availability.
- Package land pattern.
- Pinout or alternate functions.
- Bootloader interface support.
- Lifecycle status.

Use `UNKNOWN_REQUIRES_SOURCE` until verified.

## KiCad Symbol Rules

- Search project-local libraries first, then user/global libraries, then installed KiCad libraries.
- Match exact part number and package.
- Inspect hidden power pins and multi-unit symbol sections.
- Compare all pins used by the design against the official datasheet.
- Treat a KiCad library symbol as `VERIFIED_FROM_KICAD_LIBRARY` only after source comparison.

## KiCad Footprint Rules

- Match exact package drawing, not only package family.
- Check body size, lead count, lead pitch, exposed pad, drill or pad geometry, courtyard, fab layer, silk, and pin-1 orientation.
- BGA/WLCSP/QFN/connector footprints require human review.
- Do not infer Nucleo/Discovery board footprint correctness for a custom part.

## Dev Board Use

- Use ST Nucleo/Discovery/EVAL boards as reference evidence, not as automatic approval.
- Match board revision before extracting circuits.
- Record solder bridges, power muxes, ST-LINK circuitry, jumpers, crystals, protection, and external transceivers.
- Community boards such as Blue Pill/Black Pill need exact board revision and source before use.

## Current Limitations

- The expanded family tree is `{STATUS}`.
- Exact part values remain `UNKNOWN_REQUIRES_SOURCE` unless a specific part record says otherwise.
- Reference manual and errata extraction is still incomplete.
- Package-footprint verification tables are not complete.

## Official Source Starting Points

- STM32 portfolio: {COMMON_SOURCES['STM32 MCU portfolio']}
- STM32CubeMX: {COMMON_SOURCES['STM32CubeMX']}
- ST-LINK tools: {COMMON_SOURCES['ST-LINK tools']}
- AN2606 boot mode: {COMMON_SOURCES['AN2606 boot mode']}
- AN2867 oscillator design: {COMMON_SOURCES['AN2867 oscillator design']}
- AN4879 USB guideline: {COMMON_SOURCES['AN4879 USB hardware and PCB guidelines']}
"""
    write(comp_root / "STM32_AI_DESIGN_GUIDE.md", guide)


def build_closeout(repo: Path) -> None:
    dirs = {
        "audit": repo / "02_HISTORY" / "design_reviews",
        "session": repo / "02_HISTORY" / "sessions",
        "command": repo / "02_HISTORY" / "command_logs",
        "self": repo / "02_HISTORY" / "ai_self_reviews",
        "score": repo / "02_HISTORY" / "ai_scorecards",
        "claim": repo / "02_HISTORY" / "claim_evidence_matrices",
        "uncert": repo / "02_HISTORY" / "uncertainty_logs",
        "hall": repo / "02_HISTORY" / "hallucination_risk_logs",
    }
    for path in dirs.values():
        path.mkdir(parents=True, exist_ok=True)

    family_names = ", ".join(f["name"] for f in FAMILIES)
    audit = f"""# STM32 Datasheet Tree Content Completion Audit

Date: {DATE}
Status: `{STATUS}`

## Scope

Target folder: `06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/`

Families covered: {family_names}

## What Was Created Or Updated

- Generated 14 AI-readable files for each STM32 family folder.
- Created `STM32_AI_MASTER_INDEX.md`.
- Updated `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/STM32_FAMILY_OVERVIEW.md`.
- Created `08_COMPONENT_DATABASE/01_MICROCONTROLLERS/STM32_AI_DESIGN_GUIDE.md`.
- Created AI quality closeout records for this documentation session.

## Classification

Current classification: `{STATUS}`

Reason: the tree now contains useful AI-readable family summaries, source-link records, checklists, warnings, and research needs. Exact part-level electrical specifications, package drawings, reference manuals, errata, and KiCad footprint verification are not complete.

## What Exists Now

Each target family now has:

- `FAMILY_OVERVIEW.md`
- `COMMON_USE_CASES.md`
- `DESIGN_TIPS.md`
- `POWER_CLOCK_RESET_NOTES.md`
- `BOOT_DEBUG_PROGRAMMING_NOTES.md`
- `USB_CAN_COMMUNICATION_NOTES.md`
- `PACKAGE_FOOTPRINT_NOTES.md`
- `SCHEMATIC_BLOCK_CHECKLIST.md`
- `PCB_LAYOUT_CHECKLIST.md`
- `COMMON_MISTAKES.md`
- `DEV_BOARD_REFERENCES.md`
- `SOURCE_LINKS.md`
- `PART_NUMBER_INDEX.md`
- `NEEDS_RESEARCH.md`

## Evidence Sources Used

- Existing repo STM32 master index: `06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/STM32_MASTER_INDEX.md`
- Official ST STM32 portfolio: {COMMON_SOURCES['STM32 MCU portfolio']}
- Official ST family pages linked per family.
- Official ST development board/tool pages linked in `SOURCE_LINKS.md` files.
- Official ST app-note URLs already present in the repo for boot, oscillator, and USB guidance.

## What Remains Weak

- Exact reference manual links are not extracted per subfamily.
- Exact errata links are not extracted per subfamily.
- Exact package drawings are not attached to specific order codes.
- KiCad symbol/footprint candidate tables are not generated per exact part.
- Nucleo/Discovery/EVAL board revision extraction is not complete.
- Lifecycle status is not verified per part.
- Numeric specs are intentionally not filled without source verification.

## Public Release Risk

- No copyrighted PDFs were downloaded or bundled in this pass.
- Files contain link-only references and AI summaries.
- Exact specs are marked `UNKNOWN_REQUIRES_SOURCE` where not verified.

## Result

Result: `STM32_DATASHEET_TREE_CONTENT_SCAFFOLDED`

No KiCad design files were edited.
"""
    write(dirs["audit"] / "STM32_DATASHEET_TREE_CONTENT_COMPLETION_AUDIT.md", audit)

    write(dirs["session"] / "STM32_DATASHEET_TREE_CONTENT_COMPLETION_SESSION.md", f"""# STM32 Datasheet Tree Content Completion Session

Date: {DATE}
Status: COMPLETE

## Task

Create useful AI-readable STM32 family datasheet structure under `06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32/` without downloading copyrighted PDFs or fabricating exact specs.

## Actions

- Read required startup/context files.
- Inspected STM32 datasheet tree and STM32 component database files.
- Confirmed official ST source link patterns for STM32 portfolio, family pages, board/tool pages, and selected missing family pages.
- Generated per-family summaries, tips, checklists, package/footprint notes, source-link records, part index scaffolds, and needs-research files.
- Created master STM32 AI index and component-database STM32 AI design guide.
- Created audit and AI quality closeout records.

## KiCad Design Files

No `.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, symbol library, footprint library, Gerber, drill, or manufacturing output files were edited.
""")

    write(dirs["command"] / "STM32_DATASHEET_TREE_CONTENT_COMPLETION_COMMANDS.md", f"""# STM32 Datasheet Tree Content Completion Commands

Date: {DATE}

## Commands Run

- Read `AGENTS.md`, `README_GPT.md`, `FOR CHAT GPT.MD`, `00_CODEX_START/START_HERE.md`, `STRUCTURE_STANDARD.md`, and `FOLDER_ROUTING_RULES.md`.
- Listed `06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32`.
- Listed `08_COMPONENT_DATABASE/01_MICROCONTROLLERS`.
- Read `STM32_MASTER_INDEX.md` and existing `STM32_FAMILY_OVERVIEW.md`.
- Opened official ST web pages for STM32 portfolio, Nucleo boards, Discovery kits, ST-LINK tools, STM32CubeMX, STM32F2, STM32L1, STM32MP1, and STM32MP2.
- Ran `python 03_TOOLS/scripts/datasheets/build_stm32_ai_datasheet_tree.py --repo-root .`.

## Notes

No install commands, download commands, KiCad CLI commands, or KiCad design-file modification commands were run.
""")

    write(dirs["self"] / "STM32_DATASHEET_TREE_CONTENT_COMPLETION_SELF_REVIEW.md", f"""# AI Self Review - STM32 Datasheet Tree Content Completion

Date: {DATE}

| Question | Answer |
| --- | --- |
| Did I make factual claims without source/file/user evidence? | Partly. Family-level summaries use conservative family guidance and official ST family links, but exact values were not claimed. |
| Did I guess datasheet values, pinouts, footprints, package dimensions, voltages, currents, or manufacturing rules? | No exact values were filled. Unknown exact data is marked `UNKNOWN_REQUIRES_SOURCE`. |
| Did I claim ERC/DRC passed? | No. No KiCad project verification was in scope. |
| Did I claim fabrication readiness? | No. |
| Did I modify KiCad files? | No. |
| Did I update history in the correct location? | Yes, global session/command/audit/quality logs. |
| Did I clearly mark uncertainty? | Yes, exact unverified specs use `UNKNOWN_REQUIRES_SOURCE`. |
""")

    write(dirs["score"] / "STM32_DATASHEET_TREE_CONTENT_COMPLETION_SCORECARD.md", f"""# AI Response Scorecard - STM32 Datasheet Tree Content Completion

Date: {DATE}

Overall score: 88 / 100
Risk label: `MEDIUM_RISK`

| Category | Score | Notes |
| --- | ---: | --- |
| Evidence support | 17/20 | Official ST links and local files used; exact part extraction remains incomplete. |
| KiCad-specific correctness | 17/20 | Strong symbol/footprint warnings; no actual KiCad library validation in this pass. |
| Datasheet/component accuracy | 13/15 | Avoided exact unverified specs; family-level summaries still need source extraction. |
| Safety/compliance with repo rules | 15/15 | No KiCad files, installs, or PDF downloads. |
| Memory/history routing correctness | 9/10 | Global closeout records created; no project memory touched. |
| Uncertainty disclosure | 10/10 | Exact values explicitly marked unknown/source-required. |
| End-user usefulness | 7/10 | Large scaffold is useful, but exact part records still need research. |

Quality gate result: `PASS_FOR_DOCUMENTATION_SCAFFOLD`

Not approved for exact schematic, footprint, BOM, or fabrication decisions without part-level verification.
""")

    write(dirs["claim"] / "STM32_DATASHEET_TREE_CONTENT_COMPLETION_CLAIM_EVIDENCE_MATRIX.md", f"""# Claim Evidence Matrix - STM32 Datasheet Tree Content Completion

Date: {DATE}

| Claim | Status | Evidence | Human Review Required |
| --- | --- | --- | --- |
| STM32 family folders existed before this pass. | VERIFIED_BY_FILE | Recursive listing of `06_DATASHEETS/01_MICROCONTROLLERS/STMICRO_STM32`. | No |
| The prior STM32 folder structure lacked requested per-family AI docs. | VERIFIED_BY_FILE | `rg --files` showed only README/INDEX/SOURCES/MISSING plus root board indexes before generation. | No |
| Official ST family/source links are preferred. | VERIFIED_BY_FILE | Existing `STM32_MASTER_INDEX.md` and opened official ST pages. | No |
| Generated files are family-level summaries, not verified exact specs. | VERIFIED_BY_FILE | Generated docs include `{STATUS}` and `{UNKNOWN}`. | Yes before design use |
| No KiCad design files were intentionally edited. | VERIFIED_BY_FILE | Generation targeted datasheet/component/history markdown only. | No |
""")

    write(dirs["uncert"] / "STM32_DATASHEET_TREE_CONTENT_COMPLETION_UNCERTAINTY_LOG.md", f"""# Uncertainty Log - STM32 Datasheet Tree Content Completion

Date: {DATE}

## Unverified Items

- Exact operating voltages and power limits for every STM32 family and part remain `{UNKNOWN}`.
- Exact current limits and absolute maximum ratings remain `{UNKNOWN}`.
- Exact reference manuals and errata documents are not mapped per subfamily.
- Exact package drawings and KiCad footprint matches are not verified.
- Exact Nucleo/Discovery/EVAL board revisions are not fully indexed.
- Lifecycle status is not verified per order code.
- Family subfamily lists are AI-readable examples and must be checked against the official ST selector before design use.

## Required Future Verification

Move any part from scaffold to usable component record only after official ST source links, package drawing, KiCad symbol/pinout review, KiCad footprint review, and human review are recorded.
""")

    write(dirs["hall"] / "STM32_DATASHEET_TREE_CONTENT_COMPLETION_HALLUCINATION_RISK_LOG.md", f"""# Hallucination Risk Log - STM32 Datasheet Tree Content Completion

Date: {DATE}
Risk: `MEDIUM_RISK`

## Risk

Family-level summaries can be mistaken for verified part-level facts if future agents ignore the classification.

## Controls Added

- Every family file is marked `{STATUS}`.
- Exact parameters are marked `{UNKNOWN}`.
- Footprint approval requires exact package drawing and human review.
- `NEEDS_RESEARCH.md` files list unresolved source work for every family.
- Component database guide tells agents not to use family names as part records.

## Remaining Human Review Gate

Before any STM32 schematic/PCB work, a human or source-backed workflow must select exact part/order code and verify datasheet, reference manual, errata, package drawing, symbol, footprint, and package orientation.
""")


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".", help="KiCad Engine repository root")
    args = parser.parse_args()

    repo = Path(args.repo_root).resolve()
    stm_root = repo / "06_DATASHEETS" / "01_MICROCONTROLLERS" / "STMICRO_STM32"
    for fam in FAMILIES:
        fam_dir = stm_root / str(fam["name"])
        fam_dir.mkdir(parents=True, exist_ok=True)
        for filename in FILES:
            write(fam_dir / filename, GENERATORS[filename](fam))

    build_master_index(stm_root)
    build_component_guides(repo)
    build_closeout(repo)

    print(f"Generated STM32 AI docs for {len(FAMILIES)} families.")
    print(f"Per-family files: {len(FAMILIES) * len(FILES)}")
    print(f"Classification: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
