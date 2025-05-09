![CodeDiggs Logo](cropped-CodeDiggs_200x200.png)

# Context Tree Neural Layer

[![Test & Lint](https://github.com/your-username/context-tree-nn-layer/actions/workflows/test.yml/badge.svg)](https://github.com/your-username/context-tree-nn-layer/actions/workflows/test.yml)

## Overview
Context-aware neural layer with a dynamic tree structure to store and prioritize persistent clues across training epochs.

## Features
- 🌳 Context tree with node persistence tracking
- 🧠 Re-evaluation logic for persistent clues based on contextual drift
- 🎯 Hierarchical attention prioritizing stable/persistent nodes
- 🧪 Unit test suite and GitHub Actions CI
- 🛠️ CLI interface (`cli.py`) for training, exporting, and visualizing
- 🔁 Auto-version bumping via `make release`
- 📦 PEP 621 compliant `pyproject.toml` (no `setup.py`)
- 🧾 Editable install with verification script `verify_env.py`
- 📘 Docs with Sphinx (`make docs`)
- 🧰 Makefile for automation

## Installation (Python 3.9 recommended)
```bash
git clone https://github.com/your-username/context-tree-nn-layer.git
cd context-tree-nn-layer
python -m venv venv
source venv/Scripts/activate    # Git Bash
pip install -U pip setuptools wheel
pip install -e .
```

## Commands
```bash
make verify     # Check Python, pip, editable install
make install    # Install in editable mode
make test       # Run unit tests
make cli        # Run CLI training/export/plot
make docs       # Build docs locally
make release    # Bump version, tag, push
```

## CLI Usage
```bash
python cli.py --version
python cli.py --train --export --plot
```

## Documentation
Generate local HTML docs:
```bash
make docs
open docs/_build/html/index.html
```

Or deploy via GitHub Pages: Settings → Pages → Source: `/docs`

## Maintainers
This repo is Skoda-style: clear, concise, modular, and testable.
Built with ❤️ by Code Copilot and [you].

