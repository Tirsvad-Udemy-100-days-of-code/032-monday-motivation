# Monday Motivation Domain Dictionary

## Metadata
| Key | Value |
| --- | --- |
| ID | DICT-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-17 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version: eight terms | [7d48d63] |
| 2026-10-17 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted by S01 as Product Owner after the autonomous run (stand-in review stays on record) | [61e13cd] |

---

## Purpose and Scope

Maps each Product Owner (PO) term of the Monday Motivation project to its professional IT term. PO language: English (`en`); PO domain: Software and IT (`it`). The PO terms are the words of the course assignment; the IT terms are the names used in code and design.

## Dictionary

| PO term | Language | IT term | Definition | Used as PO term in | Used as IT term in |
| --- | --- | --- | --- | --- | --- |
| quote | en | Quote | A single motivational sentence with its author, kept as one line of text. | BC, SA | source code |
| quotes list | en | Quote source | The text file with one quote per line from which a quote is chosen. | BC | source code |
| Monday email | en | Notification message | The email with the subject "Monday Motivation" that carries one quote. | BC, SA, MIL | source code |
| day check | en | Weekday check | The test whether a given date is a Monday. | BC, MIL | source code |
| random pick | en | Random selection | The choice of one quote from the list by chance. | BC, MIL | source code |
| mail password | en | App password | The secret that lets the program log in to the mail account; it is never stored in the project. | BC, SA | source code |
| test send | en | Dry run | A run that shows the message on screen and sends nothing. | BC, MIL | source code |
| mail account | en | SMTP account | The Gmail account that the program logs in to and sends from. | BC, SA | source code |

## Rules

- The Domain Model, use cases and user stories use the PO term; the Operation Contract, Sequence Diagram, Design Class Diagram and ERD use the IT term. This project has none of those artifacts; source code uses the IT term.
- One IT term per PO term and one PO term per IT term; no synonyms.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[7d48d63]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/commit/7d48d63e6b73c5d2459bac3bd6720751726d1d6f
[61e13cd]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/commit/61e13cdbe9cffdc9181e78eb16036f80bd3942d5
