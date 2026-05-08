"use strict";

const path = require("path");
const { runCommand, commandExists } = require("./commandRunner");

async function findPython() {
  const candidates = process.platform === "win32" ? ["python", "py"] : ["python3", "python"];
  for (const command of candidates) {
    const exists = await commandExists(command);
    if (exists.found) return command;
  }
  return "";
}

async function runHealthCheck(workspacePath) {
  const python = await findPython();
  if (!python) {
    throw new Error("Python was not found. Cannot run health_check.py.");
  }
  const healthScript = path.join(workspacePath, "health_check.py");
  const args = python === "py"
    ? ["-3", healthScript, "--repo-root", workspacePath]
    : [healthScript, "--repo-root", workspacePath];
  const command = python;
  return runCommand({
    command,
    args,
    cwd: workspacePath,
    timeoutMs: 120000
  });
}

module.exports = {
  runHealthCheck
};
