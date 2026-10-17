# MIL-002 Core behaviour

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-17 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [7d48d63] |
| 2026-10-17 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted by S01 as Product Owner after the autonomous run (stand-in review stays on record) | pending |

---

## Purpose

Decides whether the program does what the assignment asks and whether its rules are proven by tests that need neither a network nor a credential.

## Deliverable

A pull request with the working program: reading the quotes, picking a random quote, checking for Monday, composing and sending the email, a command line with a dry run, and a `pytest` suite for each rule.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pytest` passes in a fresh `.venv` with no network and no mail environment variables set | Exit 0 | Any failure or any test that needs a variable |
| 2 | `python -m monday_motivation --dry-run --force` prints the subject and a quote and sends nothing | Output shown, no connection opened | A connection is opened or a credential printed |
| 3 | Line coverage of `src/` measured once with `coverage` | 90 % or more | Below 90 % |
| 4 | A scan of the diff and of `git grep` for the mail credential variable names finds names only, never a value | No value found | A value found |
| 5 | The `qc-programming-python` checklist is applied and the `RC-*` verdict is `Go` | Go | No-Go or Go-with-conditions |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | The layout, configuration and constants must exist first |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1: Monday email with a random quote | BC-001 |
| Objective 2: testable day check | BC-001 |
| Objective 3: environment-variable credentials | BC-001 |
| Objective 4: tests without network | BC-001 |
| Success criteria 1, 2 and 5 | BC-001 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in) |

## Target Date

2026-10-26 — inside the Business Case window.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement is_monday | Write `is_monday(today)` that compares the weekday of a date handed in with the Monday constant, so tests choose the date instead of patching the clock (Business Case objective 2). | No | |
| 2 | Implement read_quotes | Write `read_quotes(path)` that returns the non-empty lines of the quotes file and raises a clear error when the file is missing or empty. | No | |
| 3 | Implement pick_random_quote | Write `pick_random_quote(quotes, rng)` that returns one entry using a `random.Random` handed in, so a test can seed it. | No | |
| 4 | Implement build_message | Write `build_message(sender, recipient, quote)` that returns an `EmailMessage` with the subject "Monday Motivation" and the quote in the body, formatted with an f-string as in the lecture. | No | |
| 5 | Implement load_settings | Write `load_settings(environ)` that reads the sender address, the Gmail app password and the recipient from environment variables named in `constants.py`, fails with a message naming the missing variable, and never includes a value in any message. | No | |
| 6 | Implement send_email | Write `send_email(message, settings, smtp_factory)` that opens the SMTP connection, starts TLS, logs in and sends; the factory is handed in so tests use a fake and no network is touched. | No | |
| 7 | Implement main and the command line | Write `main(argv, today, environ)` that runs the day check, picks the quote and sends the email; `--dry-run` prints instead of sending and `--force` skips the day check. Add `__main__` so `python -m monday_motivation` works. | No | |
| 8 | Write the pytest suite | Add tests for each function and for `main`, using temporary files, a seeded generator and a fake SMTP class; no test reads `.env` or the real environment. | No | |
| 9 | Review the core against the Python checklist | Measure coverage once, run the credential scan, review the code against `qc-programming-python`, write the `RC-*` record and fix findings before the pull request. | No | |

---

[BC-001]: ../business-case.md
[7d48d63]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/commit/7d48d63e6b73c5d2459bac3bd6720751726d1d6f
