[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Malaysia**

# Mula di sini

## Keperluan

- Python 3.13 atau lebih baharu
- Git
- Akaun Gmail dengan kata laluan aplikasi, hanya untuk penghantaran sebenar

## Cipta `.venv` setempat

Windows (PowerShell):

```powershell
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation.git
cd 032-monday-motivation
py -3.13 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux dan macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Semak pemasangan

```bash
python -m pytest
```

![Larian ujian](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/raw/branch/main/docs/images/run-tests.png)
