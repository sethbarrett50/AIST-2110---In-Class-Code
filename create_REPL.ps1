<# 
.SYNOPSIS
  Ensures Python 3 is installed on Windows and launches a REPL
  with an OS-agnostic `clear` lambda available.

.DESCRIPTION
  - Detects Python 3 (`python3`, `python`, or `py -3`).
  - Installs with winget (preferred). Falls back to Chocolatey or Scoop if present.
  - Starts a REPL with: clear = lambda: os.system("cls" if os.name == "nt" else "clear")

.NOTES
  Requires Windows PowerShell 5.1 or PowerShell 7+. For installation, may require elevation.
#>

#Requires -Version 5.1
$ErrorActionPreference = 'Stop'

function Write-Info { param([string]$Msg) Write-Host "[INFO] $Msg" -ForegroundColor Cyan }
function Write-Warn { param([string]$Msg) Write-Host "[WARN] $Msg" -ForegroundColor Yellow }
function Write-Err  { param([string]$Msg) Write-Host "[ERR ] $Msg" -ForegroundColor Red }

try {
  $isWindows = $true
  if ($PSVersionTable.PSVersion.Major -ge 6) {
    $isWindows = $IsWindows
  } else {
    $isWindows = ([System.Environment]::OSVersion.Platform -eq 'Win32NT')
  }
  if (-not $isWindows) {
    Write-Err "Unsupported OS. This script is for Windows only."
    exit 1
  }
} catch {
  Write-Err "Unable to determine OS: $($_.Exception.Message)"
  exit 1
}

function Ensure-Admin {
  $current = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
  if (-not $current.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Warn "Elevation required for installation. Relaunching as Administrator..."
    $psi = @{
      FilePath  = "powershell.exe"
      ArgumentList = "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", "`"$PSCommandPath`""
      Verb = "RunAs"
    }
    try {
      Start-Process @psi
      exit 0
    } catch {
      Write-Err "Elevation declined or failed: $($_.Exception.Message)"
      exit 1
    }
  }
}

function Test-Command { param([Parameter(Mandatory)][string]$Name) Get-Command $Name -ErrorAction SilentlyContinue | ForEach-Object { $_ } }

function Get-PythonCandidate {
  $cmd = Test-Command -Name 'python3'
  if ($cmd) {
    $ver = & $cmd.Source -V 2>&1
    if ($ver -match '^Python 3\.') { return @{ Cmd = $cmd.Source; Args = @() } }
  }
  $cmd = Test-Command -Name 'python'
  if ($cmd) {
    $ver = & $cmd.Source -V 2>&1
    if ($ver -match '^Python 3\.') { return @{ Cmd = $cmd.Source; Args = @() } }
  }
  $cmd = Test-Command -Name 'py'
  if ($cmd) {
    $ver = & $cmd.Source -3 -V 2>&1
    if ($LASTEXITCODE -eq 0 -and $ver -match '^Python 3\.') { return @{ Cmd = $cmd.Source; Args = @('-3') } }
  }
  return $null
}

function Install-Python {
  $winget = Test-Command -Name 'winget'
  if ($winget) {
    Write-Info "Installing Python 3 via winget..."
    Ensure-Admin
    try {
      & $winget.Source install --id Python.Python.3 -e --source winget `
        --accept-package-agreements --accept-source-agreements --silent
      return
    } catch {
      Write-Warn "winget install failed: $($_.Exception.Message)"
    }
  } else {
    Write-Warn "winget not found."
  }

  $choco = Test-Command -Name 'choco'
  if ($choco) {
    Write-Info "Installing Python 3 via Chocolatey..."
    Ensure-Admin
    try {
      & $choco.Source install python -y
      return
    } catch {
      Write-Warn "Chocolatey install failed: $($_.Exception.Message)"
    }
  } else {
    Write-Warn "Chocolatey not found."
  }

  $scoop = Test-Command -Name 'scoop'
  if ($scoop) {
    Write-Info "Installing Python 3 via Scoop..."
    try {
      & $scoop.Source install python
      return
    } catch {
      Write-Warn "Scoop install failed: $($_.Exception.Message)"
    }
  } else {
    Write-Warn "Scoop not found."
  }

  Write-Err "No supported package manager succeeded (winget/choco/scoop). Install Python 3 manually and re-run."
  exit 1
}

function Ensure-Python {
  $py = Get-PythonCandidate
  if ($py) {
    $ver = & $py.Cmd @($py.Args + '-V') 2>&1
    Write-Info "Found Python: $($py.Cmd) $($py.Args -join ' ') ($ver)"
    return $py
  }

  Write-Info "Python 3 not found. Attempting installation..."
  Install-Python

  $py = Get-PythonCandidate
  if (-not $py) {
    Write-Err "Python 3 installation appears to have failed. Please install manually and re-run."
    exit 1
  }
  $ver = & $py.Cmd @($py.Args + '-V') 2>&1
  Write-Info "Installed Python: $($py.Cmd) $($py.Args -join ' ') ($ver)"
  return $py
}


$python = Ensure-Python

Write-Info "Launching Python REPL with an OS-agnostic 'clear' lambda."
Write-Info "Tip: type 'clear()' in the REPL to clear the screen."
$pyArgs = $python.Args + @('-i', '-c', 'import os, sys; clear = lambda: os.system("cls" if os.name == "nt" else "clear"); print("\nHelper loaded: clear() -> clears the terminal (os-agnostic). Python", sys.version.split()[0], "\n")')
& $python.Cmd @pyArgs