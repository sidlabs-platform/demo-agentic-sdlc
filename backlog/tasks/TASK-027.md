# Task: Build Learner Dashboard and Progress UI

| Field | Value |
|---|---|
| **Task ID** | TASK-027 |
| **Story** | STORY-014 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 6h |
| **Wave**     | 6                 |
| **Type / Agent** | Frontend — `@5-ui-develop-agent` |

## Description
Create a learner dashboard that lists enrollments, completion summaries, progress bars, and direct resume links.

## Implementation Details
**Files to create/modify:**
- `src/templates/dashboard.html`, `src/templates/components/progress_bar.html`
- `src/static/css/dashboard.css`, `src/static/js/dashboard.js`
**Approach:** Use session/API helpers from TASK-024 and authenticated `/api/v1/enrollments` response; show useful empty state, course completion status, and prominent next-lesson/resume link.

## API Changes
Consumes `GET /api/v1/enrollments`.

## Data Model Changes
N/A.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-024 | Shared page shell and session/API helpers. |
| TASK-021 | Learner dashboard response contract. |

**Wave:** 6

## Acceptance Criteria
- [ ] Dashboard displays enrolled course and progress data, including empty state.
- [ ] Refresh uses persisted API state rather than transient client-only progress.
- [ ] From dashboard, Learner reaches a next lesson in no more than two clicks.

## Test Requirements
- **Unit tests:** N/A — UI.
- **Integration tests:** Render empty/in-progress/completed response states.
- **Edge cases:** Expired token, API error, zero lessons, completed enrollment.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-014 |
| Epic | EPIC-007 |
| BRD | BRD-FR-036, BRD-FR-024, BRD-NFR-007–008 |

## Developer Agent Notes
`@5-ui-develop-agent`: Frontend LLD COMP-006 sections 3.1, 3.3, and 4.1. Reuse progress-bar partial; don't calculate authoritative progress in client code.

## Definition of Done
- [ ] Dashboard displays server state and meets two-click criterion
- [ ] Responsive empty/error/populated states verified
- [ ] Acceptance criteria verified
