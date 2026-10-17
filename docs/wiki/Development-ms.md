[English](Development) · [Dansk](Development-da) · **Bahasa Malaysia**

# Pembangunan

## Struktur

| Laluan | Kandungan |
| --- | --- |
| `src/monday_motivation/constants.py` | Semua pemalar |
| `src/monday_motivation/domain/` | Peraturan: `is_monday`, `pick_random_quote`, ralat |
| `src/monday_motivation/application/` | Kes penggunaan `deliver_monday_quote`, `MailSettings` |
| `src/monday_motivation/infrastructure/` | `read_quotes`, `load_settings`, `build_message`, `send_email` |
| `src/monday_motivation/presentation/` | Baris perintah, `main` |
| `tests/` | `unit`, `integration`, `e2e` |

Kebergantungan menghala ke dalam: domain tidak mengimport apa-apa daripada lapisan lain. Sambungan SMTP diberikan kepada `send_email`, jadi ujian menggunakan sambungan palsu dan tidak pernah menyentuh rangkaian.

## Ujian dan semakan

```bash
python -m pytest
ruff check .
ruff format --check .
mypy src
```

![Larian ujian](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/raw/branch/main/docs/images/run-tests.png)

## Dokumentasi API

Kod sumber menggunakan komen Doxygen (`@brief`, `@param`, `@return`, `@raises`).

```bash
doxygen Doxyfile
```

Output HTML ditulis ke `doxygen-out/` dan diabaikan oleh git.
