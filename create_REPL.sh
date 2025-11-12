#!/usr/bin/env bash

set -euo pipefail

log()  { printf "\033[1;34m[INFO]\033[0m %s\n" "$*"; }
warn() { printf "\033[1;33m[WARN]\033[0m %s\n" "$*"; }
err()  { printf "\033[1;31m[ERR ]\033[0m %s\n" "$*" >&2; }

trap 'err "Failed at line $LINENO. Exit status: $?."' ERR

require_cmd() {
  command -v "$1" >/dev/null 2>&1
}

os=$(uname -s 2>/dev/null || echo "Unknown")
case "$os" in
  Darwin|Linux) : ;;  
  *) err "Unsupported OS: $os. This script supports macOS and Linux only."; exit 1 ;;
esac

# Try to resolve a Python 3 interpreter
PY=""
pick_python() {
  if require_cmd python3; then
    PY="python3"
    return 0
  fi
  if require_cmd python; then
    # Check major version
    if python -V 2>&1 | grep -qE '^Python 3\.'; then
      PY="python"
      return 0
    fi
  fi
  return 1
}

install_python_macos() {
  if ! require_cmd brew; then
    err "Homebrew is not installed. Install it from https://brew.sh/ and re-run."
    exit 1
  fi
  log "Installing Python via Homebrew..."
  brew update
  brew install python || {
    warn "Default 'python' formula failed, trying python@3.12..."
    brew install python@3.12
    if ! require_cmd python3; then
      warn "Linking Homebrew python..."
      brew link python@3.12 --force || true
    fi
  }
}

install_python_linux() {
  if require_cmd apt-get; then
    log "Installing Python via apt-get..."
    sudo apt-get update -y
    sudo apt-get install -y python3 python3-pip python3-venv
  elif require_cmd dnf; then
    log "Installing Python via dnf..."
    sudo dnf install -y python3 python3-pip
  elif require_cmd yum; then
    log "Installing Python via yum..."
    sudo yum install -y python3 python3-pip
  elif require_cmd pacman; then
    log "Installing Python via pacman..."
    sudo pacman -Sy --noconfirm python
  elif require_cmd zypper; then
    log "Installing Python via zypper..."
    sudo zypper --non-interactive install python3
  else
    err "No supported package manager found (apt/dnf/yum/pacman/zypper). Install Python 3 manually and re-run."
    exit 1
  fi
}

ensure_python() {
  if pick_python; then
    log "Found Python: $PY ($($PY -V 2>&1))"
    return 0
  fi

  log "Python 3 not found. Attempting installation..."
  if [ "$os" = "Darwin" ]; then
    install_python_macos
  else
    install_python_linux
  fi

  if ! pick_python; then
    err "Python 3 installation appears to have failed. Please install manually and re-run."
    exit 1
  fi
  log "Installed Python: $PY ($($PY -V 2>&1))"
}

ensure_python

log "Launching Python REPL with an OS-agnostic \`clear\` lambda."
log "Tip: type \`clear()\` in the REPL to clear the screen."
exec "$PY" -i -c 'import os, sys
clear = lambda: os.system("cls" if os.name == "nt" else "clear")
print("\nHelper loaded: clear() -> clears the terminal (os-agnostic). Python", sys.version.split()[0], "\n")'
