"use strict";

const fs = require("fs");
const path = require("path");
const os = require("os");
const { writeSetupLog } = require("./logWriter");

function normalizeForCompare(inputPath) {
  return path.resolve(inputPath).toLowerCase();
}

function assertSafeWorkspacePath(targetPath) {
  const resolved = path.resolve(targetPath);
  const normalized = normalizeForCompare(resolved);
  const home = normalizeForCompare(os.homedir());
  const unsafePrefixes = [];

  if (process.platform === "win32") {
    unsafePrefixes.push(
      "c:\\windows",
      "c:\\program files\\kicad",
      "c:\\program files (x86)\\kicad",
      "c:\\program files\\",
      "c:\\program files (x86)\\"
    );
  } else if (process.platform === "darwin") {
    unsafePrefixes.push("/applications/kicad", "/system", "/library", "/usr/bin", "/usr/sbin");
  } else {
    unsafePrefixes.push("/usr", "/bin", "/sbin", "/lib", "/lib64", "/etc", "/opt/kicad");
  }

  if (resolved === path.parse(resolved).root) {
    throw new Error("Refusing to install into a filesystem root.");
  }
  for (const prefix of unsafePrefixes) {
    if (normalized === prefix || normalized.startsWith(prefix.endsWith(path.sep) ? prefix : `${prefix}${path.sep}`)) {
      throw new Error(`Refusing unsafe install path: ${resolved}`);
    }
  }
  if (!normalized.startsWith(home) && process.platform !== "win32") {
    throw new Error("For this first installer version, choose a user-writable folder under your home directory.");
  }
  return resolved;
}

function copyRecursive(source, target, result) {
  const stat = fs.lstatSync(source);
  if (stat.isSymbolicLink()) {
    result.skipped.push(`Skipped symlink: ${source}`);
    return;
  }
  if (stat.isDirectory()) {
    fs.mkdirSync(target, { recursive: true });
    for (const entry of fs.readdirSync(source)) {
      copyRecursive(path.join(source, entry), path.join(target, entry), result);
    }
    return;
  }
  if (fs.existsSync(target)) {
    result.skipped.push(`Kept existing file: ${target}`);
    return;
  }
  fs.mkdirSync(path.dirname(target), { recursive: true });
  fs.copyFileSync(source, target);
  result.copied.push(target);
}

function createWorkspace(options) {
  const payloadRoot = path.resolve(options.payloadRoot);
  const templateRoot = path.join(payloadRoot, "repo-template");
  const targetPath = assertSafeWorkspacePath(options.targetPath);

  if (!fs.existsSync(templateRoot)) {
    throw new Error(`Missing payload template: ${templateRoot}`);
  }

  fs.mkdirSync(targetPath, { recursive: true });
  const result = {
    targetPath,
    copied: [],
    skipped: [],
    warnings: []
  };
  copyRecursive(templateRoot, targetPath, result);

  const markerPath = path.join(targetPath, ".kicad-engine-workspace.json");
  const marker = {
    name: "KICAD_ENGINE",
    createdOrUpdatedAt: new Date().toISOString(),
    installerVersion: options.installerVersion || "0.1.0",
    note: "Created by KiCad Engine Installer. This file does not contain credentials."
  };
  if (!fs.existsSync(markerPath)) {
    fs.writeFileSync(markerPath, `${JSON.stringify(marker, null, 2)}\n`, "utf8");
    result.copied.push(markerPath);
  } else {
    result.skipped.push(`Kept existing file: ${markerPath}`);
  }

  const logEntries = [
    `Workspace path: ${targetPath}`,
    `Payload template: ${templateRoot}`,
    `Files copied: ${result.copied.length}`,
    `Existing files skipped: ${result.skipped.length}`,
    "Installed KiCad folders were not modified.",
    "No credentials were requested or stored."
  ];
  result.setupLog = writeSetupLog(targetPath, logEntries);
  return result;
}

module.exports = {
  assertSafeWorkspacePath,
  createWorkspace
};
