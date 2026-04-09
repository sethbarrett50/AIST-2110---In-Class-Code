SHELL := /usr/bin/env bash
.DEFAULT_GOAL := help

UV  ?= uv
PY  ?= python
RUFF ?= ruff

help: 
	@echo "Targets:"
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@echo "Examples:"
	@echo "  make sync"

sync: 
	$(UV) sync

lint: ## Lint with ruff and apply safe auto-fixes
	$(UV) run $(RUFF) format .
	$(UV) run $(RUFF) check . --fix

check-out: ## Checks for output cells in Juypter Notebook files
	$(UV) run tools/check_notebook_outputs.py  --verbose

deps.check: ## Check for dependency issues
	uv run deptry .