# Connector Orientation Examples

## Barrel Jack

Correct bottom-edge concept:

- port opening faces down/off-board
- solder-leg side faces up/inward
- review uses footprint family plus geometry and 3D model, not coordinates alone

Wrong bottom-edge concept:

- solder-leg side sits on the board edge where the plug should enter
- reviewer says “rotation 180 looks fine” without proving the front/back meaning

## USB-C

Correct bottom-edge concept:

- receptacle mouth faces down/off-board
- footprint `PCB Edge` direction aligns to `Edge.Cuts`
- shell/body overhang is mechanically expected

Wrong bottom-edge concept:

- USB-C sits on the bottom edge but the mouth faces inward
- review says “J2 is centered at the bottom edge” with no mouth-direction proof

## ESP32 Module

Correct top-edge concept:

- antenna keepout faces the top edge
- the clear antenna zone stays outward

Wrong concept:

- module is rotated so the antenna keepout faces board interior
- review says “U2 is near the top” without proving which side is the antenna side
