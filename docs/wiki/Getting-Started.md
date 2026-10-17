**English** · [Dansk](Getting-Started-da) · [Bahasa Malaysia](Getting-Started-ms)

# Getting started

## Requirements

- Python 3.13 or later
- Git
- A Gmail account with an app password, only for a real send

## Create the local `.venv`

Windows (PowerShell):

```powershell
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation.git
cd 032-monday-motivation
py -3.13 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Check the installation

```bash
python -m pytest
```

![The test run](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/raw/branch/main/docs/images/run-tests.png)
