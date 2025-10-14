@echo off
REM launch the watcher script with execution policy bypass
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0watch-docfx.ps1"