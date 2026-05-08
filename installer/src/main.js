"use strict";

const path = require("path");
const { app, BrowserWindow, dialog, ipcMain, shell } = require("electron");
const { detectPlatform } = require("./installer-core/platformDetect");
const { checkDependencies, installDependency } = require("./installer-core/dependencyCheck");
const { createWorkspace } = require("./installer-core/workspaceCreate");
const { runHealthCheck } = require("./installer-core/healthCheckRunner");
const { runCommand, commandExists } = require("./installer-core/commandRunner");

let mainWindow;

function installerRoot() {
  return app.isPackaged ? process.resourcesPath : app.getAppPath();
}

function payloadRoot() {
  return path.join(installerRoot(), "payload");
}

function manifestsRoot() {
  return path.join(payloadRoot(), "manifests");
}

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1120,
    height: 760,
    minWidth: 900,
    minHeight: 640,
    title: "KiCad Engine Installer",
    webPreferences: {
      preload: path.join(__dirname, "preload.js"),
      nodeIntegration: false,
      contextIsolation: true
    }
  });

  mainWindow.loadFile(path.join(__dirname, "renderer", "index.html"));
}

app.whenReady().then(() => {
  createWindow();
  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") app.quit();
});

ipcMain.handle("installer:getInitialState", async () => {
  const platform = detectPlatform();
  return {
    platform,
    payloadRoot: payloadRoot(),
    defaultWorkspacePath: platform.defaultWorkspacePath,
    installerVersion: app.getVersion()
  };
});

ipcMain.handle("installer:chooseWorkspacePath", async () => {
  const result = await dialog.showOpenDialog(mainWindow, {
    title: "Choose KiCad Engine workspace folder",
    properties: ["openDirectory", "createDirectory"]
  });
  if (result.canceled || !result.filePaths.length) return null;
  return result.filePaths[0];
});

ipcMain.handle("installer:checkDependencies", async () => {
  return checkDependencies({ manifestsRoot: manifestsRoot() });
});

ipcMain.handle("installer:installDependency", async (_event, payload) => {
  return installDependency({
    manifestsRoot: manifestsRoot(),
    dependencyId: payload.dependencyId,
    confirmed: Boolean(payload.confirmed)
  });
});

ipcMain.handle("installer:createWorkspace", async (_event, payload) => {
  return createWorkspace({
    payloadRoot: payloadRoot(),
    targetPath: payload.targetPath,
    installerVersion: app.getVersion()
  });
});

ipcMain.handle("installer:runHealthCheck", async (_event, payload) => {
  return runHealthCheck(payload.workspacePath);
});

ipcMain.handle("installer:openVSCode", async (_event, payload) => {
  const exists = await commandExists("code");
  if (exists.found) {
    return runCommand({
      command: "code",
      args: [payload.workspacePath],
      timeoutMs: 10000
    });
  }
  await shell.openPath(payload.workspacePath);
  return {
    ok: false,
    exitCode: null,
    stdout: "",
    stderr: "VS Code command was not found. Opened the workspace folder instead."
  };
});
