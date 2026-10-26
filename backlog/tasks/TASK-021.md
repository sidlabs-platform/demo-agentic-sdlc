# Task: Implement Learner Enrollment and Progress Dashboard API

| Field | Value |
|---|---|
| **Task ID** | TASK-021 |
| **Story** | STORY-009 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 6h |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Return the authenticated Learner's enrollments with course and lesson/module progress summaries.

## Implementation Details
**Files to create/modify:** `src/progress/models.py`, `src/progress/service.py`, `src/progress/router.py`, `tests/progress/test_dashboard_api.py`.
**Approach:** Implement DashboardResponse and `get_learner_dashboard()` per COMP-004. Aggregate only records for verified user and retain stable course ordering as defined by service conventions.

## API Changes
| Endpoint | Method | Description |
|---|---|---|
| `/api/v1/enrollments` | GET | Return authenticated Learner's enrollment dashboard. |

## Data Model Changes
Read-only access to `enrollments`, `progress_records`, `courses`, `modules`, and `lessons`.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-007 | Authenticated Learner dependency for the endpoint. |
| TASK-018 | Enrollment response/service conventions. |
| TASK-020 | Progress data and completion behavior. |

**Wave:** 5

## Acceptance Criteria
- [ ] Response includes all the user's enrollments and defined progress counts.
- [ ] Other users' records are never included.
- [ ] Empty enrollment set returns an empty dashboard, not an error.

## Test Requirements
- **Unit tests:** Aggregate counts and model serialization.
- **Integration tests:** Endpoint returns own records only.
- **Edge cases:** No enrollment, zero lessons, completed course.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-009 |
| Epic | EPIC-005 |
| BRD | BRD-FR-024, BRD-NFR-001, BRD-NFR-003, BRD-NFR-017 |

## Developer Agent Notes
`@4-develop-agent`: Progress Tracking LLD COMP-004 sections 2.2, 3, and 4.1. Use Pydantic response models and derive identity from auth dependency.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] No linting errors
- [ ] Acceptance criteria verified
