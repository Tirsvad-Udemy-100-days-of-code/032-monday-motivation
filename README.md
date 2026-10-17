# 🚀 Monday Motivation

Send a motivational quote by email every Monday: a small, tested Python solution to day 32 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp", for course participants and anyone browsing for ideas.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

On a Monday the program reads `quotes.txt` (one quote per line), picks a random quote and emails it with the subject "Monday Motivation" through Gmail SMTP. It has no runtime dependencies: only the Python standard library.

![A dry run showing the email][shot-dry-run]

| Part | What it is for |
| --- | --- |
| `src/monday_motivation/` | The program, in four layers: `domain`, `application`, `infrastructure`, `presentation`; every constant is in `constants.py` |
| `tests/` | `pytest` tests (`unit`, `integration`, `e2e`); none uses the network or a credential |
| `docs/` | Project documents, the wiki pages (English, Danish, Bahasa Malaysia) and the screenshots |
| `Doxyfile` | Doxygen configuration for the API documentation |

The functions follow the assignment's steps: `is_monday`, `read_quotes`, `pick_random_quote`, `build_message`, `load_settings`, `send_email` and `main`. The date is handed to `is_monday`, so a test can use any day without patching the clock.

## 📋 Requirements

- Python 3.13 or later, to run the program and the tests.
- A Gmail account with an [app password][app-password], only to send a real email. A dry run needs none.
- Doxygen, only to build the API documentation.

## 🛠️ Setup

Create a local virtual environment, upgrade `pip` and install the package with the development tools.

Windows (PowerShell):

```powershell
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

To send a real email, put the sender, the app password and the recipient in the environment. Never write them in a file that is committed; `.env` is ignored by git and `.env.example` shows the names.

```bash
export GMAIL_ADDRESS="you@gmail.com"
export GMAIL_TOKEN="your app password"
export MONDAY_RECIPIENT="friend@example.com"
```

## ▶️ Run

```bash
python -m monday_motivation --dry-run --force   # show the email, send nothing, any day
python -m monday_motivation                     # send a real email, only on a Monday
```

| Option | Meaning |
| --- | --- |
| `--dry-run` | Show the email instead of sending it; no credential is needed |
| `--force` | Run on any day, not only on a Monday |
| `--quotes PATH` | Use another quotes file, one quote per line |

On any other day the program says so and sends nothing:

![Run on a day that is not a Monday][shot-not-monday]

## 🧪 Tests

```bash
python -m pytest
```

![The test run][shot-tests]

Optional checks: `ruff check .`, `ruff format --check .`, `mypy src`. The API documentation is built with `doxygen Doxyfile` (output in `doxygen-out/`).

## 📄 License

GNU Affero General Public License v3.0: see [LICENSE][license].

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Domain dictionary][DICT-001] | The PO terms and the IT terms |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/issues
[license]: ./LICENSE
[app-password]: https://support.google.com/accounts/answer/185833
[shot-dry-run]: ./docs/images/run-dry-run.png
[shot-not-monday]: ./docs/images/run-not-monday.png
[shot-tests]: ./docs/images/run-tests.png
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[DICT-001]: ./docs/dictionary.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
