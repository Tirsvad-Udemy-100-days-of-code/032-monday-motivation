**English** · [Dansk](Development-da) · [Bahasa Malaysia](Development-ms)

# Development

## Layout

| Path | Content |
| --- | --- |
| `src/monday_motivation/constants.py` | Every constant |
| `src/monday_motivation/domain/` | Rules: `is_monday`, `pick_random_quote`, errors |
| `src/monday_motivation/application/` | The use case `deliver_monday_quote`, `MailSettings` |
| `src/monday_motivation/infrastructure/` | `read_quotes`, `load_settings`, `build_message`, `send_email` |
| `src/monday_motivation/presentation/` | The command line, `main` |
| `tests/` | `unit`, `integration`, `e2e` |

Dependencies point inward: the domain imports nothing from the other layers. The SMTP connection is handed to `send_email`, so tests use a fake and never touch the network.

## Tests and checks

```bash
python -m pytest
ruff check .
ruff format --check .
mypy src
```

![The test run](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/raw/branch/main/docs/images/run-tests.png)

## API documentation

The source uses Doxygen comments (`@brief`, `@param`, `@return`, `@raises`).

```bash
doxygen Doxyfile
```

The HTML output is written to `doxygen-out/` and is ignored by git.
