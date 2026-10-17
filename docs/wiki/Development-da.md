[English](Development) · **Dansk** · [Bahasa Malaysia](Development-ms)

# Udvikling

## Opbygning

| Sti | Indhold |
| --- | --- |
| `src/monday_motivation/constants.py` | Alle konstanter |
| `src/monday_motivation/domain/` | Regler: `is_monday`, `pick_random_quote`, fejl |
| `src/monday_motivation/application/` | Brugsscenariet `deliver_monday_quote`, `MailSettings` |
| `src/monday_motivation/infrastructure/` | `read_quotes`, `load_settings`, `build_message`, `send_email` |
| `src/monday_motivation/presentation/` | Kommandolinjen, `main` |
| `tests/` | `unit`, `integration`, `e2e` |

Afhængighederne peger indad: domænet importerer intet fra de andre lag. SMTP-forbindelsen gives til `send_email`, så testene bruger en falsk forbindelse og aldrig rører netværket.

## Tests og kontroller

```bash
python -m pytest
ruff check .
ruff format --check .
mypy src
```

![Testkørslen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/raw/branch/main/docs/images/run-tests.png)

## API-dokumentation

Kildekoden bruger Doxygen-kommentarer (`@brief`, `@param`, `@return`, `@raises`).

```bash
doxygen Doxyfile
```

HTML-outputtet skrives til `doxygen-out/` og ignoreres af git.
