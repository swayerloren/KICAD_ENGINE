"use strict";

const fs = require("fs");
const path = require("path");

function timestamp() {
  return new Date().toISOString().replace(/[:.]/g, "-");
}

function redact(text) {
  if (!text) return "";
  return String(text)
    .replace(/(api[_-]?key|access[_-]?token|secret|password)\s*[:=]\s*["']?[^"'\s]+/gi, "$1=<redacted>")
    .replace(/-----BEGIN [^-]+ PRIVATE KEY-----[\s\S]*?-----END [^-]+ PRIVATE KEY-----/g, "<redacted private key>");
}

function ensureLogDir(workspacePath) {
  const outputDir = path.join(workspacePath, "05_OUTPUTS", "setup_reports");
  fs.mkdirSync(outputDir, { recursive: true });
  return outputDir;
}

function writeSetupLog(workspacePath, entries, filePrefix = "KICAD_ENGINE_INSTALLER_SETUP_LOG") {
  const outputDir = ensureLogDir(workspacePath);
  const logPath = path.join(outputDir, `${filePrefix}_${timestamp()}.md`);
  const lines = [
    "# KiCad Engine Installer Setup Log",
    "",
    `Generated: ${new Date().toISOString()}`,
    `Workspace: \`${redact(workspacePath)}\``,
    "",
    "This log is local. It must not contain credentials, API keys, passwords, or private tokens.",
    "",
    "## Entries",
    ""
  ];
  for (const entry of entries) {
    lines.push(`- ${redact(entry)}`);
  }
  fs.writeFileSync(logPath, `${lines.join("\n")}\n`, "utf8");
  return logPath;
}

module.exports = {
  redact,
  writeSetupLog
};
