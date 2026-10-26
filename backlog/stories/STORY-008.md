# Story: Enroll in a Published Course

| Field | Value |
|---|---|
| **Story ID** | STORY-008 |
| **Epic** | EPIC-005 |
| **Status** | Ready |
| **Assignee** | Unassigned |
| **Estimate** | M |
| **Priority** | P0 |

## User Story
**As a** Learner, **I want** to enroll in a published course, **so that** my participation and starting status are recorded.

## Acceptance Criteria
1. **Given** a published course and authenticated Learner, **When** enrollment is requested, **Then** a unique enrollment is created with `not_started` status.
2. **Given** an unpublished/missing course or existing enrollment, **When** enrollment is requested, **Then** the documented 400/404 response is returned without duplicate data.
3. **Given** a valid Learner token, **When** enrollments are accessed, **Then** only that Learner's data is returned.

## BRD & Design References
| BRD ID | HLD/LLD Component |
|---|---|
| BRD-FR-019 | COMP-004, `LLD/progress-tracking.md` |
| BRD-NFR-001, BRD-NFR-003 | COMP-001/004 |

## Tasks Breakdown
| Task ID | Description | Estimate |
|---|---|---|
| TASK-018 | Implement enrollment service and schemas | 5h |
| TASK-019 | Expose Learner enrollment endpoint | 4h |

## UI/UX Notes
Enrollment action is covered by STORY-013.

## Technical Notes
- **Stack:** FastAPI, Pydantic v2, aiosqlite.
- **Key considerations:** Require learner identity; validate published state; honor unique(user_id, course_id).
- **Configuration:** Shared database settings.

## Dependencies
- TASK-018 needs TASK-002 schema, TASK-007 identity, and TASK-008 course queries; TASK-019 needs TASK-018.

## Definition of Done
- [ ] Enrollment success, duplicate, unpublished, missing, and cross-user cases are tested
- [ ] No regressions in existing tests
