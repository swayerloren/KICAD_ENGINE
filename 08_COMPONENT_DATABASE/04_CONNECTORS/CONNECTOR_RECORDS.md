# Connector Records

Date: 2026-05-02

Status: generic connector placeholders for AI-assisted KiCad design. Every record in this file is `UNVERIFIED_PLACEHOLDER` until matched to an exact manufacturer part number and drawing.

## Required Rule

Do not use any connector record below as a production schematic, PCB, or BOM decision without:

- Exact manufacturer part number.
- Exact datasheet or mechanical drawing.
- Verified KiCad symbol.
- Verified KiCad footprint.
- Verified mating connector or cable.
- Verified pin numbering view.
- Verified mechanical orientation.
- Verified 3D or enclosure clearance.

## Records

### CONN_USB_C_16PIN_USB2_RECEPTACLE_GENERIC

- Connector: USB-C 16-pin USB2-only receptacle.
- Verified/source status: `UNVERIFIED_PLACEHOLDER`.
- Footprint verification checklist: exact part number, pad geometry, shell tabs, pegs, board-edge offset, duplicated D+/D-, CC1/CC2, VBUS/GND pins, courtyard, 3D model.
- Mechanical orientation warning: mid-mount, top-mount, vertical, and hybrid connectors differ.
- Pin numbering warning: verify from manufacturer PCB footprint view; do not use mating-face view blindly.
- 3D model status: `Unknown - requires source verification`.
- Mating connector status: USB-C plug/cable type must be defined.
- Datasheet/source link placeholder: `Unknown - requires source verification`.
- Common mistakes: missing CC pull-downs, wrong shell pad footprint, D+/D- swap, backfeeding VBUS.
- AI warnings: do not treat USB-C as a Micro-B replacement.

### CONN_USB_C_24PIN_FULL_FEATURE_RECEPTACLE_GENERIC

- Connector: USB-C 24-pin full-feature receptacle.
- Verified/source status: `UNVERIFIED_PLACEHOLDER`.
- Footprint verification checklist: exact high-speed pad rows, shell, mounting holes, board-edge offset, SBU, CC, superspeed pairs, USB2 pair, VBUS/GND, courtyard, 3D model.
- Mechanical orientation warning: full-feature connectors vary strongly by mount style and row geometry.
- Pin numbering warning: top/bottom row orientation must be verified against the connector drawing.
- 3D model status: `Unknown - requires source verification`.
- Mating connector status: USB-C cable and port role must be defined.
- Datasheet/source link placeholder: `Unknown - requires source verification`.
- Common mistakes: using 24-pin footprint with 16-pin symbol, ignoring superspeed escape, assuming PD support.
- AI warnings: full-feature connector does not imply USB PD controller or high-speed compliance.

### CONN_MICRO_USB_B_GENERIC

- Connector: micro USB B.
- Verified/source status: `UNVERIFIED_PLACEHOLDER`.
- Footprint verification checklist: shell tabs, mounting pegs, pin pitch, ID pin, shield pads, board edge, plug insertion keepout, 3D model.
- Mechanical orientation warning: top-entry and mid-mount variants differ.
- Pin numbering warning: verify VBUS, D-, D+, ID, and GND against drawing view.
- 3D model status: `Unknown - requires source verification`.
- Mating connector status: micro USB B plug/cable must be defined.
- Datasheet/source link placeholder: `Unknown - requires source verification`.
- Common mistakes: wrong shield footprint, weak mechanical anchoring, ID pin mishandled.
- AI warnings: legacy connector; check durability and product requirements.

### CONN_BARREL_JACK_5_5X2_1_GENERIC

- Connector: barrel jack 5.5x2.1.
- Verified/source status: `UNVERIFIED_PLACEHOLDER`.
- Footprint verification checklist: center pin diameter, sleeve geometry, switched contact pins, mounting posts, board edge, panel fit, courtyard, 3D model.
- Mechanical orientation warning: horizontal, vertical, panel-mount, and switched styles differ.
- Pin numbering warning: switched contact pins are often misread; verify with continuity diagram.
- 3D model status: `Unknown - requires source verification`.
- Mating connector status: 5.5x2.1 plug and polarity must be defined.
- Datasheet/source link placeholder: `Unknown - requires source verification`.
- Common mistakes: wrong center pin size, wrong switched pin wiring, no polarity mark.
- AI warnings: do not assume center-positive; label and protect input.

