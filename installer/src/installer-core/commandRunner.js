"use strict";

const path = require("path");
const { spawn, spawnSync } = require("child_process");

function resolveCommand(command) {
  if (process.platform !== "win32") return command;
  if (command.includes("\\") || command.includes("/") || path.extname(command)) return command;
  const result = spawnSync("where", [command], { encoding: "utf8", windowsHide: true });
  if (result.status !== 0 || !result.stdout) return command;
  const candidates = result.stdout.split(/\r?\n/).map((line) => line.trim()).filter(Boolean);
  return candidates.find((candidate) => /\.(cmd|bat|exe)$/i.test(candidate)) || candidates[0] || command;
}

function runCommand(options) {
  const {
    command,
    args = [],
    cwd,
    env = {},
    timeoutMs = 30000,
    shell = false
  } = options;

  return new Promise((resolve) => {
    const startedAt = new Date();
    let stdout = "";
    let stderr = "";
    let timedOut = false;

    let child;
    try {
      let executable = resolveCommand(command);
      const useShell = shell || /\.(cmd|bat)$/i.test(executable);
      if (useShell && process.platform === "win32" && !command.includes("\\") && !command.includes("/")) {
        executable = command;
      }
      child = spawn(executable, args, {
        cwd,
        env: { ...process.env, ...env },
        windowsHide: true,
        shell: useShell
      });
    } catch (error) {
      resolve({
        ok: false,
        command,
        args,
        exitCode: null,
        stdout,
        stderr: String(error.message || error),
        startedAt: startedAt.toISOString(),
        finishedAt: new Date().toISOString(),
        timedOut
      });
      return;
    }

    const timer = setTimeout(() => {
      timedOut = true;
      child.kill();
    }, timeoutMs);

    child.stdout.on("data", (chunk) => {
      stdout += chunk.toString();
    });
    child.stderr.on("data", (chunk) => {
      stderr += chunk.toString();
    });
    child.on("error", (error) => {
      clearTimeout(timer);
      resolve({
        ok: false,
        command,
        args,
        exitCode: null,
        stdout,
        stderr: String(error.message || error),
        startedAt: startedAt.toISOString(),
        finishedAt: new Date().toISOString(),
        timedOut
      });
    });
    child.on("close", (exitCode) => {
      clearTimeout(timer);
      resolve({
        ok: exitCode === 0 && !timedOut,
        command,
        args,
        exitCode,
        stdout: stdout.trim(),
        stderr: stderr.trim(),
        startedAt: startedAt.toISOString(),
        finishedAt: new Date().toISOString(),
        timedOut
      });
    });
  });
}

async function commandExists(command) {
  const lookup = process.platform === "win32"
    ? { command: "where", args: [command], timeoutMs: 8000 }
    : { command: "which", args: [command], timeoutMs: 8000 };
  const result = await runCommand(lookup);
  return {
    found: result.ok,
    path: result.stdout.split(/\r?\n/).find(Boolean) || "",
    detail: result.stdout || result.stderr
  };
}

module.exports = {
  runCommand,
  commandExists
};
