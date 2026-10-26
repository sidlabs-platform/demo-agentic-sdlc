# Task: Build Lesson Viewer and Quiz Interactions

| Field | Value |
|---|---|
| **Task ID** | TASK-026 |
| **Story** | STORY-013 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 7h |
| **Wave**     | 5                 |
| **Type / Agent** | Frontend — `@5-ui-develop-agent` |

## Description
Build the lesson page for safe content display, completion controls, lesson navigation, and learner quiz answer submission/feedback.

## Implementation Details
**Files to create/modify:**
- `src/templates/lesson.html`
- `src/static/css/lesson.css`, `src/static/js/lesson.js`
**Approach:** Render only server-sanitized HTML from lesson API. Use session/API helpers from TASK-024 for lesson completion and quiz attempt; display returned explanation and completion state. Keep previous/next navigation and reuse shared layout.

## API Changes
Consumes `GET /api/v1/lessons/{id}`, `POST /api/v1/lessons/{id}/complete`, and `POST /api/v1/quizzes/{id}/attempt`.

## Data Model Changes
N/A.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-024 | Shared page shell and session/API helpers. |
| TASK-013 | Sanitized lesson content API. |
| TASK-014 | Learner quiz attempt API. |
| TASK-020 | Completion API. |

**Wave:** 5

## Acceptance Criteria
- [ ] Lesson view displays sanitized HTML, title, completion action, and navigation.
- [ ] Completion control confirms the API result and displays failure states.
- [ ] Quiz answer submission displays correctness/explanation without exposing answer keys before submission.

## Test Requirements
- **Unit tests:** N/A — UI.
- **Integration tests:** Verify lesson, completion, and quiz response rendering.
- **Edge cases:** API/network failures, already-complete lesson, unsafe stored content, empty quiz.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-013 |
| Epic | EPIC-007 |
| BRD | BRD-FR-018, BRD-FR-039, BRD-NFR-005, BRD-NFR-007–008 |

## Developer Agent Notes
`@5-ui-develop-agent`: Frontend LLD COMP-006 sections 2.2, 3, 4.1, and 6. Treat lesson HTML as already sanitized; never render raw Markdown or correct-answer data.

## Definition of Done
- [ ] Lesson and quiz behavior is verified with mocked API responses
- [ ] Responsive layout and error states work; no console errors
- [ ] Acceptance criteria verified