### CONN_JST_PH_2PIN_GENERIC

- Connector: JST-PH 2-pin.
- Verified/source status: `UNVERIFIED_PLACEHOLDER`.
- Footprint verification checklist: exact JST or compatible manufacturer, top/side entry, through-hole/SMD, latch orientation, peg holes, pin pitch, pad/hole size, 3D model.
- Mechanical orientation warning: cable exit direction matters for enclosure and strain relief.
- Pin numbering warning: verify pin 1 from PCB drawing and cable mating face.
- 3D model status: `Unknown - requires source verification`.
- Mating connector status: PH housing, crimp terminal, and wire gauge required.
- Datasheet/source link placeholder: `Unknown - requires source verification`.
- Common mistakes: using clone footprint, reversing battery polarity, missing latch clearance.
- AI warnings: do not use PH family name as footprint proof.

### CONN_JST_XH_2PIN_GENERIC

- Connector: JST-XH 2-pin.
- Verified/source status: `UNVERIFIED_PLACEHOLDER`.
- Footprint verification checklist: exact part, vertical/right-angle orientation, drill size, peg geometry, latch direction, pitch, courtyard, 3D model.
- Mechanical orientation warning: larger cable exit and latch clearance required.
- Pin numbering warning: verify from manufacturer drawing and cable assembly.
- 3D model status: `Unknown - requires source verification`.
- Mating connector status: XH housing, crimp terminal, and wire gauge required.
- Datasheet/source link placeholder: `Unknown - requires source verification`.
- Common mistakes: confusing PH/XH pitch, wrong right-angle orientation, missing mating housing.
- AI warnings: verify current rating and wire gauge from exact part.

### CONN_JST_GH_4PIN_GENERIC

- Connector: JST-GH 4-pin.
- Verified/source status: `UNVERIFIED_PLACEHOLDER`.
- Footprint verification checklist: exact GH side/top entry part, latch orientation, pad geometry, shell/mechanical tabs, 3D model.
- Mechanical orientation warning: low-profile latch and cable exit must be reviewed in 3D.
- Pin numbering warning: small-pitch connector drawings are easy to mirror; verify PCB view.
- 3D model status: `Unknown - requires source verification`.
- Mating connector status: GH housing and crimp terminals required.
- Datasheet/source link placeholder: `Unknown - requires source verification`.
- Common mistakes: using SH/GH/PH footprint interchangeably, wrong cable orientation.
- AI warnings: verify assembly capability for small pitch.

### CONN_PIN_HEADER_2_54MM_GENERIC

- Connector: 2.54mm pin header.
- Verified/source status: `UNVERIFIED_PLACEHOLDER`.
- Footprint verification checklist: pin count, row count, vertical/right-angle, shrouded/unshrouded, keyed, drill size, courtyard, mating cable.
- Mechanical orientation warning: right-angle headers change cable exit and board-edge clearance.
- Pin numbering warning: dual-row odd/even numbering must match mating cable.
- 3D model status: `Unknown - requires source verification`.
- Mating connector status: jumper, Dupont-style housing, IDC cable, or shrouded plug must be defined.
- Datasheet/source link placeholder: `Unknown - requires source verification`.
- Common mistakes: unkeyed connector used where polarity matters, reversed IDC cable.
- AI warnings: not suitable for rugged field wiring without retention/strain relief.

### CONN_TERMINAL_BLOCK_3_5MM_GENERIC

- Connector: 3.5mm terminal block.
- Verified/source status: `UNVERIFIED_PLACEHOLDER`.
- Footprint verification checklist: exact pitch, wire entry direction, screw/spring type, pin count, hole size, current rating, torque, 3D model.
- Mechanical orientation warning: wire entry must face accessible enclosure opening.
- Pin numbering warning: terminal numbering depends on viewing direction.
- 3D model status: `Unknown - requires source verification`.
- Mating connector status: wire gauge and ferrule/stripped-wire requirements must be defined.
- Datasheet/source link placeholder: `Unknown - requires source verification`.
- Common mistakes: wrong pitch, blocked screwdriver access, insufficient copper for current.
- AI warnings: verify field-wiring strain relief and touch safety.

