# Task: Expose Sanitized Lesson Retrieval

| Field | Value |
|---|---|
| **Task ID** | TASK-013 |
| **Story** | STORY-005 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 4h |
| **Wave**     | 4                 |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Implement the learner/admin lesson-content read route returning Pydantic response data containing rendered sanitized HTML.

## Implementation Details
**Files to create/modify:** `src/courses/router.py`, `src/courses/service.py`, `tests/courses/test_lesson_content_api.py`.
**Approach:** Load lesson Markdown via course service, call `render_and_sanitize_markdown()` from TASK-012, and return LessonContentResponse. Require authenticated user per LLD.

## API Changes
| Endpoint | Method | Description |
|---|---|---|
| `/api/v1/lessons/{id}` | GET | Return lesson content as sanitized HTML. |

## Data Model Changes
N/A.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-007 | Authenticated-user dependency. |
| TASK-010 | Lesson lookup and response schemas. |
| TASK-012 | Markdown renderer/sanitizer. |

**Wave:** 4

## Acceptance Criteria
- [ ] Existing lesson returns title and sanitized HTML; unknown lesson returns 404.
- [ ] No raw Markdown or unsanitized HTML is returned.
- [ ] Response matches LessonContentResponse.

## Test Requirements
- **Unit tests:** N/A — renderer in TASK-012.
- **Integration tests:** Authenticated read and missing lesson.
- **Edge cases:** Stored raw HTML/XSS payload and empty Markdown.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-005 |
| Epic | EPIC-003 |
| BRD | BRD-FR-015, BRD-NFR-005, BRD-NFR-003, BRD-NFR-017 |

## Developer Agent Notes
`@4-develop-agent`: Course Management LLD COMP-002 sections 4.1 and 5.2. The frontend must consume this already-sanitized response, not render Markdown itself.

## Definition of Done
- [ ] Code follows project conventions and tests pass
- [ ] No linting errors
- [ ] Acceptance criteria verified
