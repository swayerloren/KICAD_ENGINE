# 3D Model Review Rules

Status: `AI_GUIDANCE_ONLY`

## Required Evidence

Before treating a 3D model as useful evidence, record:

- Model source.
- License or redistribution status if the model is copied into the repo.
- Related exact part number or package.
- KiCad footprint path that references the model.
- Model path style: project-local, KiCad environment variable, or absolute path.
- Scale, rotation, offset, and board-side orientation review status.

## Rules

- Do not use a 3D model to approve pad geometry.
- Do not use a 3D model to approve connector pin numbering.
- Do not copy vendor STEP/WRL files into a public repo unless redistribution is reviewed.
- Do not use user-specific absolute paths in portable project-local libraries.
- Prefer `${KICAD9_3DMODEL_DIR}` or project-local relative paths where appropriate.
- For connectors, compare the model, footprint, mating direction, board edge, cable exit, and mechanical drawing together.

## Status Labels

- `MODEL_NOT_REQUIRED`
- `MODEL_MISSING`
- `MODEL_CANDIDATE_ONLY`
- `MODEL_PATH_VERIFIED`
- `MODEL_ORIENTATION_REVIEWED`
- `MODEL_REQUIRES_HUMAN_MECHANICAL_REVIEW`

## Review Gate

3D model review never replaces exact package drawing review. It can only support visual and mechanical checking after the footprint has a separate evidence record.

