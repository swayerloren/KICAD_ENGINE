# 3D Model Guidance

Status: `AI_GUIDANCE_ONLY`

## Purpose

This folder defines how AI agents should treat KiCad 3D model references during symbol, footprint, and library review. 3D models are useful for visual and mechanical review, but they do not verify pad geometry, pin numbering, orientation, or electrical correctness.

## Required 3D Model Record Fields

| Field | Required | Guidance |
| --- | --- | --- |
| `part_number` | Yes | Exact MPN or `generic_placeholder`. |
| `footprint` | Yes | KiCad footprint the model is attached to. |
| `model_path` | Yes | Prefer `${KICAD9_3DMODEL_DIR}` or project-relative paths. |
| `source` | Yes | KiCad stock library, vendor model, user-provided model, or generated model. |
| `redistribution_status` | Yes | `KICAD_LIBRARY`, `REDISTRIBUTION_CONFIRMED`, `LOCAL_PRIVATE_ONLY`, or `UNKNOWN_REQUIRES_REVIEW`. |
| `scale_rotation_offset_status` | Yes | `UNVERIFIED`, `VISUALLY_REVIEWED`, or `MECHANICALLY_REVIEWED`. |
| `board_side_status` | Yes | Confirm top/bottom side alignment. |
| `mechanical_review_required` | Yes | `true` for connectors, tall parts, enclosures, RF, modules, and board-edge parts. |
| `notes` | Yes | Include screenshots, package drawing links, or unresolved fit risks. |

## What Belongs Here

- 3D model source rules.
- Path and environment-variable guidance.
- Scale, rotation, offset, and board-side review guidance.
- Mechanical-fit review notes.
- Checklists for connectors, modules, tall electrolytics, antennas, board-edge connectors, and enclosure-sensitive parts.

## What Does Not Belong Here

- Installed KiCad 3D model files.
- Copied vendor 3D models without redistribution review.
- Active project footprints or boards.
- Claims that a 3D render approves manufacturing fit.

## Agent Review Checklist

Before saying a 3D model is acceptable, confirm:

- The model path resolves on the target machine or is project-local.
- The model belongs to the same package and exact connector/mechanical variant.
- Scale, rotation, offset, and board side were visually reviewed.
- The model does not hide a footprint mismatch.
- Tall parts, connectors, mounting hardware, and enclosure limits have human review when required.

## Hard Rule

A footprint may not be promoted to verified because a 3D model "looks right." Footprint verification still requires exact manufacturer package or connector drawing evidence and pad-by-pad review.
