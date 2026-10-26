# Task: Implement Reporting Models and Read-Only Service

| Field | Value |
|---|---|
| **Task ID** | TASK-022 |
| **Story** | STORY-010 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 8h |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Implement typed report models, aggregate queries, per-course learner details, and CSV formatting/stream source.

## Implementation Details
**Files to create/modify:** `src/reporting/__init__.py`, `src/reporting/models.py`, `src/reporting/service.py`, `tests/reporting/test_reporting_service.py`.
**Approach:** Follow COMP-005 LLD. Read-only queries against courses/enrollments/progress/users; calculate completion rates safely; format CSV through a streaming-compatible iterator or content source.

## API Changes
N/A — routes are TASK-023.

## Data Model Changes
N/A — uses existing shared tables.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-002 | Reporting source tables and DB access. |

**Wave:** 2

## Acceptance Criteria
- [ ] Dashboard aggregates and per-learner progress match LLD response models.
- [ ] Service does not mutate course, enrollment, or progress state.
- [ ] CSV columns/values are correctly escaped and empty datasets remain valid.

## Test Requirements
- **Unit tests:** Rate math, learner aggregation, CSV formatting.
- **Integration tests:** Queries against representative temporary database.
- **Edge cases:** No enrollments, zero denominator, commas/quotes/newlines in names.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-010 |
| Epic | EPIC-006 |
| BRD | BRD-FR-025–027, BRD-NFR-001, BRD-NFR-016–017 |

## Developer Agent Notes
`@4-develop-agent`: Reporting LLD COMP-005 sections 2–6. Keep service read-only; CSV streaming response wiring belongs in TASK-023.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] No linting errors
- [ ] Acceptance criteria verified
