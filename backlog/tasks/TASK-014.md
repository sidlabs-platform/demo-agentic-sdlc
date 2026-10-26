# Task: Implement Quiz Authoring and Attempt APIs

| Field | Value |
|---|---|
| **Task ID** | TASK-014 |
| **Story** | STORY-006 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 8h |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Implement quiz Pydantic models, Admin question CRUD, learner-safe question retrieval, answer scoring, and persisted attempts with explanation.

## Implementation Details
**Files to create/modify:** `src/courses/models.py`, `src/courses/service.py`, `src/courses/router.py`, `tests/courses/test_quiz_api.py`.
**Approach:** Follow Course Management LLD. Store options as JSON text; keep correct answer out of learner question response. On attempt, compare selected answer, persist QuizAttempt, and return correctness/explanation.

## API Changes
| Endpoint | Method | Description |
|---|---|---|
| `/api/v1/modules/{moduleId}/quizzes` | POST | Admin creates a question. |
| `/api/v1/quizzes/{id}` | PUT/DELETE | Admin updates/deletes a question. |
| `/api/v1/quizzes/{id}/attempt` | POST | Learner submits answer and receives result. |

## Data Model Changes
Uses `quiz_questions` and `quiz_attempts` from TASK-002.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-002 | Quiz and attempt tables. |
| TASK-007 | Admin/Learner role checks. |
| TASK-010 | Module existence and course schema conventions. |

**Wave:** 4

## Acceptance Criteria
- [ ] Admin CRUD is role-restricted and validates question/options.
- [ ] Learner attempt is persisted and returns `is_correct` plus explanation.
- [ ] Learner-facing schemas never reveal correct answer before an attempt.

## Test Requirements
- **Unit tests:** Scoring, schema validation, persistence function.
- **Integration tests:** CRUD and attempt endpoint with admin/learner clients.
- **Edge cases:** Missing quiz, invalid option selection, malformed JSON stored options.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-006 |
| Epic | EPIC-003 |
| BRD | BRD-FR-016–018, BRD-NFR-003, BRD-NFR-016–017 |

## Developer Agent Notes
`@4-develop-agent`: Course Management LLD COMP-002 sections 2.2, 3, and 4; Database LLD quiz_attempts table. Keep answer key private in learner responses.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] No linting errors
- [ ] Acceptance criteria verified
