# 99_BACKUPS

## PURPOSE
Pre-edit backups and recovery snapshots.

## WHAT_BELONGS_HERE
- Snapshots created before KiCad edits.
- Recovery copies needed to roll back agent work.

## WHAT_DOES_NOT_BELONG_HERE
- Secrets.
- New source-of-truth project files.
- Public release payload files.

## AI_AGENT_RULES
- Create backups before approved KiCad source edits.
- Do not delete backups.

## SAFE_EDIT_RULES
- Write new timestamped backups only when needed.
- Never overwrite existing backups.

## PUBLIC_RELEASE_NOTES
- Public payloads should normally exclude private backups.
- ZIP users do not need this folder populated for the basic workflow.
- Recreate it locally by making timestamped pre-edit backups before approved KiCad source changes.
- Never commit generated backup copies, copied boards, or personal recovery archives.
