"""UNROUTED_NETS_GATE."""

from __future__ import annotations

import re

from .base_gate import FAIL, INCOMPLETE, PASS, BaseGate, GateBlocker


class UnroutedNetsGate(BaseGate):
    gate_id = "UNROUTED_NETS_GATE"
    gate_name = "Unrouted Nets Gate"
    stage = 8

    def evaluate(self):
        report = self.first_existing("_verification/kicad_cli/drc_after_repair.rpt", "_verification/kicad_cli/drc.rpt")
        evidence = [self.evidence_path("drc_report", report)]
        if not report:
            return self.make_result(
                INCOMPLETE,
                "No DRC report was found for unrouted-net evidence.",
                [self.missing_evidence_blocker("DRC unrouted-net report", "_verification/kicad_cli/drc_after_repair.rpt")],
                evidence=evidence,
            )

        text = self.read_text(report)
        match = re.search(r"Found\s+(\d+)\s+unconnected pads", text, re.I)
        if not match:
            return self.make_result(
                INCOMPLETE,
                "DRC report does not contain an unconnected-pad summary.",
                [self.missing_evidence_blocker("unconnected pad summary", self.rel(report))],
                evidence=evidence,
            )

        unconnected_pads = int(match.group(1))
        if unconnected_pads > 0:
            return self.make_result(
                FAIL,
                f"DRC reports {unconnected_pads} unconnected pad(s).",
                blockers=[
                    GateBlocker(
                        id="UNROUTED_OR_UNCONNECTED_PADS",
                        severity="CRITICAL",
                        message=f"DRC reports {unconnected_pads} unconnected pad(s).",
                        evidence_path=self.rel(report),
                        remediation="Route, intentionally no-connect, or document every unconnected pad before passing.",
                    )
                ],
                evidence=evidence,
                details={"unconnected_pads": unconnected_pads},
            )

        return self.make_result(
            PASS,
            "DRC report shows 0 unconnected pads.",
            evidence=evidence,
            details={"unconnected_pads": unconnected_pads},
        )
