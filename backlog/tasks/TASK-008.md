# Task: Implement Course Schemas and Lifecycle Services

| Field | Value |
|---|---|
| **Task ID** | TASK-008 |
| **Story** | STORY-004 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 8h |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Implement course Pydantic schemas and business operations for metadata CRUD, publish/unpublish, role-aware listing, and course detail.

## Implementation Details
**Files to create/modify:** `src/courses/__init__.py`, `src/courses/models.py`, `src/courses/service.py`, `tests/courses/test_course_service.py`.
**Approach:** Follow Course Management LLD COMP-002. New courses are draft; publish requires modules and lessons; unpublish preserves enrollments; Learners see published courses while Admins can see all.

## API Changes
N/A — service functions consumed by TASK-009 routes.

## Data Model Changes
Uses `courses`, `modules`, `lessons`; no schema changes.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-002 | Course hierarchy schema and connection. |

**Wave:** 2

## Acceptance Criteria
- [ ] Create/update/delete/publish/unpublish/list/detail functions match BRD/LLD behavior.
- [ ] Course deletion removes child content and publish rejects empty course structure.
- [ ] Publish/unpublish actions log actor, course, action, and duration without logging secrets.
- [ ] All public service signatures are typed and use Pydantic schemas.

## Test Requirements
- **Unit tests:** CRUD, visibility, publish validation, enrollment preservation.
- **Integration tests:** Service operations against temporary SQLite DB.
- **Edge cases:** Missing ID, no modules/lessons, empty catalog, cascading delete.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-004 |
| Epic | EPIC-003 |
| BRD | BRD-FR-004–010, BRD-NFR-001, BRD-NFR-011, BRD-NFR-013, BRD-NFR-015–017 |

## Developer Agent Notes
`@4-develop-agent`: Course Management LLD COMP-002 sections 2–3, 5, 6, and 9. Keep published-course reads independent from AI modules.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] No linting errors
- [ ] Acceptance criteria verified
