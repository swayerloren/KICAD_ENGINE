# Uncertainty Log

- `knowledge_scrape/_scripts/` remains for a later dedicated migration phase
  and was intentionally not touched here.
- Older moved phases may still have legacy `MOVED_PENDING_POST_MOVE_VALIDATION`
  rows outside the 90/91 scope; this task normalized only the targeted 90/91
  rows to `MOVED_VALIDATED`.
- The current no-KiCad-design-change proof is limited to `git diff` plus the
  known preexisting dirty schematic path, not a new full hash packet.
