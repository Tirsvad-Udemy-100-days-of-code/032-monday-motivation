# Monday Motivation Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-17 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version: three stakeholders | pending |

---

## Purpose

This analysis names the people who own, use or look at the Monday Motivation project, so that every other artifact can cite stable stakeholder IDs for ownership, review and communication. It uses the Power/Interest grid and maps each concern to FURPS+.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant: Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | A correct, tested and documented solution to the assignment, produced by a clean, reviewed process |
| S02 | Udemy coursists | Course participants who share code and compare solutions | Udemy course community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, accepts the plan and every milestone, and is the only person who can supply the mail credentials. Both power and interest are high.
- **Keep Informed (S02):** cannot change the project but depends on its readability and run instructions; the README and wiki are written for them.
- **Monitor (S03):** casual visitors with no influence; the repository description, topics and README serve them without further effort.

## Primary Concerns and FURPS+ Mapping

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | The Monday email is sent with a random quote | Functionality |
| S01 | Credentials are never committed or printed | Functionality (security) |
| S01 | Rules are covered by tests that need no network | Reliability |
| S02 | Code is readable and uses the assignment's function names | Usability |
| S02 | The README tells how to run the program and the tests | Usability |
| S02 | Instructions exist in English, Danish and Bahasa Malaysia | Usability |
| S03 | The repository states clearly what it is | Usability |
| S03 | Nothing has to be installed to run it | Supportability (+ constraint: no runtime dependencies) |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull request | At each milestone | Run summary with review verdicts and stand-in decisions | All milestones |
| S02 | README and wiki | Once per release | Run instructions and screenshots | MIL-003 |
| S03 | Repository page | Once per release | Description, topics and README | MIL-003 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S02 wants a script that is easy to copy; S01 wants layered, tested code | S01, S02 | Keep the layers few and small (constants, quotes, mail, application) and keep the assignment's function names, so the code stays readable |
| S01 wants real credentials in use; S03 and the repository must hold none | S01, S03 | Credentials are read from environment variables at run time; `.env` is ignored by git; no test or screenshot uses them |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Monday email with a random quote | Objective 1 |
| S01 | Testable day check | Objective 2 |
| S01 | Credentials and dependencies | Objective 3 |
| S01 | Tests without network | Objective 4 |
| S02 | Run instructions in three languages | Objective 5 |
| S03 | Description and topics | Objective 6 |

## Sign-Off

Accepted by S01 as Product Owner when the plan is accepted in chat.

---

[BC-001]: ./business-case.md
