# RC-008 Python core review

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-008 |
| CrossReference | [PY-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-17 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial review record | [4cbd1cc] |

---

## Artifact Under Review

- Instance reviewed: [PY-002]
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Modules, functions and constants use snake_case / UPPER_SNAKE; classes PascalCase; exceptions end in `Error`. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names follow the assignment and the dictionary: `is_monday`, `read_quotes`, `pick_random_quote`, `build_message`, `load_settings`, `send_email`, `main`. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format --check` and `ruff check` pass; no `noqa` or other suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy --strict src` passes, so every signature is annotated. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare `except`; `read_quotes` and `send_email` re-raise with `raise ... from error`; the CLI catches only `MondayMotivationError`. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; no builtin is shadowed. |
| 7 | Files, locks and connections are managed with context managers | Pass | The quotes file is read with `with path.open(...)`; the SMTP connection is a `with` block. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every public module, class and function has a Doxygen docstring. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No logging is used; the CLI writes its result to the stream it is given (user output, not diagnostics). Error messages name a variable, never a value; `MailSettings.token` is excluded from `repr`; tests assert the token is absent from output and error text. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | The project has no Design Class Diagram; the Business Case scope has no design artifacts. The few classes are the exception types, `MailSettings` and the `SmtpConnection` protocol. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 48 tests named for behaviour; none opens a network connection (a fake SMTP is injected), none reads `.env` or the real environment (the e2e test runs with a minimal environment). |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` runs without errors; no `Any` is used. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | `dependencies = []`; dev extras pytest, coverage, ruff and mypy are all used. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Constants live in `constants.py` only; the Monday rule lives in `is_monday` only; the quote file is read in `read_quotes` only. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | Imports point inward: `domain` imports only `constants`; `application` imports `domain`; `infrastructure` imports `application` and `domain`; `presentation` wires the rest. No cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Behaviour is added by new functions; `deliver_monday_quote` depends on a `Callable`, and `send_email` on a factory handed in (dependency inversion). No type tests. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | `domain`, `application`, `infrastructure`, `presentation` under `src/monday_motivation/`; `unit`, `integration`, `e2e` under `tests/`. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All names are English ASCII, lowercase snake_case, no spaces. |

## Overall Verdict

Go — all applicable Mandatory criteria pass; criterion 10 is not applicable because the project has no Design Class Diagram. Measured once: 99 % line coverage of `src/` (target 90 %).

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Challenge this stand-in review if wanted | S01 | 2026-10-31 |

---

[PY-002]: ../../../src/monday_motivation/
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[4cbd1cc]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/commit/4cbd1cc75fb65f59682f854b61220fe250707c37
