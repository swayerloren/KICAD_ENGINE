# User Correction Capture Rules

A user correction is any message saying the agent output was wrong, incomplete, unsafe, failed in practice, or needs to be redone.

## Required Capture

When a correction occurs:

1. Write a correction record in `02_HISTORY/user_corrections/` or project `history/user_corrections/`.
2. Record the corrected behavior.
3. Record affected files, components, footprints, symbols, workflows, or outputs.
4. Add an issue if the correction creates unresolved work.
5. Update project memory if it changes durable project behavior.
6. Update global memory if it changes reusable behavior.
7. Mark records `UNVERIFIED` unless the user explicitly confirms the corrected fact.

## Do Not

- Do not argue with a user correction.
- Do not silently overwrite history.
- Do not hide the earlier mistake.
- Do not promote project-specific corrections into global memory unless reusable.
- Do not record secrets from a correction message.

