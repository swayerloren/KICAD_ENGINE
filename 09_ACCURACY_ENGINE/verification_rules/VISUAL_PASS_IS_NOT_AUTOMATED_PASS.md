# Visual Pass Is Not Automated Pass

Status: `MANDATORY`

## Rule

Automated visual crop `PASS` is not the same as schematic visual `PASS`.

Automated crop `PASS` means only that the workflow was able to produce visual evidence and did not detect the limited set of machine-screened issues. It does not prove that the schematic is readable.

The visual tooling must prefer the status `AUTOMATED_CROP_PASS_ONLY` over the word `PASS` whenever it has not performed actual human-readable image judgment. If an older report or script says close-up status `PASS`, agents must reinterpret that as `AUTOMATED_CROP_PASS_ONLY` unless the same report contains explicit rendered-image inspection findings for every crop.

## Do Not Equate These States

Do not treat any of the following as human-readable schematic approval:

- `ERC_PASS`
- annotation checker `PASS`
- all physical symbols have footprint fields
- crop files exist
- `CLOSE_UP_REVIEW.md` exists
- automated crop result `PASS`
- no visible footprint/library/path strings detected
- no `?` token detected by file parsing
- raw `.kicad_sch` text edits that changed references without KiCad-native annotation
- CLI ERC when LJ reports the open GUI still shows question-mark references

## Annotation Native-State Rule

When annotation state is disputed, the KiCad GUI is an evidence source. If the GUI shows question-mark references, a parser or CLI report cannot be used to claim visual or annotation pass. Agents must use verified KiCad-native GUI annotation or stop and instruct LJ to run:

`Tools -> Annotate Schematic -> Re-annotate all symbols -> Save -> Run ERC`

## Required Claim Language

Use precise language:

- `AUTOMATED_CROP_PASS_ONLY`: crop generation and automated screening succeeded.
- `VISUAL_PASS`: rendered full-page image and each required close-up crop were visually inspected and found human-readable.
- `VISUAL_FAIL`: any visible overlap, crowding, clipped label, note-in-circuitry, or unreadable block remains.
- `VISUAL_NOT_VERIFIED`: the agent did not inspect rendered PNG/crop evidence.

## Mandatory Blockers

Mark the schematic blocked when:

- any crop visibly contains overlapping text, values, references, labels, wires, pins, or symbols
- notes are inside active circuitry and interfere with review
- long values make the block unreadable
- question-mark references are visible in KiCad or rendered output
- the crop is missing the intended block
- the agent cannot inspect the rendered image

## Prohibited Report Pattern

Do not write or accept a report that says only:

```text
Close-up visual review status: PASS
Human visual result: NOT_REVIEWED
```

That combination is internally contradictory. The correct status is `AUTOMATED_CROP_PASS_ONLY` plus `VISUAL_NOT_VERIFIED`, and it blocks `READY_FOR_LJ_VISUAL_REVIEW`.

## Required Script Behavior

Visual scripts may report:

- `AUTOMATED_SCREEN_PASS`: one crop had no limited machine-screen findings.
- `AUTOMATED_CROP_PASS_ONLY`: crops were generated and limited machine screens found no blockers.
- `FAIL`: limited machine screens found a blocker.
- `VISUAL_REVIEW_INCOMPLETE`: required visual evidence is missing.

Visual scripts must not output bare `PASS` for schematic human readability unless they actually inspect rendered images for overlaps, crop framing, notes, and readability. Current scripts do not do that; therefore their non-failing status is evidence generation only.

## Reporting Requirement

Every schematic visual report must include two separate rows:

| Check | Meaning |
| --- | --- |
| Automated crop generation | Whether exports/crops/reports were created and basic text screens passed. |
| Human-readable visual inspection | Whether rendered full-page/crops are actually readable. |

The schematic-to-PCB gate may not pass unless both are acceptable and all other required gates pass.