### CONN_UFL_IPEX_MHF1_GENERIC

- Connector: U.FL/IPEX MHF1.
- Verified/source status: `UNVERIFIED_PLACEHOLDER`.
- Footprint verification checklist: exact U.FL or MHF1 brand, footprint, connector height, keepout, ground pads, cable plug, 3D model.
- Mechanical orientation warning: cable bend radius and mating cycle limits are critical.
- Pin numbering warning: center conductor and ground shell must match footprint drawing.
- 3D model status: `Unknown - requires source verification`.
- Mating connector status: exact coax pigtail plug required.
- Datasheet/source link placeholder: `Unknown - requires source verification`.
- Common mistakes: treating U.FL and MHF variants as identical, no RF keepout, poor cable clearance.
- AI warnings: not a user-serviceable connector unless product design explicitly supports it.

### CONN_SMA_EDGE_LAUNCH_GENERIC

- Connector: SMA edge launch.
- Verified/source status: `UNVERIFIED_PLACEHOLDER`.
- Footprint verification checklist: exact connector, board thickness, launch geometry, ground via fence, edge plating/clearance, stackup, 3D model.
- Mechanical orientation warning: connector body and nut clearance depend on board edge and enclosure.
- Pin numbering warning: RF center pin and ground tabs must match launch drawing.
- 3D model status: `Unknown - requires source verification`.
- Mating connector status: SMA cable/antenna gender and torque requirements must be defined.
- Datasheet/source link placeholder: `Unknown - requires source verification`.
- Common mistakes: wrong board thickness, no controlled impedance launch, missing ground vias.
- AI warnings: footprint is stackup-specific.

### CONN_RP_SMA_PIGTAIL_GENERIC

- Connector: RP-SMA pigtail.
- Verified/source status: `UNVERIFIED_PLACEHOLDER`.
- Footprint verification checklist: board-end connector, cable assembly, panel bulkhead, nut/washer clearance, bend radius, strain relief, 3D model.
- Mechanical orientation warning: RP-SMA is usually panel/bulkhead cable hardware, not a simple PCB footprint.
- Pin numbering warning: verify board-end connector pinout separately from RP-SMA gender.
- 3D model status: `Unknown - requires source verification`.
- Mating connector status: antenna/cable gender and reverse-polarity convention must be defined.
- Datasheet/source link placeholder: `Unknown - requires source verification`.
- Common mistakes: confusing SMA and RP-SMA gender, ignoring cable bend radius, no strain relief.
- AI warnings: define both RF ends of the pigtail.

### CONN_SEALED_AUTOMOTIVE_GENERIC

- Connector: generic sealed automotive connector.
- Verified/source status: `UNVERIFIED_PLACEHOLDER`.
- Footprint verification checklist: exact header/housing, terminals, seals, cavity plugs, CPA/TPA, mounting holes, board thickness, current, wire gauge, 3D model.
- Mechanical orientation warning: latch, keying, harness exit, and seal compression must be verified.
- Pin numbering warning: cavity numbering can differ between mating face and wire side.
- 3D model status: `Unknown - requires source verification`.
- Mating connector status: full connector system must be defined.
- Datasheet/source link placeholder: `Unknown - requires source verification`.
- Common mistakes: using housing without correct terminals/seals, reversing cavity numbers, no harness strain relief.
- AI warnings: never substitute automotive connector families without exact system review.

### CONN_HONDA_SUB_HARNESS_PLACEHOLDER

- Connector: generic Honda-style sub-harness connector placeholder.
- Verified/source status: `UNVERIFIED_PLACEHOLDER`.
- Footprint verification checklist: exact vehicle/model/year or manufacturer system, cavity numbering, mating harness, terminals, lock, seals, mechanical fit, 3D model.
- Mechanical orientation warning: OEM harness connectors often use keyed housings and cavity views that are easy to reverse.
- Pin numbering warning: service manual view, mating face, and wire-side view must be distinguished.
- 3D model status: `Unknown - requires source verification`.
- Mating connector status: exact OEM or supplier mating connector required.
- Datasheet/source link placeholder: `Unknown - requires source verification`.
- Common mistakes: using marketplace photos as pinout evidence, assuming similar Honda connectors share footprints.
- AI warnings: placeholder only; do not use until exact source evidence exists.
