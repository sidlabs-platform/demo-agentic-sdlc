# Story: Manage and Take Quizzes

| Field | Value |
|---|---|
| **Story ID** | STORY-006 |
| **Epic** | EPIC-003 |
| **Status** | Ready |
| **Assignee** | Unassigned |
| **Estimate** | M |
| **Priority** | P0 |

## User Story
**As an** Admin or Learner, **I want** quiz questions authored and answers scored, **so that** learners can assess their understanding and receive feedback.

## Acceptance Criteria
1. **Given** an Admin submits a valid question with at least two options, **When** it is created/updated/deleted, **Then** the quiz record reflects that operation.
2. **Given** a Learner fetches or attempts a quiz, **When** a response is returned, **Then** question responses omit the correct answer and attempts include score and explanation.
3. **Given** a learner submits an answer, **When** the attempt is processed, **Then** it is persisted with user, answer, correctness, and timestamp.

## BRD & Design References
| BRD ID | HLD/LLD Component |
|---|---|
| BRD-FR-016–018 | COMP-002, `LLD/course-management.md` and `LLD/database.md` |
| BRD-NFR-003, BRD-NFR-016–017 | COMP-001/002 |

## Tasks Breakdown
| Task ID | Description | Estimate |
|---|---|---|
| TASK-014 | Implement quiz authoring and attempt endpoints/services | 8h |

## UI/UX Notes
Quiz interaction is part of the Learner study experience (STORY-014); quiz authoring is part of STORY-016.

## Technical Notes
- **Stack:** FastAPI, Pydantic v2, aiosqlite.
- **Key considerations:** Never expose `correct_answer` in learner question schema; persist attempt before responding.
- **Configuration:** Shared database settings.

## Dependencies
- TASK-002 quiz/attempt tables, TASK-007 RBAC, and TASK-010 module data.

## Definition of Done
- [ ] Admin CRUD, learner scoring, persistence, and unauthorized access are tested
- [ ] No regressions in existing tests
