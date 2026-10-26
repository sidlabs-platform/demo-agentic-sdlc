# Task: Expose Admin Module and Lesson CRUD Routes

| Field | Value |
|---|---|
| **Task ID** | TASK-011 |
| **Story** | STORY-005 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 6h |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Expose Admin-only module and lesson CRUD routes using the service and schemas from TASK-010.

## Implementation Details
**Files to create/modify:** `src/courses/router.py`, `tests/courses/test_content_api.py`.
**Approach:** Add POST/PUT/DELETE handlers from the Course Management LLD. Validate request bodies with Pydantic v2 and map missing resources to 404.

## API Changes
| Endpoint | Method | Description |
|---|---|---|
| `/api/v1/courses/{courseId}/modules` | POST | Create a module. |
| `/api/v1/modules/{id}` | PUT/DELETE | Update/delete a module. |
| `/api/v1/modules/{moduleId}/lessons` | POST | Create a lesson. |
| `/api/v1/lessons/{id}` | PUT/DELETE | Update/delete a lesson. |

## Data Model Changes
N/A.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-007 | Admin-only authorization. |
| TASK-010 | Module/lesson schemas and service operations. |

**Wave:** 4

## Acceptance Criteria
- [ ] Routes return expected response schemas/status codes and enforce Admin role.
- [ ] Missing resources return 404 and invalid bodies return 422.
- [ ] Module delete follows cascade semantics.

## Test Requirements
- **Unit tests:** N/A — service tests in TASK-010.
- **Integration tests:** Route CRUD, permission, missing-resource cases.
- **Edge cases:** Learner calls, invalid parent IDs, malformed payload.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-005 |
| Epic | EPIC-003 |
| BRD | BRD-FR-011–014, BRD-NFR-003, BRD-NFR-017 |

## Developer Agent Notes
`@4-develop-agent`: Course Management LLD COMP-002 sections 4 and 6. This task adds Admin routes only; sanitized GET is TASK-013.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] No linting errors
- [ ] Acceptance criteria verified
