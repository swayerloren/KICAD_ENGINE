# Accuracy Gate Checklist

Status: `MANDATORY_FOR_ENGINEERING_CLAIMS`

Use this checklist before creating or approving schematics, PCBs, footprints, BOMs, or fab outputs.

## Source Evidence

- [ ] Each part has a source document, source URL, user-provided fact, or explicit missing-source status.
- [ ] Each exact value is sourced or marked `Unknown - requires source verification`.
- [ ] Each component record path and verification status is named.
- [ ] Datasheet redistribution/copyright status is respected.

## Schematic Evidence

- [ ] Symbol candidate is named.
- [ ] Symbol pinout status is stated.
- [ ] Power pins and power nets are reviewed.
- [ ] Reset, boot, programming, oscillator, strap, or mode pins are reviewed where applicable.
- [ ] Connector pin numbering is verified or human-review-required.

## PCB Evidence

- [ ] Footprint candidate is named.
- [ ] Exact package drawing status is stated.
- [ ] Footprint-to-datasheet match status is stated.
- [ ] Pin 1 and orientation are reviewed.
- [ ] Connector orientation is verified or human-review-required.
- [ ] Polarity-sensitive components are flagged.
- [ ] RF/USB/CAN/power layout rules are reviewed where applicable.

## Verification Evidence

- [ ] ERC required status is stated.
- [ ] DRC required status is stated.
- [ ] BOM review status is stated.
- [ ] Fab outputs are marked `NOT_FINAL` unless final human review accepted them.

## AI Closeout Evidence

- [ ] AI self-review created when engineering claims were made.
- [ ] AI response scorecard created when engineering claims were made.
- [ ] Claim/evidence matrix created for major engineering claims.
- [ ] Uncertainty log created for unverified or partially verified items.
- [ ] Hallucination-risk log created if any claim was inferred, guessed, or weakly sourced.

