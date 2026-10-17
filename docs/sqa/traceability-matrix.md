# Monday Motivation Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-17 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version: baseline documents and their reviews | pending |

---

## Purpose

Tracks backward and forward links between artifact instances so that the Business Case's traceability can be measured. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001], [MIL-001] | [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001], [DICT-001] | [RC-002] |
| [DICT-001] | DICT | en | it | [BC-001], [SA-001] | source code | [RC-003] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003] | - |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | source code, [MIL-002] | [RC-004] |
| [MIL-002] | MIL | en | it | [BC-001], [PP-001], [MIL-001] | source code, [MIL-003] | [RC-005] |
| [MIL-003] | MIL | en | it | [BC-001], [PP-001], [MIL-002] | README, wiki | [RC-006] |

## Coverage Notes

- No instance yet of KPI, BMC, BPMN, UCD, US, UC, DM, SSD, OC, SD, DCD, ERD or ADR: the program is a single feature with plain technical tasks (see the Plan Risks and Scope in [PP-001]).
- `-` in Upstream means foundational; in Downstream it means nothing is built on it yet; in Last Reviewed it means no `RC-*` exists. [PP-001] has no QC checklist yet and is accepted by S01.
- Review records of source code are added in the milestone that produces the code.

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
