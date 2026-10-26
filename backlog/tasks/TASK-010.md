# Task: Implement Module and Lesson Services

| Field | Value |
|---|---|
| **Task ID** | TASK-010 |
| **Story** | STORY-005 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 8h |
| **Wave**     | 3                 |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Implement Pydantic models and service functions to create/update/delete modules and lessons while retaining hierarchy and sort order.

## Implementation Details
**Files to create/modify:** `src/courses/models.py`, `src/courses/service.py`, `tests/courses/test_content_service.py`.
**Approach:** Extend the course module from TASK-008 with ModuleCreateRequest/Response and LessonCreateRequest/Response and service functions. Ensure ownership through course/module relations and cascade child deletion as designed.

## API Changes
N/A — CRUD routes are TASK-011.

## Data Model Changes
Uses `modules` and `lessons`; no schema changes.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-002 | Required tables and connection. |
| TASK-008 | Course schemas/service conventions and parent course operations. |

**Wave:** 3

## Acceptance Criteria
- [ ] Module and lesson create/update/delete functions persist validated data and sort order.
- [ ] Deleting a module removes dependent lessons/quizzes consistently.
- [ ] Missing parent/child IDs produce explicit not-found results for route mapping.

## Test Requirements
- **Unit tests:** Service operations and ownership/hierarchy lookups.
- **Integration tests:** CRUD and cascade behavior in temporary DB.
- **Edge cases:** Invalid sort order, missing module/course, delete with children.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-005 |
| Epic | EPIC-003 |
| BRD | BRD-FR-011–014, BRD-NFR-015–017 |

## Developer Agent Notes
`@4-develop-agent`: Course Management LLD COMP-002 sections 2.2, 3, and 5. Keep Markdown as stored source; HTML rendering belongs only in sanitizer task.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] No linting errors
- [ ] Acceptance criteria verified
