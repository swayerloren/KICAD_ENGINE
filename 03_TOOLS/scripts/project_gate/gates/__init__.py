"""Gate modules for the read-only KiCad Engine project gate runner."""

from .base_gate import (
    BLOCKED,
    FAIL,
    INCOMPLETE,
    NOT_APPLICABLE,
    PARTIAL,
    PASS,
    BaseGate,
    GateBlocker,
    GateEvidence,
    GateResult,
)
from .drc_gate import DRCGate
from .erc_gate import ERCGate
from .fab_readiness_gate import FabReadinessGate
from .footprint_audit_gate import FootprintAuditGate
from .pcb_sync_gate import PCBSyncGate
from .pcb_visual_gate import PCBVisualGate
from .schematic_annotation_gate import SchematicAnnotationGate
from .schematic_visual_gate import SchematicVisualGate
from .unrouted_nets_gate import UnroutedNetsGate

GATE_SEQUENCE = [
    SchematicAnnotationGate,
    ERCGate,
    SchematicVisualGate,
    FootprintAuditGate,
    PCBSyncGate,
    DRCGate,
    PCBVisualGate,
    UnroutedNetsGate,
    FabReadinessGate,
]

__all__ = [
    "BLOCKED",
    "FAIL",
    "INCOMPLETE",
    "NOT_APPLICABLE",
    "PARTIAL",
    "PASS",
    "BaseGate",
    "GateBlocker",
    "GateEvidence",
    "GateResult",
    "GATE_SEQUENCE",
    "SchematicAnnotationGate",
    "ERCGate",
    "SchematicVisualGate",
    "FootprintAuditGate",
    "PCBSyncGate",
    "DRCGate",
    "PCBVisualGate",
    "UnroutedNetsGate",
    "FabReadinessGate",
]
