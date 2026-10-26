# Task: Implement Transactional Lesson Progress Updates

| Field | Value |
|---|---|
| **Task ID** | TASK-020 |
| **Story** | STORY-009 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 8h |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Implement lesson completion persistence and automatic module/course state progression in a single transaction, exposed through the Learner completion route.

## Implementation Details
**Files to create/modify:** `src/progress/models.py`, `src/progress/service.py`, `src/progress/router.py`, `tests/progress/test_completion.py`.
**Approach:** Upsert progress record; verify learner enrollment; calculate module/course completeness; transition enrollment `not_started → in_progress → completed`; commit all updates together before responding.

## API Changes
| Endpoint | Method | Description |
|---|---|---|
| `/api/v1/lessons/{id}/complete` | POST | Persist completion and return progress. |

## Data Model Changes
Uses `progress_records` and `enrollments`; no schema change.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-002 | Progress/enrollment schema. |
| TASK-007 | Authenticated Learner. |
| TASK-010 | Lesson/module/course relationship lookup. |
| TASK-018 | Enrollment validation and service contract. |

**Wave:** 4

## Acceptance Criteria
- [ ] Progress is committed before a successful response and survives refresh.
- [ ] Module and course completion states update when all required child records are done.
- [ ] Any failure rolls back the complete update; repeat completion does not corrupt state.

## Test Requirements
- **Unit tests:** State calculation and transition conditions.
- **Integration tests:** Completion transaction against temporary SQLite.
- **Edge cases:** Not enrolled, missing lesson, repeated completion, rollback, partial module.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-009 |
| Epic | EPIC-005 |
| BRD | BRD-FR-020–023, BRD-NFR-001, BRD-NFR-009, BRD-NFR-017 |

## Developer Agent Notes
`@4-develop-agent`: Progress Tracking LLD COMP-004 sections 2.2, 2.3, 5.2, and 6. Use aiosqlite transaction boundaries; don't mark a course complete until all modules meet the LLD condition.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] Progress is durable and transaction tests pass
- [ ] Acceptance criteria verified
