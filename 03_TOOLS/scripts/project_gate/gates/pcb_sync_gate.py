"""PCB_SYNC_GATE."""

from __future__ import annotations

import re

from .base_gate import BLOCKED, FAIL, INCOMPLETE, PASS, BaseGate, GateBlocker


class PCBSyncGate(BaseGate):
    gate_id = "PCB_SYNC_GATE"
    gate_name = "PCB Sync Gate"
    stage = 5

    def evaluate(self):
        pcb_files = self.find_project_files("*.kicad_pcb")
        sync_report = self.first_existing("reports/PCB_SYNC_ORIENTATION_REVIEW.md")
        schematic_gate = self.first_existing("reports/SCHEMATIC_TO_PCB_GATE_STATUS.md")
        drc_report = self.first_existing("_verification/kicad_cli/drc_after_repair.rpt", "_verification/kicad_cli/drc.rpt")
        evidence = [
            self.evidence_path("pcb_file", pcb_files[0] if pcb_files else None),
            self.evidence_path("pcb_sync_orientation_review", sync_report),
            self.evidence_path("schematic_to_pcb_gate_status", schematic_gate),
            self.evidence_path("drc_report", drc_report),
        ]
        if not pcb_files:
            return self.make_result(
                INCOMPLETE,
                "No .kicad_pcb file was found.",
                [self.missing_evidence_blocker("PCB file", "*.kicad_pcb")],
                evidence=evidence,
            )

        blockers = []
        parity_errors = 0
        if drc_report:
            parity_errors = self._parse_parity_errors(self.read_text(drc_report))
            if parity_errors > 0:
                blockers.append(
                    GateBlocker(
                        id="SCHEMATIC_PCB_PARITY_ERRORS",
                        severity="CRITICAL",
                        message=f"DRC report shows {parity_errors} schematic parity/footprint error(s).",
                        evidence_path=self.rel(drc_report),
                        remediation="Resolve schematic-to-PCB parity issues before treating the PCB as synced.",
                    )
                )
        else:
            blockers.append(self.missing_evidence_blocker("DRC schematic parity report", "_verification/kicad_cli/drc_after_repair.rpt"))

        sync_text = self.read_text(sync_report)
        human_review = "NEEDS_HUMAN_REVIEW" in sync_text or "BLOCKED_UNTIL_HUMAN_REVIEW" in sync_text
        if human_review:
            blockers.append(
                GateBlocker(
                    id="PCB_SYNC_HUMAN_REVIEW_REQUIRED",
                    severity="HIGH",
                    message="PCB sync/orientation report requires human review.",
                    evidence_path=self.rel(sync_report),
                    remediation="Complete connector, regulator, polarity, and board-orientation review.",
                )
            )

        if parity_errors > 0:
            status = FAIL
            summary = f"PCB sync fails because DRC reports {parity_errors} schematic parity/footprint issue(s)."
        elif human_review:
            status = BLOCKED
            summary = "PCB sync evidence exists but orientation/human review remains required."
        elif any(blocker.id == "MISSING_EVIDENCE" for blocker in blockers):
            status = INCOMPLETE
            summary = "PCB sync evidence is incomplete."
        else:
            status = PASS
            summary = "PCB sync evidence contains no detected parity blockers."

        return self.make_result(
            status,
            summary,
            blockers=blockers,
            evidence=evidence,
            details={"schematic_parity_errors": parity_errors, "human_review_required": human_review},
        )

    def _parse_parity_errors(self, text: str) -> int:
        match = re.search(r"Found\s+(\d+)\s+Footprint errors", text, re.I)
        if match:
            return int(match.group(1))
        match = re.search(r"SCHEMATIC_PARITY_ISSUES[_\s:=-]+(\d+)", text, re.I)
        if match:
            return int(match.group(1))
        return 0
