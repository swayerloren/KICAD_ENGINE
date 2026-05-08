"use strict";

const fs = require("fs");
const os = require("os");
const path = require("path");

function detectPlatform() {
  const raw = process.platform;
  const home = os.homedir();
  if (raw === "win32") {
    return {
      key: "windows",
      raw,
      label: "Windows",
      defaultWorkspacePath: path.join(home, "KICAD_ENGINE"),
      pathSeparator: "\\"
    };
  }
  if (raw === "darwin") {
    return {
      key: "macos",
      raw,
      label: "macOS",
      defaultWorkspacePath: path.join(home, "KICAD_ENGINE"),
      pathSeparator: "/"
    };
  }
  return {
    key: "linux",
    raw,
    label: "Linux",
    defaultWorkspacePath: path.join(home, "KICAD_ENGINE"),
    pathSeparator: "/"
  };
}

function expandPathVariables(inputPath) {
  if (!inputPath) return inputPath;
  let expanded = inputPath
    .replace(/%ProgramFiles%/gi, process.env.ProgramFiles || "C:\\Program Files")
    .replace(/%ProgramFiles\(x86\)%/gi, process.env["ProgramFiles(x86)"] || "C:\\Program Files (x86)")
    .replace(/%LOCALAPPDATA%/gi, process.env.LOCALAPPDATA || "")
    .replace(/%APPDATA%/gi, process.env.APPDATA || "");
  if (expanded.startsWith("~/")) {
    expanded = path.join(os.homedir(), expanded.slice(2));
  }
  return expanded;
}

function pathExists(candidate) {
  try {
    return fs.existsSync(expandPathVariables(candidate));
  } catch (_error) {
    return false;
  }
}

module.exports = {
  detectPlatform,
  expandPathVariables,
  pathExists
};
