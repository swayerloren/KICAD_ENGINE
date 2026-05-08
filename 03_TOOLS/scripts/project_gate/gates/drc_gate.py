"""DRC_GATE.

Read-only aggregation of the latest DRC evidence. This gate does not run
``kicad-cli``; it parses existing DRC reports created by earlier workflow
steps.
"""

from __future__ import annotations

import re

from .base_gate import FAIL, INCOMPLETE, PASS, BaseGate, GateBlocker


class DRCGate(BaseGate):
    gate_id = "DRC_GATE"
    gate_name = "DRC Gate"
    stage = 6

    def evaluate(self):
        report = self.first_existing("_verification/kicad_cli/drc_after_repair.rpt", "_verification/kicad_cli/drc.rpt")
        evidence = [self.evidence_path("drc_report", report)]
        if not report:
            return self.make_result(
                INCOMPLETE,
                "No DRC report was found.",
                [self.missing_evidence_blocker("DRC report", "_verification/kicad_cli/drc_after_repair.rpt")],
                evidence=evidence,
            )

        text = self.read_text(report)
        violations = self._parse_count(text, r"Found\s+(\d+)\s+DRC violations")
        unconnected_pads = self._parse_count(text, r"Found\s+(\d+)\s+unconnected pads")
        footprint_errors = self._parse_count(text, r"Found\s+(\d+)\s+Footprint errors")
        blockers = []
        if violations > 0:
            blockers.append(
                GateBlocker(
                    id="DRC_VIOLATIONS_DETECTED",
                    severity="CRITICAL",
                    message=f"DRC report shows {violations} DRC violation(s).",
                    evidence_path=self.rel(report),
                    remediation="Resolve DRC violations or document explicit human acceptance before continuing.",
                )
            )
        if footprint_errors > 0:
            blockers.append(
                GateBlocker(
                    id="DRC_SCHEMATIC_PARITY_ERRORS",
                    severity="CRITICAL",
                    message=f"DRC report shows {footprint_errors} footprint/schematic parity error(s).",
                    evidence_path=self.rel(report),
                    remediation="Resolve schematic-to-PCB parity issues.",
                )
            )
        if unconnected_pads > 0:
            blockers.append(
                GateBlocker(
                    id="DRC_UNCONNECTED_PADS",
                    severity="CRITICAL",
                    message=f"DRC report shows {unconnected_pads} unconnected pad(s).",
                    evidence_path=self.rel(report),
                    remediation="Route or intentionally document every unconnected pad before passing DRC.",
                )
            )

        status = FAIL if blockers else PASS
        summary = (
            f"DRC failed: {violations} DRC violation(s), {footprint_errors} parity issue(s), "
            f"{unconnected_pads} unconnected pad(s)."
            if blockers
            else "DRC report shows no violations, parity issues, or unconnected pads."
        )
        return self.make_result(
            status,
            summary,
            blockers=blockers,
            evidence=evidence,
            details={
                "drc_violations": violations,
                "footprint_or_parity_errors": footprint_errors,
                "unconnected_pads": unconnected_pads,
            },
        )

    def _parse_count(self, text: str, pattern: str) -> int:
        match = re.search(pattern, text, re.I)
        return int(match.group(1)) if match else 0
