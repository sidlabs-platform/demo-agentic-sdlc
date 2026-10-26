# Task: Wire Feature APIs and Frontend Page Routes

| Field | Value |
|---|---|
| **Task ID** | TASK-031 |
| **Story** | STORY-001 |
| **Status** | To Do |
| **Assignee** | Unassigned |
| **Estimate** | 4h |
| **Wave**     | 7                 |
| **Type / Agent** | Backend — `@4-develop-agent` |

## Description
Complete application assembly by mounting all delivered API routers and implementing the HTML page router for the Jinja2 templates built by frontend tasks.

## Implementation Details
**Files to create/modify:** `src/main.py`, `src/frontend/__init__.py`, `src/frontend/router.py`, route integration tests under `tests/`.
**Approach:** Register auth, course, AI, progress, and reporting routers under their `/api/v1/` prefixes; mount static files and create the page routes in COMP-006 LLD for login/register, learner, and Admin pages. Use Jinja2 templates and auth checks consistent with page contracts.

## API Changes
Wires existing `/api/v1/*` routers and adds HTML GET routes `/login`, `/register`, `/dashboard`, `/courses`, `/courses/{id}`, `/lessons/{id}`, `/admin/courses`, `/admin/generate`, `/admin/reports`.

## Data Model Changes
N/A.

## Dependencies
| Prerequisite Task | Reason |
|---|---|
| TASK-001 | Base FastAPI application and app factory. |
| TASK-004 | App startup must initialize database and seeds. |
| TASK-006 | Auth router. |
| TASK-009 | Course router. |
| TASK-011 | Module/lesson router. |
| TASK-013 | Sanitized lesson route. |
| TASK-014 | Quiz routes. |
| TASK-017 | AI router. |
| TASK-019 | Enrollment router. |
| TASK-020 | Lesson completion route. |
| TASK-021 | Learner dashboard API. |
| TASK-023 | Reporting router. |
| TASK-024 | Shared shell and public auth page assets. |
| TASK-025 | Catalog and course-detail templates/assets. |
| TASK-026 | Lesson and quiz interaction assets. |
| TASK-027 | Learner dashboard assets. |
| TASK-028 | Admin course-management assets. |
| TASK-029 | Admin AI-generation assets. |
| TASK-030 | Admin reports assets. |

**Wave:** 7

## Acceptance Criteria
- [ ] All API routers and static assets are reachable from the application.
- [ ] Each Frontend LLD page route renders its corresponding template; restricted pages honor role requirements.
- [ ] Lifespan startup/shutdown remains functional and route integration has endpoint coverage.
- [ ] Representative non-AI API p95 response time is validated against the BRD target of <2 seconds.

## Test Requirements
- **Unit tests:** Page route response/template selection.
- **Integration tests:** App-level route smoke tests for every API router and HTML page; role-protected pages; representative non-AI p95 timing check.
- **Edge cases:** Missing template/static asset, anonymous restricted-page access, route path conflicts.

## Parent References
| Ref Type | ID |
|---|---|
| Story | STORY-001 |
| Epic | EPIC-001 |
| BRD | BRD-FR-001–042, BRD-INT-001–007, BRD-NFR-001, BRD-NFR-003, BRD-NFR-017 |

## Developer Agent Notes
`@4-develop-agent`: HLD COMP-001–006, Frontend LLD COMP-006 sections 2.2 and 4, and each feature's route LLD. This is an integration task, not a reason to reimplement service logic. Coordinate URL prefixes and avoid double-prefixing `/api/v1`.

## Definition of Done
- [ ] All routes are reachable and tested through the app instance
- [ ] No import-cycle or router-registration errors
- [ ] Acceptance criteria verified
