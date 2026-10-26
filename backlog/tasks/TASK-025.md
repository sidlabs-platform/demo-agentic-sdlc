# Task: Build Course Catalog and Detail Pages

| Field | Value |
|---|---|
| **Task ID** | TASK-025 |
| **Story** | STORY-012 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 7h |
| **Type / Agent** | Frontend — `@5-ui-develop-agent` |

## Description
Create responsive catalog and course detail templates with course cards, module/lesson navigation, and enrollment action.

## Implementation Details
**Files to create/modify:**
- `src/templates/catalog.html`, `src/templates/course_detail.html`
- `src/templates/components/course_card.html`
- `src/static/css/courses.css`, `src/static/js/courses.js`
**Approach:** Extend shared base and use the API/session helpers from TASK-024; use API data for published courses and ordered course detail; enrollment uses the Learner's bearer token and displays success/errors. Keep browser code framework-free.

## API Changes
Consumes `GET /api/v1/courses`, `GET /api/v1/courses/{id}`, and `POST /api/v1/courses/{id}/enroll`.

## Data Model Changes
N/A.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-024 | Shared page shell, styles, and session/API helpers. |
| TASK-009 | Course catalog/detail API contract. |
| TASK-019 | Enrollment API contract. |

**Wave:** 5

## Acceptance Criteria
- [ ] Catalog cards display title, description, difficulty, and enrollment control.
- [ ] Detail view displays modules and lessons in service-provided order.
- [ ] Enrollment success/error is communicated without falsely indicating persistence.

## Test Requirements
- **Unit tests:** N/A — UI.
- **Integration tests:** Verify template data rendering and enrollment request behavior.
- **Edge cases:** Empty catalog, API unavailable, missing course, already enrolled.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-012 |
| Epic | EPIC-007 |
| BRD | BRD-FR-037–038, BRD-FR-019, BRD-NFR-008 |

## Developer Agent Notes
`@5-ui-develop-agent`: Frontend LLD COMP-006 sections 2–5. Use reusable course card partial and API output; page routes are assembled by TASK-031.

## Definition of Done
- [ ] UI is verified with empty and populated data
- [ ] Responsive desktop/tablet layout; no console errors
- [ ] Acceptance criteria verified
