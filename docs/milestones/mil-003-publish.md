# MIL-003 Documentation and publication

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
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

Decides whether the project can be shown to course participants and repository visitors: documented in three languages with screenshots, and published with a description and topics.

## Deliverable

A pull request with the README, screenshots, the wiki in English, Danish and Bahasa Malaysia, and the repository description and topics set on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The README follows `framework/templates/README-template.md` and `bash framework/scripts/check-readme.sh` passes | Exit 0 | Failures |
| 2 | The README and every wiki page contain at least one screenshot that exists in the repository | All images resolve | A missing image |
| 3 | The wiki has the same page set in English, Danish (`-da`) and Bahasa Malaysia (`-ms`), and each page starts with the language line | Same set in all three | A page is missing |
| 4 | Following the README from a clean clone creates `.venv`, upgrades `pip`, installs and runs the tests | Tests pass | Any step fails |
| 5 | Repository description and topics are set on the git host | Both present when read back through the API | Either missing |
| 6 | `bash framework/scripts/check-languages.sh` passes and the review records of the documents are `Go` | Pass and Go | Fail |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The program must work before it is documented |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 5: documented setup, run and test in three languages with screenshots | BC-001 |
| Objective 6: description and topics | BC-001 |
| Success criteria 4 and 6 | BC-001 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in) |

## Target Date

2026-10-31 — the end of the Business Case window.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the README | Create `README.md` from the framework template: overview, requirements, setup with `python -m venv .venv` and `python -m pip install --upgrade pip`, run, tests, license and links. S02 and S03 read it first. | No | |
| 2 | Capture the screenshots | Run the program with `--dry-run` using a placeholder address, render the real captured output as an image with the local browser and save the images in `docs/images/` for the README and the wiki. No credential or real address appears in them. | No | |
| 3 | Write the English wiki | Add `docs/wiki/` pages Home, Getting-Started, Usage and Development with `_Sidebar.md` and `_Footer.md`. English is the authoritative text. | No | |
| 4 | Write the Danish wiki | Add the same page set as `<Page>-da.md`, translated page by page; code, commands and file names stay English. | No | |
| 5 | Write the Bahasa Malaysia wiki | Add the same page set as `<Page>-ms.md`, translated page by page; code, commands and file names stay English. | No | |
| 6 | Publish the wiki | Make the wiki pages reach the git host's wiki (Gitea wiki repository or the publish workflow) and check the three languages are listed. | No | |
| 7 | Set the repository description and topics | Set the description and topics (python, udemy, 100-days-of-code, email, smtp, pytest, motivation) through the Gitea API and read them back. | No | |
| 8 | Generate and check the Doxygen documentation | Run `doxygen Doxyfile`, confirm the output has no warnings for the public functions, and keep the output ignored by git. | No | |
| 9 | Final review and project summary | Update the Traceability Matrix, run the framework checks, write the `RC-*` records and prepare the end-of-run summary. | No | |

---

[BC-001]: ../business-case.md
[7d48d63]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/commit/7d48d63e6b73c5d2459bac3bd6720751726d1d6f
