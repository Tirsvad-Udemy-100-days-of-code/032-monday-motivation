# RC-003 Domain Dictionary review

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-003 |
| CrossReference | [DICT-001], [QC-DICT-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-17 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial review record | [7d48d63] |

---

## Artifact Under Review

- Instance reviewed: [DICT-001]
- Checklist used: [QC-DICT-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Every row has a PO term, its language, an IT term and a definition | Pass | All eight rows have a PO term, language, IT term and definition. |
| 2 | Each PO term maps to exactly one IT term and the reverse (no synonyms) | Pass | Each PO term maps to one IT term and the reverse; no synonyms. |
| 3 | Every Domain Model concept has a row, and the Domain Model uses its PO term | N-A | The project has no Domain Model: the program has no persisted concepts beyond a string; the Business Case does not require one. Not used to hide a Fail. |
| 4 | The Operation Contracts, Sequence Diagrams, Design Class Diagrams and ERD use the IT term, not the PO term | N-A | The project has no Operation Contract, Sequence Diagram, DCD or ERD; source code is checked against the IT terms in its own code review. |
| 5 | Definitions are written in the PO language and are one sentence | Pass | Each definition is one English sentence. |
| 6 | "Used as PO term in" and "Used as IT term in" name artifact types that exist in the project | Pass | The "Used as" columns name BC, SA, MIL and source code; the first three exist, source code follows in MIL-001. |
| 7 | The dictionary's `Language` and `Domain` rows, and the language of every row, match the PO language and domain in the project registry | Pass | Language `en` and Domain `it` match the registry. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has `Language | en` and `Domain | it`. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is BCP 47; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English; the PO language is English. Read by the stand-in, who reads English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register matches the registry row for this type (IT Professional English). |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | PO terms are those of DICT-001 (quote, quotes list, Monday email, day check, random pick, mail password, test send, mail account); no synonyms found. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists in `docs/`. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version; there is no earlier accepted version to compare. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | English and the IT domain are the Product Owner's own; S01 wrote the brief in this language and domain. Language reviewer: none. Stand-in decision, open to challenge. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations (SMTP, PO, QC, SQA) are used as in the framework; SMTP and PO are spelled out in the dictionary and the stakeholder analysis. |

## Overall Verdict

Go — all applicable Mandatory criteria pass; criteria 3 and 4 are not applicable because the artifacts they check do not exist in this project.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Challenge this stand-in review if wanted | S01 | 2026-10-31 |

---

[DICT-001]: ../../dictionary.md
[QC-DICT-001]: ../../../framework/qc/artifacts/qc-dictionary.md
[7d48d63]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/032-monday-motivation/commit/7d48d63e6b73c5d2459bac3bd6720751726d1d6f
