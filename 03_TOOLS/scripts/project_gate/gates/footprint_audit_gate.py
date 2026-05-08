"""FOOTPRINT_AUDIT_GATE."""

from __future__ import annotations

import re

from .base_gate import BLOCKED, FAIL, INCOMPLETE, PARTIAL, PASS, BaseGate, GateBlocker


class FootprintAuditGate(BaseGate):
    gate_id = "FOOTPRINT_AUDIT_GATE"
    gate_name = "Footprint Audit Gate"
    stage = 4

    def evaluate(self):
        report = self.first_existing("reports/FOOTPRINT_PACKAGE_AUDIT.md")
        validation = self.first_existing("reports/project_validation/project_validation_report.md")
        evidence = [
            self.evidence_path("footprint_package_audit", report),
            self.evidence_path("project_validation_report", validation),
        ]
        if not report:
            return self.make_result(
                INCOMPLETE,
                "No footprint/package audit report was found.",
                [self.missing_evidence_blocker("footprint/package audit", "reports/FOOTPRINT_PACKAGE_AUDIT.md")],
                evidence=evidence,
            )

        text = self.read_text(report)
        status_line = self._status_line(text)
        blockers = []
        if "BLOCKED_UNTIL_HUMAN_REVIEW" in text or "NEEDS_HUMAN_REVIEW" in text:
            for item in self._remaining_blockers(text):
                blockers.append(
                    GateBlocker(
                        id="FOOTPRINT_HUMAN_REVIEW_REQUIRED",
                        severity="HIGH",
                        message=item,
                        evidence_path=self.rel(report),
                        remediation="Verify exact package drawing, footprint, pin mapping, orientation, and polarity before passing this gate.",
                    )
                )
            if not blockers:
                blockers.append(
                    GateBlocker(
                        id="FOOTPRINT_HUMAN_REVIEW_REQUIRED",
                        severity="HIGH",
                        message="Footprint audit report requires human review.",
                        evidence_path=self.rel(report),
                    )
                )
            status = BLOCKED
            summary = f"Footprint audit status is {status_line or 'NEEDS_HUMAN_REVIEW'}."
        elif re.search(r"Status:\s*`?FAIL", text, re.I):
            status = FAIL
            summary = "Footprint audit report indicates failure."
        elif "UNVERIFIED" in text:
            status = PARTIAL
            summary = "Footprint audit exists but contains unverified items."
        else:
            status = PASS
            summary = "Footprint audit report exists and contains no obvious blockers."

        return self.make_result(
            status,
            summary,
            blockers=blockers,
            evidence=evidence,
            details={"report_status": status_line, "human_review_terms_present": "NEEDS_HUMAN_REVIEW" in text},
        )

    def _status_line(self, text: str) -> str:
        match = re.search(r"Status:\s*`?([^`\n]+)`?", text, re.I)
        return match.group(1).strip() if match else ""

    def _remaining_blockers(self, text: str) -> list[str]:
        if "## Remaining Footprint Blockers" not in text:
            return []
        section = text.split("## Remaining Footprint Blockers", 1)[1].split("\n## ", 1)[0]
        return [re.sub(r"^\d+\.\s*", "", line.strip()) for line in section.splitlines() if re.match(r"\d+\.\s+", line.strip())]
