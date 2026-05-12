#!/usr/bin/env python3
"""Read-only helper wrappers for tolerant pcbnew object access.

These helpers are intentionally conservative. They reduce fragile direct method
assumptions in board-aware scripts, but they do not replace KiCad validation.
"""

from __future__ import annotations

from typing import Any


def safe_call(obj: Any, method_name: str, default: Any = None) -> Any:
    method = getattr(obj, method_name, None)
    if method is None or not callable(method):
        return default
    try:
        return method()
    except Exception:
        return default


def safe_net_name(item: Any) -> str | None:
    net = safe_call(item, "GetNet")
    if net is not None:
        name = safe_call(net, "GetNetname")
        if isinstance(name, str) and name:
            return name
    name = safe_call(item, "GetNetname")
    if isinstance(name, str) and name:
        return name
    return None


def safe_layer_name(board: Any, item: Any) -> str | None:
    layer_id = safe_call(item, "GetLayer")
    if layer_id is None:
        return None
    if board is not None:
        name = safe_call(board, "GetLayerName", default=None)
        if callable(getattr(board, "GetLayerName", None)):
            try:
                resolved = board.GetLayerName(layer_id)
                if isinstance(resolved, str) and resolved:
                    return resolved
            except Exception:
                pass
    if isinstance(layer_id, str):
        return layer_id
    return None


def safe_track_width(item: Any) -> int | float | None:
    width = safe_call(item, "GetWidth")
    if isinstance(width, (int, float)):
        return width
    return None


def safe_via_drill(item: Any) -> int | float | None:
    for name in ("GetDrill", "GetDrillValue", "GetDrillSize"):
        value = safe_call(item, name)
        if isinstance(value, (int, float)):
            return value
    return None


def safe_position(item: Any) -> tuple[int | float, int | float] | None:
    pos = safe_call(item, "GetPosition")
    if pos is None:
        return None
    for x_name, y_name in (("x", "y"), ("X", "Y")):
        x = getattr(pos, x_name, None)
        y = getattr(pos, y_name, None)
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            return (x, y)
    for x_name, y_name in (("GetX", "GetY"),):
        x_method = getattr(pos, x_name, None)
        y_method = getattr(pos, y_name, None)
        if callable(x_method) and callable(y_method):
            try:
                return (x_method(), y_method())
            except Exception:
                pass
    return None


__all__ = [
    "safe_call",
    "safe_layer_name",
    "safe_net_name",
    "safe_position",
    "safe_track_width",
    "safe_via_drill",
]
