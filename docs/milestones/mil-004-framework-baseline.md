# MIL-004: Framework baseline

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [PP-001], [MIL-003] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; accepted with the Go verdict of the review record (autonomous, not independent) | pending |

---

## Purpose

This gate decides whether Monday Motivation has the baseline of the framework: the adopted framework release, the wiki in English, Danish and Malay in the framework's shape (language line first, one sidebar with the Languages section last), the README in the framework template with an appendix that lists only the documents of the repository, complete licence and project URL metadata, a current traceability matrix and reviewed documents, merged to the default branch with a green build. The work is delivered on the branch `mil-004-baseline` and one pull request. It changes no behaviour of the program.

## Deliverable

A merged pull request that holds: the updated Business Case, Project Plan, Artifact Registry and Traceability Matrix and their review records; the wiki sidebar in `docs/wiki/`; the README without the private framework files in its appendix; `pyproject.toml` with the licence expression, the project URLs and a build requirement that reads the licence expression; `.editorconfig` and `.env.example` of the framework baseline; and the framework release adopted by the project. The program and its tests do not change.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | BC-001, PP-001 and MIL-004 each have an `Accepted` Version History row and a review record, and the wiki has a review record | Verdict `Go` (the wiki `Go-with-conditions` until it is checked on the host) | Any missing or `No-Go` |
| 2 | `python -m pytest` runs | Exit code 0 | Any failure |
| 3 | `docs/wiki/` has `_Sidebar.md` and the pages Home, Getting-Started, Usage and Development in en, da and ms, each starting with the language line | 12 pages and the sidebar (and the footer) | A page or language missing |
| 4 | `framework/scripts/check-readme.sh`, `framework/scripts/check-languages.sh` and `framework/scripts/check-editorconfig.sh` run | Exit code 0 | Any finding |
| 5 | `pyproject.toml` sets `license`, `license-files`, the authors and the project URLs for the repository, the documentation and the issue tracker | All set | Any missing |
| 6 | All CI (continuous integration) checks of the pull request | Green | Red or pending |
| 7 | The pull request carries one `Closes #N` line per task of this milestone | Every issue is closed after the merge | An issue stays open |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-003] accepted | Documents and baselines the finished program, its tests and its wiki |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 to 6 | Criterion 2 (the behaviour is unchanged and its tests pass) |
| Objective 7 | Criteria 1, 3, 4, 5 and 7 (documents, wiki, README, licence and issues) |
| Success criterion 7 | Criteria 1 and 6 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in, autonomous mode, not independent) |

## Target Date

2026-11-23: one week after the start, as the Business Case constraint requires.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Adopt the framework release | Track the `framework/` submodule and `.gitmodules`, install the skills and hooks, add `.editorconfig` and bring `.env.example` to the framework's template with the three placeholders of the program, so the project follows the same rules as the other projects of the portfolio. | No | Objective 7 |
| 2 | Update and review the planning documents | Add this milestone to the Business Case and Project Plan, set the domain of the changed documents to education, bring the Traceability Matrix up to date and review each changed document against its QC checklist, so the plan-first gate is met. | No | Objective 7 |
| 3 | Bring the wiki sidebar to the framework's shape | Give the sidebar the wiki title, one list of the English pages and a Languages section last, keeping the existing pages and their names, and add a review record for the wiki. | No | Objective 7 |
| 4 | Bring the README to the framework template | Keep the text of the README, add the framework files to the project layout and give the appendix only the documents that are in the repository, so the README is complete and checkable. | No | Objective 7 |
| 5 | Complete the licence metadata | Set the licence expression and the licence file and the project URLs in `pyproject.toml` and raise the build requirement to the setuptools version that reads a licence expression, so package tools can read them. | No | Objective 7 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-003]: ./mil-003-publish.md
