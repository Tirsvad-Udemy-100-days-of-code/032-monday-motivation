# MIL-001 Foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-17 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decides whether the project skeleton, configuration and tooling are sound enough to build the program on. A No-Go sends the work back before any behaviour is coded.

## Deliverable

A pull request that adds the `src/` and `tests/` layout, `pyproject.toml`, `.gitignore`, `constants.py`, the `Doxyfile` and the quotes data file, with a passing smoke test in a fresh `.venv`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pip install -e .[dev]` and `pytest` succeed in a fresh `.venv` created with the commands documented in the pull request | Both exit 0 | Either fails |
| 2 | `pyproject.toml` requires Python 3.13 or later and lists no runtime dependencies | `dependencies = []` | Any runtime dependency |
| 3 | `git check-ignore .env .venv` lists both | Both ignored | Either is tracked |
| 4 | `doxygen Doxyfile` runs without errors | Exit 0, no error output | Errors |
| 5 | The `qc-programming-python` checklist is applied to the code and the `RC-*` verdict is `Go` | Go | No-Go or Go-with-conditions |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First gateway; follows the accepted Project Plan |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 3: no runtime dependencies, credentials not in source | BC-001 |
| Objective 4: tests with `pytest` | BC-001 |
| Success criteria 3 and 5 | BC-001 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in) |

## Target Date

2026-10-21 — inside the Business Case window 2026-10-17 to 2026-10-31.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create the source layout and pyproject.toml | Add `src/monday_motivation/` and `tests/` and a `pyproject.toml` that sets `requires-python >= 3.13`, an empty runtime dependency list, a `dev` extra with `pytest`, the pytest `pythonpath` and test paths, and a console entry point. This is the configuration the Business Case constrains (Python 3.13+, `venv`, `pytest`, `pyproject.toml`). | No | |
| 2 | Add the Python .gitignore | Add the standard Python `.gitignore` plus `.env`, `.venv/`, Doxygen output and test caches, so credentials and generated files never reach the repository (Business Case risk: credential committed). | No | |
| 3 | Add constants.py | Create `constants.py` holding every constant: mail subject, SMTP host and port, quotes file name, the weekday number of Monday and the names of the environment variables that carry the credentials. The brief requires constants in one file. | No | |
| 4 | Add the quotes data file | Copy the course's `quotes.txt` (100 quotes, one per line) into the package as data so the program finds it from an installed or editable package, independent of the working directory. | No | |
| 5 | Add the Doxyfile | Create a `Doxyfile` for the `src/` tree that writes HTML to an ignored folder, and document the Doxygen comment style used in the source (`@file`, `@brief`, `@param`, `@return`). | No | |
| 6 | Add the package smoke test | Add one test that imports the package and reads the constants, proving the `.venv`, editable install and pytest wiring work before behaviour is built. | No | |
| 7 | Review the foundation against the Python checklist | Review the code against `qc-programming-python`, write the `RC-*` record and fix findings before the pull request. | No | |

---

[BC-001]: ../business-case.md
