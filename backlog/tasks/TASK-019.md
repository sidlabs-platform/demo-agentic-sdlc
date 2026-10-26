# Task: Expose Learner Enrollment Route

| Field | Value |
|---|---|
| **Task ID** | TASK-019 |
| **Story** | STORY-008 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 4h |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Add the learner-only enrollment route and map service outcomes to the API contract.

## Implementation Details
**Files to create/modify:** `src/progress/router.py`, `tests/progress/test_enrollment_api.py`.
**Approach:** Use `get_current_user`/Learner role dependency and pass verified user ID to TASK-018. Follow the status codes and response fields in Progress Tracking LLD.

## API Changes
| Endpoint | Method | Description |
|---|---|---|
| `/api/v1/courses/{id}/enroll` | POST | Enroll authenticated Learner. |

## Data Model Changes
N/A.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-007 | Authenticated Learner dependency. |
| TASK-018 | Enrollment service and schema. |

**Wave:** 4

## Acceptance Criteria
- [ ] Learner enrollment returns 201 and expected response.
- [ ] Missing/draft/already-enrolled course outcomes match LLD.
- [ ] Anonymous requests are denied; use the COMP-004 Learner endpoint contract and authenticated identity.

## Test Requirements
- **Unit tests:** N/A — service tests in TASK-018.
- **Integration tests:** Success, invalid course, duplicate enrollment, and auth.
- **Edge cases:** Concurrent duplicate requests.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-008 |
| Epic | EPIC-005 |
| BRD | BRD-FR-019, BRD-NFR-003, BRD-NFR-017 |

## Developer Agent Notes
`@4-develop-agent`: Progress Tracking LLD COMP-004 section 4.1 specifies a Learner route. Do not trust a client-supplied user ID; route is mounted by TASK-031. Follow that detailed role contract unless the product owner explicitly resolves the broader Admin-as-Learner convention.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] No linting errors
- [ ] Acceptance criteria verified
