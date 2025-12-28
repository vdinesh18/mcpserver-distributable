# mcpserver-distributable

Portable distributable package for MCP server components.

## Description

This repository packages the `mcpserver` module for distribution and provides
utility scripts and tests. It includes a minimal example (`test.py`) and
packaging metadata in `pyproject.toml`.

## Prerequisites

- Python 3.13+
- Git

## Quickstart

Create and activate a virtual environment, install dependencies, and run tests:

PowerShell:
```powershell
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass; .\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
if (Test-Path requirements.txt) { pip install -r requirements.txt }
python test.py
```

CMD:
```cmd
python -m venv venv
venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
python test.py
```


## Packaging

Build a source / wheel distribution (requires `build` package):

```bash
pip install build
python -m build
```

Install locally:

```bash
pip install .
```

## Usage

- Run `python test.py` to execute the included tests and example outputs.
- The package code lives under `src/mcpserver`.

## CI

CI runs on push/PR via GitHub Actions: ![CI](https://github.com/vdinesh18/mcpserver-distributable/actions/workflows/ci.yml/badge.svg)

## Contributing

1. Fork the repo and create a feature branch.
2. Run tests locally: `python test.py`.
3. Submit a PR targeting `main`.

## License

Specify your license here.
