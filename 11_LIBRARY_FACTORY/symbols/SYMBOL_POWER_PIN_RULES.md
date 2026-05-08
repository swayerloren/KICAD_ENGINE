# Symbol Power Pin Rules

## Purpose

Power pins are common sources of AI and schematic errors.

## Rules

- Verify every VDD/VCC/VBAT/AVDD/VDDA/VIO/VREF and ground pin from source evidence.
- Do not rely on hidden power pins unless the project intentionally uses that KiCad convention.
- Prefer visible power pins for new custom symbols when AI review and human readability matter.
- Show analog power and ground pins distinctly when the datasheet treats them distinctly.
- Show exposed thermal pads if they must be tied to ground or another net.

## Electrical Type

- Assign KiCad electrical types deliberately.
- Power inputs should not be marked passive unless there is a clear reason.
- No-connect pins should not silently look usable.
- Bidirectional or multifunction pins require source-backed type decisions.

## Review Gate

A symbol cannot be approved if any power or ground pin is missing, hidden unexpectedly, or typed without review.

