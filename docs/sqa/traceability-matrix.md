# Monday Motivation Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [MIL-004] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-17 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | MIL-003: coverage note on README, wiki and screenshots | [70d79de] |
| 2026-10-17 | Deprecated | Jens Tirsvad Nielsen | S01 | Accepted by S01 as Product Owner after the autonomous run (stand-in review stays on record) | [61e13cd] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added MIL-004, the review records of the baseline and the wiki; domain column brought up to date; reviewed rows brought up to date (autonomous, not independent) | [8530b42] |

---

## Purpose

Tracks backward and forward links between artifact instances so that the Business Case's traceability can be measured. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | education | - | [SA-001], [PP-001], [MIL-001], [MIL-004] | [RC-009] (Go, re-review of the whole document), [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001], [DICT-001] | [RC-002] |
| [DICT-001] | DICT | en | it | [BC-001], [SA-001] | source code | [RC-003] |
| [PP-001] | PP | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004] | [RC-010] (Go, review of the whole document against QC-PP-001, which the plan had not met before) |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | source code, [MIL-002] | [RC-004] |
| [MIL-002] | MIL | en | it | [BC-001], [PP-001], [MIL-001] | source code, [MIL-003] | [RC-005] |
| [MIL-003] | MIL | en | it | [BC-001], [PP-001], [MIL-002] | README, wiki, [MIL-004] | [RC-006] |
| [MIL-004] | MIL | en | education | [BC-001], [PP-001], [MIL-003] | - | [RC-011] (Go) |
| [PY-001] | PY | - | - | [MIL-001] | - | [RC-007] |
| [PY-002] | PY | - | - | [MIL-002], [PY-001] | - | [RC-008] |
| Wiki | Wiki | en, da, ms | education | [BC-001], [MIL-004] | - | [RC-012] (Go-with-conditions) |

## Coverage Notes

- No instance yet of KPI, BMC, BPMN, UCD, US, UC, DM, SSD, OC, SD, DCD, ERD or ADR: the program is a single feature with plain technical tasks (see the Plan Risks and Scope in [PP-001]).
- `-` in Upstream means foundational; in Downstream it means nothing is built on it yet; in Last Reviewed it means no `RC-*` exists.
- Review records of source code are added in the milestone that produces the code. The source code is reviewed in [RC-007] and [RC-008] and not again in [MIL-004], which changes no source file.
- The domain of [BC-001], [PP-001], MIL-004 and the wiki is `education` since [MIL-004]. The other documents keep the domain `it` they were accepted with; a change of their domain would need a new review of each (see the Open Issues of [PP-001]).
- [PP-001] is reviewed against `QC-PP-001` for the first time in [RC-010]; the earlier records of the plan used no checklist.
- The README and the screenshots (`docs/images/`) are documentation, not artifacts with an ID; they are checked with `check-readme.sh` and the Go/No-Go criteria of [MIL-003] and [MIL-004]. The wiki (`docs/wiki/`) has its own review record, [RC-012].
- The review records and this matrix have no QC checklist for themselves and are not reviewed.

---

[BC-001]: ./../business-case.md
[SA-001]: ./../stakeholder-analysis.md
[DICT-001]: ./../dictionary.md
[PP-001]: ./../project-plan.md
[MIL-001]: ./../milestones/mil-001-foundation.md
[MIL-002]: ./../milestones/mil-002-core.md
[MIL-003]: ./../milestones/mil-003-publish.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-dictionary.md
[RC-004]: ./reviews/rc-004-mil-001.md
[RC-005]: ./reviews/rc-005-mil-002.md
[RC-006]: ./reviews/rc-006-mil-003.md
[PY-001]: ../../src/monday_motivation/
[RC-007]: ./reviews/rc-007-python-foundation.md
[PY-002]: ../../src/monday_motivation/
[RC-008]: ./reviews/rc-008-python-core.md
[70d79de]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/commit/70d79dec5c7933b71652c1ce87c6f49b4c4ca449
[61e13cd]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/commit/61e13cdbe9cffdc9181e78eb16036f80bd3942d5
[MIL-004]: ./../milestones/mil-004-framework-baseline.md
[RC-009]: ./reviews/rc-009-business-case-baseline.md
[RC-010]: ./reviews/rc-010-project-plan-baseline.md
[RC-011]: ./reviews/rc-011-milestone-004.md
[RC-012]: ./reviews/rc-012-wiki.md
[8530b42]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/commit/8530b4238a3ff0fe427a962078c97d8c2db7cff7
