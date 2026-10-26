# Task: Expose Course Lifecycle and Discovery Routes

| Field | Value |
|---|---|
| **Task ID** | TASK-009 |
| **Story** | STORY-004 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 8h |
| **Wave**     | 3                 |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Create the versioned course API routes and apply role dependencies for Admin mutations and Learner/Admin reads.

## Implementation Details
**Files to create/modify:** `src/courses/router.py`, `tests/courses/test_course_api.py`.
**Approach:** Delegate business rules to TASK-008; use Pydantic request/response schemas and `require_role`/`get_current_user` dependencies. Match endpoint/status codes in Course Management LLD.

## API Changes
| Endpoint | Method | Description |
|---|---|---|
| `/api/v1/courses` | GET/POST | Role-aware list / Admin create. |
| `/api/v1/courses/{id}` | GET/PUT/DELETE | Detail, Admin update/delete. |
| `/api/v1/courses/{id}/publish` | POST | Admin publish. |
| `/api/v1/courses/{id}/unpublish` | POST | Admin unpublish. |

## Data Model Changes
N/A.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-007 | Enforce identity/roles. |
| TASK-008 | Consume course service and schemas. |

**Wave:** 3

## Acceptance Criteria
- [ ] Routes and HTTP status codes match the LLD.
- [ ] Learner listing hides drafts and Admin mutations reject Learners.
- [ ] Unknown IDs return 404; create/update validation is returned as 422.

## Test Requirements
- **Unit tests:** N/A — service tests in TASK-008.
- **Integration tests:** Each route's successful and denied paths.
- **Edge cases:** Missing course, empty publish attempt, learner draft access.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-004 |
| Epic | EPIC-003 |
| BRD | BRD-FR-004–010, BRD-NFR-003, BRD-NFR-017 |

## Developer Agent Notes
`@4-develop-agent`: Course Management LLD COMP-002 section 4. Router is registered by TASK-031; do not duplicate service rules in handlers.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] No linting errors
- [ ] Acceptance criteria verified
