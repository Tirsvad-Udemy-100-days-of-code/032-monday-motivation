[English](Getting-Started) · **Dansk** · [Bahasa Malaysia](Getting-Started-ms)

# Kom i gang

## Krav

- Python 3.13 eller nyere
- Git
- En Gmail-konto med en appadgangskode, kun for en rigtig afsendelse

## Opret det lokale `.venv`

Windows (PowerShell):

```powershell
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation.git
cd 032-monday-motivation
py -3.13 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux og macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Kontrollér installationen

```bash
python -m pytest
```

![Testkørslen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/raw/branch/main/docs/images/run-tests.png)
