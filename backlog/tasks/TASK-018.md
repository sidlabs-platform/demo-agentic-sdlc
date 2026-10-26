# Task: Implement Learner Enrollment Service

| Field | Value |
|---|---|
| **Task ID** | TASK-018 |
| **Story** | STORY-008 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 5h |
| **Wave**     | 3                 |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Implement enrollment request/response models and service behavior for Learners enrolling in published courses.

## Implementation Details
**Files to create/modify:** `src/progress/__init__.py`, `src/progress/models.py`, `src/progress/service.py`, `tests/progress/test_enrollment_service.py`.
**Approach:** Follow COMP-004 LLD. Check course status, enforce unique learner/course relationship, create `not_started` enrollment, and calculate course progress fields for response.

## API Changes
N/A — route is TASK-019.

## Data Model Changes
Uses `enrollments`; no schema change.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-002 | Enrollment/course data tables. |
| TASK-007 | Authenticated Learner identity and role. |
| TASK-008 | Published course lookup and hierarchy queries. |

**Wave:** 3

## Acceptance Criteria
- [ ] Published course enrollment creates one `not_started` record with response summary.
- [ ] Duplicate, draft, and missing courses map to the documented errors.
- [ ] Enrollment is scoped to the verified authenticated user.

## Test Requirements
- **Unit tests:** Enrollment eligibility and response counts.
- **Integration tests:** Service behavior with temporary SQLite.
- **Edge cases:** Unique constraint race and course with no content.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-008 |
| Epic | EPIC-005 |
| BRD | BRD-FR-019, BRD-NFR-001, BRD-NFR-003, BRD-NFR-017 |

## Developer Agent Notes
`@4-develop-agent`: Progress Tracking LLD COMP-004 sections 2–4 and Database LLD enrollment constraints. Keep duplicate enrollment behavior explicit; do not accept user ID from payload.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] No linting errors
- [ ] Acceptance criteria verified
