# Power Net Rules

## Purpose

Make power nets explicit and reviewable.

## Rules

- Name every power rail clearly.
- Do not create ambiguous rails such as `VCC` without context.
- Record nominal voltage and source status for each rail.
- Check absolute maximum ratings and recommended operating conditions from source documents.
- Check current demand and regulator capability before connecting loads.
- Connect all required analog, digital, RF, USB, and backup power pins intentionally.
- Treat exposed pads as electrical or thermal requirements until verified.
- Add power flags only to express real driven power sources, not to silence ERC blindly.

## Required Review

Flag:

- Mixed 5 V and 3.3 V domains.
- USB VBUS handling.
- Battery and charger paths.
- Automotive or inductive input paths.
- Reverse polarity and transient protection.
- Analog supply pins such as VDDA/VSSA.
- RF module supply pins with peak-current requirements.

## Exit Criteria

Every power pin must have a net, every rail must have a source, and every power warning must be resolved or marked `HUMAN_REVIEW_REQUIRED`.
