# Task: Build Admin Course and Content Management UI

| Field | Value |
|---|---|
| **Task ID** | TASK-028 |
| **Story** | STORY-015 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 9h |
| **Wave**     | 5                 |
| **Type / Agent** | Frontend — `@5-ui-develop-agent` |

## Description
Build the Admin course table and forms/actions for course, module, lesson, and quiz creation/editing/deletion and publish/unpublish.

## Implementation Details
**Files to create/modify:**
- `src/templates/admin/courses.html`, `src/templates/admin/course_edit.html`
- `src/static/css/admin-courses.css`, `src/static/js/admin-courses.js`
**Approach:** Follow COMP-006 Admin page; use session/API helpers from TASK-024 and connect form/actions to course, module, lesson, and quiz APIs. Show draft/published states and only confirm changes after successful response.

## API Changes
Consumes course CRUD/publish APIs, module/lesson CRUD APIs, and quiz authoring APIs.

## Data Model Changes
N/A.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-024 | Shared page shell and session/API helpers. |
| TASK-009 | Course CRUD and publish APIs. |
| TASK-011 | Module/lesson authoring APIs. |
| TASK-013 | Lesson content read contract for editing/viewing as needed. |
| TASK-014 | Quiz CRUD APIs. |

**Wave:** 5

## Acceptance Criteria
- [ ] Admin page lists course status and exposes create/edit/delete/publish/unpublish.
- [ ] Course editor supports module, lesson, and quiz authoring using API contracts.
- [ ] Validation and failed publish/API actions display the server result and retain form context.

## Test Requirements
- **Unit tests:** N/A — UI.
- **Integration tests:** Exercise representative course/module/lesson/quiz interactions with mocked APIs.
- **Edge cases:** Empty course publish, invalid form, delete confirmation, API authorization error.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-015 |
| Epic | EPIC-007 |
| BRD | BRD-FR-040, BRD-FR-004–018, BRD-NFR-008 |

## Developer Agent Notes
`@5-ui-develop-agent`: Frontend LLD COMP-006 sections 2.2, 3.1, 3.3, and 4.1. Do not duplicate backend validation or assume a write succeeded before API confirmation.

## Definition of Done
- [ ] Admin authoring workflow and API error paths verified
- [ ] Responsive layout and accessible form controls verified
- [ ] Acceptance criteria verified
