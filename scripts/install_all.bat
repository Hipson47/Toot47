@echo off
setlocal

set "LEGACY_PS=%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe"
set "MODERN_PS="
where /q pwsh.exe && set "MODERN_PS=pwsh.exe"

set "PS_EXE="
if exist "%LEGACY_PS%" (
    set "PS_EXE=%LEGACY_PS%"
) else if defined MODERN_PS (
    set "PS_EXE=%MODERN_PS%"
)

if not defined PS_EXE (
    echo [ERROR] PowerShell is not installed. Please install it and try again.
    exit /b 1
)

echo Using PowerShell: %PS_EXE%
"%PS_EXE%" -ExecutionPolicy Bypass -NoProfile -File "%~dp0\install_all.ps1" %*

endlocal 