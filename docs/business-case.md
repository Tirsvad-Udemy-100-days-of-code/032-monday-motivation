# Monday Motivation Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-17 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version: Monday Motivation project baseline | pending |

---

## Executive Summary

Course participants of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp" are set an assignment on day 32: send a motivational quote by email every Monday. This project delivers a small, readable, runnable Python solution to that assignment, with the assignment's function names, tests, documentation and a three-language wiki. It is a portfolio and learning artefact; it has no revenue goal. The solution needs Python 3.13 or later and the standard library only (no runtime dependencies), and is published to the Gitea repository so that other course participants and repository visitors can read, run and compare it.

## Methodological and Standards Foundation

The project follows the SQA and QC framework mounted at `framework/`: artifacts are scaffolded from the framework catalog and reviewed against its QC checklists. Quality characteristics follow ISO/IEC 25010:2023. Requirements and design follow Larman's *Applying UML and Patterns* in the light form that a single-feature program needs. Source code follows the framework's Python conventions and Clean Architecture (domain rules do not import infrastructure).

## Problem Statement

- The assignment is described in a lecture video; there is no reviewed, tested and documented reference solution that the course participant can keep, run and share.
- A bare script that mixes file reading, date logic and SMTP is hard to test and hard to read for other participants.
- Credentials for the mail account must never be committed or printed, and a beginner's script often hard-codes them.

## Business Opportunity

A clean solution lets the course participant demonstrate disciplined practice (plan, test, document) on a small assignment, gives other participants a readable comparison point, and gives repository visitors an idea of how to structure a small Python program without third-party packages.

## Objectives

1. Deliver a program that, on a Monday, picks one random quote from `quotes.txt` and sends it by email with the subject "Monday Motivation".
2. Keep the day check testable by passing the date in, so a test can run on any weekday without patching the clock.
3. Read mail credentials only from environment variables, never from source code, and have no runtime dependencies.
4. Cover the rules with automated `pytest` tests that need neither network nor credentials.
5. Document how to create a local `.venv`, upgrade `pip`, run the program and run the tests, in the README and in a wiki in English, Danish and Bahasa Malaysia, with screenshots.
6. Publish the repository with a description and topics.

## Scope

### In Scope

- Python package under `src/`, tests under `tests/`, documents under `docs/`.
- `constants.py` for constants; `pyproject.toml` for project configuration; Python `.gitignore`; Doxygen comments in the source and a `Doxyfile`.
- Functions named after the assignment's steps: reading the quotes, picking a random quote, checking for Monday, composing and sending the email.
- README from the framework template with screenshots; wiki pages in English, Danish and Bahasa Malaysia with screenshots.
- Repository description and topics on the git host.

### Out of Scope

- Scheduling the program (cron, Task Scheduler, PythonAnywhere); the user starts it.
- A user interface, a web service or a database.
- Providers other than Gmail SMTP as a tested target; the host and port are constants that a reader may change.
- Sending real mail from tests, from CI or from the screenshots; the mail credentials are for the Product Owner's own use and are never imported into the project.
- Translating the framework documents; project documents are written once, in English.

## Expected Benefits

### Tangible Benefits

- A runnable, tested solution published in a public repository.
- A reproducible setup (`.venv`, `pip`, `pytest`) written down in three languages.
- Generated API documentation through Doxygen.

### Intangible Benefits

- Practice of a plan-first, reviewed workflow on a small project.
- A readable reference for other course participants.

## Strategic Alignment

The project supports the Product Owner's learning goal in the 100 Days of Code course and the repository's purpose: documented solutions to the course assignments, shared with other learners.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Automated tests pass | 100 % of tests pass; no test uses the network or a credential | `pytest` exit code 0 on a clean `.venv` |
| 2 | Line coverage of `src/` | At least 90 % | Measured once with `coverage` during the milestone review (not a project dependency) |
| 3 | Runtime dependencies | 0 packages in `[project].dependencies` | Inspection of `pyproject.toml` |
| 4 | Wiki completeness | 3 languages, same page set, each page has at least one screenshot | Page list compared in the milestone review |
| 5 | Secrets in the repository | 0 values | `git grep` for the token variable names finds only names, never values |
| 6 | Setup from a clean clone | A new `.venv` is set up and the tests run in 6 commands or fewer | Following the README once |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| A credential is committed or printed | High: the mail account could be abused | `.env` is ignored by git; credentials are read from environment variables only; no test or screenshot touches them; the review checks with `git grep` |
| Gmail refuses the login (app password needed, policy change) | Medium: the real run fails | The README explains the app password; the failure is raised as a clear error; tests use a fake SMTP object |
| Screenshots show private data | Medium: an address leaks | Screenshots come from a dry run with a placeholder address |
| Translations contain mistakes | Low: a reader is misled | English is authoritative; Danish and Bahasa Malaysia follow it page by page and are marked as checked by the stand-in only |
| Scope grows (scheduling, UI) | Low: the deadline slips | Out of Scope lists them; a change needs a new milestone |

## Assumptions

- The Product Owner is S01 and also develops and reviews; no other person reviews before the plan is accepted.
- The course participants (S02) and repository visitors (S03) cannot be interviewed within this project; their needs are taken from the Product Owner's brief.
- Python 3.13 or later is installed on the machine that runs the program ("greater than 3.13" in the brief is read as 3.13 or later).
- A Gmail app password exists for the Product Owner's account and is supplied only as an environment variable at run time.
- The repository `Tirsvad-Udemy-100-days-of-code/032-monday-motivation` on the Gitea host is the target; the organisation URL in the brief names its owner.

## Constraints

- Python 3.13 or later; `venv` for the environment; `pytest` for tests; `pyproject.toml` for configuration.
- No runtime dependencies unless needed.
- Folder structure `src/`, `tests/`, `docs/`.
- Delivery within 2 weeks: from 2026-10-17 to 2026-10-31.
- One pull request per milestone, on its own branch.
- Credentials are never printed, never passed on a command line and never imported into the project.

## Cost–Benefit Assessment

The assessment is qualitative: the project is a learning exercise with no revenue, so a monetary return would be invented.

| Costs | Benefits |
| --- | --- |
| About 2 weeks of the Product Owner's spare time, mostly review of the AI's work | A tested reference solution and a reusable project template |
| Review effort for each milestone | Documentation in three languages for a wider audience |
| No licence or infrastructure cost (the Gitea host exists) | Public portfolio evidence |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, developer and reviewer: wants a correct, documented solution and a clean process |
| S02 | Course participants: want readable, runnable code with the assignment's function names and clear run instructions |
| S03 | Repository visitors: want a clear description, topics and README, and no runtime dependencies |

## Recommendation

Proceed — the scope is small, the risks are mitigated, and the outcome meets the Product Owner's learning goal and the needs of S02 and S03.

---

[SA-001]: ./stakeholder-analysis.md
