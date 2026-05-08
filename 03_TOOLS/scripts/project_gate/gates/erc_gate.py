"""ERC_GATE.

Read-only aggregation of the latest ERC evidence. This gate does not run
``kicad-cli``; upstream workflow steps are responsible for creating ERC
reports.
"""

from __future__ import annotations

import re

from .base_gate import FAIL, INCOMPLETE, PARTIAL, PASS, BaseGate, GateBlocker


class ERCGate(BaseGate):
    gate_id = "ERC_GATE"
    gate_name = "ERC Gate"
    stage = 2

    def evaluate(self):
        report = self.first_existing(
            "_verification/kicad_cli/erc_after_repair.rpt",
            "_verification/kicad_cli/erc.rpt",
            "reports/ERC_REPORT.md",
            "reports/ERC_DRC_REPORT.md",
        )
        evidence = [self.evidence_path("erc_report", report)]
        if not report:
            return self.make_result(
                INCOMPLETE,
                "No ERC report was found.",
                [self.missing_evidence_blocker("ERC report", "_verification/kicad_cli/erc_after_repair.rpt")],
                evidence=evidence,
            )

        text = self.read_text(report)
        errors, warnings, total = self._parse_counts(text)
        blockers = []
        if errors > 0:
            for idx, item in enumerate(self._extract_error_items(text), start=1):
                blockers.append(
                    GateBlocker(
                        id="ERC_ERROR",
                        severity="CRITICAL",
                        message=item,
                        evidence_path=self.rel(report),
                        remediation="Resolve ERC errors or document explicit human acceptance before continuing.",
                    )
                )
                if idx >= 10:
                    break
            if not blockers:
                blockers.append(
                    GateBlocker(
                        id="ERC_ERRORS_DETECTED",
                        severity="CRITICAL",
                        message=f"ERC report contains {errors} error(s).",
                        evidence_path=self.rel(report),
                        remediation="Resolve ERC errors before PCB progression or fabrication claims.",
                    )
                )
            status = FAIL
            summary = f"ERC failed with {errors} error(s) and {warnings} warning(s)."
        elif warnings > 0:
            status = PARTIAL
            summary = f"ERC has no errors but has {warnings} warning(s)."
        else:
            status = PASS
            summary = "ERC report shows zero errors and zero warnings."

        return self.make_result(
            status,
            summary,
            blockers=blockers,
            evidence=evidence,
            details={"errors": errors, "warnings": warnings, "messages": total},
        )

    def _parse_counts(self, text: str) -> tuple[int, int, int]:
        match = re.search(r"ERC messages:\s*(\d+)\s+Errors\s+(\d+)\s+Warnings\s+(\d+)", text, re.I)
        if match:
            return int(match.group(2)), int(match.group(3)), int(match.group(1))
        errors = len(re.findall(r";\s*error\b", text, re.I))
        warnings = len(re.findall(r";\s*warning\b", text, re.I))
        return errors, warnings, errors + warnings

    def _extract_error_items(self, text: str) -> list[str]:
        lines = text.splitlines()
        items: list[str] = []
        for index, line in enumerate(lines):
            if re.search(r";\s*error\b", line, re.I):
                heading = lines[index - 1].strip() if index > 0 else "ERC error"
                location = lines[index + 1].strip() if index + 1 < len(lines) else ""
                items.append(f"{heading}: {location}".strip(": "))
        return items
