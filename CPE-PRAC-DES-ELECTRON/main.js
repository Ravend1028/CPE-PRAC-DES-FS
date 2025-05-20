import { app, BrowserWindow } from 'electron';
import path from 'path';
import { exec } from 'child_process';

let backendProcess;

const createWindow = () => {
  const win = new BrowserWindow({
    width: 1620,
    height: 1420,
    // fullscreen: true,
    webPreferences: {
      nodeIntegration: false
    }
  });

  win.loadURL('http://localhost:5173');
};

app.whenReady().then(() => {
  backendProcess = exec('npm run start-app');

  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });

  app.on('before-quit', () => {
    backendProcess.kill();
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});
