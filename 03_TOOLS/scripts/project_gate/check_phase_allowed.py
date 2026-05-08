#!/usr/bin/env python3
"""Compatibility wrapper for the canonical live-state gate checker."""

from __future__ import annotations

import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = next((path for path in [SCRIPT_DIR, *SCRIPT_DIR.parents] if (path / "AGENTS.md").exists()), SCRIPT_DIR).resolve()
PROJECT_STATE_DIR = REPO_ROOT / "03_TOOLS" / "scripts" / "project_state"
if str(PROJECT_STATE_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_STATE_DIR))

from live_state_gate_wrapper import main  # type: ignore  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main())
