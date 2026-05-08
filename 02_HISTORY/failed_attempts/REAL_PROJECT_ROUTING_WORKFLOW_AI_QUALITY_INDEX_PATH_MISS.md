# REAL_PROJECT_ROUTING_WORKFLOW_AI_QUALITY_INDEX_PATH_MISS

Date: `2026-05-07`

## Failure

The first AI-quality index rebuild command used the wrong path:

```powershell
python 03_TOOLS/scripts/indexing/build_ai_quality_index.py
```

That file does not exist.

## Resolution

The correct command was run successfully:

```powershell
python 03_TOOLS/scripts/ai_quality/build_ai_quality_index.py
```

## Impact

- No repo content was lost.
- AI-quality indexes were still rebuilt successfully before closeout.
