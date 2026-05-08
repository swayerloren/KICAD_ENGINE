#!/usr/bin/env python3
"""Read-only extraction helpers for real KiCad PCB routing-engine bridge work."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

from _kicad_pcb_bridge_common import (
    bbox_to_mm,
    copper_layer_names,
    infer_keepout_type,
    infer_net_role,
    infer_pair_name,
    infer_routing_priority,
    is_fixed_mechanical,
    is_mounting_hole,
    layer_names_from_set,
    mm,
    point_to_mm,
)


def safe_net_name(name: str) -> str:
    return str(name).strip()


def shape_points_to_mm(pcbnew: Any, outline: Any) -> list[dict[str, float]]:
    points: list[dict[str, float]] = []
    count = int(outline.PointCount())
    for index in range(count):
        point = outline.CPoint(index)
        points.append({"x_mm": mm(pcbnew, point.x), "y_mm": mm(pcbnew, point.y)})
    return points


def board_outline(board: Any, pcbnew: Any) -> tuple[dict[str, Any], list[dict[str, Any]], list[str]]:
    copper_layers = copper_layer_names(board)
    segments: list[dict[str, Any]] = []
    unsupported: list[str] = []
    xs: list[float] = []
    ys: list[float] = []

    for drawing in board.GetDrawings():
        if not hasattr(drawing, "GetLayerName") or str(drawing.GetLayerName()) != "Edge.Cuts":
            continue
        shape_name = str(drawing.GetShapeStr())
        entry: dict[str, Any] = {
            "shape": shape_name,
            "layer": "Edge.Cuts",
            "bbox_mm": bbox_to_mm(pcbnew, drawing.GetBoundingBox()),
        }
        if hasattr(drawing, "GetStart") and hasattr(drawing, "GetEnd"):
            start = drawing.GetStart()
            end = drawing.GetEnd()
            entry["start_mm"] = point_to_mm(pcbnew, start)
            entry["end_mm"] = point_to_mm(pcbnew, end)
            xs.extend([entry["start_mm"]["x_mm"], entry["end_mm"]["x_mm"]])
            ys.extend([entry["start_mm"]["y_mm"], entry["end_mm"]["y_mm"]])
        else:
            bbox = entry["bbox_mm"]
            xs.extend([bbox["xmin"], bbox["xmax"]])
            ys.extend([bbox["ymin"], bbox["ymax"]])
        if shape_name in {"Arc", "Circle"} and hasattr(drawing, "GetRadius"):
            entry["radius_mm"] = mm(pcbnew, drawing.GetRadius())
        segments.append(entry)

    if not segments:
        unsupported.append("board outline not extracted because no Edge.Cuts items were found")
        outline = {
            "shape": "NOT_EXTRACTED",
            "width_mm": 0.0,
            "height_mm": 0.0,
            "allowed_signal_layers": copper_layers,
            "notes": "No Edge.Cuts items found on the board.",
        }
        return outline, segments, unsupported

    xmin = min(xs)
    xmax = max(xs)
    ymin = min(ys)
    ymax = max(ys)
    outline = {
        "shape": "EDGE_CUTS_POLYLINE",
        "width_mm": round(xmax - xmin, 6),
        "height_mm": round(ymax - ymin, 6),
        "allowed_signal_layers": copper_layers,
        "xmin": xmin,
        "xmax": xmax,
        "ymin": ymin,
        "ymax": ymax,
        "segments": segments,
        "notes": "Board outline width and height are derived from Edge.Cuts geometry bounding extents.",
    }
    return outline, segments, unsupported


def footprints_and_pads(board: Any, pcbnew: Any) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    components: list[dict[str, Any]] = []
    footprints: list[dict[str, Any]] = []
    pads: list[dict[str, Any]] = []

    for footprint in sorted(board.GetFootprints(), key=lambda item: item.GetReference()):
        ref = str(footprint.GetReference())
        value = str(footprint.GetValue())
        pos = footprint.GetPosition()
        layer_name = str(footprint.GetLayerName())
        footprint_name = str(footprint.GetFPID().GetLibItemName())
        full_library_name = str(footprint.GetFPID().GetFullLibraryName())
        component_entry = {
            "ref": ref,
            "kind": footprint_name or value or ref,
            "value": value,
            "footprint_name": footprint_name,
            "footprint_library": full_library_name,
            "x_mm": mm(pcbnew, pos.x),
            "y_mm": mm(pcbnew, pos.y),
            "rotation_deg": round(float(footprint.GetOrientationDegrees()), 6),
            "side": "B" if layer_name == "B.Cu" else "F",
            "fixed_mechanical": is_fixed_mechanical(ref, value, footprint_name),
            "mounting_hole": is_mounting_hole(ref, value, footprint_name),
            "layer": layer_name,
        }
        components.append(component_entry)
        footprints.append(component_entry.copy())

        for pad in footprint.Pads():
            pad_pos = pad.GetPosition()
            pad_layers = layer_names_from_set(board, pad.GetLayerSet())
            pads.append(
                {
                    "id": f"{ref}:{pad.GetNumber()}",
                    "component": ref,
                    "pad_name": str(pad.GetPadName() or pad.GetNumber()),
                    "net": safe_net_name(pad.GetNetname()),
                    "net_code": int(pad.GetNetCode()),
                    "net_class": str(pad.GetNetClassName() or "Default"),
                    "x_mm": mm(pcbnew, pad_pos.x),
                    "y_mm": mm(pcbnew, pad_pos.y),
                    "layer": str(pad.GetLayerName()),
                    "layers": pad_layers,
                    "shape": str(pad.GetFriendlyName()),
                    "role": "PAD",
                }
            )

    return components, footprints, pads


def tracks_and_vias(board: Any, pcbnew: Any) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[str]]:
    raw_tracks: list[dict[str, Any]] = []
    vias: list[dict[str, Any]] = []
    unsupported: list[str] = []
    grouped_segments: dict[str, list[dict[str, Any]]] = defaultdict(list)
    grouped_vias: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for item in board.GetTracks():
        item_type = type(item).__name__
        net_name = safe_net_name(item.GetNetname())
        net_class_name = str(item.GetNetClassName() or "Default")
        if item_type == "PCB_TRACK":
            start = item.GetStart()
            end = item.GetEnd()
            segment = {
                "x1": mm(pcbnew, start.x),
                "y1": mm(pcbnew, start.y),
                "x2": mm(pcbnew, end.x),
                "y2": mm(pcbnew, end.y),
                "layer": str(item.GetLayerName()),
                "width_mm": mm(pcbnew, item.GetWidth()),
            }
            raw_tracks.append(
                {
                    "type": item_type,
                    "net": net_name,
                    "net_class": net_class_name,
                    "segment": segment,
                }
            )
            grouped_segments[net_name].append(segment)
        elif item_type == "PCB_VIA":
            via_entry = {
                "type": item_type,
                "net": net_name,
                "net_class": net_class_name,
                "x_mm": mm(pcbnew, item.GetPosition().x),
                "y_mm": mm(pcbnew, item.GetPosition().y),
                "drill_mm": mm(pcbnew, item.GetDrillValue()),
                "diameter_mm": mm(pcbnew, item.GetFrontWidth()),
                "top_layer": str(board.GetLayerName(item.TopLayer())),
                "bottom_layer": str(board.GetLayerName(item.BottomLayer())),
                "reason": "NOT_EXTRACTED",
            }
            vias.append(via_entry)
            grouped_vias[net_name].append(via_entry)
        else:
            unsupported.append(f"track item type {item_type} not extracted")

    traces: list[dict[str, Any]] = []
    net_names = sorted(set(grouped_segments) | set(grouped_vias))
    for net_name in net_names:
        traces.append(
            {
                "id": f"trace:{net_name or 'NO_NET'}",
                "net": net_name,
                "routing_status": "ROUTED",
                "critical": False,
                "via_count": len(grouped_vias.get(net_name, [])),
                "via_reason": "NOT_EXTRACTED" if grouped_vias.get(net_name) else "",
                "segments": grouped_segments.get(net_name, []),
                "review_required": False,
                "notes": "Trace grouping is derived from PCB_TRACK and PCB_VIA items on the board.",
            }
        )

    return raw_tracks, vias, traces, sorted(set(unsupported))


def zones_and_keepouts(board: Any, pcbnew: Any) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[str]]:
    zones: list[dict[str, Any]] = []
    keepouts: list[dict[str, Any]] = []
    unsupported: list[str] = []

    for index, zone in enumerate(board.Zones()):
        name = safe_net_name(zone.GetNetname()) or f"ZONE_{index}"
        bbox = bbox_to_mm(pcbnew, zone.GetBoundingBox())
        outer_points = shape_points_to_mm(pcbnew, zone.Outline().COutline(0))
        is_rule_area = bool(getattr(zone, "GetIsRuleArea", lambda: False)())
        has_keepout_parameters = bool(zone.HasKeepoutParametersSet())
        is_keepout = is_rule_area
        zone_entry = {
            "name": f"ZONE_{index}_{name or 'NO_NET'}",
            "net": name,
            "layer": str(zone.GetLayerName()),
            "net_class": str(zone.GetNetClassName() or "Default"),
            "bbox_mm": bbox,
            "outline_points_mm": outer_points,
            "priority": int(zone.GetAssignedPriority()),
            "rule_area": is_rule_area,
            "has_keepout_parameters": has_keepout_parameters,
            "type": "KEEPOUT_ZONE" if is_keepout else "COPPER_ZONE",
        }
        if is_keepout:
            keepout_name = zone_entry["name"]
            keepouts.append(
                {
                    "name": keepout_name,
                    "type": infer_keepout_type(f"{keepout_name} {name}"),
                    "xmin": bbox["xmin"],
                    "ymin": bbox["ymin"],
                    "xmax": bbox["xmax"],
                    "ymax": bbox["ymax"],
                    "geometry": "POLYGON",
                    "points": outer_points,
                    "layer": str(zone.GetLayerName()),
                    "source": "ZONE_OUTLINE",
                    "do_not_allow_tracks": bool(zone.GetDoNotAllowTracks()),
                    "do_not_allow_vias": bool(zone.GetDoNotAllowVias()),
                    "do_not_allow_pads": bool(zone.GetDoNotAllowPads()),
                    "do_not_allow_copper_pour": bool(zone.GetDoNotAllowCopperPour()),
                    "do_not_allow_footprints": bool(zone.GetDoNotAllowFootprints()),
                }
            )
        elif has_keepout_parameters:
            unsupported.append(
                f"{zone_entry['name']} exposes keepout-style zone parameters in KiCad API but is not a rule area; extracted as COPPER_ZONE"
            )
        zones.append(zone_entry)

    if any(zone.get("outline_points_mm") for zone in zones):
        pass
    else:
        unsupported.append("zone polygon outlines not extracted")
    return zones, keepouts, unsupported


def connectivity_summary(board: Any) -> tuple[dict[str, Any], list[str]]:
    unsupported: list[str] = []
    summary = {
        "unconnected_count": "NOT_EXTRACTED",
        "ratsnest_per_net": "NOT_EXTRACTED",
        "status": "NOT_EXTRACTED",
    }
    try:
        connectivity = board.GetConnectivity()
        connectivity.RecalculateRatsnest()
        unconnected_count = int(connectivity.GetUnconnectedCount(False))
        summary = {
            "unconnected_count": unconnected_count,
            "ratsnest_per_net": "NOT_EXTRACTED",
            "status": "CONNECTED" if unconnected_count == 0 else "UNCONNECTED_ITEMS_PRESENT",
        }
        unsupported.append("per-net ratsnest extraction not implemented; only total unconnected count is extracted")
    except Exception as exc:
        unsupported.append(f"connectivity extraction failed: {type(exc).__name__}: {exc}")
    return summary, unsupported


def netclasses_and_rules(board: Any, pcbnew: Any, pads: list[dict[str, Any]], traces: list[dict[str, Any]]) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any], list[str]]:
    unsupported: list[str] = []
    net_settings = board.GetDesignSettings().m_NetSettings
    observed_names = {"Default"}
    observed_names.update(str(name) for name in net_settings.GetNetclasses().keys())
    observed_names.update(str(item.get("net_class", "Default")) for item in pads if item.get("net_class"))
    observed_names.update(str(item.get("net_class", "Default")) for item in traces if item.get("net_class"))

    net_classes: dict[str, Any] = {}
    for name in sorted(item for item in observed_names if item):
        try:
            if name == "Default":
                net_class = net_settings.GetDefaultNetclass()
            elif net_settings.HasNetclass(name):
                net_class = net_settings.GetNetClassByName(name)
            else:
                net_class = net_settings.GetDefaultNetclass()
                unsupported.append(f"net class {name} not found explicitly; default net class substituted")
            net_classes[name] = {
                "width_mm": mm(pcbnew, net_class.GetTrackWidth()),
                "clearance_mm": mm(pcbnew, net_class.GetClearance()),
                "allowed_layers": copper_layer_names(board),
                "via_allowed": True,
                "max_vias": 2,
                "pair_routing": "MATCHED_PAIR" if "USB" in name.upper() else "",
                "impedance_sensitive": "USB" in name.upper(),
                "high_current": any(token in name.upper() for token in ("POWER", "5V", "VIN", "3V3", "VBUS")),
                "review_required": "USB" in name.upper(),
            }
        except Exception as exc:
            unsupported.append(f"net class {name} extraction failed: {type(exc).__name__}: {exc}")

    copper_layers = copper_layer_names(board)
    default_netclass = net_classes.get("Default", {"width_mm": 0.2, "clearance_mm": 0.15})
    layer_rules = {
        "available_layers": copper_layers,
        "default_signal_layer": copper_layers[0] if copper_layers else "F.Cu",
        "usb_preferred_layers": copper_layers[:2] or ["F.Cu", "B.Cu"],
        "power_preferred_layers": copper_layers[:2] or ["F.Cu", "B.Cu"],
        "critical_net_layer_bias": copper_layers[:2] or ["F.Cu", "B.Cu"],
    }
    via_rules = {
        "critical_reason_required": True,
        "default_allowed": True,
        "max_default_vias": 2,
        "notes": "Per-via engineering intent is not stored in KiCad; reasons remain NOT_EXTRACTED.",
    }
    trace_rules = {
        "default_width_mm": default_netclass["width_mm"],
        "default_clearance_mm": default_netclass["clearance_mm"],
        "usb_target_width_mm": 0.25,
        "power_target_widths_mm": {"POWER_INPUT": 0.75, "RAIL_3V3": 0.5},
        "avoid_right_angles": True,
    }
    return net_classes, layer_rules, via_rules, trace_rules, sorted(set(unsupported))


def nets_from_board(
    board: Any,
    pcbnew: Any,
    pads: list[dict[str, Any]],
    traces: list[dict[str, Any]],
    vias: list[dict[str, Any]],
    zones: list[dict[str, Any]],
    keepouts: list[dict[str, Any]],
    net_classes: dict[str, Any],
    connectivity: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[str]]:
    unsupported: list[str] = []
    pad_counts: dict[str, int] = defaultdict(int)
    for pad in pads:
        pad_counts[safe_net_name(pad["net"])] += 1

    track_counts: dict[str, int] = defaultdict(int)
    for trace in traces:
        track_counts[safe_net_name(trace["net"])] += len(trace.get("segments", []))

    via_counts: dict[str, int] = defaultdict(int)
    for via in vias:
        via_counts[safe_net_name(via["net"])] += 1

    zone_counts: dict[str, int] = defaultdict(int)
    for zone in zones:
        zone_counts[safe_net_name(zone["net"])] += 1

    keepout_names = [item["name"] for item in keepouts if item["type"] in {"RF_KEEPOUT", "ANTENNA_KEEPOUT"}]
    nets: list[dict[str, Any]] = []
    net_settings = board.GetDesignSettings().m_NetSettings
    connectivity_zero = connectivity.get("unconnected_count") == 0
    for _, net_item in board.GetNetInfo().NetsByNetcode().items():
        name = safe_net_name(net_item.GetNetname())
        if not name:
            continue
        role = infer_net_role(name)
        power = role in {"POWER_INPUT", "RAIL_3V3", "BUCK_SW", "BUCK_BST"} or name.startswith("+")
        usb = role in {"USB_D+", "USB_D-"}
        ground = role == "GROUND"
        critical = role in {"POWER_INPUT", "RAIL_3V3", "USB_D+", "USB_D-", "BUCK_SW", "BUCK_BST", "EN_BOOT", "PROTECTION"}
        try:
            effective_netclass = net_settings.GetEffectiveNetClass(name)
            net_class_name = str(effective_netclass.GetName() or net_item.GetNetClassName() or "Default")
        except Exception:
            net_class_name = str(net_item.GetNetClassName() or "Default")
        if net_class_name not in net_classes:
            net_class_name = "Default"

        track_count = track_counts.get(name, 0)
        via_count = via_counts.get(name, 0)
        zone_count = zone_counts.get(name, 0)
        pad_count = pad_counts.get(name, 0)
        if track_count > 0 or via_count > 0:
            routing_status = "ROUTED"
            source = "TRACK_OR_VIA_ITEMS"
        elif zone_count > 0 and (ground or power or connectivity_zero):
            routing_status = "ROUTED"
            source = "ZONE_INFERENCE"
        elif connectivity_zero and pad_count > 1:
            routing_status = "ROUTED"
            source = "CONNECTIVITY_INFERENCE"
            unsupported.append(f"{name}: routed status inferred from zero unconnected items rather than explicit net-by-net ratsnest data")
        elif pad_count <= 1:
            routing_status = "ROUTED"
            source = "NO_ROUTE_NEEDED_INFERENCE"
        else:
            routing_status = "UNROUTED"
            source = "NO_CONDUCTOR_ITEMS_FOUND"

        nets.append(
            {
                "name": name,
                "role": role,
                "net_class": net_class_name,
                "routing_priority": infer_routing_priority(role, power, usb, critical),
                "routing_status": routing_status,
                "critical": critical,
                "power": power,
                "usb": usb,
                "ground": ground,
                "pads": [pad["id"] for pad in pads if safe_net_name(pad["net"]) == name],
                "paired_with": infer_pair_name(name),
                "must_avoid_keepouts": keepout_names,
                "trace_width_rule": {"target_mm": net_classes.get(net_class_name, net_classes.get("Default", {})).get("width_mm", 0.2)},
                "clearance_rule": {"mm": net_classes.get(net_class_name, net_classes.get("Default", {})).get("clearance_mm", 0.15)},
                "layer_rule": {"allowed": copper_layer_names(board), "preferred": copper_layer_names(board)[:2] or ["F.Cu", "B.Cu"]},
                "via_rule": {"allowed": True, "reason_required": critical, "max_count": 2},
                "review_required": critical or usb,
                "notes": f"routing_status source: {source}",
            }
        )
    nets.sort(key=lambda item: (-int(item["routing_priority"]), item["name"]))
    return nets, sorted(set(unsupported))


def ground_strategy(zones: list[dict[str, Any]]) -> dict[str, Any]:
    gnd_zones = [zone for zone in zones if safe_net_name(zone.get("net", "")).upper() == "GND"]
    return {
        "present": bool(gnd_zones),
        "strategy": "GND_ZONES_PRESENT" if gnd_zones else "NOT_EXTRACTED",
        "stitching_regions": [],
        "local_return_requirements": [],
        "notes": "Ground strategy is inferred from GND zones only; stitching intent is NOT_EXTRACTED.",
    }


def build_routing_schema(project_name: str, board_path: str | Path, board: Any, pcbnew: Any) -> dict[str, Any]:
    outline, edge_segments, outline_unsupported = board_outline(board, pcbnew)
    components, footprints, pads = footprints_and_pads(board, pcbnew)
    raw_tracks, vias, traces, track_unsupported = tracks_and_vias(board, pcbnew)
    zones, keepouts, zone_unsupported = zones_and_keepouts(board, pcbnew)
    connectivity, connectivity_unsupported = connectivity_summary(board)
    net_classes, layer_rules, via_rules, trace_rules, class_unsupported = netclasses_and_rules(board, pcbnew, pads, raw_tracks)
    nets, net_unsupported = nets_from_board(board, pcbnew, pads, traces, vias, zones, keepouts, net_classes, connectivity)
    unsupported = sorted(
        set(
            outline_unsupported
            + track_unsupported
            + zone_unsupported
            + connectivity_unsupported
            + class_unsupported
            + net_unsupported
        )
    )
    return {
        "schema_version": "1.0",
        "project": project_name,
        "board_path": str(Path(board_path)),
        "board_outline": outline,
        "components": components,
        "footprints": footprints,
        "pads": pads,
        "net_classes": net_classes,
        "nets": nets,
        "keepouts": keepouts,
        "zones": zones,
        "edge_cuts": edge_segments,
        "layer_rules": layer_rules,
        "via_rules": via_rules,
        "trace_rules": trace_rules,
        "ground_strategy": ground_strategy(zones),
        "routing_status": {
            "phase": "REAL_BOARD_EXTRACTED",
            "drc_risk": "NOT_EXTRACTED",
            "all_critical_planned": all(item.get("critical") is False or item.get("routing_status") in {"ROUTED", "PLANNED"} for item in nets),
            "notes": "Real-board routing extraction completed in read-only mode.",
            "unconnected_count": connectivity["unconnected_count"],
            "ratsnest_status": connectivity["status"],
        },
        "tracks": raw_tracks,
        "traces": traces,
        "vias": vias,
        "not_extracted": unsupported,
        "autorouting_policy": "REVIEW_ONLY",
    }
