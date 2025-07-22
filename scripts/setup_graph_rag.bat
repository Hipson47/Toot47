@echo off
setlocal

set "LEGACY_POWERSHELL=%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe"
set "PWSH_EXE="

if exist "%LEGACY_POWERSHELL%" (
    set "PWSH_EXE=%LEGACY_POWERSHELL%"
) else (
    where /q pwsh.exe && set "PWSH_EXE=pwsh.exe"
)

if not defined PWSH_EXE (
    echo [ERROR] PowerShell (powershell.exe or pwsh.exe) could not be found.
    echo Please install PowerShell and ensure it's in your system's PATH.
    exit /b 1
)

echo Found PowerShell executable: %PWSH_EXE%
%PWSH_EXE% -ExecutionPolicy Bypass -NoProfile -File "%~dp0\setup_graph_rag.ps1"

pause
endlocal 